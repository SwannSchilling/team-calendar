# Team Calendar — Independent Competitor Research (Capstone Report)

**Prepared 2026-09-19.** An adversarial re-verification of `docs/Team-Calendar_Competitor-Research_Comparison.md`, treated as a **hypothesis to challenge, not truth**. Objective: *discover the truth, not a flattering report.* Companion files: `01` landscape · `02` feature matrix · `03` timelines · `04` pricing · `05` pain points · `06` gap analysis · `07` positioning · `08` source register. Team Calendar facts are pinned to the repo's own `FEATURE_INVENTORY.md` @ `edbc187` (2026-08-29).

---

## 1 · Executive summary (the honest version)
1. **The "established alternatives" are mostly not established.** The supplied list is dominated by **2024–2026 micro-entrants** (solo-dev / no-code): inkStar (iOS **2026-07**, 0 ratings), InkSchedule (iOS **2026-05**, 1 rating), INKOS (**0** Wayback captures, built on the *Emergent* no-code builder, **no** App-Store app), InkLinka (**2026-04**), Taddoo/NeedleFlow (**2026-06**). The **actual incumbents** are a short US list: **DaySmart Body Art / InkBook (iOS 2011)**, **REV23 (~2010)**, **Vagaro (2009/12)**, plus Porter/Tattoo-Studio-Pro/Get-Ink/Tattoogenda/Venue-Ink. **Traction is the tell (App-Store rating counts, machine-read):** the tattoo-*named* field is brand-new plus Porter/Tattoo-Studio-Pro/Get-Ink/Tattoogenda/Venue-Ink. unreviewed (inkStar **0**, InkLinka **0**, InkSchedule **1**), while the *real* installed base is **generic tools** — Square Appointments **195,291**, Booksy **856,739**, Vagaro Pro **15,686**, plus marketplace Tattoodo **7,175**. The true competitor is therefore "Square + a spreadsheet", not another tattoo app.
2. **Two "features" the market treats as table-stakes are, for Team Calendar, currently NOT real:** *online client self-booking* is **`sim`** (mock slots, no server) and *automated reminders* are **`unv`** (no scheduled Cloud Function in the repo). Both are advertised in the old report as ✓. They must be treated as **roadmap**, not capability.
3. **Two of Team Calendar's most-advertised USPs were over-rated, but the *flagship* one survived an adversarial test.** inkStar advertises **0 "station"** on both its site *and* App-Store copy (its "chair" is idiomatic) → the prior report's *"inkStar already has station booking"* is **refuted**. Room/resource coordination *does* exist elsewhere (Anolla=workstations verified; Inkoru "cabina"; Tat2App "chairs"; **TattooManager "Räume"**) — so the honest claim is **the combination** (chair **+** per-station conflict **+** buffer **+** absence, checked pre-save), **not** the bare idea.
4. **Team Calendar's genuinely hard-to-copy ground is the money-and-floor layer**: a **transaction-level artist/shop ledger with checkout → month-close → locked periods → carry-forward** (`live`), which **no competitor advertises** those close/lock semantics for, and the **offline browser-PWA** (`live`; rivals only *claim* offline or ship it **native-first**). Calenza is the strongest financial comparator (**POS + cash-drawer + payout**), but reconciles the *day*, not a *closed ledger*.
5. **Where Team Calendar is behind:** the periphery rivals advertise as "operating system" — aftercare, ink-registration, inventory/gift/merch, flash-days, **POS/cash-drawer**, SMS/WhatsApp/unified-inbox, campaigns, Google-Calendar sync, in-product multi-language. And **German is no longer a moat** by itself (Taddoo 9-lang, NeedleFlow, ellume/Damin cross-vertical).

## 2 · The central question, answered
> **"Why would a tattoo studio choose Team Calendar instead of the established alternatives?"**

