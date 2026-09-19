# 01 — Competitor Landscape (independent)

**All sources accessed 2026-09-19.** Evidence classes: `Verified`(official page) · `Store`(Apple App-Store record) · `Claimed`(marketed, depth unconfirmed) · `Historical`(archived) · `Unverified`(third-party only) · `Not found`(absent in sources checked ≠ absent in product).
*"Product age" = earliest reliable primary evidence actually found (App-Store `releaseDate` first, then earliest **substantive** Wayback capture; a reused/parked domain is **not** product age).*

## Market shape (read this first)
- The category is **young, fragmented, low-moat**: the supplied "established alternatives" are mostly **2024–2026 micro-entrants** (solo-dev / no-code, 0–a-few App-Store ratings). The **real incumbents are a handful of US/Western products**: **DaySmart Body Art / InkBook** (iOS **2011**), **REV23** (site "since ~2010"), **Vagaro** (2009/2012), plus **Porter/Tattoo Studio Pro/Get Ink/Tattoogenda/Venue Ink**.
- **"Tattoo-specific"** is often aspirational: **inkStar** (tattoo+PMU+piercing+barber), **Calenza** (barber/salon/spa/studio), **Anolla** (26-language generalist), **InkLinka/InkLink** (broad) are **multi-vertical**, not tattoo-only.
- A long tail of **consumer booking marketplaces** (Tattoodo 2016 / inckd. / TATM / TRAZA / InkPick / Book-ink) is **adjacent**, not studio back-office. **AI-tattoo-generators and kids' tattoo makers are excluded** (hundreds exist; no overlap).

---

## Team Calendar (the subject)
- **Company:** not disclosed in repo; ships **EN + DE** ⇒ **DACH** orientation. Stack Next.js + Firebase. *(Firm/legal entity — product-owner item.)*
- **Product age:** baseline pinned to repo commit `edbc187`, **2026-08-29**; public site is a feature-showcase GitHub Pages build.
- **Status:** pre-GA. **live** core = staff scheduling + workstation-resource + conflict + buffer + reference images + full commission ledger (checkout/month-close/locked) + offline PWA + notifications + roles. **simulated/unverified** = client self-booking, reminders, reviews/waitlist/social/GDPR backends. **undeployed** = multi-tenant. **planned** = Stripe deposits, consent client-flow, team messaging, reporting, theming, public API.
- **Positioning today (repo):** "replaces paper sheet + group-chat schedule + who-owes-who spreadsheet"; differentiators = ledger, chairs-as-resources, reference images, self-reschedule link, review→10%-off funnel, multi-tenant.

