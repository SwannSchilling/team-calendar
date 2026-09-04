# Team Calendar — Feature Showcase (GitHub Pages)

A single-page product tour for **Team Calendar**, the studio-management PWA built for tattoo studios.
It presents the full `FEATURE_INVENTORY.md` (81 features, 11 work areas) in a guided, three-depth structure:

1. **Hero** — one-line positioning + live day-view mock + stat strip.
2. **A day in the studio** — five before/after story beats (the daily pain points the app removes).
3. **The toolkit** — seven pillar sections with snappy feature cards and hand-built vector mockups.
4. **What the other tools don't have** — the 10 differentiators, expandable.
5. **The full inventory** — all 81 features, filterable by search / work area / status / role, each row expandable.
6. **Roadmap + honesty note** — planned items and the status legend, flagged as of a pinned repo commit.

## Stack

- [Astro](https://astro.build) (static output) with a dark ink & amber design system in plain CSS
- `three.js` noise-dissolve load-in (the Codrops transition, repurposed as a one-shot reveal) + GSAP core for text/scroll motion
- Feature data parsed from `FEATURE_INVENTORY.md` into `src/data/features.json` (see below)
- GitHub Actions → GitHub Pages (project subpath)

## Develop

```bash
npm install
npm run dev      # http://localhost:4321/team-calendar/
npm run build    # outputs dist/
npm run preview
```

> The repo keeps both `package-lock.json` (used by CI via `npm ci`) and `pnpm-lock.yaml` (local convenience).
> Pick one and delete the other when convenient — CI is npm-based.

## Deploy to GitHub Pages

The `.github/workflows/deploy.yml` workflow builds on every push to `main` and deploys via
`actions/deploy-pages`. One-time setup:

1. In the repo, **Settings → Pages** → set **Source** to **GitHub Actions**.
2. Push to `main` — the site goes live at
   `https://SwannSchilling.github.io/team-calendar/`.

If you rename the repo or move to a `username.github.io` repo, update `site` + `base` in
`astro.config.mjs` (and drop `base` when publishing at the domain root).

## Content pipeline

`FEATURE_INVENTORY.md` is the source of truth. After editing it, regenerate the data file:

```bash
node scripts/parse-inventory.mjs   # rewrites src/data/features.json
```

The parser verifies feature ids 1..N, category counts and status totals — read its console output
before committing. Curated marketing copy lives separately in `src/data/tour.ts`
(hero, story beats, pillar intros, differentiator punch lines, roadmap).

## German version (i18n)

The site has a hand-written German edition at `/team-calendar/de/` (EN/DE toggle in the frame nav).
It is a dedicated static build — no runtime JS translation:

| Locale | Entry | Copy | Features |
|---|---|---|---|
| EN | `src/pages/index.astro` → `<TourPage locale="en">` | `src/data/tour.ts` | `src/data/features.json` |
| DE | `src/pages/de/index.astro` → `<TourPage locale="de">` | `src/data/tour.de.ts` | `src/data/features.de.json` |

To update content in both languages:

```bash
node scripts/parse-inventory.mjs        # regenerate EN features.json from FEATURE_INVENTORY.md
# translate/adjust the DE twins by hand: features.de.json + tour.de.ts
node scripts/check-i18n.mjs             # verifies 81/81 ids, statuses, flags, categories aligned
npm run build
node scripts/verify-i18n-dist.mjs       # 33 post-build checks on dist/index.html + dist/de/index.html
```

Status and role labels are data-driven (`src/utils/text.ts`: `STATUS_LABELS` / `ROLE_LABELS`);
inventory UI strings live in `tour.ui` (EN) and `tour.de.ts` → `ui` (DE), mockup copy is passed
as a `copy` prop from `tour.mock` / `tour.de.mock`. Role filter keys stay language-agnostic
tokens (Owner/Admin/Artist/Client) so both locales filter identically.

The 404 page is shared and EN-only (accepted limitation — it can get a DE twin later).

## Screenshot capture spec (for real UI shots)

The visuals in this repo are hand-built vector mockups. When you have the app running, capture
the following and swap them into the corresponding components 1:1 (same framing, dark UI):

| Mockup component | Capture from | State to show |
|---|---|---|
| `MockDayGrid` | `/team/calendar` (day view) | 3 chairs, 4-5 appointments, one with reference-image chip, one time-off block, a buffer gap |
| `MockLedger` | `/finance` | 3 ledger rows with artist/shop split, checked-out chip, a closed+locked month |
| `MockPhone` | PWA on device (or devtools device emulation) | Home screen with installed icon + badge, 2 notification cards, offline indicator |
| `MockFlow` | `/booking` | The guided booking steps as they appear to a client |
| `MockTenant` | `/select-tenant` | A user with two studios, switching UI |
| `MockMatrix` | role-aware nav | No single shot — keep the table |
| `MockLink` | reschedule link email | The one-time link message (48h expiry visible) |
| `MockRefs` | appointment detail | Appointment with 2-3 reference thumbnails |

Guidelines: export as AVIF/WebP, cap width at 1600px, keep the app in its default (dark) theme,
redact real client names. Each component is a single self-contained file in `src/components/` —
replace its markup with an `<img>` of the same class to keep the layout intact.
