# 05 — Customer Pain Points (independent)

**Accessed 2026-09-19.** Two independent lenses, kept explicitly separate:
- **§A Vendor-framed pain (`T1`)** — *how each competitor markets the problem it solves* → tells us **who they target and which pains the market considers monetisable**. This is *their* claim about the customer, not the customer's own voice.
- **§B Customer/community pain (`T3`)** — what practitioners actually say (Reddit r/TattooArtists, dated, linked). Independent of any vendor.
`§C` then maps both onto **what Team Calendar genuinely relieves today vs. only simulates**.

---

## §A · The problem each competitor *sells against* (vendor framing, `T1`)
| Competitor | The pain it names on its own page | Implied target |
|---|---|---|
| **inkStar** | *"clients didn't show. **No call. No text. Just an empty chair and lost income.**"* · *"clients book through social channels, forms need to be signed … **answering DMs, updating your calendar, sorting paperwork** … keep admin from taking over evenings"* | solo/multi **artist drowning in DMs + no-shows + admin in the evenings** |
| **Ink Studio Manager** | *"**Nie wieder Terminchaos, No-Shows oder Zettelwirtschaft**"* (never again booking-chaos, no-shows or paper-shuffle) · *"**Keine Doppelbuchungen** mehr"* · *"Erinnerungen reduzieren No-Shows"* | German **shop owner still on paper/spreadsheet** |
| **TattooManager** | *"**Weniger Doppelbuchungen** — Räume, Artists und Zeiten sauber koordiniert"* · *"Automatische Erinnerungen … reduzieren No-Shows"* | German **studios** (solo→large), rooms+staff coordination |
| **TatTool** | *"…schedule … **without double-booking artists**"* ; *"reconciled … revenue targets"* | studios wanting **one connected toolkit + reporting** |
| **Calenza** | *"**books reconcile to the cent**"* · *"**expected cash equals collected minus payouts**"* | **multi-vertical shop owner** whose daily cash/commissions don't reconcile |
| **InkLinka** | *"**Often lost in chats, files or separate folders** … scattered across chats and devices"* · *"Move from **manual coordination** to a scalable operating system"* · *"Why not spreadsheets?"* | **growing studio** outgrown chat+spreadsheet coordination |
| **Anolla** | *"coordinate studio **resources** … **avoid awkward situations in front of the customer**"* (resource/inventory planning) | generalist **service business**, incl. studios |

**What the vendors collectively signal is "monetisable"** (their hero copy, i.e. the pains they believe sell): ① **booking chaos / DM sprawl**, ② **no-shows & lost chair-time**, ③ **double-bookings / coordination**, ④ **paper/spreadsheet ("Zettelwirtschaft")**, ⑤ **money that doesn't reconcile (commissions/cash)**, ⑥ **admin eating non-billable hours**. **Note the asymmetry:** the money-reconciliation pain (⑤) is claimed by only **Calenza/InkLinka/TatTool** with any depth — which is exactly Team Calendar's strongest verified turf.


## §B · What practitioners *actually* say (`T3` — r/TattooArtists corpus, 628 items, harvested via the pain-point subagent, accessed 2026-09-19)
> **Read this correctly:** Reddit is a **self-selected, un-representative** sample — treat as **directional, not statistical**. Its *strength* is that it is **vendor-independent** and matches the vendor framing in §A almost theme-for-theme (an independent corroboration, not a marketing echo). Hit-counts are corpus occurrences of theme keywords.

**① Booking chaos / DM-sprawl — the loudest pain (26 hits).**
- *"the booking nightmare. Trying to jump between **Instagram DMs, WhatsApp, and Google Calendar** to keep track of clients…"* — *How do you actually manage your tattoo workflow?* (2026-06-02, `1tum85p`)
- *"using **instagram dms and a paper planner and my phone** … and it's getting really exhausting — I need a better way to save time for drawing instead of using my off time for administrative work."* — *Advice/recommendations for booking services* (2026-07-30, `1vapgm5`)
- *"…keep booking in IG DMs, push people to a form/email, or have someone else screen messages?"* (2026-01-15, `1qd5z06`)

**② Deposits / commitment — the single biggest theme (104 hits).**
- *"I said yes to $2,000, but he **ghosted me right after I asked for a deposit**."* (2025-02-23, `1iw1ag5`)
- *"I like to establish the client is **serious then take a deposit**, but … I don't like being **pushy like a phone-shop salesman**."* (2023-09-15, `16jdgze`)
- *"especially when it has to do with **taking deposits** … I **fear scamming** … gotta protect my clients as well."* (2026-07-30, `1vapgm5`)
 → *Deposit collection is felt as a **trust / awkwardness** problem, not just a money problem.*

