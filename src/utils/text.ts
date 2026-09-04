import type { Feature } from '../types';

export type Locale = 'en' | 'de';

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
  return at > 60 ? p.slice(0, at + 1) : cut.trimEnd() + '\u2026';
}

// Split a "For" string into normalized role tokens (language-agnostic keys).
// Handles annotations like "Admins (define)" / "Admins (definieren)" and multi-word audiences.
// Both EN and DE base words map to the same tokens so filters stay consistent.
export function rolesFor(feature: Feature): string[] {
  const raw = feature.for || '';
  const out: string[] = [];
  const push = (r: string) => {
    if (!out.includes(r)) out.push(r);
  };
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

export const STATUS_LABELS: Record<Locale, Record<string, string>> = {
  en: {
    live: 'Live',
    progress: 'In progress',
    pending: 'Deploy pending',
    planned: 'Roadmap',
    verify: 'Verify',
  },
  de: {
    live: 'Live',
    progress: 'In Arbeit',
    pending: 'Deployment ausstehend',
    planned: 'Roadmap',
    verify: 'Verifizieren',
  },
};

// Display labels for the normalized role tokens from rolesFor().
export const ROLE_LABELS: Record<Locale, Record<string, string>> = {
  en: { Owner: 'Owner', Admin: 'Admin', Artist: 'Artist', Client: 'Client', Everyone: 'Everyone' },
  de: { Owner: 'Inhaber', Admin: 'Admin', Artist: 'K\u00fcnster', Client: 'Kunde', Everyone: 'Alle' },
};
