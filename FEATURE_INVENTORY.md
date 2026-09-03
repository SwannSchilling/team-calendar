# Feature Inventory — Next-Gen Scheduler (Studio Management PWA)

> **What this is:** A consolidated, evidence-based inventory of every feature in the app, organized by category, with plain-language "what / who it's for / why it matters" notes and a status flag on each item. Built to be handed to copywriters and product owners. No marketing copy — just accurate, sourced facts.
>
> **Compiled:** from the repository state as of the latest commit of the multi-tenant identity wave (`edbc187`, 2026-08-29). Supersedes `FEATURE_INVENTORY_01`–`04.md` (intermediate planning drafts) and complements `app_feature_overview.md` (the founder-toned promo version).

---

## How to use this document

- **For copywriters:** each entry gives you *What* (plain language), *For* (the audience), and *Why* (the benefit/pain solved). Use those to draft copy; the Status flag tells you what you may safely claim today.
- **For accuracy:** the ⚠️ **verify** flag marks features where the UI exists in the code but the corresponding Cloud Function is **not present in the current repo** (`functions/src/index.ts` exports 17 functions; several called by the frontend are absent). Confirm with the product owner before claiming these are live.
- **Method (sources):** routes + components + Cloud Functions + types/data model + Firestore rules, cross-checked against `DESIGN_SPEC`, `DEVELOPMENT_HISTORY`, `PROJECT_PROGRESS`, feature docs, and Kiro specs. Discrepancies between docs and code are flagged inline rather than silently resolved.

## Status legend

| Marker | Meaning |
|---|---|
| ✅ | **Live** — built and in production (code + verified docs). |
| 🟡 | **In progress / known issues** — code is present but has documented bugs, or a backend piece is missing/partial. |
| 🔶 | **Deploy pending** — implemented + tested, awaiting deployment (the multi-tenant wave, as of 2026-08-29). |
| ⏳ | **Planned** — roadmap / spec only, not yet built. |
| ⚠️ | **Verify** — UI is in the repo but the matching Cloud Function was not found in the current source. Confirm before claiming. |

> A feature can carry two markers (e.g. **🟡 ⚠️**) when it is *shipped in UI but its backend callable is unverified*.

## Who "for" means (audience taxonomy)

- **Owner** — studio owner(s).
- **Admin** — day-to-day manager with full backend access.
- **Artist / Team member** — the person doing the work; sees their own book + relevant finance.
- **Client / Customer** — end user who books, manages their profile, reschedules, reviews.

---

## Executive summary

**Next-Gen Scheduler** is a scheduling/booking **PWA built for tattoo studios** (and creative studios generally), on **Next.js + Firebase** (Firestore, Auth, Cloud Functions, Storage). It replaces three things — a paper booking sheet, a group-chat schedule, and a spreadsheet for who-owes-who — with one source of truth.

- **Multi-tenant** (businesses/tenants with slugs + memberships, strict isolation; one account can span multiple studios).
- **Roles:** Client, Team Member (Artist), Admin, Owner.
- **Strongest differentiators:** (1) studio **commission / split-pay ledger** baked into the scheduler, (2) **chairs/workstations as bookable resources** with per-station conflict detection, (3) **design-reference images per appointment**, (4) **secure one-time self-reschedule links** with studio-configurable policy, (5) **in-app review funnel** with a 10%-off incentive code + Instagram/Google tracking, (6) **artist-first PWA** with notification tiers.

A **caveats-for-copywriters** section near the end lists exactly what must **not** be over-claimed today (simulated booking availability, missing backends, undeployed multi-tenant, unverified reminders).

---

## Category 1 — Booking & Scheduling

**1. Smart / Guided Booking (two modes)** — 🟡 ⚠️
- **What:** A guided client booking page with two modes — **Quick Book** (a recommended slot with a match score) and **Choose Your Own Time** (custom filters: service, artist, date, time, location).
- **For:** Clients.
- **Why:** Removes the "DM us to book" back-and-forth; a guided path instead of a bare form.
- **Verify:** UI is live but **availability and booking confirmation are currently client-side simulated (mock slots / mock booking IDs)**; the `getSmartAvailability` callable is commented out / not in the repo. **Do not claim "real-time online booking"** until the backend ships.

**2. Service catalog / service picker** — ✅
- **What:** Admin-defined service types, each with duration, price (in cents), optional hourly rate, color, default and active flags; clients pick from pill-style buttons.
- **For:** Admins (define), Clients (pick).
- **Why:** Drives correct durations/prices through the whole flow; hourly-rate support fits custom tattoo work.

