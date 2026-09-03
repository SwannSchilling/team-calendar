#!/usr/bin/env node
// One-off parser: FEATURE_INVENTORY.md -> src/data/features.json
// Run: node scripts/parse-inventory.mjs
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const src = readFileSync(join(root, 'FEATURE_INVENTORY.md'), 'utf8');
const lines = src.split(/\r?\n/);

const STATUS = [
  { ch: '✅', key: 'live' },
  { ch: '🟡', key: 'progress' },
  { ch: '🔶', key: 'pending' },
  { ch: '⏳', key: 'planned' },
  { ch: '⚠️', key: 'verify' },
];

function parseStatus(flags) {
  const found = STATUS.filter((s) => flags.includes(s.ch)).map((s) => s.key);
  return found.length ? found : ['live'];
}

const DIFF_MARK = '*(Differentiator.)*';
const NICHEDIFF_MARK = '*(Niche + Differentiator.)*';
const NICHE_MARK = '*(Niche.)*';

const categories = [];
let curCat = null;
let curFeat = null;
let inDiff = false;
let inNiche = false;
let inGeneral = false;

const differentiators = [];
const niche = [];
const general = [];

for (const raw of lines) {
  const line = raw.trim();

  if (line.startsWith('## ')) {
    inDiff = /Standout|differentiator/i.test(line);
    inNiche = /Niche \(tattoo/i.test(line);
    inGeneral = false;
    if (line.startsWith('## Category ')) {
      const m = line.match(/^## Category (\d+) — (.+)$/);
      curCat = {
        num: Number(m[1]),
        title: m[2].trim(),
        id: m[2].trim().toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, ''),
        features: [],
        plannedNote: null,
      };
      categories.push(curCat);
      curFeat = null;
    } else if (!inDiff) {
      curCat = null;
      curFeat = null;
    }
    continue;
  }

  if (line === '---' || line === '') continue;

  if (inNiche && line.startsWith('**General-purpose**')) { inNiche = false; inGeneral = true; continue; }

  if (inDiff) {
    const m = line.match(/^\d+\.\s+\*\*(.+?)\*\*\s*\((.+?)\)\s*—\s*(.+)$/);
    if (m) differentiators.push({ title: m[1].trim(), refs: m[2].trim(), line: m[3].trim().replace(/\*\*/g, '') });
    continue;
  }
  if (inNiche) { if (line.startsWith('- ')) niche.push(line.slice(2).trim()); continue; }
  if (inGeneral) { if (line.startsWith('- ')) general.push(line.slice(2).trim()); continue; }

  if (!curCat) continue;

  const planned = line.match(/^>\s*\*\*Planned \(([^)]+)\):\*\*\s*(.+?)\s*—\s*⏳/);
  if (planned) {
    curCat.plannedNote = { area: planned[1].trim(), text: planned[2].trim().replace(/\*\*/g, '') };
    continue;
  }

  const fh = line.match(/^\*\*(\d+)\.\s+(.+?)\*\*\s+—\s+(.+)$/);
  if (fh) {
    curFeat = {
      id: Number(fh[1]),
      title: fh[2].trim(),
      status: parseStatus(fh[3]),
      what: '', for: '', why: '', notes: [],
      differentiator: false, niche: false,
    };
    curCat.features.push(curFeat);
    continue;
  }

  if (!curFeat) continue;

  const b = line.match(/^[-] +\*\*([^*]+?)\*\*[:]?\s*(.*)$/);
  if (b) {
    const key = b[1].trim().toLowerCase();
    let val = b[2].trim();
    if (/^what/.test(key)) curFeat.what = val;
    else if (/^for/.test(key)) curFeat.for = val.replace(/\.$/, '');
    else if (/^why/.test(key)) curFeat.why = val;
    else curFeat.notes.push({ key: b[1].trim(), text: val });
    continue;
  }
  // wrapped continuation of the previous bullet
  if (curFeat.notes.length) curFeat.notes[curFeat.notes.length - 1].text += ' ' + line;
  else if (curFeat.why) curFeat.why += ' ' + line;
  else curFeat.what += ' ' + line;
}

for (const cat of categories) {
  for (const f of cat.features) {
    const blob = [f.what, f.why, f.for, ...f.notes.map((n) => n.text)].join(' ');
    f.differentiator = blob.includes(DIFF_MARK) || blob.includes(NICHEDIFF_MARK);
    f.niche = blob.includes(NICHE_MARK) || blob.includes(NICHEDIFF_MARK);
  }
}

const allFeatures = categories.flatMap((c) => c.features);
const counts = { live: 0, progress: 0, pending: 0, planned: 0, verify: 0 };
for (const f of allFeatures) {
  if (f.status.includes('live')) counts.live += 1;
  if (f.status.includes('progress')) counts.progress += 1;
  if (f.status.includes('pending')) counts.pending += 1;
  if (f.status.includes('planned')) counts.planned += 1;
  if (f.status.includes('verify')) counts.verify += 1;
}

const data = {
  compiled: 'Repository state as of 2026-08-29 (commit edbc187)',
  categories,
  differentiators,
  niche,
  general,
  statusCounts: counts,
  totalFeatures: allFeatures.length,
};

mkdirSync(join(root, 'src', 'data'), { recursive: true });
writeFileSync(join(root, 'src', 'data', 'features.json'), JSON.stringify(data, null, 2) + '\n');
console.log('features:', allFeatures.length, '| categories:', categories.length, '| differentiators:', differentiators.length, '| niche:', niche.length, '| general:', general.length);
console.log('status counts (multi-flag):', JSON.stringify(counts));
for (const c of categories) console.log(`  cat ${c.num} ${c.title}: ${c.features.length}${c.plannedNote ? ' + planned: ' + c.plannedNote.text : ''}`);
const diffIds = allFeatures.filter((f) => f.differentiator).map((f) => f.id).join(',');
const nicheIds = allFeatures.filter((f) => f.niche).map((f) => f.id).join(',');
console.log('differentiator ids:', diffIds);
console.log('niche ids:', nicheIds);