**③ No-shows / ghosting (31 hits).**
- *"i have a client completely **ghost and no-show** me today. actually insane … what do you [do]?"* — *NO SHOW (vent)* (2025-06-07, `1l5a9bi`)
- *"I work in an appointment-only studio … I do almost all consultations online, but …"* (no-show consults) (2026-05-11, `1ta07ot`)

**④ Double-bookings / resource conflicts (39 hits) — incl. the resource/room pain that maps to Team Calendar's station wedge.**
- *"…set to **not allow double booking** and appointment requests turned off, but the leads feature [let people request 9am] **on a day we are closed**."* — *Need a new … booking platform as Meta has gone off* (2024-06-01, `1d5a0e8`)
- *"I have an **extra booth** I use for this **so it doesn't conflict**."* — *What do you charge for guest spots?* (2023-05-31, `13w7j89`) → a real artist reasoning about **booth/chair capacity**, i.e. the *station* concept exists in heads, not just in software.

**⑤ Tool-choice churn / comparison-shopping (20 hits) — competitive signal.**
- *"**What tattoo software do most of you use?** … what's been your **experience**? Would you **recommend one over the other**?"* (2025-09-17, `1njig5s`)
- *"**What do you use to book clients?** … I'm the **front-desk manager** for a local shop…"* (2023-01-05, `1043wqb`) → the buyer is **not only the artist** — a **receptionist/front-desk** persona exists (relevant: role-based UI).
- *"Need a new messaging-and-booking platform **as Meta has gone off**"* (2024-06-01, `1d5a0e8`) → platform-dependence on Instagram/Facebook booking is itself a **migration risk** competitors exploit.

*(Thread ids map to `https://www.reddit.com/r/TattooArtists/comments/<id>`; verbatim excerpts held in `_research/raw/reddit/corpus.jsonl`.)*

## §C · Mapping pain → Team Calendar's *actual* state (the uncomfortable read)
| Community/vendor pain (§A+§B) | Loud? | Does Team Calendar genuinely relieve it **today**? |
|---|---|---|
| ① Booking chaos / DM-sprawl → clients self-book | **#1 loudest** | **NO (partially).** Staff-side *team calendar* yes; **customer self-booking is `sim`** (mock slots, no `getSmartAvailability`). The pain competitors monetise hardest is TC's weakest cell. |
| ② Deposit collection / "is this client serious" | **biggest theme (104)** | **PARTLY.** TC *books-keeps* deposits in the ledger, but **online deposit-at-booking is `pln` (Stripe)** — so it does **not** yet solve the *"avoid the awkward deposit chase"* pain inkStar/Taddoo/InkLinka sell. |
| ③ No-shows / ghosting | high | **UNVERIFIED.** 24h/1h **reminders have no scheduled Cloud Function in the repo** → cannot claim no-show relief until proven. |
| ④ Double-bookings / room–chair conflicts | medium | **YES — genuine.** per-station **conflict + capacity + buffer checked pre-save** (`live`), and §B shows practitioners reason about it ("extra booth so it doesn't conflict"). **Under-served, under-marketed.** |
| ⑤ Money that reconciles (commissions/cash/payout) | medium (vendor-side high) | **YES — strongest.** transaction-level artist/shop split + checkout + **month-close + locked months + carry-forward** (`live`) — the community's trust/precision need with almost no competitor advertising the close/lock semantics. |
| Front-desk/receptionist persona (§B `1043wqb`) | — | **YES.** three-tier + custom roles & role-scoped views (`live`) serve a buyer that solo-artist apps (inkStar/Taddoo) mostly don't. |

