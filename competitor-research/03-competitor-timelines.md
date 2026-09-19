# 03 — Competitor Product Timelines (independent research)

**Research date / all sources accessed:** 2026-09-19
**Team Calendar baseline pinned to:** repo `FEATURE_INVENTORY.md` @ commit `edbc187` (2026-08-29)

> Method. Product age = **earliest reliable primary evidence actually found**, not guessed.
> Anchors, in order: (1) official **App Store `releaseDate`** (Apple iTunes Search/Lookup API — a primary store record);
> (2) earliest **substantive** Wayback capture (a page that *is* the product, not a "coming soon" splash);
> (3) on-site founding statements; (4) registration records.
> A domain's first-ever capture is **not** product age (see Linework/Calenza/Anolla).
> If no exact date: *"Exact launch date not established from primary sources; earliest evidence: …"*.

**Evidence classes:** `Verified`=official current page · `Claimed`=marketed, depth unconfirmed · `Store`=App Store record (primary) · `Historical`=archived (may differ from today) · `Unverified`=third-party only · `Not found`=absent in sources checked (≠ proof of absence).

---

## The five most important competitors

### 1. inkStar — `inkstar.app`
Founders named on-site **Piotr Morawski & Lea Zerle** ("studio owners who happen to also code"); App Store seller **Piotr Morawski**; bundle `io.syncflux.inkstar`.
- **2026-04-22 — Earliest archived live product** (first HTTP-200 capture already the live DE product, hero *"Wir sind Studio-Inhaber, die zufällig auch coden"*). — `web.archive.org/web/20260422…/…/de/p/about-us`
- **2026-07-29 — First iOS release** `releaseDate` v1.0.8, **userRatingCount 0**. — iTunes Lookup trackId `6745954415` — `Store`
- **2026 — Current:** "appointment planner for tattoo, PMU, piercing and barber studios" (not tattoo-exclusive).
- **Age verdict: brand-new 2026 entrant, effectively pre-ratings — NOT an incumbent** (corrects prior doc's implicit "established" framing).

### 2. INKOS — `inkos.me`
Operator not established; locale `pt-PT`; built on **Emergent** no-code (`assets.emergent.sh`); manifest `name` *"INKOS · Gestão para Tatuadores"*.
- **No Wayback captures at all** (CDX→0 rows). **No App Store listing** — `Not found`.
- **2026-09-19 — Observed live** installable PWA (`start_url:/dashboard`, service worker, manifest). Routes (robots/sitemap): `bookings, clients, artists, projects, messages, inbox, settings`. Tagline *"CRM, agenda, projetos e pagamentos."* — `Verified` (thin)
- **Age verdict: recent, very low-footprint micro-entrant. Exact launch date not established from primary sources; earliest evidence = live SPA seen 2026-09-19.** Only CRM+agenda+clients+artists+projects+payments+inbox corroborated; prior doc's wider INKOS feature list is **largely Unverified**.

### 3. TatTool — `tattool.io`
Operator reported (prior doc) **Bilfi ApS** — `Unverified` ("ApS" is a Baltic/Estonian-style suffix; marketplace *Tattoodo* = "TATTOODO ApS" → possible lineage, **hypothesis only**).
- **2025-02-11 — First capture** (non-200). **2025-02-13 — Earliest substantive = pre-launch waitlist** *"TatTool — Launching soon. Your All-in-One Tattoo Studio Management Platform."* — `Historical`
- **2026 — Current:** banner **"TatTool is now in public beta."** /features: Calendar (artist **and location** availability), Reports, Payments & revenue (**online+offline payments**, deposits, verification), Consent forms, **Ink registration (ink inventory, batch tracking, data sheets)**, Flows (SMS/email/webhook automation), Clients, To-Dos, Team & Permissions. — `Verified/Claimed`
- **No iOS app** for "TatTool" — `Not found`. **Age verdict: 2025-era entrant, still public beta (2026).**

### 4. InkSchedule — `inkschedule.app`
App Store seller **FROM ASHES TO INK LLC**; bundle `com.inkschedule.app`. Prior doc's "founded by Alain Kessler" — **Unverified** (SPA, no primary source reached).
- **No substantive Wayback body** — `Not found`.
- **2026-05-12 — First iOS release** `releaseDate`, **userRatingCount 1**, curVer 2026-09-15. Store copy: calendar, client records, in-app messaging, **payments/balances/payouts**, **resident artists / guest spots / solo**, portfolio. No offline/station language. — trackId `6762936619` — `Store`
- **Age verdict: brand-new 2026 entrant.**

### 5. Ink Studio Manager — `inkstudiomanager.de` (German)
- **2024-09-19 — Earliest capture = pre-launch placeholder** *"Wir arbeiten an einer großartigen Sache – schau bald wieder vorbei!"*. — `Historical`
- **2024→2026 — Active** (~736 captures). Hero *"Nie wieder Terminchaos, No-Shows oder Zettelwirtschaft"*; documented: Termine, Kunden, **Warteliste**, **Anzahlungen**, Einnahmen, Erinnerungen, Team-/Artist-Kalender, Referenzbilder, CSV/eTermin import. — `Verified/Claimed`
- **Age verdict: domain+splash 2024-09; substantive product post-dates the splash** (late-2024/2025 copy).

---

## Remaining named competitors

### Calenza — `calenza.app` (multi-vertical barber/salon/spa/studio)
- **2025-07-10 — Only Wayback capture (single 200 row) = hosting placeholder** ("Site en construction" / OVHcloud, FR host) — **not the product**; CDX shows exactly **one** capture total. — `Historical`
- **2025-late→2026 — Live product** (post-dates the placeholder): *"booking, artist pay and checkout … books reconcile to the cent; per-artist pay auto-tallied; cash drawer reconciliation."* — `Verified/Claimed`
- No iOS app under "Calenza" — `Not found`. **Age verdict: recent entrant, product post-dates the 2025 placeholder; near-zero archive footprint. Exact launch date not established from primary sources.**

### Linework — `linework.com` ("Built by tattooers, for tattooers")
- **2000 → ~2015 — unrelated earlier use of the (lapsed & reused) domain** (2000-06-20 = domain-parking "Coming Soon / domain registered"; dense 2002–2003 captures pre-date any SaaS). **None of this is the product — do not date the product from it.** — `Historical`
- **2021 — "coming soon" placeholder** on the reused domain. — `Historical`
- **2022-11-07 — Earliest substantive product snapshot:** already the tattoo product (nav *For studios / For artists / Magazine*; *"Take the pain out of managing your tattoo [studio]"*; *Sign up for free*). — `Historical`
- **2023–2026 — Active** (nav adds *Invest*; free→paid model; 2025 snapshot shows an India-market flag). Live: bookings, services & flash, deposits, SMS/email reminders, consent, shared studio calendar, "free starting plan". — `Verified/Claimed`
- **Age verdict: tattoo product live by ≈2022; recent-but-not-greenfield. Domain history (2000) is unrelated.**

### Anolla — `anolla.com` (broad modular platform, 26 languages)
- **2018-08-06 — Earliest capture** (long-established generalist SaaS). — `Historical`
- **Tattoo positioning is a recent marketing vertical** (`/en/tattoo-software`). — `Claimed`
- **Age verdict: established generalist; tattoo positioning recent.** Far higher maturity than the entrants above.

### TattooManager — `tattoomanager.de` (German)
- **2025-01-07 — First capture** (~57). **2026 live:** *"Terminplanung, Kunden, Einverständiserklärungen, Kommunikation, Finanzen … Server in Deutschland."*
- **"150+ artists" claim NOT found on current site — Unverified.**
- Separate iOS app **"Tattoo Manager" (Peter Yermakov, 2023-02-26, 0 ratings)**; **operator match to tattoomanager.de unconfirmed (possible name collision).** — `Store`/`Unverified`
- **Age verdict: ~2024/2025.**

### InkLinka — `inklinka.com` (project-centric CRM)
- **No substantive Wayback body** — `Not found`. **2026-04-17 — Companion iOS release** (trackId `6761559803`, **0 ratings**). — `Store`
- **2026 live web:** Guest Planner for Studios, Payments & Payouts, SMS/Email Automation, Forms/Widgets/**AI Chat**, **Aftercare & Merch Sales**, **AI Business Analyst**, **Universal Stencil Maker**, Studio Efficiency Check; **Stripe**; "multi-studio" language. — `Verified/Claimed`
- **Age verdict: brand-new 2026 entrant.**

---

## Notable non-listed entrants from the independent App-Store sweep (primary `releaseDate`)

| Product | Apple seller (operator) | iOS `releaseDate` | ratings | Note |
|---|---|---|---|---|
| Tattoodo | TATTOODO ApS | **2016-03-08** | 7 175 | consumer *booking marketplace* (adjacent) |
| Tattoo Studio Pro | Zadie Studio, LLC | **2020-02-14** | 88 | "all-in-one for tattoo studios" |
| INKbusiness | INKSEARCH sp. z o.o. | **2021-10-20** | 0 | tattoo-industry business tool (PL) |
| Pixieset Studio Manager | Pixieset Media Inc. | **2025-01-16** | 2 245 | booking/payments/contracts (tattoo-adjacent) |
| Ink Link | Ink Art Media Group LLC | **2026-04-02** | 4 | booking/business for artists & studios |

*Primary sources: Apple iTunes Search/Lookup API (`releaseDate`,`sellerName`,`userRatingCount`), accessed 2026-09-19; Wayback CDX + snapshots (`web.archive.org`).*

## Pattern the timeline reveals
The "team-calendar-for-tattoo-studios" category is **young and fragmented**:
- **Most named competitors are 2024–2026 micro-entrants** — several solo-dev / no-code builds (inkStar = 1 founder-artist, 0 ratings; INKOS = Emergent no-code, 0 archives; InkLinka/InkSchedule 0–1 ratings), with thin market presence.
- **TatTool** (2025, still *beta*) and **Ink Studio Manager** (2024/25, German) are the more substantive small products.
- **A few established generalists** (Anolla, 2018-era domain; 26-language platform) sit above this tier in maturity.
- **Older adjacent consumer marketplaces** exist (Tattoodo 2016, 7k+ ratings) but are a different job (client finds artist), not studio back-office.

**Bottom line for the owner:** Team Calendar is entering a **crowded, fast-churning, low-moat segment** that is *young* — not empty, and **not** dominated by entrenched incumbents. The competitive bar to beat on *feature breadth* is inkStar/INKOS/TatTool/InkLinka/Calenza (all small & young), while the bar to beat on *trust/maturity* is low across the 2026 micro-entrants.
