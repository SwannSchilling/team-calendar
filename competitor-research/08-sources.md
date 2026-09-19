# 08 — Source Register (independent research)

**Access date for every external source below: 2026-09-19** unless otherwise noted. Team Calendar internal baseline pinned to repo commit `edbc187` (2026-08-29).

**Evidence tiers:** `T1` official (product pages / pricing / legal / App-Store record / the repo) · `T2` historical (Wayback / CDX) · `T3` independent/community (App-Store rating counts, review pages — customer signal only).

**Classification vocabulary used across deliverables:** `Verified` (primary/official) · `Store` (Apple record) · `Claimed` (marketed, depth unconfirmed) · `Historical` (archived state) · `Unverified` (third-party only) · `Not found` (absent in sources checked — **not** proof of absence in-product).

## Method & tooling-honesty note (read first)
- **`web_search` tool was non-functional** (upstream HTTP 401) and a **Firecrawl** keyless path was **quota-exhausted**; generic search-engine scraping (**Bing RSS / DuckDuckGo-lite**) proved **unreliable / stale-cached** (served near-identical tattoo-*idea* results regardless of query, then bot-challenged).
- **Consequence:** load-bearing corroboration here is **primary-source only** — the vendor's own official pages, the **Apple App-Store lookup API** (`releaseDate`/`sellerName`/`bundleId`/`userRatingCount`/full description), and **Wayback CDX** (`web.archive.org/cdx`, statuscode:200, matchType domain|prefix) for age; archived page bodies read via `web.archive.org/web/<TS>id_/…`.
- **Anti-fabrication rule applied:** no launch date is asserted that was not *observed*; "product age" is phrased as **earliest reliable evidence found**, not "founded"; a first Wayback capture is **not** treated as product age (reused/parked domains — see Linework 2000, Calenza 2025, Ink Studio Manager 2024 placeholders).
- Raw evidence bank (working artifacts): `_research/raw/` (`pricing.md`, `discovery.md`, `inklinka.com__*`, `tm_*`, `lw_home.txt`, `an_tattoo.txt`, `tm_*`).

---

## Team Calendar (subject) — internal baseline
- `FEATURE_INVENTORY.md` @ commit `edbc187` (2026-08-29) — **authoritative self-aware baseline** (81 features, 11 categories, status flags). `T1`
- `docs/Team-Calendar_Competitor-Research_Comparison.md` (853 lines) — the **hypothesis under test** (over-optimistic ✓ marks; refuted in part). `T1(claim)`
- `docs/Team-Calendar-DE-Korrektur_ueberarbeitet.md` + `docs/DE-Korrekturen…` — TC's own copy drafts; **§5 explicitly forbids** "keine Doppelbuchungen", "DSGVO-sicher", "zero no-shows", "rechtssicher". `T1`
- `FEATURE_INVENTORY.md` §"caveats for copywriters" — do **not** claim real-time online booking / GDPR self-service / automatic reminders until product-owner confirms. `T1`

---

## Core named competitors (supplied list) — primary sources
**TatTool**
- https://www.tattool.io/ — `T1` — "public beta", positioning copy ("…without double-booking artists")
- https://www.tattool.io/features — `T1` — ink registration (batch/data-sheets), "checks **artist and location** availability", location closures, To-Dos, online+offline payments
- https://www.tattool.io/pricing — `T1` — $49/$119/$249/$399, seats 3/10/25/50, trial, no free tier (USD)
- Wayback CDX first-200 = **2025-02-11**; 2025-02-13 = *"Launching soon"* waitlist — `T2` — age; no iOS app (iTunes search: none)
- Operator **Bilfi ApS** = `Unverified` (not on site); Tattoodo-lineage = hypothesis