**3. Real-time conflict detection / double-booking prevention** — ✅
- **What:** `checkTimeSlotAvailability` checks workstation conflicts, member time-off, and working hours before a slot is accepted.
- **For:** Artists, Admins.
- **Why:** Nothing double-books a person or a chair; wrong-room / wrong-artist collisions are caught, not discovered at 2pm.

**4. Staff booking on behalf of clients** — ✅
- **What:** Full appointment form for staff, including ad-hoc "add client" inline so a new client can be booked in one pass.
- **For:** Artists, Admins.
- **Why:** Fast phone/counter booking without forcing a full client signup.

**5. Appointment management (CRUD)** — ✅
- **What:** Create / view / edit appointments from the calendar; each carries a client note and a team note.
- **For:** Artists, Admins.
- **Why:** One place to manage the whole day's book.

**6. Appointment status workflow** — ✅
- **What:** Lifecycle states `booked / completed / cancelled / no_show / pending_reschedule / time_off`, with transitions and related alerts.
- **For:** Artists, Admins, Owners.
- **Why:** Feeds accurate stats (no-shows, completed), finance, and reminders.

**7. Multi-view team calendar** — ✅
- **What:** **Day** (per-workstation time grid), **Week** (agenda), **Month** (overview).
- **For:** Everyone (role-scoped).
- **Why:** The core surface; multiple views fit different planning horizons.

**8. "My schedule only" filter** — ✅
- **What:** Team members filter the calendar to just their own appointments.
- **For:** Artists.
- **Why:** No more scrolling through six people's bookings to find yours.

**9. Appointment detail modal (linked context)** — ✅
- **What:** A detail view linking the client's contact info, assigned artist, workstation, notes, reference images, and who created the booking.
- **For:** Artists, Admins.
- **Why:** Full context in one click before the client walks in.

**10. Reference / booking images per appointment** — ✅
- **What:** Client or team uploads reference images (design refs, before/after); auto-resized on upload, deletable; surfaced in the artist's upcoming schedule and the team-member profile; a notification to the assigned team member is designed.
- **For:** Artists, Clients.
- **Why:** A creative-studio workflow — the artist sees exactly what to draw before the appointment. *(Differentiator.)*

**11. Client self-reschedule via secure one-time link** — 🟡
- **What:** A tokenized, expiring link (48h, admin-configurable) that lets a client pick an alternative slot computed from the artist's real working hours + time-off + reschedule slots.
- **For:** Clients, Admins (policy).
- **Why:** Cuts "can I move my appointment?" messages without giving clients a full login.
- **Note (status conflict):** Backend functions exist, but feature doc 008 marks this **"in progress / blocked"** (documented bugs in `initiateReschedule` — date-range / working-hours), while `PROJECT_PROGRESS` lists it **DONE**. Treated as 🟡 pending verification.

**12. Reschedule policy controls + per-artist slot windows** — ✅
- **What:** Admin policy knobs — `searchStartDaysBefore`, `maxSearchDays`, `maxSlotsPerSearch`, `tokenExpirationHours` — plus per-member reschedule slot windows.
- **For:** Admins.
- **Why:** Studios control how far out / how many slots a client may search; artists can carve out their own reschedulable windows.

**13. Per-artist & business-wide working hours** — ✅
- **What:** Working-hours definitions at both the business level and per artist.
- **For:** Admins, Artists.
- **Why:** Drives availability, conflict checks, and reschedule slot search.

**14. Time-off scheduling (with reason) + staff status bar** — ✅
- **What:** Artists book time off with a reason; a status bar surfaces it across the team.
- **For:** Artists, Admins.
- **Why:** Prevents booking into a known absence; the team can see who's out.

**15. Buffer time (per artist + per workstation)** — ✅
- **What:** `bufferMinutes` on both team members and workstations.
- **For:** Admins, Artists.
- **Why:** Built-in clean-up/setup time so appointments don't butt against each other.

**16. Workstation / chair as a bookable resource** — ✅
- **What:** Appointments are tied to a location + a specific workstation; workstations have **capacity** and **buffer**, and conflict detection runs **per workstation** (day view renders a per-chair time grid).
- **For:** Admins, Artists.
- **Why:** Most booking tools book *people*; this books the **physical chair too**, so two artists can't be double-booked into the same station. *(Differentiator.)*

**17. Multi-location scheduling** — ✅
- **What:** Appointments carry a `locationId`; each location has its own timezone and currency.
- **For:** Owners running more than one site.
- **Why:** Correct time and currency across regions from one app.

