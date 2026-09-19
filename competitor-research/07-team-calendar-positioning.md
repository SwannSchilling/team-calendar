# 07 — Evidence-Based Positioning (what can honestly be claimed)

**Accessed 2026-09-19.** Per the brief, this section decides **what is defensible**, not advertising copy. Every "can claim" line below is tied to `FEATURE_INVENTORY.md` (live) **and** a competitor gap; anything not provably live is pushed to "qualify" or "do-not-claim."

## Positioning thesis (evidence-backed, deliberately narrow)
> **Team Calendar is, today, a staff-side studio *floor* scheduler + a studio *books* ledger, delivered as an offline-capable PWA — strongest for DACH multi-artist studios. It is not yet a customer self-service portal and not yet a full all-in-one operating system.**
That is both the honest position *and* the strategically winnable one, because the crowded field is mostly *young* (2024–2026 micro-apps) and mostly *weak on exactly the money-and-floor layer* Team Calendar can prove.

## Where Team Calendar should fight (selected wedges, each with a real competitor gap)
| # | Wedge | Why defensible | Who it beats / who contests |
|---|---|---|---|
| **W1** | **Workstation/chair as a first-class, conflict-checked, buffer-attached resource** | live; no tattoo-specific rival documents a **per-station capacity/conflict** engine; **inkStar's "chair" is idiomatic (0 "station")** | beats the tattoo core; contested only by **Anolla (generalist)** and niche **Inkoru/Tat2App/Damin** → frame as *combination*, not *existence* |
| **W2** | **Controlled ledger: checkout → monthly-close → locked months → opening-balance carry-forward** | live; no rival advertises the *close/lock* semantics | beats all on the *close* idea; **Calenza** is the financial comparator (POS/cash-drawer/payout) → TC = *accountant-grade close*, Calenza = *POS day-book* |
| **W3** | **Offline that actually persists (browser PWA + IndexedDB + sync-on-reconnect)** | live & genuinely rare as a *browser* capability | inkStar/INKOS *claim* offline; Taddoo/NeedleFlow/Seance are **native-first** → TC = installable, cross-OS, one codebase |
| **W4** | **DACH-native (DE product, DE/EN UI, DE ledger/print reports)** | repo evidence | German tattoo-native rivals are **2026 micro** (Taddoo, NeedleFlow, Stenz); real DE threats are **cross-vertical Damin/ellume**, not tattoo specialists |
| **W5 (roadmap, don't lead on it yet)** | Multi-tenant "many studios, one login, enforced isolation" | architecture strong but **undeployed** | inkStar "multi-company", INKOS/InkLinka "multi-studio" are labels; TC's isolation model is the strongest *claim* **once deployed** |

## Claim discipline (the risky items)
| Statement | Verdict | Safe wording |
|---|---|---|
| "Clients book online / real-time availability" | **do-NOT-claim** | *"Guided booking is on the roadmap"* (it is `sim` today) |
| "Automatic reminders cut no-shows" | **do-NOT-claim as live** | `unv` (no scheduled CF in repo) — *"reminders are being finalised"* |
| "In-app reviews / 10%-off loop / Instagram+Google proof" | **do-NOT-claim** | `unv` + hardcoded + placeholder links |
| "Many studios, one login, isolated" | **qualify** | *"multi-studio in development"* (`undep`) |
| "Works offline" | **can claim** (it's live) | but say *"browser PWA, installs to the home screen"*; don't imply the *whole* suite is offline (offline booking still `sim`) |
| "Book the chair, not just the person" | **can claim — the flagship** | anchor on *per-station conflict + capacity + buffer*, checked **before save** |
| "No double bookings" | **qualify** | the *pre-save conflict check* is the real claim, not an absolute |
| "DSGVO-sicher / GDPR-safe / legally compliant" | **do-NOT-claim** | say *"versioned consent + self-serve data rights (some flows pending)"*; compliance is a legal claim, not a feature |
| "Zero no-shows / numbers are right / nobody checks chairs" | **do-NOT-claim** (banned by the product's *own* copy-correction doc) | concrete, bounded claims only |
| "Replaces your payment processor" | **can claim (accurately)** | *"no payment fees today because there is no online payment"* — flip the Stripe-`pln` gap honestly |

## What NOT to compete on
Do not chase **INKOS / Anolla** on breadth (gift cards, merch, inventory, campaigns, mini-sites, AI assistants, 26 languages). The category already has **many all-in-ones** — being "also an all-in-one" without a wedge is losing. Compete on the **depth of the appointment + the money + the offline floor**, which is precisely where the young field is thin.

## Head-to-head framing (say what you win *against this one*)
- **vs inkStar** (feature-surface twin, but solo & 0-rating, 2026): **do not** fight on self-booking/reminders (it markets them, TC only simulates) → fight on **station-conflict + ledger-close + PWA-offline**, and on the fact that TC's ledger is *accountant-grade*, not a "commission tracker".
- **vs TatTool** (broadest tattoo-native, still **beta**, US-priced $49–$399): concede ink-registration & automation *today*; win on **ledger month-close/lock** (TatTool has payments/reports, no close/lock) and **offline PWA** (TatTool "offline payments" ≠ full offline app).
- **vs Calenza** (financial comparator): concede **POS + cash-drawer + one-tap payday**; win on **transaction-level artist/shop allocation + monthly-close + locked periods** (Calenza reconciles the *day*, not a *closed ledger*).
- **vs Ink Studio Manager / TattooManager** (German all-in-ones): *German alone is no longer a moat* (Taddoo/NeedleFlow are German too). Need a concrete edge beyond language → **station-resource + ledger-close + offline PWA** are exactly the edges those two don't document.
- **vs INKOS / InkLinka / Anolla / InkLink** (all young, broad, some no-code): concede surface breadth; win on **architectural rigour (multi-tenant isolation — once deployed) + the ledger + verified offline**. Note **INKOS**'s own breadth is **unverified marketing**; **InkLinka** charges a ~5% deposit fee — a *"your books, not a payment middleman"* angle.
- **vs the generic tools the repo benchmarked against (Booksy / Phorest / Square / Vagaro / Zenoti):** ⚠️ **the wrong yardstick.** The repo framed TC's "uniqueness" against *generic salon/booking* tools. Against **tattoo-specific peers**, booking/consent/deposits/waitlist/refs are **commoditised** — the true thin-air set is **W1–W4** only. Re-anchor every "differentiator" to the tattoo-peer set, not to Square.

## To upgrade "can-claim" today → later (evidence to earn)
| If the team ships… | A claim unlocks |
|---|---|
| `getSmartAvailability` real slots + `/{slug}/booking` | "clients self-book online" (W: closes the biggest gap vs Taddoo/inkStar) |
| scheduled reminder CF | "reminders reduce no-shows" (currently `unv`) |
| review / waitlist / social / GDPR CFs | the review-loop + waitlist + GDPR self-serve claims |
| multi-tenant deploy | "many studios, one login, enforced isolation" |
| Stripe deposits | "collect deposits online" + a *transparent-pricing* counter to the ~5%/6% rivals |

## DACH note (because the product ships EN+DE)
Team Calendar is de-facto a **DACH** product. That is a real, under-served position: German tattoo-*native* rivals are **2026 solos/micro** (Taddoo 9-lang, NeedleFlow, Stenz), and the only mature German options are **cross-vertical** (Damin, ellume). **But** — do **not** claim "the only German option," and do **not** claim *"DSGVO-sicher"* (legal). Sellable German frame: **"in Deutsch, Server-stand & Belege nachvollziehbar bis zum Monatsabschluss, Offline-fähig, Stuhl-Konfliktprüfung"** — concrete claims, none of them legal guarantees.

## Bottom line for positioning
Lead with **W1 (station-conflict scheduling)** + **W2 (close-grade ledger)** as the two provable, hard-to-copy wedges; support with **W3 offline-PWA** and **W4 DACH-native**; treat multi-tenant as *architecture/roadmap*; **stay out** of the all-in-one breadth war; and **never market the `sim`/`unv`/`undep`/`pln` cells as live.** The defensible story is *depth where the market is shallow*, not *breadth*.
