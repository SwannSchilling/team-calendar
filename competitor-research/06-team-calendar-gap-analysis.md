# 06 — Team Calendar Gap Analysis (independent, evidence-based)

**Sources accessed 2026-09-19.** Team Calendar column is taken from the repo's own `FEATURE_INVENTORY.md` (@ commit `edbc187`, 2026-08-29) — **not** from marketing. Where that file flags a feature as simulated / backend-missing / undeployed, that status is carried here. Competitor columns are `Verified`/`Claimed`/`Historical`/`Unverified`/`Not found` per their primary pages / App-Store records.

**Team Calendar status vocabulary (task §9):** `live` · `beta` · `partial` · `planned` · `unclear`.
**Competition strength:** none / low / some / common / commoditised (≈every serious rival has it).

---

## A. Team Calendar capability status (from FEATURE_INVENTORY, the honest baseline)

> The supplied comparison report marked many of these as a bare "✓ Yes". The repo's own inventory says otherwise for a critical minority. Those corrections are the load-bearing part of this deliverable.

| Capability | TC status | Why (repo evidence) |
|---|---|---|
| Team calendar day/week/month; role-scoped | **live** | #7, #28 |
| Per-artist & business working hours | **live** | #13 |
| Time-off (with reason) + staff status | **live** | #14 |
| **Buffer time per artist AND per workstation** | **live** | #15 (`bufferMinutes` on both) |
| **Workstation/chair as bookable resource, per-station conflict + capacity** | **live** | #16 + #3 (`checkTimeSlotAvailability` per workstation) |
| Real-time conflict detection (person + chair + working hours) | **live** | #3 |
| Appointment status workflow (incl. no_show, pending_reschedule) | **live** | #6 |
| Reference / design images per appointment | **live** | #10 |
| Service catalog (duration/price/hourly) | **live** | #2 |
| Staff books on behalf of client (ad-hoc add) | **live** | #4 |
| Multi-location (per-location timezone + currency) | **live** | #17, #43 |
| Three-tier roles + custom roles + role-based UI | **live** | #29,#30 |
| **Commission / artist-vs-shop split ledger (per transaction)** | **live** | #35 |
| Ledger checkout/finalise; month-close; carry-forward; locked months | **live** | #36,#37 |
| "Paid-upfront €0.00" commission-integrity rule | **live** | #39 |
| Finance print report (EN/DE) + perspective-aware display | **live** | #40,#41 |
| Recurring appointments / recurring ledger entries | **live** | #38 |
| Push notifications (new / cancel / stats / badge) + in-app centre | **live** | #51–#56 |
| Notification tiers for staff | **live** | #56 |
| **Installable PWA + offline mode + IndexedDB + sync-on-reconnect** | **live** | #74,#75,#76 |
| Passwordless magic-link auth | **live** | #77 |
| Admin settings/CRUD (hours, roles, services, workstations, locations) | **live** | #71,#72 |
| Review stats/triggers | **live** | #64 |
| Next-visit 10%-off code (**hardcoded**) | **live(partial)** | #65 |
| **Client self / smart booking (real-time availability)** | **partial → actually SIMULATED** | #1: mock slots/IDs; `getSmartAvailability` absent → **do not claim online booking** |
| **Secure one-time client reschedule link** | **partial** | #11 has real CF but doc-vs-code conflict ("blocked" vs "done") |
| Waitlist (join/leave) | **partial/unclear** | #67 UI+rules but `joinWaitlist` CF not in repo |
| Waitlist keyed to artist+time+**workstation** | **partial/unclear** | #68 (no staff UI found) |
| In-app post-visit review submission | **unclear** | #63 `submitReview` CF not found |
| Social proof funnel (IG follow + Google review, tracked) | **unclear** | #66 `trackSocialEngagement` CF absent; links are "yourcompany" placeholders |
| GDPR self-service export / deletion | **unclear** | #26/#27 CFs not found |
| Admin form builder | **live** | #59 (single-form today) |
| Client-facing intake / consent flow | **partial (NEXT)** | #60 storage+rules present, client flow not wired |
| Email delivery | **partial** | #61 queue only; delivery external |
| **24h / 1h automated reminders** | **unclear** | #57 docs say WORKING, **no scheduled CF found** — verify before claiming |
| **Multi-tenant isolation (1 login, many studios)** | **partial (built, UNDEPLOYED)** | #44–#46 deploy pending as of 2026-08-29 |
| Composite cross-studio client profile | **partial** | #24 (multi-tenant wave) |
| Branded public booking URL /{slug}/booking + discovery | **planned** | #48 deferred (task 10.3) |
| **Stripe deposits / payment at booking** | **planned** | #42 |
| Team internal messaging | **planned** | Cat-3 planned |
| Advanced reporting/analytics dashboard | **planned** | Cat-10 planned |
| Multi-language / theming / public API / business bootstrap | **planned** | #80,#81, planned |

---

## B. USP validation — does a competitor already have it?