> **Planned (Booking):** **Block-out time slots** (shorter than time-off) — ⏳.

---

## Category 2 — Client Management

**18. Client profiles / database** — ✅
- **What:** A client record with name, email, phone, and **Instagram handle**, plus contact info and booking history.
- **For:** Artists, Admins.
- **Why:** Everything about a client lives in one place, not scattered across notes apps and group chats. The Instagram field is a social-first touch for creative studios. *(Niche.)*

**19. Live client stats** — ✅
- **What:** Auto-maintained counters — total visits, completed, cancelled, no-shows — updated by the `updateClientStats` Cloud Function.
- **For:** Admins, Owners.
- **Why:** Real retention / no-show signal without manual tracking.

**20. Client search** — ✅
- **What:** Search clients by name, email, or phone.
- **For:** Artists, Admins.
- **Why:** Fast lookup at the desk or before an appointment.

**21. Booking enable / disable per client (`canBook`)** — ✅
- **What:** An admin-gated activation flag that controls whether a client may self-book.
- **For:** Admins.
- **Why:** Studios control who can book online (e.g., only after a phone screening or a first-visit deposit).

**22. Add / edit / delete clients from admin** — ✅
- **What:** Full client CRUD in the admin area, plus "add client" inline in the booking form.
- **For:** Admins.
- **Why:** Keep the client database clean and current.

**23. Client self-signup (email/password + magic link)** — ✅
- **What:** Clients can create an account (email/password or passwordless magic link); new accounts start **pending activation** until an admin enables `canBook`.
- **For:** Clients.
- **Why:** Self-service onboarding, still gated by the studio.
- **Note:** post multi-tenant deploy, the onboarding flow changes with the client-onboarding wave (see §49).

**24. Composite client profile (multi-tenant)** — 🔶
- **What:** Client documents keyed as `clients/{businessId}_{authUid}`, so one person can be a client across multiple studios.
- **For:** Clients who visit more than one studio; Owners.
- **Why:** A single account spanning studios without data leaking between them. Part of the multi-tenant wave (deploy pending).

**25. Versioned privacy consent + re-consent** — ✅
- **What:** Consent is versioned; when the privacy policy updates, clients are prompted to re-consent.
- **For:** Clients, Owners (compliance).
- **Why:** GDPR-style consent trail with auditability.

**26. Self-service data export (JSON download)** — 🟡 ⚠️
- **What:** A client can download all of their data as JSON (right to data portability).
- **For:** Clients.
- **Why:** A GDPR data-right, self-served.
- **Verify:** UI exists; the `requestDataExport` callable is **not found** in the current repo. Confirm before claiming.

**27. Self-service account / data deletion (with reason)** — 🟡 ⚠️
- **What:** A client can request deletion of their account / data, providing a reason.
- **For:** Clients.
- **Why:** The "right to be forgotten," self-served and logged.
- **Verify:** UI exists; the `requestDataDeletion` callable is **not found** in the current repo. Confirm before claiming.

---

## Category 3 — Team & Staff

**28. Multi-artist team calendar with per-artist color coding** — ✅
- **What:** A shared team calendar where each artist is color-coded and their schedule is distinct.
- **For:** Admins, Owners.
- **Why:** Admins see everyone; the visual separation makes a busy shop readable.

**29. Three-tier roles + custom role definitions** — ✅
- **What:** Owner / Admin / Member (Artist) tiers, plus the ability to define custom roles.
- **For:** Owners, Admins.
- **Why:** Granular, studio-specific permission shapes rather than only three fixed buckets.

**30. Role-based UI access** — ✅
- **What:** UI gates by role — admin dashboard, finance gated by a `financeEnabled` flag, client-only navigation, and role-aware header nav.
- **For:** Everyone.
- **Why:** A new hire doesn't see the whole shop's financials on day one; nobody is locked out of what they need.

**31. Client → staff promotion flow** — 🔶
- **What:** An atomic, auth-account-aware flow that turns a client into a team member.
- **For:** Owners, Admins.
- **Why:** Hire an existing client without manual account surgery.
- **Status:** The **new P6 implementation is deploy pending** (multi-tenant wave); the **old flow is live** in the meantime.

**32. Team member management (complete setup)** — ✅
- **What:** Full team-member administration, including working hours, colors, reschedule slots, and promotion.
- **For:** Admins, Owners.
- **Why:** One place to run the team.

**33. Per-team-member stats** — ✅
- **What:** Stats per team member, maintained by the `updateTeamMemberStats` Cloud Function.
- **For:** Admins, Owners.
- **Why:** Performance / activity view per artist.