### Strategic take-aways from the pain evidence
1. **TC's provable value sits on pains ④+⑤ — real, but *quieter* than the market's loudest pains ①–③.** The loud pains (self-booking from DMs, deposit collection, reminders) are exactly TC's `sim`/`pln`/`unv` cells → they are the **fastest ship-fast backlog**, *and* until they ship, **TC must not advertise that it relieves ①–③**.
2. **The reconciliation/precision pain (⑤) is the least-contested with the highest trust stakes** (Reddit "fear scamming", Calenza's "reconcile to the cent") → this, plus the chair-conflict floor (④), is where TC can credibly *lead*, because no competitor pairs depth there with offline-PWA.
3. **Do not fight the DM-sprawl war on marketing while the booking flow is simulated** — that's inkStar/Taddoo/InkLinka's home turf where they *ship*. Concede it on copy, win where you can prove it.
4. **Platform-risk angle (§B `1d5a0e8` "as Meta has gone off"):** artists fear Instagram-dependent booking; TC's *owned* calendar+ledger+offline, *if* paired with a real booking link, answers a live migration anxiety — but only post-`getSmartAvailability`.

## §D · Independent theme ranking + strategic anti-bias flags (`T3`, pain-point pass)
Source: `_research/raw/painpoints.md` (109 machine-extracted quotes, 110 citations) over `_research/raw/reddit/corpus.jsonl` (628 posts+comments). **Ranking basis = keyword/phrase regex over title+body of a pain-targeted corpus → an ordering signal, not a random sample.**

**Ranked by frequency (tattoo + adjacent SMB threads):**
**① deposit-chasing/non-payment ≈ ② tool complaints/switching (113 each) › ③ no-shows/late-cancel (94) › ④ commission/month-end (66) › ⑤ guest/resident artists (49) › ⑥ double-book/chair-conflict (39) › ⑦ WhatsApp/email-chaos (37)** › then retention (33), consent/paperwork (31), IG-DM overload (29), reminders (25), empty-chairs (20), admin-burden (20), references-lost-in-chat (12), waitlist (10), **multi-location (8)**, paper/Zettelwirtschaft (6), **offline/internet (1)**.

**Sharp corroboration (verbatim, thread-ids → `reddit.com/r/<sub>/comments/<id>`):**
- no-shows: *"...only 40% of these people [who book consultations] turn up"* (`1ta07ot`); *"every week at least 1 cancels, last week it was 4"* (`1n20t5r`)
- double-book: *"still double booking whenever someone forgets to log their time off"* — the conflict is **human-forgetfulness**, not tooling (`1ltvfhw`, r/smallbusiness)
- references: *"the worst part is having the reference pics all over the place... lost the ability to just see photos attached to the specific appointments"* (`18hoxdt`)
- waitlist: *"i had a whole 'waiting list' and then lost it!"* — lost-in-a-notebook (`17gdp8d`)
- admin: *"I spend up to 2 hours every evening just replying [to enquiries]"* (`1sz6kgd`)
- tool-spend: *"Phorest is the worst. Wildly expensive for what it is"* / *"I use square... $30 a month so they send text confirmations"* (`1op2fyz`, `1d5a0e8`)

**Anti-bias flags the strategy brief must absorb:**
1. **Offline is already someone else's headline** (inkStar: *"Full functionality even without internet... nothing gets lost"*) **yet has ~zero community demand signal** (only 1 weak infra-hobby hit). → **Team Calendar must not market offline as unique, nor even as a lead pain-reliever**; keep it a *reliability/form-factor* footnote unless the team's **own** pilot customers report studio-connectivity problems.
2. **The commission/ledger pillar is the WEAKEST customer-verified theme** — mostly *vendor-asserted* ("napkin-math"); community threads argue what the split *should* be & boss burnout ("bookkeeping, payroll"), only **one** comment describes manual weekly percentage-settlement. → **D2 (the close-grade ledger) is the least externally validated wedge → flag for primary research (interviews) before it leads marketing.**
3. **The real incumbent is generic tools, not tattoo apps.** App-Store ratings (machine-read via iTunes Lookup): **Square Appointments 195,291 · Booksy 856,739 · Vagaro Pro 15,686 · Tattoodo 7,175** vs the tattoo-*named* field **inkStar 0 · InkLinka 0 · InkSchedule 1**. **Square is a *liked* answer** in-thread ($30/mo texts praised) → attack **named failure modes**, not the brand.
4. **Table-stakes** at all rivals (do not differentiate on presence): deposits, no-show/reminder protection, IG→booking-link redirection, waitlist, e-consent.
5. **Two under-owned pains worth owning** (vivid, cheap to demo): the **manager-as-single-point-of-knowledge** ("our manager knows where everything is... if they are away it becomes hard") and the **lost-waitlist/data-loss** story.
6. **Community-trust hazard:** these very threads are **vendor-farmed** ("I opened Blackbook… free lifetime access", "built an app, DM me", a 2018 "paid research" disclosure). → Team Calendar should win attention with **evidence-led, non-promotional** participation, not astroturfing.
