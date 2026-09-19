# 02 — Normalized Feature Matrix (independent)

**Accessed 2026-09-19.** Built from official product pages + Apple App-Store records + Wayback; never from marketing alone. Team Calendar column = the repo's own `FEATURE_INVENTORY.md` (@`edbc187`).

**Legend:** `✔` documented (official page / App-Store) · `✔?` advertised, depth unverified · `~` partial · `✖` **not found in sources checked (≠ absent in product — several rivals are tiny SPAs)** · `★` Team Calendar *staff-side* differentiator · `sim` simulated · `unv` backend not in repo · `pln` planned · `undep` built-but-undeployed.
Competitor abbrev: ISM=Ink Studio Manager; INOS=INKOS.

### Columns: TC | TatTool | inkStar | INOS | InkSchd | ISM | TatMgr | InkLinka | Linework | Calenza | Anolla

## 1 · Scheduling
| Feature | TC | TatTool | inkStar | INOS | InkSchd | ISM | TatMgr | InkLinka | Linework | Calenza | Anolla |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Online booking | sim | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Appointment / artist / shared calendar | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Station/chair as bookable resource | ★ | ✖(loc) | ✖ | ✖ | ✖ | ✖ | ~ | ✖ | ✖ | ✖ | ✔ |
| Per-resource conflict detection | ★ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ~ |
| Buffer / setup time | ★ | ✖ | ✔ | ~ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| Breaks | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ | ~ | ✖ | ✖ | ✖ | ✖ |
| Working hours | ✔ | ✔ | ✔ | ~ | ✖ | ✖ | ~ | ✖ | ✖ | ✖ | ✔ |
| Holidays / closures | ~ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| Absences / time-off | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| Guest / resident artists | ~ | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ | ✔ | ✖ | ✔ | ✔ |
| Walk-ins | ✔ | ✔? | ✖ | ✔? | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ |
| Recurring appointments | ~ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| Multi-session tattoos | ~ | ~ | ✔ | ✔ | ✖ | ✔ | ~ | ✔ | ✖ | ✖ | ~ |
| Waitlist | unv | ✖ | ✔ | ✖ | ✔? | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ |

## 2 · Client management
| Feature | TC | TatTool | inkStar | INOS | InkSchd | ISM | TatMgr | InkLinka | Linework | Calenza | Anolla |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Client profiles / DB | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Client / tattoo history | ~ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ~ | ✔ | ✔ |
| Notes | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Reference / design images | ★ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ |
| Project management | ~ | ~ | ~ | ✔ | ✖ | ✔ | ~ | ✔ | ✖ | ✖ | ~ |
| Consultation | ~ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ~ |
| Consent / intake + e-sign | ~ (NEXT) | ✔ | ✔ | ✔ | ✖ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ |
| Medical / anamnesis | ✖ | ✔ | ✔ | ✔? | ✖ | ✖ | ✖ | ~ | ~ | ✖ | ~ |
| Aftercare | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✔ |
| Customer portal / mini-site | ~ | ✖ | ✔? | ✔ | ✖ | ✖ | ✔ | ✔? | ✔? | ✖ | ✔ |

## 3 · Booking workflow
| Feature | TC | TatTool | inkStar | INOS | InkSchd | ISM | TatMgr | InkLinka | Linework | Calenza | Anolla |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Public booking link / page | pln | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Customer self-booking | **sim** | ✔ | ✔(AI) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Customer self-reschedule | ~ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✔? | ✔ | ✖ | ✔ |
| Secure one-time link | ✔ | ✖ | ✔? | ✖ | ✖ | ✖ | ✖ | ✔? | ✖ | ✖ | ✖ |
| Login requirement / gating | ✔ | ✔? | ✔? | ✔? | ✖ | ✖ | ✖ | ✔? | ✔? | ✖ | ✔ |
| Deposit at booking | ✔(ledger) | ✔ | ✔ | ✔ | ✔(Stripe) | ✔ | ✔ | ✔(Stripe) | ✔(Stripe) | ✔ | ✔ |
| Cancellation policy | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ~ |
| Automated reminders 24h/1h | **unv** | ✔ | ✔(24h/2h) | ✔? | ✔? | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ |
| SMS | ✖ | ✔ | ✔ | ✔? | ✔? | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ |
| Email | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