> **Planned (Team):** **Internal team messaging** — ⏳.

---

## Category 4 — Payments & Finance

> This is the module most booking tools skip. It is complete and is the app's primary differentiator.

**34. Finance module (complete)** — ✅
- **What:** A full finance area: ledgers, sync, checkout, commission, month-close, recurring entries, and printing.
- **For:** Owners, Admins, Artists.
- **Why:** Studio money is tracked inside the scheduler instead of on a napkin.

**35. Per-artist commission / split-pay ledger** — ✅
- **What:** Per-transaction artist-vs-shop split, tracked on each ledger entry.
- **For:** Owners, Artists.
- **Why:** The "who owes what" answer is automatic, per transaction. *(Differentiator.)*

**36. Ledger checkout / finalize** — ✅
- **What:** A checkout-and-finalize step for ledger entries; finalized entries lock in place.
- **For:** Admins, Owners.
- **Why:** No "wait, did we already pay that out?" — confirmed entries can't be double-counted.

**37. Month-close + carry-forward + locked months** — ✅
- **What:** Close a month, carry forward balances, and lock closed months from further edits.
- **For:** Owners.
- **Why:** Clean period boundaries with immutability for accounting.

**38. Recurring events / recurring ledger entries** — ✅
- **What:** Support for recurring (repeating) appointments / ledger items.
- **For:** Admins.
- **Why:** Regulars and retainer work without re-entry.

**39. "Paid upfront" €0.00 rule (commission integrity)** — ✅
- **What:** A rule that treats fully-paid-upfront jobs so the commission split stays consistent (e.g., a €0.00 residual with the full amount attributed correctly).
- **For:** Owners, Artists.
- **Why:** Prevents commission math from breaking on prepaid jobs. *(Niche.)*

**40. Finance print report (bilingual EN/DE)** — ✅
- **What:** A printable finance report; labels are provided in **English and German**.
- **For:** Owners, Admins.
- **Why:** A real document to hand to an accountant or keep on file; the EN/DE labels hint at a growing EU audience.

**41. Perspective-aware finance display** — ✅
- **What:** The same ledger can be viewed from the artist's perspective or the shop's perspective.
- **For:** Artists, Owners.
- **Why:** Each role sees the split from the side that matters to them.

**42. Stripe payment integration (deposits / full payment at booking)** — ⏳
- **What:** Take deposits or full payments at booking time via Stripe.
- **For:** Studios, Clients.
- **Why:** Reduce no-shows and capture revenue in-flow. *(Planned / roadmap.)*

---

## Category 5 — Multi-location & Multi-tenant

**43. Multi-location (full)** — ✅
- **What:** Locations with full admin CRUD, each carrying a **timezone**, a **currency**, and a default setting.
- **For:** Owners, Admins.
- **Why:** Run several sites from one app with correct time/currency per site.

**44. Multi-tenant architecture (strict isolation)** — 🔶
- **What:** Businesses/tenants with slugs + memberships; one user account can belong to multiple studios; Firestore rules enforce strict per-tenant isolation.
- **For:** Owners, Operators running several studios.
- **Why:** "One account, many studios" without any cross-studio data leakage.
- **Status:** Implemented + tested; **deployment pending** as of 2026-08-29. *(Differentiator.)*

**45. Tenant selection / switching UI** — 🔶
- **What:** A `/select-tenant` route, a `TenantContextSwitcher`, and an `/access-denied` screen.
- **For:** Users with multiple studios.
- **Why:** Switch the active studio in-app; clean fallback when a user lacks access to the requested tenant.

**46. Business / tenant onboarding** — 🔶
- **What:** `createBusinessOwnerMembership` Cloud Function performs 7-document atomic provisioning, including a composite owner client profile; an ops CLI script (`create_tenant.py`) also exists.
- **For:** Operators, DevOps.
- **Why:** A studio can be stood up atomically and consistently.
- **Status:** Part of the multi-tenant wave (deploy pending).

**47. Business bootstrap script (`create_business.py`)** — ⏳
- **What:** A proposed one-step business bootstrap script.
- **For:** DevOps, Owners.
- **Why:** Faster, scriptable studio creation. *(Documented as "Proposed — not yet implemented".)*

**48. Branded public booking URL (`/{slug}/booking`) + public studio discovery** — ⏳
- **What:** Each studio gets its own public slug URL that clients hit directly, plus public discovery of studios.
- **For:** Studios, Clients.
- **Why:** "yourstudio.app/booking" instead of "DM us to book." *(Deferred — task 10.3; not yet built.)*