**Honestly — only for a specific studio, and only on two provable grounds.** A **multi-chair, staffed, DACH studio that lives or dies by *who-is-booked-where* and *does-the-money-reconcile*** — not a solo artist needing a pretty DM-to-booking link (that's inkStar/Taddoo/InkLinka's strength, and a space where Team Calendar's own booking is currently simulated) — has a real reason to choose Team Calendar, **today**, because:
- it can **book the workstation/chair as a first-class resource and block the double-booking of *the room*, not just *the person*** (rare; the tattoo core set doesn't do this as a conflict-checked object), and
- it runs a **controlled commission ledger that closes the month** (per-transaction artist/shop split, checkout lock, month-close, locked periods, opening-balance carry-forward, audit trail) — which the field's "commission tracking" mostly is *not*.
- delivered as an **installable offline-first PWA** on one codebase (vs native apps / no-code SPAs).

**It is *not yet* a reason to choose Team Calendar if the studio's top pain is "stop answering Instagram DMs / collect deposits online / auto-remind clients"** — because those three flows are `sim`/`pln`/`unv` in the repo. Selling against them today would be the over-claim this report exists to stop. **The defensible pitch is depth where the market is shallow (money + floor + offline), not breadth where the market is deep.**


## 3 · Where the source comparison document was wrong (hypothesis refutations)
| Prior doc asserted | Independent finding | Verdict |
|---|---|---|
| "inkStar advertises **Station Booking**" | inkStar pages & App-Store copy carry **0 "station"**; resource dimension is **locations**; "chair" is idiomatic ("empty chair") | **Refuted** |
| "inkStar / InkSchedule are **established**" | App-Store `releaseDate` **2026-07-29 (0 ratings)** / **2026-05-12 (1 rating)** | **Refuted (greenfield micro-apps)** |
| INKOS feature breadth (unified inbox, campaigns, inventory, Google-sync…) | only `CRM/agenda/projects/payments/inbox` routes confirmed; app = **Emergent no-code**, **0** Wayback, **no** App-Store record | **Mostly Unverified** |
| TattooManager "**150+ artists**" | no such figure on tattoomanager.de (only "zufriedene Kunden & Benutzer") | **Not found / Unverified** |
| TattooManager lacks resources / reminders | home copy: *"Weniger Doppelbuchungen — **Räume**, Artists und Zeiten…"*, *"Termine, **Pausen und Ressourcen**"*, *"Automatische **Erinnerungen** per E-Mail und SMS"* | **Under-rated (corrected to `~`/`✔`)** |
| Linework & Calenza "older/established" (implied by domain) | **Linework** domain 2000 = parking page, product ≈2022; **Calenza** 1× 2025 OVHcloud placeholder → product **post-dates** 2025-07 | **Corrected (age ≠ domain age)** |
| (TC's own ✓ marks) self-booking ✓, reminders ✓, reviews/waitlist/GDPR ✓, multi-tenant ✓ | repo: self-booking **`sim`**; reminders/reviews/waitlist/social/GDPR **backends absent**; multi-tenant **built-undeployed** | **Over-stated vs code** |

---

## 4 · What Team Calendar **can credibly claim today**
*(every item = `live` in the repo AND a real competitor gap)*
1. **Book the workstation/chair as a first-class resource with per-station conflict + capacity + buffer, checked *before save*** — the flagship, defensible differentiator (*frame as the combination, not "we have chairs"*).
2. **A controlled commission ledger that *closes* the month** — per-transaction artist/shop split, checkout/finalise, **monthly close, locked periods, opening-balance carry-forward**, audit trail, perspective-aware reports.
3. **Offline-capable installable PWA** — service-worker + IndexedDB + sync-on-reconnect, on one codebase, cross-OS (state it as *"browser PWA that installs to the home screen"*).
4. **Staff-side depth**: day/week/month team calendar, working hours, time-off, statuses, roles (incl. custom), per-location **timezone + currency**, reference/design images per appointment, push-notification centre.
5. **In the studio's own language & ledger idiom** (DE/EN, DE print reports) — *as a concrete product fact*, **not** as a compliance guarantee.
6. **"No payment/processing fees today"** — truthfully, because online payment is *absent* (see §5: never dress this as a feature).

## 5 · What Team Calendar **must NOT claim** (until product-owner proves it)
- ❌ **"Clients book online / real-time availability"** — it is **`sim`** (mock slots, no `getSmartAvailability`). *Roadmap only.*
- ❌ **"Automatic reminders cut no-shows"** — **`unv`** (no scheduled CF). Do not imply it runs.
- ❌ **In-app reviews, the 10%-off reward loop, Instagram→Google proof funnel, GDPR self-service export/delete** — **`unv`/hardcoded/placeholder**.
- ❌ **"Many studios, one login, enforced isolation"** — multi-tenant is **built but undeployed** ⇒ say *"in development."*
- ❌ **"Collect deposits / take payments online"** — **`pln`** (Stripe).
- ❌ **Anything using the product's *own* banned words** — *"keine Doppelbuchungen / DSGVO-sicher / zero no-shows / rechtssicher / numbers are right / nobody checks chairs"* (per the repo's DE copy-correction §5). Use the **bounded** versions: "pre-save conflict check," "versioned consent," "self-serve data requests (flows pending)."
- ⚠️ **No numeric market claims** (e.g. "150+ studios", "fastest", "the only German option") that no source substantiates.

## 6 · Potential differentiation (defensible wedges, ranked)
| # | Wedge | Why it holds | Nearest threat |
|---|---|---|---|
| **D1** | **Per-station resource booking** (chair + conflict + buffer + absence, pre-save) | no *tattoo* rival documents the conflict-engine combo; only generalist **Anolla** + niche apps + **TattooManager ("Räume", room-level)** come near | Anolla (breadth); a rival copying it is *plausible* → keep as the moat |
| **D2** | **Close-grade commission ledger** (txn split → checkout → month-close → locked → carry-forward) | nobody advertises the *close/lock* semantics; trust-critical nobody advertises the *close/lock* semantics; it's the trust-critical, least-copied layer least-copied — ⚠️ **but the WEAKEST customer-verified theme in §05 (mostly vendor-asserted "napkin-math"); validate with interviews before letting it lead marketing** | **Calenza** (POS/cash-drawer) is the money comparator — but day-book, not a closing ledger |
| **D3** | **Offline-first browser PWA** (installable, one codebase) | rare *as a browser capability*; rivals are native-first or *claim* offline | inkStar/INKOS *claim* offline; native apps (Taddoo/NeedleFlow/Seance) own true native offline |
| **D4** | **DACH-native product** (DE/EN, DE ledger idiom, staffed-studio focus) | German *tattoo-native* rivals are 2026 micros; mature German options are cross-vertical | cross-vertical **Damin/ellume**, and 2026 **Taddoo/NeedleFlow** (don't claim "only German") |
| **D5** | **Multi-tenant chains** (one login, rule-enforced isolation) — *architecture/roadmap only* | strongest *stated* isolation model; rivals say "multi-studio" loosely | only marketable **after deploy**; inkStar/INKOS/InkLinka/Anolla claim multi-brand today |
| **D6** | **De-risk the owner as single point of failure** (manager-away continuity, never-lose-the-waitlist) | the *most vivid* community pains — *"our manager knows where everything is… if they are away it becomes hard"*, *"had a whole waiting list and then lost it!"* — cheap, dramatic demos; **no rival owns this story** | none (open territory) |

> **Position against the *right* yardstick:** the repo benchmarked "uniqueness" against generic salon tools (Booksy/Square/Phorest). Re-anchor to **tattoo peers**: against them, booking/consent/deposits/waitlist/refs are **commoditised**; only **D1–D4** survive as thin air. **Do not** compete on breadth (gift/merch/inventory/campaigns/mini-sites/AI) — that lane already has INKOS/Anolla/InkLinka.

## 7 · Important missing capabilities (build-to-compete list, by pain-weight)
- **Now (they block the loudest claims & pains):** real **`getSmartAvailability` + `/{slug}/booking` online self-book** (kills the `sim` liability, answers pain ①); **24h/1h reminder** Cloud Functions (pain ③); **Stripe deposit-at-booking** (pain ②, biggest theme); review / waitlist / social / **GDPR export+delete** CFs; **deploy multi-tenant**.
- **Soon (operating-system parity, currently absent):** **aftercare**, **ink registration** (TatTool-only today), **guest/resident-artist management** (vs simple client→staff), **POS/cash-drawer** (vs Calenza), **SMS/WhatsApp + unified inbox**, **Google/Apple calendar sync**, **flash-days**, **inventory/gift-merch**, **campaigns**.
- **Later:** **analytics depth** (targets/forecasts — TatTool/NeedleFlow/Calenza), **public API**, **in-product multi-language**, **theming**, **AI assistant** (optional).

## 8 · Unknowns requiring product-owner verification (public research cannot settle)
1. **Are the `unv` backends truly live in prod** (smart-availability, reminders, review submit, waitlist join, social-track, GDPR export/delete) even though **absent from the repo snapshot**? — decides 6 headline claims.
2. **Did multi-tenant deploy** since `edbc187` (2026-08-29)? If not ⇒ "many studios one login" stays roadmap.
3. **Is client self-reschedule (`#11`) actually live/bug-free** (docs conflict)?
4. **Is the station+buffer+absence engine wired to the *client-facing* flow or staff-calendar-only?** If the client flow is simulated, **D1 is currently a *staff-side* claim** → phrase accordingly.
5. **Which "described" flows (consent intake, deposits) are wired end-to-end vs UI-only?**
6. **Business facts:** real user/studio counts (e.g. never repeat an unverified "N+ artists"), funding, legal entity (the repo names no company), and target geography (repo ships EN+DE ⇒ DACH).
7. **Primary buyer** = multi-seat studio vs solo artist (decides whether "no multi-tenant yet" even matters).

## 9 · Recommended next research
1. **Product-owner interrogation first** (cheap, decisive) — resolve §8 items 1–6; they gate every customer-facing claim.
2. **Competitor feature *verification* by hands-on trial** (free trials): inkStar, Taddoo, NeedleFlow, Calenza, TatTool, InkLinka — to turn `Claimed`/`Not found` into observed truth on **station, offline, ledger-close, reminders** (the four crux cells) instead of marketing-copy inference.
3. **Deep-dive the German field** (Taddoo, NeedleFlow, Damin, ellume) — the *only* arena where Team Calendar's DACH position is genuinely contested; establish whether any German product ships station-resource + ledger-close + offline together.
4. **Re-run pricing/feature captures quarterly** (SPA/React pricing is volatile; e.g. InkSchedule's own trial-length contradiction shows how fast pages drift) and keep the **App-Store `releaseDate`/rating-count** as the traction tripwire for the 2026 cohort.
5. **Build a small, honest review panel**: 5–8 studios (DACH-weighted) validating pain ranking & the D1/D2 wedge — because the Reddit corroboration here is **directional, self-selected**, not representative.
6. **Earn community trust honestly** — these threads are already vendor-farmed (self-disclosed "paid research" 2018; *"free lifetime access to the app I built"* pitches). Do **not** astroturf; enter with evidence-led, non-promotional posts, and lean on the offline-claim discipline below.

---
### Method, limits & provenance
- **`web_search` was down (401)** and **Firecrawl quota-exhausted**; **Bing-RSS/DDG scraping was stale-cached/bot-challenged** ⇒ this run leaned on **primary** sources: vendor official pages, the **Apple App-Store Lookup API**, and **Wayback CDX** (see `08` for every URL + its class + the exact access date). Search-engine output was **discarded, not silently reused.**
- Four specialist passes ran: **pricing** sweep, **competitor-discovery**, **mid-tier deep-dive** (TattooManager/InkLinka/Linework/Anolla), **pain-point** mining (`_research/raw/` holds raw evidence incl. `reddit/corpus.jsonl`). Cross-checked where independent paths agreed (`releaseDate`↔CDX↔official copy); disagreements recorded, not averaged away.
- **Standing limits:** competitor `✖`/`Not found` = *absent from pages checked*, never *proven absent* (many rivals are unreadable SPAs); **no numeric rankings or "winner"** produced (none is evidenced); **no invented dates** (age = earliest *observed* evidence).
> **Bottom line:** Team Calendar is *not* entering an empty market, but is *not* facing entrenched incumbents either — the field is **young, fragmented, low-moat, price-sensitive**. Choose the narrow, provable story: **the studio that can book the chair *and* close the month, offline** — and go fix the `sim`/`unv`/`undep`/`pln` cells before letting marketing wander into them.