### USP-1 · "Book the chair, not just the artist" (workstation as first-class resource + per-station conflict)
**Status: PARTIALLY commoditised at the edges — differentiated by *combination*, NOT unique.**
| Competitor | Station/workstation-as-bookable-resource? | Evidence (accessed 2026-09-19) |
|---|---|---|
| **Anolla** (generalist) | **YES — verified** | `/en/tattoo-software`: "Multi-**Resource** Booking — reserve artists, booths, **workstations** or equipment sets in one transaction"; "Resource Management — link **workstations**, booths, … equipment." |
| **Inkoru** (ES, 2025-05, App-Store) | **YES** | books appointments per **"cabina" (= booth/chair/station), no overlap** (App-Store copy) |
| **Tat2App** (2026-06, App-Store) | **YES (chairs)** | "multi-location & **chairs**", walk-ins |
| **Damin** (DE cross-vertical) | **YES (device)** | "*Geräte*-Buchung" = device/resource booking (salon/tattoo POS) |
| **inkStar** | **NO (not found)** | 0 "station"; resource dimension = **locations** ("unlimited employees & **locations**", "multi-location setup"); "chair" is idiomatic ("empty chair", "before sitting in the chair") |
| **TatTool** | **NO (location-level only)** | "checks **artist and location** availability"; "location closures" — *not* chair-level |
| INKOS / InkSchedule / Ink Studio Mgr / Linework / Calenza / InkLinka | **not found** | no station/workstation language on primary pages |
**Verdict.** The prior report's *central* claim — "inkStar already has station booking, so this isn't unique" — is **NOT supported** by inkStar's own pages (inkStar is artist + *location*, not *chair*). True station-resource booking **does exist** in the market (Anolla, Inkoru, Tat2App, Damin) but is **not a tattoo-standard, not combined with conflict+buffer+absence, and not paired with an offline ledger.** So Team Calendar's defensible message is **the combination** (artist **+** chair **+** buffer **+** absence **+** conflict, pre-save), **not** the bare "books chairs" idea. *(Caveat: absence of a marketing page-word ≠ proof the feature is absent in-product — several rivals are tiny SPAs; treat competitor "not found" as such.)*

### USP-2 · Transaction-level artist/shop ledger + checkout + month-close + locked months
**Status: RARE / genuinely strong.** No competitor's primary page advertises month-close / locked-months / immutable carry-forward / pre-save checkout-lock. The closest financial comparator is **Calenza** (commissions + **cash-drawer reconciliation** + POS + "books reconcile to the cent") — but that is day-book POS reconciliation, **not** a locked period ledger. inkStar/others have "commission tracking" (allocation), not a closing ledger. → **This is Team Calendar's most defensible differentiator** (still to be product-owner-confirmed as production-live).

### USP-3 · Offline-first PWA
**Status: commoditised as a CLAIM; differentiated by *form factor*.** inkStar (`17× offline`; "even when you go offline") and INKOS advertise offline; App-Store apps Taddoo / Seance / TATTOO CRM / NeedleFlow claim "works offline" (all **native-first**). Team Calendar's is a **browser PWA** (`service worker` + `IndexedDB` + sync-on-reconnect, **live**). Not unique; the *browser-PWA-instead-of-native* angle is the differentiator (single codebase, installable, cross-OS).

### USP-4 · Guided client self-booking / real-time availability
**Status: TEAM CALENDAR IS BEHIND.** Every serious rival ships online self-booking/reschedule (inkStar AI slots + waitlist-backfill; INKOS public booking; Calenza walk-ins; **Taddoo** live booking-link + **online deposit** + Google/Apple calendar mirror). Team Calendar's is **simulated** (mock slots; `getSmartAvailability` absent) and the branded `/{slug}/booking` URL is **deferred**. → **Do NOT market online booking.**

### USP-5 · In-app review → 10%-off → Instagram/Google loop
**Status: UNVERIFIED for TC; matched/broadly beaten by INKOS.** INKOS already has review requests, campaigns, gift cards, products/merch, flash-days, inventory (broader). TC's loop has **missing backends** (`submitReview`, `trackSocialEngagement` not in repo; social links are "yourcompany" placeholders) and a **hardcoded** code. → Not a claim today.

### USP-6 · Waitlist tied to artist+time+**workstation**
**Status: commoditised (plain waitlists); TC's chair-aware variant is a *potential* edge but UNVERIFIED.** inkStar (auto-backfill), INKOS, Ink Studio Manager (`4× Warteliste`), Anolla (`3× waitlist`) have waitlists. TC's workstation-keyed waitlist is genuinely novel *in concept* but **backend not in repo** → claim only after verification.

### USP-7 · Multi-tenant (one login, many studios, rule-enforced isolation)
**Status: architecturally ahead in *design*, but UNDEPLOYED → not marketable yet.** inkStar "multi-company"; INKOS/InkLinka "multi-studio"; Anolla multi-brand. TC's strict Firestore per-tenant isolation is the strongest *stated* model **but flagged "deployment pending"** in the repo → position as **roadmap/architecture**, not current capability.