**49. Client onboarding wave (composite client model)** — ⏳
- **What:** Studio picker at signup, multi-studio switching for pure clients, and public studio discovery.
- **For:** Clients, Studios.
- **Why:** Until this ships, **pure-client self-booking is degraded** relative to the multi-tenant design.
- **Status:** Requirements authored (Kiro spec `client-onboarding`); implementation pending (gates G1–G5).

**50. Business branding fields (`primaryColor`, `secondaryColor`, `logoUrl`)** — ⏳
- **What:** Branding fields on the Business document.
- **For:** Owners.
- **Why:** Studio theming / white-labeling.
- **Status:** Fields exist but **no UI applies them yet**; today the only live branding touch is the **default location name shown as the app title** in the header. Tied to the "customizable themes" roadmap item.

---

## Category 6 — Notifications & Reminders

**51. Push notifications (booking created)** — ✅
- **What:** `sendNewAppointmentNotification` fires on a new booking (push + in-app + email queue).
- **For:** Artists, Clients.
- **Why:** Everyone knows a new appointment landed, immediately.

**52. Push notifications (cancel / reschedule)** — ✅
- **What:** `sendAppointmentModifiedNotification` fires when an appointment is cancelled or rescheduled.
- **For:** Artists, Clients.
- **Why:** Cancellation / change is surfaced in real time, not discovered later.

**53. Stats notifications** — ✅
- **What:** Team / client stats updates emit notifications via `updateClientStats` / `updateTeamMemberStats`.
- **For:** Admins, Owners.
- **Why:** Activity signal without opening the dashboard.

**54. App-icon badge count** — ✅
- **What:** `syncBadgeCount` keeps the PWA icon's unread badge in sync.
- **For:** Everyone.
- **Why:** At-a-glance "something needs attention" on the home screen.

**55. In-app notification center** — ✅
- **What:** A centralized in-app inbox for all notifications.
- **For:** Everyone.
- **Why:** History and retrieval of every event in one place.

**56. Notification tiers for staff** — ✅
- **What:** Staff can set a tier / level of push noise.
- **For:** Artists.
- **Why:** Control how much the app pings you — a quality-of-life differentiator for busy chairs. *(Differentiator.)*

**57. Automated 24h / 1h reminders (scheduled Cloud Function)** — 🟡 ⚠️
- **What:** Scheduled reminders sent 24h and 1h before an appointment.
- **For:** Artists, Clients.
- **Why:** The single biggest no-show reducer.
- **Verify (status conflict):** `PROJECT_PROGRESS` lists this as **WORKING**, but **no scheduled-reminder function was found in the current repo** and the design spec lists reminders as future work. **Confirm before claiming.**

**58. Client-facing notifications** — ⏳
- **What:** Notification delivery to clients (beyond current triggers).
- **For:** Clients.
- **Why:** Close the loop on the client side. *(Planned.)*

---

## Category 7 — Forms & Paperwork

**59. Admin form builder** — 🟡
- **What:** A `FormBuilder` for creating studio forms, plus `ClientForm` rendering; storage and Firestore rules exist.
- **For:** Admins.
- **Why:** Define any form (intake, consent) without hard-coding.
- **Note:** Currently a single-form setup ("in a real app you'd have a list of forms"); a multi-form manager is on the roadmap.

**60. Client-facing intake / consent forms** — 🟡 / ⏳
- **What:** Clients complete intake/consent forms (medical/health context for tattooing) before or at the appointment.
- **For:** Clients, Artists.
- **Why:** Paperwork done before the chair, not during it.
- **Status:** Builder + storage + rules are in place; the **client-facing wired flow is the next roadmap step** ("NEXT").

**61. Email delivery infra (mail queue)** — 🟡
- **What:** A mail queue exists to stage outgoing email.
- **For:** Studio (outbound comms).
- **Why:** Asynchronous, reliable email.
- **Note:** Actual **delivery is handled externally** — the repo stores/queues; sending is a separate concern.

**62. Forms authorization model / email tenant scoping** — ⏳
- **What:** Scoping forms and email to tenants + an authorization model for forms.
- **For:** Owners, Admins.
- **Why:** Keep forms/email correct in a multi-tenant world. *(Roadmap.)*

---

## Category 8 — Reviews & Reputation

**63. In-app post-visit reviews** — 🟡 ⚠️
- **What:** Clients leave a review straight from the app after an appointment; the UI is complete and Firestore rules allow client creation of reviews.
- **For:** Clients, Studios.
- **Why:** No chasing people down for a Google review.
- **Verify:** The `submitReview` callable is **not found** in the current repo. Confirm before claiming end-to-end review submission.

