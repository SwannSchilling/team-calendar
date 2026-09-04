// i18n integrity check: EN (features.json) vs DE (features.de.json).
// Verifies: same feature ids, same status arrays, same differentiator/niche flags,
// and that DE 'for' strings resolve to the same role tokens as EN.
import { readFileSync } from 'node:fs';

const base = 'F:/GithubProjects/codrops-barbajs-page-transition/src/data/';
const en = JSON.parse(readFileSync(base + 'features.json', 'utf8'));
const de = JSON.parse(readFileSync(base + 'features.de.json', 'utf8'));

// Mirror of src/utils/text.ts rolesFor (plain-string logic only).
function rolesFor(forStr) {
  const raw = forStr || '';
  const out = [];
  const push = (r) => { if (!out.includes(r)) out.push(r); };
  for (const tok of raw.split(/,| and | und |\+/)) {
    const t = tok.replace(/\(.*?\)/g, '').trim().toLowerCase();
    const first = t.split(/\s+/)[0];
    if (!first) continue;
    if (/^(owner|operator|studio|business|inhaber|betreiber)/.test(first)) push('Owner');
    else if (/^admin/.test(first)) push('Admin');
    else if (/^(artist|team|k\u00fcnster|k\u00fcnstler)/.test(first)) push('Artist');
    else if (/^(client|kunde|kunden)/.test(first)) push('Client');
    else if (/^(everyone|alle)/.test(first)) push('Everyone');
  }
  return out.length ? out : [raw.trim()];
}

const flat = (d) => d.categories.flatMap((c) => c.features.map((f) => ({ ...f, catId: c.id })));
const enMap = new Map(flat(en).map((f) => [f.id, f]));
const deList = flat(de);

let problems = 0;
const fail = (msg) => { problems++; console.log('  PROBLEM:', msg); };

if (enMap.size !== deList.length) fail('feature count differs: EN ' + enMap.size + ' vs DE ' + deList.length);
if (en.categories.length !== de.categories.length) fail('category count differs');
if (JSON.stringify(en.statusCounts) !== JSON.stringify(de.statusCounts)) fail('statusCounts differ');
if (en.totalFeatures !== de.totalFeatures) fail('totalFeatures differ');
if (en.differentiators.length !== de.differentiators.length) fail('differentiator count differs');
if (en.niche.length !== de.niche.length) fail('niche count differs');
if (en.general.length !== de.general.length) fail('general count differs');

for (const f of deList) {
  const e = enMap.get(f.id);
  if (!e) { fail('DE id ' + f.id + ' missing in EN'); continue; }
  if (JSON.stringify(e.status) !== JSON.stringify(f.status)) fail('id ' + f.id + ' status differs: EN ' + e.status + ' DE ' + f.status);
  if (e.differentiator !== f.differentiator) fail('id ' + f.id + ' differentiator flag differs');
  if (e.niche !== f.niche) fail('id ' + f.id + ' niche flag differs');
  if (e.catId !== f.catId) fail('id ' + f.id + ' category differs');
  // Raw fallbacks are display-only chips (never match filter keys), so normalize them to RAW.
  const norm = (arr) => arr.map((x) => (['Owner','Admin','Artist','Client','Everyone'].includes(x) ? x : 'RAW'));
  const re = norm(rolesFor(e.for)), rd = norm(rolesFor(f.for));
  if (JSON.stringify(re) !== JSON.stringify(rd)) fail('id ' + f.id + ' roles differ: EN [' + re + '] DE [' + rd + '] (' + JSON.stringify(e.for) + ' / ' + JSON.stringify(f.for) + ')');
}
// Every EN id present in DE?
for (const id of enMap.keys()) if (!deList.some((f) => f.id === id)) fail('EN id ' + id + ' missing in DE');

if (problems === 0) console.log('i18n parity OK: 81/81 features aligned (ids, statuses, flags, categories, role tokens)');
else console.log(problems + ' problems found');
process.exit(problems === 0 ? 0 : 1);