---

## C. Where Team Calendar is BEHIND / MISSING (increasingly standard among rivals)

| Capability | TC status | Who already has it (primary evidence) | Class |
|---|---|---|---|
| **Online client self-booking / real-time availability** | simulated | inkStar(AI slots), INKOS(public booking), Calenza(walk-ins), **Taddoo**(booking-link + online deposit + cal-mirror), InkLinka, most | **BEHIND (critical)** |
| **Automated 24h/1h reminders** | unverified | inkStar(24h+2h SMS/email), ISM("Erinnerungen"), **TattooManager(Räume+email/SMS)**, TatTool(Flows), InkLinka | **BEHIND** |
| Client-facing **consent / intake + e-sign (QR)** | partial(NEXT) | TatTool, inkStar(QR+GDPR), INKOS, ISM, InkLinka, INKbusiness | **BEHIND** |
| **Online deposit via processor** | planned(Stripe) | Taddoo(online deposit), inkStar, InkLinka(Stripe), InkLink(Stripe/Square) | **BEHIND** |
| **Guest / resident artists + guest spots** | only client→staff (partial) | TatTool(guest spots), inkStar, INKOS, Calenza(walk-ins), Taddoo(guest spot days), Tattoogenda | **GAP** |
| **Aftercare workflow** | none | inkStar, INKOS, InkLinka, Taddoo, Porter/REV23 | **GAP** |
| **Ink registration** (batch/data-sheet) | none | **TatTool** (ink inventory, batch tracking, data sheets, booking usage) | **GAP** |
| Inventory / gift cards / merch | none | INKOS(inventory+gift cards+merch), InkLinka(Aftercare&Merch), Anolla(inventory) | **GAP** |
| **Flash days / bookable flash** | none | INKOS(flash sales/flash-days), Anolla, Taddoo(flash) | **GAP** |
| **POS / ticketing / cash-drawer** | none (ledger≠POS) | **Calenza**(POS+cash drawer), Porter/Get Ink/DaySmart card reader | **GAP** |
| SMS / WhatsApp / **unified inbox** | none (email+push only) | inkStar(SMS), InkLinka(SMS/Email), INKOS(**unified inbox**), Taddoo(IG/WA) | **GAP** |
| **Google/Apple Calendar two-way sync** | none | INKOS, inkStar, **Taddoo**(mirror+feed), NeedleFlow(iCloud/G/Outlook) | **GAP** |
| Marketing campaigns / automation | none | INKOS(campaigns), Anolla(marketing automation) | **GAP** |
| **Analytics depth** (targets/forecasts) | planned | TatTool(targets/forecasts), Calenza(day→yr+export), NeedleFlow(forecasts) | **BEHIND** |
| AI assistant / voice | none | inkStar(AI+voice), InkLinka(AI Chat/Analyst) | **GAP (optional)** |
| Public API | planned | (InkSchedule listed API in prior doc) | minor gap |
| Multi-language *in-product* | partial (finance EN/DE) | Anolla(26 lang), Taddoo(9), NeedleFlow(8) | **BEHIND** |

**Net.** Team Calendar's *verified* strength is the **staff-side scheduling + offline PWA + the financial ledger**. Its *advertised-in-the-old-report* strengths (online booking, reminders, reviews, waitlist, multi-tenant, consent) are **simulated, unverified, or planned** today. And it is **missing** the "operating-system" periphery (aftercare, ink registry, inventory, gift/merch, flash-days, POS, inbox, campaigns, calendar-sync) that INKOS/inkStar/Calenza/TatTool advertise.

---

## D. Unknowns that require product-owner confirmation (public research cannot settle)
1. Are the ⚠️ backends (`getSmartAvailability`, `submitReview`, `joinWaitlist`, `trackSocialEngagement`, `requestDataExport/Deletion`, scheduled reminders) **live in production** even though **absent from this repo snapshot**? (This decides whether 5 headline features can be marketed at all.)
2. Has the **multi-tenant wave deployed** since `edbc187` (2026-08-29)? If not, "many studios, one login" is roadmap.
3. Is **client self-reschedule** genuinely live/bug-free (docs conflict)?
4. Is the **station + buffer + absence conflict engine** wired into *client-facing* booking, or only the *staff* calendar? (If client booking is simulated, the station USP is currently **staff-side only** — reposition accordingly.)
5. Which "described" capabilities (consent "described", deposits) are wired **end-to-end** vs UI-only?
6. **Business facts:** actual user/customer counts (e.g. re-verify any "N+ artists" claim — TattooManager's "150+ artists" was **not found** on its own site), funding/bootstrapped status, and target geography (TC ships **EN + DE** ⇒ a **DACH** play).
7. Primary buyer: **multi-seat studio** vs **solo artist**? (Determines whether the "no multi-tenant yet" gap is even in scope.)