**64. Review stats / triggers** — ✅
- **What:** Stats around reviews are maintained by live Cloud Functions.
- **For:** Owners, Admins.
- **Why:** Reputation signal aggregated, not manual.

**65. Next-visit incentive code (10% off)** — ✅
- **What:** After a review, the client is offered a 10%-off code for their next visit (currently **hardcoded in the UI**).
- **For:** Clients, Studios.
- **Why:** Turns a review into a repeat-visit; a loop most booking tools stop short of. *(Niche + Differentiator.)*

**66. Social engagement funnel (Instagram follow + Google review)** — 🟡 ⚠️
- **What:** The review flow can route to an Instagram follow and a Google review, with engagement tracking.
- **For:** Studios.
- **Why:** One action grows both the studio's socials and its Google rating.
- **Verify / Note:** The `trackSocialEngagement` callable is **not found** in the repo, and the Instagram/Google links are currently **placeholders ("yourcompany")** — not wired to a real studio.

---

## Category 9 — Waitlist

**67. Client waitlist UI (join / leave) + rules** — 🟡 ⚠️
- **What:** Clients can join/leave a waitlist; the UI and Firestore rules exist.
- **For:** Clients, Studios.
- **Why:** When the slot they want is gone, they land in a waitlist tied to that request — not a text you'll forget to follow up on.
- **Verify:** The `joinWaitlist` callable is **not found** in the current repo. Confirm before claiming.

**68. Waitlist tied to artist + time + workstation (with status lifecycle)** — ⚠️
- **What:** Waitlist entries are keyed to a **specific artist, time, and workstation**, with a status lifecycle.
- **For:** Studios, Artists.
- **Why:** A waitlist that knows *which chair / which artist* frees up — a plus over generic "I'm interested" lists.
- **Verify / Note:** A staff-list rule exists, but **no dedicated staff UI was found** yet; treat as partially surfaced. *(Differentiator.)*

---

## Category 10 — Admin & Settings

**69. Performance dashboard (metrics + alerts)** — ✅
- **What:** An admin performance dashboard with key metrics and alerts.
- **For:** Owners, Admins.
- **Why:** A single pane for how the studio is doing.

**70. Admin appointment list (search, edit, delete)** — ✅
- **What:** A searchable admin list of all appointments with edit/delete.
- **For:** Admins.
- **Why:** Bulk oversight and correction outside the calendar.

**71. Admin settings suite** — ✅
- **What:** One area to manage locations, workstations, service types, roles, working hours, forms, reschedule policy, and ledgers.
- **For:** Admins, Owners.
- **Why:** The studio's configuration is all in one place.

**72. Admin CRUD: business hours, roles, services, workstations, locations** — ✅
- **What:** Full create/read/update/delete for the core reference data.
- **For:** Admins.
- **Why:** Studio can model itself accurately (hours, staff, services, chairs, sites).

**73. Debug tools (admin-only diagnostics)** — ✅
- **What:** An admin-only debug/diagnostics tab.
- **For:** Operators, Devs.
- **Why:** Faster triage.
- **Note:** Internal tooling — **excluded from marketing / copywriting.**

> **Planned (Admin / Finance):** **Advanced reporting & analytics dashboard** — ⏳.

---

## Category 11 — Platform & App Experience

**74. Installable PWA** — ✅
- **What:** A full PWA — `manifest.json`, service worker, install prompt, and iOS install instructions.
- **For:** Everyone.
- **Why:** Installs to the home screen like a native app.

**75. Offline mode + connection indicator + real-time sync** — ✅
- **What:** Service-worker caching, an offline indicator (shows offline / cache state), and IndexedDB persistence; data syncs on reconnect.
- **For:** Artists (bad signal in the chair), Everyone.
- **Why:** The app keeps working in the studio even when the Wi-Fi doesn't.

**76. Real-time everything** — ✅
- **What:** Calendar, waitlist, ledger, and notifications update live via Firestore `onSnapshot` listeners.
- **For:** Everyone.
- **Why:** No refresh; the whole team sees changes as they happen.

**77. Passwordless magic-link sign-in** — ✅
- **What:** Email magic-link login in addition to email/password.
- **For:** Clients + staff.
- **Why:** Lower-friction, secure sign-in.

**78. Role-aware navigation + pending-activation home state** — ✅
- **What:** The shell adapts to the user's role and their activation state (booking-enabled / pending / staff).
- **For:** Everyone.
- **Why:** Each person lands on the screen that's actually theirs.