**inkStar**
- https://www.inkstar.app/en/p/home — `T1` — founders *Piotr Morawski & Lea Zerle*; "empty chair" idiomatic; multi-vertical
- https://www.inkstar.app/en/p/features — `T1` — **0 "station"**; commission tracking; multi-company/location; offline-first
- https://www.inkstar.app/en/p/pricing — `T1` — €8.99/€29/€99; SMS €0.12/msg; 7-day trial
- iTunes Lookup id **6745954415** — `T1/Store` — bundleId `io.syncflux.inkstar`, **releaseDate 2026-07-29**, `userRatingCount 0`, full copy (offline×17, deposit, AI, waitlist, GDPR) — **station hits = 0**
- Wayback first-200 = 2026-04-22 — `T2`

**INKOS**
- https://inkos.me/manifest.webmanifest / robots / sitemap — `T1` — **PWA on `assets.emergent.sh`** (no-code); routes `bookings,clients,artists,projects,messages,inbox,settings`; pt-PT; "CRM, agenda, projetos e pagamentos"
- iTunes search "INKOS"/"INKOS me" — `Store` — **no App-Store listing**
- Wayback CDX = **0 captures** — `T2` — recent/low footprint; broad prior-report feature list = **Unverified**

**InkSchedule**
- https://inkschedule.app — `T1` — SPA; calendar/clients/messaging/payments/payouts/guest spots/portfolio
- iTunes Lookup (bundle `com.inkschedule.app`, seller **FROM ASHES TO INK LLC**) — `Store` — **iOS 2026-05-12**, ratingCount 1 — "founder Alain Kessler" = **Unverified**
- https://inkschedule.app pricing (in-page) — `T1` — $29/$79/$149; Stripe; **trial 14d-vs-30d contradiction recorded**

**Ink Studio Manager**
- https://inkstudiomanager.de — `T1` — hero "Nie wieder Terminchaos, No-Shows oder Zettelwirtschaft"; "Keine Doppelbuchungen mehr"; **Warteliste / Anzahlungen / Erinnerungen**; Team-Kalender; Referenzbilder
- https://inkstudiomanager.de#Preise — `T1` — **€35 per artist / month (net)**, 14-day trial
- Wayback CDX first-200 **2024-09-19** = "coming soon" splash; ~736 captures → active late-2024/2025 — `T2`

**TattooManager**
- https://tattoomanager.de — `T1` — Terminplanung/Kunden/Einverständniserklärungen/Finanzen; "Server in Deutschland"; **no "150+" found → Unverified**
- https://tattoomanager.de/preise/ — `T1` — €19.99→€399.99 (6 tiers), 30-day trial all tiers
- Wayback CDX first **2025-01-07** (~57) — `T2` — iOS "Tattoo Manager" (**Peter Yermakov**, 2023-02-26) = **possible name collision, unconfirmed**

**InkLinka**
- https://inklinka.com/en , `/en/why-inklinka`, `/en/guest-visit-planner`, `/en/payments-payouts`, `/en/sms-email-automation`, `/en/business-analytics`, `/en/tattoo-stencil-maker`, `/en/aftercare-merch-sales`, `/en/studio-efficiency-check`, `/en/pricing`, `/en/privacy`, `/en/terms` — `T1` — feature set, Stripe, "multi-studio", **~5% platform fee (Claimed, app-bundle i18n)**
- iTunes (companion app **2026-04-17**, 0 ratings) — `Store` — brand-new; station/offline **not found**

**Linework**
- https://www.linework.com/ , https://linework.com/pricing — `T1` — "Built by tattooers, for tattooers"; **Free $0 all features + 6% txn fee; Pro $19 → Stripe 2.9%+30¢**; "free starting plan" = Verified
- Wayback: domain 2000 = **parking/"Coming Soon"** placeholder (unrelated occupant); product live ≈**2022** — `T2` — age corrected

**Calenza**
- https://calenza.app/studio — `T1` — POS + commissions (commission/salary/hybrid) + **cash-drawer reconciliation** ("expected cash equals collected minus payouts"), "books reconcile to the cent", checkout, reports day→yr+export, walk-ins; **multi-vertical** (barber/salon/spa/studio); **no station/offline/consent**
- https://calenza.app — `T1` — **no /pricing (404); pricing "not publicly disclosed"**; iTunes "Calenza" = Not found
- Wayback single 200 row = OVHcloud "Site en construction" placeholder (post-2025-07) — `T2`

