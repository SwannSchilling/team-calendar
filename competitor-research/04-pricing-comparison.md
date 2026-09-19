# 04 — Pricing Comparison (independent)

**All pricing captured / verified on 2026-09-19** from official pricing pages where reachable. Currencies kept native (not converted). "not pub" = field not published on the official page (treated as **not publicly disclosed — not "free"**).

### Method & honesty notes
- Prices are **plan/sticker prices** from the vendor's own pricing page. Where a page is a client-rendered SPA (InkSchedule, InkLinka) or the plan price lives only in an **in-app purchase** (App-Store apps), the numeric price is *not verifiable* from the public page and is written as **not publicly disclosed**, **not** estimated.
- Where a page is internally contradictory (trial length), the conflict is recorded, not silently resolved.
- **Transaction / payment-processor / deposit / SMS per-unit fees are almost universally NOT published** — only **four** concrete fee-rates exist anywhere in the market (listed at the bottom). Everyone else: "not publicly disclosed."

---

## Master pricing table (accessed 2026-09-19)

| Product | Free plan | Free trial | Entry (per month) | Per-artist / seats | Multi-location / Enterprise | Transaction fee | Payment processor | SMS | Cur | Source (official) | Conf. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **TatTool** | No | yes (β) | **$49** | seats 3 / 10 / 25 / 50 | Enterprise $399 / 50 seats (sales) | none pub (tax @ checkout) | not pub (online+offline payments feature) | not pub | **USD** | tattool.io/pricing | Verified |
| **inkStar** | No | 7-day, no card | **€8.99** Starter | 1 / 1 / 5 users (Plus/Pro) | Pro=multi-loc; Enterprise custom | none pub | Stripe (rate not pub) | **€0.12 / message** | **EUR** | inkstar.app/en/p/pricing | Verified |
| **InkSchedule** | No | yes *(page says BOTH 14-day and 30-day — conflict)* | **$29** Solo | Solo 1 / Studio ≤5 / Ent ∞ | Enterprise $149, multi-loc | none pub | Stripe (deposits) | included | **USD** | inkschedule.app | Verified (price) |
| **Ink Studio Manager** | No | 14-day auto | **€35 per artist** (flat) | per-artist only | not pub | not pub | not pub | not pub | **EUR (net)** | inkstudiomanager.de (#Preise) | Verified |
| **TattooManager** | No | 30-day (all tiers) | **€19.99** Basic | caps 3 / 5 / 10 / 20 | sites 3 / 5; top €399.99 | none pub | not pub | included Pro+ | **EUR (net)** | tattoomanager.de/preise/ | Verified |
| **Linework** | **YES $0** | n/a | **$0** Free (all features) / Pro **$19** | Artist & Studio | none pub | **6%** on Free; **2.9% + 30¢** on Pro | Stripe | unlimited texts, $0 | **USD** | linework.com/pricing | Verified |
| **InkLinka** | not est. | yes | **not publicly disclosed** | plan limits not pub | multi-currency | ~**5%** platform fee *(Claimed, from app bundle, not a public price page)* | Stripe → charged to client *(Claimed)* | plan-limited | multi-cur | inklinka.com/en/pricing (SPA shell) | Unverified |
| **INKOS** | — | — | **not established** | — | — | — | — | — | — | inkos.me empty; no site found | **Unresolved** |
| **Calenza** | not est. | not est. | **not publicly disclosed** (no /pricing route; sitemap has none) | n.d. | n.d. | n.d. | n.d. | n.d. | ($ via demo) | calenza.app | Unknown |
| **Anolla** | **YES core** | n/a | **no monthly fee** (usage-based) | unlimited core | capable | **% "applies only after the job is confirmed"** (rate not pub) | direct + integrated | feature | feature | **EUR** implied | anolla.com/en/tattoo-software | Verified model / Unverified number |
| **Team Calendar** | n/a | n/a | **not publicly disclosed** (pre-GA showcase; no public price page in repo) | — | architecture supports multi-studio | **none today** (no online payment) | **none** — payments are ledger/cash; **Stripe deposits = planned (⏳)** | (push; SMS n/a) | — | repo `FEATURE_INVENTORY.md` | Claimed |

---

## App-Store "studio-management" apps (free app + hidden in-app subscription)

| Product (operator) | App price | Subscription | Notes | Conf. |
|---|---|---|---|---|
| Tattoo Studio Pro (Zadie Studio LLC) | Free + 30-day trial | **not disclosed (in-app purchase)** | ⚠️ the publicly visible **$99 / $149 are one-time DIY *website templates*, NOT the studio plan** — do not cite as plan price | Verified app / Unknown price |
| Ink Link (Ink Art Media Group LLC) | Free | **not disclosed (IAP)** | "Artist Pro" / "Studio Pro" tiers exist; prices not exposed | Unknown price |
| INKbusiness (INKSEARCH sp. z o.o.) | Free | not disclosed | last app update **2022 → likely abandoned** | Unverified |
| Pixieset Studio Manager | $0 free / $8–$40 | platform tiers | ⚠️ **NOT tattoo** — a **photography/creative studio** manager (Acuity-like); likely mis-listed; tiers are platform/Client-Gallery | Excluded from tattoo set |

---

## The fee landscape — only four published fee rates exist anywhere in this market
| Rate | Product | Value | Status |
|---|---|---|---|
| SMS / message | inkStar | **€0.12 / message** | Verified (official) |
| Transaction fee | Linework | **6%** (Free) → **Stripe 2.9% + 30¢** (Pro $19) | Verified (official) |
| Platform fee on deposits | InkLinka | **~5%** (+ Stripe fee charged to client) | Claimed (app-bundle i18n, not a public price page) |
| Store-sale commission (free tier) | Pixieset | **15%** free / 0% paid | Claimed (and product is not tattoo) |

**Implication.** Almost every competitor (TatTool, InkSchedule, both German vendors, Anolla, all App-Store apps) keeps deposit / payment-processor / SMS per-unit pricing **opaque**. "Not publicly disclosed" is therefore a genuine, defensible market observation, not a gap in this research. **A competitor that published flat, predictable processing/SMS pricing could attack this opacity** — relevant to Team Calendar only if/when it ships online payments (Stripe deposits are currently *planned ⏳*; today there are **no payment/transaction/SMS fees** because there is **no online payment or SMS**).

---

## Pricing-pattern read-outs (evidence-based)
1. **Two dominant models:** (a) **flat per-artist** (Ink Studio Manager €35/artist; TattooManager seat caps; TatTool seat bands) and (b) **feature-tier SaaS** (inkStar, InkSchedule). InkLinka/Anolla lean toward **usage/transaction** monetisation.
2. **Entry prices cluster at the low end** (€8.99–€35 / $29–$49), and **two players are effectively free-to-enter** (Linework free tier w/ 6%; Anolla free core + usage). → **Willingness-to-pay in this segment is low and price-sensitive.** Team Calendar must assume competitors win on *price and on "all features free, we take 6%"*, not on tiered features.
3. **Multi-location is not universally priced openly** — only inkStar(Pro), InkSchedule(Enterprise $149), TattooManager (site caps 3/5) publish it; INKOS/Calenza/InkLinka/Anolla/InkLinka do not. → Team Calendar's multi-studio is **architecturally real** but **commercially unpriced**, i.e. it is a *capability today, not a productised plan tomorrow*.
4. **Every competitor with online money routes through Stripe.** Team Calendar does **not** — it currently tracks money in an internal **ledger (cash/deposits)** with **Stripe deposits only *planned***. That is simultaneously a *honesty risk* (don't advertise online payments) and a possible *niche wedge* ("your books, not another payment processor").

### Sources (accessed 2026-09-19)
`tattool.io/pricing` · `inkstar.app/en/p/pricing` · `inkschedule.app` · `inkstudiomanager.de/#Preise` · `tattoomanager.de/preise/` · `linework.com/pricing` · `inklinka.com/en/pricing` · `calenza.app` · `anolla.com/en/tattoo-software` · Apple iTunes Lookup trackIds `1490817384`/`1585631896`/`6761015637` · Team Calendar `FEATURE_INVENTORY.md` @ `edbc187`.