## 4 · Financials  (★ = TC ledger is the differentiator; ✖ here is the market's blind spot)
| Feature | TC | TatTool | inkStar | INOS | InkSchd | ISM | TatMgr | InkLinka | Linework | Calenza | Anolla |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Deposits | ✔(ledger) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Payments (tracking) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| POS / ticketing | ✖ | ✔? | ✔? | ✖ | ✖ | ✖ | ✖ | ✔? | ✔? | **✔** | ✔ |
| Cash-drawer reconciliation | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | **✔** | ✖ |
| Online payment processor | **pln**(Stripe) | ✔ | ✔(Stripe) | ✖ | ✔ | ✖ | ✖ | ✔(Stripe) | ✔(Stripe) | ✔? | ✔ |
| Invoices | ✔ | ✖ | ✔ | ✖ | ✔? | ✖ | ✖ | ✖ | ✔? | ✔ | ✔ |
| Artist commissions | ★ | ~ | ✔ | ✔ | ✔ | ~ | ~ | ✔? | ~ | **✔** | ✔ |
| Artist/shop split (txn-level alloc) | ★ | ✖ | ~ | ✖ | ✖ | ✖ | ✖ | ~ | ✖ | ~ | ~ |
| Checkout / settled state | ★ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔? | ✖ |
| **Monthly close / locked months / carry-forward** | ★ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| Financial reports / analytics | ~ (adv. = pln) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔(AI) | ✔ | ✔ | ✔ |
| Payout calc | ~ | ✖ | ✖ | ✖ | ✔? | ✖ | ✖ | ✔? | ✖ | **✔** | ✖ |

## 5 · Studio management
| Feature | TC | TatTool | inkStar | INOS | InkSchd | ISM | TatMgr | InkLinka | Linework | Calenza | Anolla |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Roles / permissions (incl. custom) | ★ | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ | ✔? | ✔? | ✔ | ✔ |
| Multiple artists | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Multiple rooms / stations | ★ | ✖(loc) | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| Multiple locations | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔(sites) | ✔? | ✖ | ✖ | ✔ |
| Multi-studio / multi-brand | undep | ~ | ✔ | ✔ | ✔ | ✖ | ✔ | ✔ | ✖ | ✖ | ✔ |
| **True multi-tenant (rule-enforced)** | ★undep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ~ |
| Studio branding / theming | ✖ | ✖ | ✔ | ✔? | ✔ | ✖ | ✖ | ✔? | ✔ | ✔? | ✔ |
| Staff management | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ | ✔? | ✖ | ✔ | ✔ |

## 6 · Communication
| Feature | TC | TatTool | inkStar | INOS | InkSchd | ISM | TatMgr | InkLinka | Linework | Calenza | Anolla |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| WhatsApp | ✖ | ✖ | ✖ | ✔? | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| Instagram presence | unv | ✖ | ✔? | ✔? | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ |
| Unified inbox | ✖ | ✔(messages) | ~ | ✔ | ✔ | ✖ | ✖ | ✔ | ✖ | ✖ | ✔ |
| Automated campaigns | ✖ | ✔(Flows) | ✔ | ✔ | ✖ | ✖ | ✖ | ✔(SMS/Email) | ~ | ✖ | ✔ |
| Review requests | unv | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| Post-visit review→reward loop | unv | ✖ | ✔? | ✔? | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔? |

## 7 · Tattoo-specific
| Feature | TC | TatTool | inkStar | INOS | InkSchd | ISM | TatMgr | InkLinka | Linework | Calenza | Anolla |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Flash / flash-days (bookable) | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ |
| Tattoo projects / sessions | ~ | ~ | ✔ | ✔ | ✖ | ✔ | ~ | ✔ | ✖ | ✖ | ~ |
| Reference-image management | ★ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ |
| Ink registration (batch / data-sheet) | ✖ | **✔** | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| Stencil / workflow tools | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | **✔** | ✖ | ✖ | ✖ |
| Aftercare | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✔ |
| Guest spots / conventions | ~ | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ | ✔ | ✖ | ✔ | ✔ |
| Inventory / merch | ✖ | ✖(ink) | ✖ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✔ |
| Gift cards / vouchers | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✔? | ✖ | ✖ | ✔ |

## 8 · Technical
| Feature | TC | TatTool | inkStar | INOS | InkSchd | ISM | TatMgr | InkLinka | Linework | Calenza | Anolla |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Installable PWA** | ★ | ✖ | ~ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| **Offline mode + sync** (browser) | ★ | ✖(offline pay) | ✔(claim) | ✔(claim) | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| Native mobile app | ✖(PWA) | ✖ | ✔ | ✖ | ✔ | ✔ | ✔? | ✔ | ✖ | ✖ | ✔ |
| Browser app | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Public API | pln | ✖ | ✖ | ✖ | ✔? | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| Google / Apple Calendar sync | ✖ | ✖ | ✔ | ✔ | ✔? | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| Stripe / payment providers | pln | ✔ | ✔ | ✖ | ✔ | ✖ | ✖ | ✔ | ✔ | ✔? | ✔ |
| Accounting integration | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |

## 9 · Analytics
| Metric | TC | TatTool | inkStar | INOS | InkSchd | ISM | TatMgr | InkLinka | Linework | Calenza | Anolla |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Revenue | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Utilisation / occupancy | ✖ | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✔ |
| No-shows / cancellations | ✔(client stats) | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| Customer retention | ✔ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✔? | ✖ | ✖ | ✔ |
| Artist performance | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ | ✔ |
| Booking conversion | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✔ |

---

## Commoditisation verdict (the matrix's one-line takeaway)
- **Commoditised (assume rivals have it):** online booking, online client self-booking/reschedule, deposits, reminders, consent forms, waitlists, client profiles/history, reference images, artist **commission tracking**, basic revenue analytics, multi-studio *label*.
- **Genuinely thin air (rare across the field):** **browser-PWA offline+sync** (TC live; rivals only *claim* it or ship it **native-first**); **workstation/chair as a conflict-checked, buffer-attached resource** (documented **only** at generalist **Anolla** (workstations/booths/equipment) + niche **Inkoru("cabina")/Tat2App("chairs")/Damin(„Geräte")**, plus **TattooManager** at *room* level ("Räume") — **none pairs it with per-station conflict+buffer+offline+ledger**); **a controlled financial ledger with checkout → monthly-close → locked months → carry-forward** (nobody advertises the close/lock semantics).
- **TC's liability cells:** *simulated* online booking; *unverified* reminders/reviews/waitlist/social/GDPR backends; *undeployed* multi-tenant; *planned* online payments; and **missing** POS/cash-drawer, aftercare, ink registration, inventory, gift/merch, flash-days, SMS/WhatsApp/inbox, campaigns, calendar-sync.

> **Transparency note.** Two cells were corrected after adversarial re-reading of the vendors' *own* German copy: **inkStar** carries **0 "station"** on both its site *and* its App-Store copy (so the prior report's "inkStar has station booking" is **refuted**), while **TattooManager** does advertise **room/resource coordination** ("Räume, Artists und Zeiten bleiben sauber koordiniert"; "Termine, Pausen und Ressourcen") + email/SMS reminders — so its station & reminder cells were raised from ✖ to `~`/`✔`. `✖` means *not found in the pages checked*, never *proven absent*; several rivals are unreadable SPAs, so their `✖` is soft.