## TatTool — `tattool.io`
- **Operator:** reported **Bilfi ApS** (`Unverified`); *possible* lineage with marketplace **Tattoodo** ("TATTOODO ApS") — hypothesis only.
- **Age:** first capture **2025-02** was a *"Launching soon"* waitlist page ⇒ web evidence 2025; still **"public beta"** in 2026 (`Verified`). **No iOS app** (`Not found`).
- **Pricing:** **$49/$119/$249/$399 per month**, seat bands 3/10/25/50, USD, tax at checkout; **trial, no free tier** (`Verified`).
- **Primary features (`Verified`/`Claimed`):** Calendar (**artist + location** availability, consultations, **time-off, guest spots, location closures**), Reports (revenue/utilisation/**targets/forecasts**), Payments (**online+offline payments, deposits, verification**), **Consent forms**, **Ink registration (ink inventory, batch, data sheets, booking usage)**, Flows (**SMS/email/webhook automation**), Clients, **To-Dos**, Team & Permissions.
- **Positioning:** "the connected toolkit behind every tattoo appointment" — a **broad studio operating system** with the widest documented *tattoo-native* surface (notably ink registration & automation). **Most serious "operating-system" rival among the supplied set.**

## inkStar — `inkstar.app`
- **Founders/operator:** **Piotr Morawski & Lea Zerle** (on-site); App-Store seller **Piotr Morawski**; bundle `io.syncflux.inkstar`. Solo/small build.
- **Age:** earliest live capture **2026-04-22**; **iOS first release 2026-07-29**, `userRatingCount 0` (`Store`). ⇒ **brand-new 2026; effectively pre-ratings — NOT an incumbent.**
- **Multi-vertical:** "appointment planner for tattoo, **PMU, piercing and barber** studios."
- **Pricing:** **€8.99 / €29 / €99** (Starter/Plus/Pro, Pro=5 users), EUR, 7-day no-card trial, ~44% annual (`Claimed`), **SMS €0.12/msg** (`Verified`).
- **Primary features:** deposits-before-booking + **keep deposit on no-show**, **24h & 2h SMS/email reminders**, **AI slot-fill + online self-book/reschedule + waitlist auto-backfill**, intake/**consent (photo-consent, medical, allergy, QR e-sign, GDPR)**, **offline-first "works across devices even offline"**, **commission tracking**, **multi-company/locations**, Google/Apple calendar, **AI assistant + voice**, gift cards, analytics.
- **⚠️ CRUCIAL:** inkStar advertises **0 "station"** — its resource dimension is **locations**, and its "chair" language is idiomatic → the prior report's *"inkStar already books stations"* is **not supported**. Also: several features TC's own repo marks *simulated/unverified* (online booking, 24h reminders, self-reschedule) **inkStar markets as shipping**. **Conceptually the closest rival by feature surface.**

## INKOS — `inkos.me`
- **Operator:** not established. **Locale `pt-PT`** (Portuguese/Brazilian). Built on **Emergent** no-code builder (`assets.emergent.sh`). Manifest `name`: *"INKOS · Gestão para Tatuadores"*.
- **Age:** **0 Wayback captures; no App-Store listing.** ⇒ recent, very low-footprint; exact launch **not established**; earliest evidence = live SPA seen 2026-09-19.
- **Status:** installable **PWA** (`start_url /dashboard`, standalone, service worker). **Verified** in-product routes (`robots.txt`/`sitemap.xml`): `bookings, clients, artists, projects, messages, inbox, settings`; tagline *"CRM, agenda, projetos e pagamentos."*
- **Prior-report feature list** (unified inbox, flash-days, gift cards, inventory, Google 2-way sync, campaigns, analytics…) = **largely `Unverified`** — only CRM/agenda/projects/payments/inbox corroborated; minified-bundle keyword hits are substring-noise (`async`→`sync`, Firebase auth→"Google").
- **Positioning:** all-in-one tattoo studio PWA. **The prior report over-rated INKOS's breadth on evidence.**

## InkSchedule — `inkschedule.app`
- **Operator:** App-Store **FROM ASHES TO INK LLC**; `com.inkschedule.app`. Prior report's "founder Alain Kessler / side project" = **`Unverified`** (SPA; no primary source reached).
- **Age:** no substantive Wayback body; **iOS first release 2026-05-12**, `userRatingCount 1` (`Store`). ⇒ **brand-new 2026.**
- **Pricing:** **$29 / $79 / $149** (Solo 1 artist / Studio ≤5 / Enterprise ∞+multi-loc), USD; **trial length self-contradicts (14-day vs 30-day)**; Stripe deposits (`Verified`).
- **Features (`Store` copy):** calendar, client records, **in-app messaging**, **payments/balances/payouts**, studio & artist settings, **resident artists / guest spots / solo**, portfolio. **No offline, no station** language.
- **Positioning:** "run the business side of your work"; strong **booking + deposits + reminders + waitlist + analytics** story with a "less admin" message. Prior report's waitlist/analytics/API/AI claims **not established on reachable primary pages** → `Unverified`.

## Ink Studio Manager — `inkstudiomanager.de` (German)
- **Operator:** not established (impressum client-rendered). **German-language, DACH**.
- **Age:** first capture **2024-09-19** was a *"coming soon"* placeholder; **~736 captures** ⇒ active late-2024/2025. Substantive product **post-dates the 2024 splash.**
- **Pricing:** **€35 per artist / month (net)** flat, 14-day trial (`Verified`).
- **Features (`Verified`/`Claimed`):** online + team/artist calendar, customers, **Warteliste**, **Anzahlungen**, Einnahmen, **Erinnerungen (reduce no-shows)**, **"keine Doppelbuchungen"**, Referenzbilder, CSV/eTermin import. **Station / offline / multi-tenant / cash-reconciliation not found.**
- **Positioning:** *"Nie wieder Terminchaos, No-Shows oder Zettelwirtschaft"* — clean **German** simplicity; a **direct DACH rival** to TC's German audience.

## TattooManager — `tattoomanager.de` (German)
- **Operator:** not established. **German**, "Server in Deutschland", **DSGVO-konform** (`Verified`).
- **Age:** first capture **2025-01-07** (~57). A **separate iOS "Tattoo Manager" (Peter Yermakov, 2023-02-26)** exists — **operator match unconfirmed** (likely name-collision).
- **Pricing:** **€19.99 → €399.99** tiers (Basic→Ultra+), EUR net, 30-day trial all tiers, SMS incl. Pro+ (`Verified`).
- **Features:** customer & tattoo DB, online bookings, communication, finances, **consent/dokumentation**, **Kundenportal**. Prior report's **"150+ artists" NOT found on the site → `Unverified`**. **"Weniger Doppelbuchungen — Räume, Artists und Zeiten sauber koordiniert" + "Termine, Pausen und Ressourcen" (room/resource Station/offline/multi-tenant/cash-reconciliation **not found**. break coordination) AND email+SMS "Automatische Erinnerungen … reduzieren No-Shows" — `Verified`; true per-station capacity/conflict, offline Station/offline/multi-tenant/cash-reconciliation **not found**. cash-reconciliation still not found.
- **Positioning:** established **German all-in-one** (customers/tattoos/bookings/communication/finances).

## InkLinka — `inklinka.com` (project-centric CRM)
- **Operator:** not established (footer legal page returned nothing). **Companion iOS app 2026-04-17, 0 ratings** (`Store`) ⇒ brand-new.
- **Pricing:** SPA-gated; **numeric plan prices not disclosed**; app-bundle strings imply **~5% platform fee on deposits + Stripe fee charged to client** (`Claimed`). Multi-currency.
- **Features (`Verified`/`Claimed`):** Request→Booking→Deposit→Client→**Project**→Session model; **Guest Planner for Studios**, **Payments & Payouts**, **SMS/Email automation**, Forms/Widgets/**AI Chat**, **Aftercare & Merch sales**, **AI Business Analyst**, **Universal Stencil Maker**, Studio Efficiency Check; **Stripe**; "multi-studio" language.
- **Positioning:** connects information *around* an appointment (a direct idea-collider with TC). Broad feature surface for a brand-new product; **station/offline not found**.

## Linework — `linework.com` ("Built by tattooers, for tattooers")
- **Age (corrected):** domain first captured **2000** = a **domain-parking "Coming Soon"** page, **unrelated occupant**; product live by **≈2022**, dense captures from 2022. ⇒ **recent-but-not-greenfield; do NOT date from 2000.**
- **Pricing (`Verified`):** **genuinely free $0 Artist/Studio with ALL features but a 6% transaction fee; Pro $19 drops to Stripe 2.9%+30¢; unlimited texts $0.** (Free-to-start claim **verified true**.)
- **Features:** personal booking pages, services & **flash**, **deposits**, **SMS/email reminders**, **consent forms**, shared studio calendar, artist visibility. Booking-first; simpler than INKOS/inkStar/TC.
- **Positioning:** free-start booking + studio calendar; TC beats it on resource conflict / ledger / offline / multi-tenant / admin depth.

## Calenza — `calenza.app` (multi-vertical: barbershops/salons/spas/studios)
- **Age:** only Wayback capture (**single** 200 row) was an OVHcloud *"Site en construction"* placeholder ⇒ **product post-dates 2025-07**; near-zero archive footprint.
- **Pricing:** **not publicly disclosed** (no `/pricing`; only demo-gated).
- **Features (`Verified`):** booking (sessions + **walk-ins**), statuses **paid/no-show/rescheduled/restored**, **commissions (commission/salary/hybrid)**, **checkout/POS + deposits/split payment**, **cash-drawer reconciliation** (*expected cash = collected − payouts*), **reports day→year + export**, **one-tap payday + payout trail**. **Station / offline / consent / multi-tenant not found.**
- **Positioning:** *"books reconcile to the cent"* — **the strongest FINANCIAL comparator** (POS + commissions + cash drawer). Closest head-to-head to TC's ledger, **but no evidence of month-close/locked-months/carry-forward** → TC's ledger angle still distinct; TC lacks Calenza's **POS/cash-drawer**.

## Anolla — `anolla.com` (broad modular generalist, 26 languages)
- **Operator/geography:** established SaaS generalist (domain archived since **2018**); `/en/tattoo-software` is a recent **marketing vertical**, not a dedicated product line.
- **Pricing:** **free core, usage-based**, *"fee applies only after the job is confirmed"*, paid **Boost/add-ons** — **model `Verified`, numbers not published.**
- **Features (`Claimed`):** online booking, artist calendars, clients, appointments, payments/**POS**, marketing automation, modular add-ons, scalable **multi-studio/user/client**, AI; **Multi-Resource Booking (workstations/booths/equipment)**, **inventory**, **gift cards**, **flash**, waitlist.
- **Positioning:** **broadest product surface of all**, but **generic** — TC's edge vs it is *tattoo-specific depth*, not breadth. It is the clearest evidence that **"multi-resource/station booking" exists in the market (at a generalist).**

---

## Additional competitors surfaced by the independent scan (beyond the supplied 10)
Full detail + per-candidate fields in `_research/raw/discovery.md`. Highlights (all App-Store-validated `Store` unless noted):

| Product | Operator | iOS releaseDate | Geo | Class |
|---|---|---|---|---|
| **DaySmart Body Art / InkBook** | DaySmart Software LLC | **2011-11-03** | US | **Direct — true incumbent** |
| **REV23** | Painful Pleasures LLC | 2024-10-17 (site "since 2010") | US | **Direct — body-art suite, established** |
| **Tattoo Studio Pro** | Zadie Studio LLC | **2020-02-14** | US | Direct |
| **Porter** | Porter Apps Inc. | 2023-04-03 | global | Direct (POS + auto commissions) |
| **Get Ink** | Get Ink Ltd | 2024-11-01 | UK | Direct |
| **Tattoogenda** | Inksane | 2023-10-02 | EN | Direct |
| **Venue Ink** | Venue Live Tech Inc | 2025-04-08 | US/CA/GB | Direct |
| **Taddoo** | Tattoomii GmbH | **2026-06-24** | **DE, 9 langs** | **Direct — closest German twin (offline+waitlist+guest)** |
| **NeedleFlow** | VITALII SHVETS | 2026-06-06 | **DE** | Direct (German, offline, analytics) |
| **InkManager** | David Gonzalez Lazaro | 2026-03-31 | **ES** | Direct |
| **Inkoru** | Vicente Ferri Garcia | 2025-05-30 | **ES** | Direct (**books per "cabina" = chair/station**) |
| **Tat2App** | TAT2APP CS LLC | 2026-06-01 | US/KZ | Direct (**chairs, multi-location**) |
| **Damin** | (DE cross-vertical) | — | **DE** | **Cross-vertical salon/tattoo POS w/ *device* booking** |
| **ellume** | ellume GmbH | 2025-04-15 | **DE** | Cross-vertical studio mgmt |
| Pixieset | Pixieset Media Inc | 2025-01-16 | — | **EXCLUDED — photography, mis-listed** |
| INKbusiness | INKSEARCH sp.z o.o. | 2021-10-20 (frozen 2022) | PL | **Dormant** |

**Adjacent (excluded from direct set):** consumer marketplaces **Tattoodo** (2016, 7k+ ratings), inckd.(AG, CH), TATM, TRAZA(PTY, AU), InkPick, Book-ink, World of Ink; single-purpose consent/forms tools (Wavrr NL, InkForm, NeedleNote).
**Excluded:** AI tattoo generators / AR try-on / kids' tattoo makers / procreate brushes (no overlap).

## Community-sourced competitor **leads** (from the pain-point pass — NOT yet verified; do not cite as settled)
Surfaced inside r/TattooArtists booking threads; each carries a **founder/self-promo conflict of interest** (see caveat):
| Lead | URL | What we actually saw | Status |
|---|---|---|---|
| **Blackbook** | (app; pitched *in-thread*) | a founder *"opened Blackbook… offering **free lifetime access** to artists who join"* + posts *"I built a booking app"* | **Unverified** lead — a rival, but a self-promoted one |
| **tattooschedule.com** | tattooschedule.com | a *"tattooschedule.com"* promo DM, pitched *"a more natural [booking]… alternative"* | **Unverified** — no operator/app record reached |
| **tattooschedule.com** | tattooschedule.com | referenced as an *"alternative"* to paper/DM booking (community thread) | **Unverified** |
| **tattooschedule** | (app) | *"DM me your booking software"*-style founder DMs | **Unverified** |
**Integrity caveat.** The same *"what do you use to book clients?"* threads are **vendor-farmed**: a 2018 self-disclosed **"paid research"** post, *"I opened Blackbook… free lifetime access"*, and *"built an app… DM me"*. These are **promotional astroturfing**, so any quote from them is **Claimed/Unverified**, never community consensus. (Recorded so the reader discounts them accordingly.)

## Maturity context (the honest frame for §Market shape)
App-Store rating counts (iTunes Lookup, read 2026-09-19): **generic incumbents dominate the installed base** — Square Appointments **195,291**, Booksy **856,739**, Vagaro Pro **15,686**, marketplace Tattoodo **7,175**; whereas the **tattoo-*named* field is brand-new and essentially unreviewed** (inkStar 0, InkLinka 0, InkSchedule 1, Taddoo 0, NeedleFlow 0). **Implication:** Team Calendar's real displacement battle is against **"Square + a spreadsheet"** and generic salon tools, **not** against entrenched tattoo suites — and its 2026 cohort rivals have, at writing, **no meaningful review moat**.
