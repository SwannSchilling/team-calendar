import type { Feature } from '../types';

// Strip markdown emphasis / code markers for card-sized copy.
export function plain(md: string): string {
  return md
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\*\([^)]*\)\*/g, '')
    .trim();
}

// Shorten a feature's why-line for card display (cut at a sensible stop).
export function shortWhy(feature: Feature): string {
  const p = plain(feature.why);
  if (p.length <= 110) return p;
  const cut = p.slice(0, 110);
  const at = Math.max(cut.lastIndexOf('. '), cut.lastIndexOf('; '));
  return at > 60 ? p.slice(0, at + 1) : cut.trimEnd() + '…';
}

// Split a "For" string into normalized role tokens.
// Handles annotations like "Admins (define)" and multi-word audiences.
export function rolesFor(feature: Feature): string[] {
  const raw = feature.for || '';
  const out: string[] = [];
  const push = (r: string) => {
    if (!out.includes(r)) out.push(r);
  };
  for (const tok of raw.split(/,| and |\+/)) {
    const t = tok.replace(/\(.*?\)/g, '').trim().toLowerCase();
    const first = t.split(/\s+/)[0];
    if (!first) continue;
    if (/^owner/.test(first) || /^operator/.test(first) || /^studio/.test(first) || /^business/.test(first)) push('Owner');
    else if (/^admin/.test(first)) push('Admin');
    else if (/^artist/.test(first) || /^team/.test(first)) push('Artist');
    else if (/^client/.test(first)) push('Client');
    else if (/^everyone/.test(first)) push('Everyone');
  }
  return out.length ? out : [raw.trim()];
}

export const STATUS_LABEL: Record<string, string> = {
  live: 'Live',
  progress: 'In progress',
  pending: 'Deploy pending',
  planned: 'Roadmap',
  verify: 'Verify',
};