**Anolla**
- https://anolla.com/en/tattoo-software — `T1` — **Multi-Resource Booking (workstations/booths/equipment)**, Resource Management, inventory, gift cards, flash, waitlist, multi-studio, AI; 26 languages; **free core + usage-based fee "applies only after the job is confirmed" (model Verified, number Unverified)**
- Wayback CDX domain-since **2018** — `T2` — mature generalist; tattoo = one marketing vertical

## Independently discovered competitors — Apple App-Store lookup (`T1/Store`, primary)
`releaseDate`/`sellerName`/`bundleId`/`userRatingCount` observed 2026-09-19:
- **DaySmart Body Art / InkBook** id **475331193** (DaySmart Software LLC) — iOS **2011-11-03** — 275 ratings — true incumbent (US)
- **REV23** id **1530843532** (Painful Pleasures LLC) — iOS 2024-10-17 (site "since ~2010") — 26 ratings
- **Tattoo Studio Pro** id **1490817384** (Zadie Studio LLC) — iOS **2020-02-14** — 88 ratings/3.44★ — ⚠️ public $99/$149 = one-time *website templates*, not the (unpriced-IAP) plan
- **Porter** id **1663516602** (Porter Apps Inc.) — 2023-04-03 — 43/4.23★ — POS + **auto commissions**
- **Get Ink** id **6737286787** (Get Ink Ltd) — 2024-11-01 — 4 — **UK**
- **Tattoogenda** id **6461407749** (Inksane) — 2023-10-02 — 1
- **Venue Ink** id **6741823955** (Venue Live Tech Inc) — 2025-04-08 — 75/4.41★
- **Taddoo** id **6781711821** (Tattoomii GmbH) — **2026-06-24** — 0 — **DE, 9 langs** — live booking-link + **online deposit** + Google/Apple mirror + guest-spot days + no-show protection (App Store copy) — *no multi-tenant/ledger/station evidence*
- **NeedleFlow** id **6772499648** (VITALII SHVETS) — **2026-06-06** — 0 — **DE** — body-map, iCloud/Google/Outlook sync, finance analytics, 8-lang templates
- **Inkoru** id **6746192185** (Vicente Ferri Garcia) — 2025-05-30 — **ES** — books per **"cabina" (=chair/station)**
- **Tat2App** id **6758329610** (TAT2APP CS LLC) — 2026-06-01 — 6/5★ — **chairs + multi-location**
- **InkManager** id **6756239513** — 2026-03-31 — **ES** · **InkDesk** id **6762023231** (Inkdesk Inc.) 2026-05-18 · **CO:CREATE** id **6756740021** (Gesso Labs) 2026-02-02 · **Ink Link** id **6746192185**/*`myinklink.io`* (Ink Art Media Group LLC) 2026-04-02 · **TATUS** id **6785027276** 2026-07-09 · **TATTOO CRM** id **6808848845** (Pavlo Ptitsyn) 2026-09-08 *local-first* · **Seance Studio** id **6741437193** 2026-02-02 *offline* · **Stenz** id **6762186379** 2026-05-17 · **ellume** id **6739249102** (ellume GmbH) 2025-04-15 *DE*
- **InkLinka** companion iOS — 2026-04-17 — 0

## Adjacent / excluded (context, not direct)
- **Tattoodo** (TATTOODO **ApS**) id via iTunes — iOS **2016-03-08**, **~7,175 ratings** — `Store` — **consumer marketplace = ADJACENT** ("ApS" ties to TatTool's reported *Bilfi ApS* → lineage hypothesis only). inckd.(AG CH), TATM, TRAZA(PTY AU), InkPick, Book-ink, World of Ink — marketplaces. Wavrr(NL), InkForm, NeedleNote — consent/forms only. **Damin** (Hamburg, *Geräte*-booking) & **ellume** & **Vagaro** — cross-vertical. Generic to-beat set: Square Appointments/Fresha/Booksy/Calendly/Mindbody/Acuity/BookedIN.
- **EXCLUDED:** AI tattoo generators / AR try-on / kids' tattoo makers / Procreate brushes. **Pixieset Studio Manager** id 2025-01-16 = **"BOOKING & SCHEDULING FOR PHOTOGRAPHERS"** (photo gallery/proofing/print suite) → **mis-listed, dropped**. **INKbusiness** (INKSEARCH sp.z o.o.) iOS 2021-10-20 frozen 2022-06, site = "Coming Soon" → **dormant**.

## Community / independent corroboration (T3)
- App-Store **rating counts** above are the strongest available *traction* signal (most 2026 entrants = **0–few** ⇒ minimal public adoption).
- Direct Reddit/Trustpilot text corroboration was **not reliably obtainable** through the non-functional search paths this run; community claims are therefore **labelled as customer/community evidence only** and, where unobtainable, marked **Unknown** rather than paraphrased.

## Tooling provenance (reproducible)
`_research/fetch.py` (page→text, `--links`) · `_research/idcheck.py` (identity/keyword scan) · `_research/itunes.py` (`search`/`--ids` → Apple Lookup) · `_research/wbq.py` (Wayback CDX first/last/count, statuscode:200) · `_research/search.py` (Bing RSS — **flagged unreliable**). Windows console Unicode handled via `sys.stdout.reconfigure(encoding='utf-8',errors='replace')` + `PYTHONIOTENCODING=utf-8`.

> *This register is the honest ceiling of the evidence: every "Verified/Store" line traces to a primary URL/API above; anything not traceable is marked Claimed/Unverified/Not found, never asserted.*

## Pain-point pass — provenance & explicit evidence limits
- **Corpus:** `_research/raw/painpoints.md` (109 machine-extracted quotes / 110 citations) over `_research/raw/reddit/corpus.jsonl` (628 posts+comments) + `_research/raw/web/` (cached page text w/ SOURCE-URL/ACCESSED lines). **Quotes were extracted programmatically from caches (not retyped)** — wording/typos are the sources'. Access 2026-09-19.
- **Access method:** Reddit `.json` is bot-blocked (**403**) → harvested via public **Atom** feeds (`search.rss` + per-thread `.rss` comment feeds); ~50% of calls hit **429** → repeated+deduped.
- **Blocked and *recorded* (NOT invented around):** Trustpilot **403** · G2 **403** · Capterra **404** on probed slugs · App-Store review RSS **500** · Google-Play pages returned **no review text** · Quora **403** · every general engine (DDG html/lite, Ecosia, Startpage, searx, Google SERP) **bot-walled**. ⇒ Review-site corroboration is **absent by access**, not by absence of signal.
- **INKOS:** `inkos.me` = reachable **JS-only shell** (no static page text) → **nothing citable** about it beyond what `idcheck`/`manifest` give; its breadth stays **Unverified**.
- **Community-lead integrity flags** (see `01`): several "what do you use to book?" threads are **vendor-farmed** (self-disclosed paid-research 2018; *"free lifetime access to the app I built"*; *"DM me your booking software"*) → treated as **Claimed/Unverified**, never consensus. Leads **Blackbook / tattooschedule.com / tattoostudio-schedule** recorded in `01` as **unverified** leads only.
- **Offline-demand limit:** the *only* community offline signal was **1** weak infra-hobby hit → offline's *demand* is **Unknown**, its *existence as a rival claim* is `Verified` (inkStar hero). Kept apart deliberately.
> All numeric *traction* above (Square 195,291 · Booksy 856,739 · Vagaro Pro 15,686 · Tattoodo 7,175 · inkStar/InkLinka 0 · InkSchedule 1) is **`T3`, machine-read from iTunes Lookup**, not sampled.
