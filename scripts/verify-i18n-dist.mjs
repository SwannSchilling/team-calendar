// Verify the built EN + DE pages: lang, meta, content, row counts, no cross-leak.
import { readFileSync } from 'node:fs';

const dist = 'F:/GithubProjects/codrops-barbajs-page-transition/dist/';
const en = readFileSync(dist + 'index.html', 'utf8');
const de = readFileSync(dist + 'de/index.html', 'utf8');
let problems = 0;
const fail = (m) => { problems++; console.log('  PROBLEM:', m); };
const ok = (m) => console.log('  ok:', m);
const has = (hay, s, label, must = true) => {
  const found = hay.includes(s);
  if (must ? found : !found) ok(label);
  else fail(label + ' (present=' + found + ')');
};
const count = (hay, s) => hay.split(s).length - 1;

console.log('--- EN (/) ---');
has(en, '<html lang="en">', 'html lang=en');
has(en, '<link rel="alternate" hreflang="en"', 'hreflang en');
has(en, '<link rel="alternate" hreflang="de"', 'hreflang de');
has(en, 'hreflang="x-default"', 'hreflang x-default');
has(en, '<link rel="canonical" href="https://SwannSchilling.github.io/team-calendar/"', 'canonical EN');
has(en, '<title>Team Calendar — the studio scheduler', 'EN title');
has(en, 'One app retires', 'EN hero A');
has(en, 'Showing 81 of 81 features', 'EN count');
has(en, 'aria-current="page"', 'EN lang toggle active');
if (count(en, 'class="inv-row"') !== 81) fail('EN inv-row count ' + count(en, 'class="inv-row"'));
else ok('EN 81 inventory rows');
has(en, 'Zeige ', 'no DE count leak', false);
has(en, 'Stuhl 1', 'no DE mock leak', false);
has(en, 'Motivvorlagen', 'no DE mock leak 2', false);

console.log('--- DE (/de/) ---');
has(de, '<html lang="de">', 'html lang=de');
has(de, '<link rel="alternate" hreflang="de"', 'hreflang de');
has(de, '<link rel="canonical" href="https://SwannSchilling.github.io/team-calendar/de/"', 'canonical DE');
has(de, '<meta property="og:locale" content="de_DE"', 'og locale de_DE');
has(de, '<title>Team Calendar — Schluss mit Zetteln und guten Vorsätzen</title>', 'DE title');
has(de, 'og:title" content="Team Calendar — Schluss mit Zetteln', 'og:title DE tagline');
has(de, 'Schluss mit Zetteln und guten Vorsätzen', 'DE hero');
has(de, 'Zeige 81 von 81 Funktionen', 'DE count');
has(de, 'Einen Tag miterleben', 'DE CTA');
if (count(de, 'class="inv-row"') !== 81) fail('DE inv-row count ' + count(de, 'class="inv-row"'));
else ok('DE 81 inventory rows');
has(de, 'Stuhl 1', 'DE day grid chair');
has(de, 'Motivvorlagen', 'DE refs copy');
has(de, 'Künstler-Ansicht', 'DE ledger view');
has(de, 'Kein Login fürs Verschieben', 'DE flow foot');
has(de, 'Ein Login', 'DE tenant');
has(de, 'Rollen · wer was sieht', 'DE matrix');
has(de, 'Hallo Alex', 'DE link mock');
has(de, 'Abwesenheit', 'DE timeoff label');
has(de, 'Deployment ausstehend', 'DE status label');
has(de, 'Showing 81 of 81 features', 'no EN count leak', false);
has(de, 'One app retires', 'no EN hero leak', false);

console.log(problems === 0 ? 'DIST VERIFY OK' : problems + ' problems');
process.exit(problems === 0 ? 0 : 1);