**79. Mobile-first finance UI** — ✅
- **What:** The finance area is designed mobile-first.
- **For:** Owners, Admins (on the go).
- **Why:** Check the books from a phone at the end of the day.

**80. Multi-language support** — ⏳
- **What:** i18n across the app.
- **For:** Studios with multilingual clients/staff.
- **Why:** Reach a broader market.
- **Note:** **Partial today** — finance print is already EN/DE, and a `useRescheduleTranslation` hook exists on the reschedule page; full i18n is roadmap.

**81. Customizable themes / branding application** — ⏳
- **What:** Apply business branding (colors, logo) across the app.
- **For:** Owners.
- **Why:** White-label / studio-branded experience. *(Tied to #50; roadmap.)*

> **Planned (Platform):** **Public API** — ⏳.

---

## Standout / differentiator features (deep dive)

These are the features that most booking tools (Booksy, Phorest, Square Appointments, Vagaro, Zenoti) **do not** offer. The "why it's specific" is what copywriters should lean on.

1. **Studio commission accounting built into the scheduler** (#34–#39) — Per-transaction artist-vs-shop split with checkout, finalize, month-close, carry-forward, locked months, and a "paid upfront" integrity rule. No mainstream booking tool does studio revenue accounting. This is the **"napkin math" killer** — the single pain line that lands hardest with real shop owners.

2. **Chairs / workstations as bookable resources with conflict detection** (#16, #3) — Most tools book *people*; this books the **physical station** (capacity + buffer), preventing two artists from landing in the same chair.

3. **Design-reference workflow per appointment** (#10) — Reference / before-after images attached to the appointment, so the artist sees exactly what to draw before the client walks in. A genuine creative-industry workflow.

4. **Secure one-time client reschedule link with studio-configurable policy** (#11, #12) — Tokenized, expiring, constrained to the artist's real windows; the admin dials the search window. Rare in booking tools.

5. **In-app post-visit review with a discount-code funnel + social proof loop** (#63, #65, #66) — Closes the loop the others stop at: review → 10%-off code → Instagram follow → Google review, all tracked.

6. **Per-artist waitlist tied to artist + time + workstation** (#67, #68) — Not just "I'm interested," but a specific slot/chair request with a status lifecycle.

7. **Artist-first mobile PWA with notification tiers** (#74, #75, #56) — Staff get an installable app with controllable push noise and offline mode.

8. **True multi-tenant isolation** (#44) — One account across multiple studios, rule-enforced.

9. **Instagram handle on the client record** (#18) — A social-first client base for creative studios.

10. **Per-location timezone + currency** (#17, #43) — Multi-region studios without manual conversion.

---

## Status roll-up (approximate counts)

| Bucket | Count (approx) | Examples |
|---|---|---|
| ✅ **Live** | ~40 | Calendar core, staff booking, team/calendar, client mgmt, full finance module, admin dashboard, PWA, push triggers (new + modify + stats + badge), notification center + tiers, form builder, consent, reschedule link UI, multi-location. |
| 🟡 **In progress / known issues** | ~8 | Smart booking (simulated), client self-reschedule (documented bugs), waitlist join (CF missing), review submit (CF missing), social tracking (CF missing + placeholder links), data export / delete (CF missing), client-facing intake forms, email delivery infra. |
| 🔶 **Deploy pending** | ~4 | Multi-tenant architecture, tenant selection/switching, business/tenant onboarding, composite client profile + client→staff promotion (P6). |
| ⏳ **Planned** | ~10 | 24h/1h reminders (unverified), client-side notifications, Stripe payments, advanced reporting, team messaging, block-out times, multi-language, themes/branding, public API, slug public booking URL + client onboarding wave, business bootstrap script. |

> Counts are directional, derived from the per-feature flags above; treat the flags themselves as the source of truth.

---

## Niche (tattoo / creative studio) vs General-purpose

**Niche-specific** (why this is built for tattoo/creative studios):
- Commission split / studio finance (artist vs shop cut)
- Chair / workstation (tattoo chair) scheduling
- Design-reference images (refs / before-after)
- Instagram handle on client profile + social funnel
- 10%-off review incentive
- "Paid upfront" €0.00 commission-integrity rule
- Custom hourly rates for custom work
- No-show tracking (high no-show cost in tattoo)
- Consent / intake forms (health context)
- Waitlist for popular artists

**General-purpose** (transferable to salons, clinics, barbers, trades):
- Scheduling core (day/week/month), availability, conflict detection
- Client profiles + history + booking permission
- Roles / permissions, multi-staff
- Multi-location, multi-tenant
- Notifications & reminders
- Reviews & ratings
- Waitlist
- Ledger / invoicing basics
- Form builder
- PWA / offline
- GDPR data export / deletion
- Business hours management

---

## ⚠️ Caveats for copywriters (accuracy notes)

Read before drafting any marketing copy. These are the places where the repo state and the "aspirational" feature list disagree:

1. **No public branded booking page yet.** `yourstudio.app/booking` (slug routes) is **deferred (task 10.3)**. Today the only live "branding" is the **location name shown as the app title** in the header. Do not market a public booking URL.
2. **Smart / client self-booking is simulated.** Availability and confirmation are **client-side mock data** in the repo; the `getSmartAvailability` callable is absent/commented out. **Do not claim "clients can book online with real-time availability."**
3. **Several frontends call backends that aren't in the repo.** `submitReview`, `joinWaitlist`, `trackSocialEngagement`, `requestDataExport`, `requestDataDeletion`, `getActiveBusinesses` were **not found** in `functions/src/index.ts`. They may exist in a production deploy that isn't in this source, **or** they're unbuilt. **Verify with the product owner** before claiming reviews, waitlist, social tracking, or GDPR export/delete as live.
4. **Multi-tenant is built but not deployed** (as of the last commit, `edbc187`, 2026-08-29). Until the wave deploys, the multi-studio / composite-client behavior is not live in production.
5. **24h/1h reminders are unverified.** `PROJECT_PROGRESS` says they're WORKING, but no scheduled Cloud Function was found in the repo and the design spec lists reminders as future work. **Confirm before claiming.**
6. **Incentive code is hardcoded; social links are placeholders.** The 10%-off code is hard-coded in the UI, and the Instagram/Google funnel links point to a placeholder ("yourcompany"), not a real studio.
7. **Doc-vs-code status conflicts** to be aware of: client self-reschedule (doc 008 "in progress/blocked" vs progress "DONE") and reminders (progress "WORKING" vs no CF in repo). Both are flagged 🟡/⚠️ above.
8. **Debug tools are internal** (#73) — exclude from marketing.

---

## Appendix A — Sources referenced

**Docs:** `README`, `DESIGN_SPEC` (feature list + roadmap), `DEVELOPMENT_HISTORY`, `ONBOARDING_AND_PROVISIONING_GUIDE` (identity/ledger scope matrix), `FINANCE_UI_SPEC`, `PWA_AND_NOTIFICATIONS_GUIDE`, `MULTI_TENANT_ARCHITECTURE_REVISION`, compliance checklist, business-creation plan, `docs/features/008` (self-reschedule).

**Code:** all routes (`/`, `/auth`, `/booking`, `/consent`, `/finance`, `/finance/print`, `/reschedule`, `/review`, `/select-tenant`, `/team/calendar`, `/team/profile`, `/admin`, `/admin/forms`, `/access-denied`), all components, Cloud Functions (**17 exported** in `functions/src/index.ts`), types / data model, and Firestore rules (all collections).

**Context notes:** `PROJECT_PROGRESS`, `PROJECT_CONTEXT_HISTORY`, `1st.md`.

**Kiro specs:** `multi-tenant-identity` (done, deploy pending), `client-onboarding` (planned).

> **Known absences in repo functions** (frontend references them; not found in `functions/src/index.ts`): `submitReview`, `joinWaitlist`, `requestDataExport`, `requestDataDeletion`, `trackSocialEngagement`, `getSmartAvailability`, `getActiveBusinesses`, and any scheduled reminder. This is the basis for every ⚠️ flag in this document.

---

## Appendix B — How this document was produced

This file is a **consolidation of four earlier draft files** — `FEATURE_INVENTORY_01.md`, `_02`, `_03`, and `_04` — which were all intermediate *planning/analysis* notes rather than finished inventories (each still contained reasoning like "now let's write it" / "let me count the features"). Each draft contributed:

- **`_01`** → the compact numbered feature list and the 4-state status legend.
- **`_02`** → the audience taxonomy and competitor context (Booksy / Phorest / Square / Vagaro).
- **`_03`** → the most complete feature-by-feature detail with evidence, and the best status roll-up.
- **`_04`** → the app/tech overview, the most specific LIVE/IN-PROGRESS/PLANNED flags, and the EN/DE localization detail.

Content was **deduplicated, statuses normalized, and all planning meta-commentary stripped.** The four source drafts are now **superseded** by this file and may be deleted.
