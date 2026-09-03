// Curated tour copy for the Team Calendar showcase.
// Feature ids reference entries in ./features.json (parsed from FEATURE_INVENTORY.md).

export interface StoryBeat {
  time: string;
  title: string;
  pain: string;
  fix: string;
  featureIds: number[];
  visual: "link" | "grid" | "refs" | "ledger" | "phone";
}

export interface Pillar {
  num: string;
  id: string;
  title: string;
  kicker: string;
  intro: string;
  featureIds: number[];
  visual?: "grid" | "ledger" | "phone" | "flow" | "tenant" | "matrix";
  aside?: string;
}

export const hero = {
  kicker: "Studio management PWA",
  title: "One app retires the sheet, the chat, and the napkin.",
  sub: "Team Calendar is the scheduler built for tattoo studios — guided client booking, a team calendar that books chairs as well as people, a commission ledger that answers “who owes what”, and an installable PWA that keeps working when the Wi-Fi doesn’t.",
  ctaPrimary: { label: "Walk through a day", href: "#story" },
  ctaSecondary: { label: "Full feature inventory", href: "#inventory" },
  stats: [
    { value: "81", label: "features inventoried" },
    { value: "55", label: "live in production" },
    { value: "11", label: "work areas" },
    { value: "4", label: "roles, one app" },
  ],
};

export const storyIntro = {
  kicker: "A day in the studio",
  title: "The five moments that used to run on hope.",
  sub: "Every one of these is a place where studios lose time, money or clients today. This is how Team Calendar handles each one — and which features you can dig into behind it.",
};

export const storyBeats: StoryBeat[] = [
  {
    time: "09:41",
    title: "“Can I move my appointment?”",
    pain: "It arrives as a DM, a call, a sticky note. Someone balances two phones and a paper calendar, finds a “free” slot that isn’t, and the chair never gets updated.",
    fix: "Your client taps a secure one-time reschedule link — no login, no app to install. Slots are computed from the artist’s real working hours, time-off and reschedule windows. The studio sets the policy: how far out to search, how many slots, how long the link lives.",
    featureIds: [11, 12, 13],
    visual: "link",
  },
  {
    time: "11:05",
    title: "Two artists, one chair.",
    pain: "Most booking tools book people. Nobody checks whether the chair is free — so two artists land on station two, and one of them gets moved at the last minute.",
    fix: "Workstations are bookable resources with their own capacity and buffer. Conflict detection runs per chair — artist, time-off and working hours all checked — before a slot is accepted. Day view renders a per-chair grid, so collisions are visible, not discovered.",
    featureIds: [16, 3, 15],
    visual: "grid",
  },
  {
    time: "14:30",
    title: "“I sent the reference.”",
    pain: "Buried under 400 DMs, sometimes low-res, sometimes the wrong one — and it’s gone by the time the client sits down.",
    fix: "Reference and before/after images attach to the appointment itself. Auto-resized on upload, deletable, and surfaced in the artist’s upcoming schedule and profile — exactly what to draw, before the client walks in.",
    featureIds: [10, 9],
    visual: "refs",
  },
  {
    time: "20:00",
    title: "The end-of-day math.",
    pain: "Who got paid what? Splits done on a napkin, argued over deposits, re-entered into a spreadsheet — and nobody trusts the numbers by month end.",
    fix: "Every ledger entry carries the per-transaction artist ↔ shop split. Checkout locks entries in place; month-close carries balances forward and locks the month. When the accountant asks, there’s a printable report — EN/DE.",
    featureIds: [35, 36, 37, 40],
    visual: "ledger",
  },
  {
    time: "22:15",
    title: "Dead Wi-Fi, loud studio.",
    pain: "The studio connection drops. The schedule lives on the laptop at the front desk. The phone that just rang is the one that can’t reach the app.",
    fix: "It’s a PWA: installed to the home screen, working offline, syncing when the connection returns — and the app-icon badge tells you what needs attention. Push tiers let each artist decide how much the phone is allowed to ping.",
    featureIds: [74, 75, 54, 56],
    visual: "phone",
  },
];

export const pillarsIntro = {
  kicker: "The toolkit",
  title: "Eleven work areas. Seven you’ll actually use daily.",
  sub: "Everything below is in the full inventory at the bottom — filter it by area, status or role. These are the pillars a studio touches every day.",
};

export const pillars: Pillar[] = [
  {
    num: "01",
    id: "booking",
    kicker: "Booking",
    title: "Bookings without the back-and-forth.",
    intro: "The client gets a guided path — a recommended slot with a match score, or full control over service, artist, date and time. The front desk books in one pass, even for a brand-new client.",
    featureIds: [1, 2, 3, 4, 10],
    visual: "flow",
  },
  {
    num: "02",
    id: "calendar",
    kicker: "Team calendar",
    title: "The core surface.",
    intro: "Day, week and month views, scoped to every role. Filter to your own schedule, mark time off with a reason, and let per-chair buffers do the cushioning.",
    featureIds: [7, 8, 14, 15, 16, 6],
    visual: "grid",
  },
  {
    num: "03",
    id: "finance",
    kicker: "Studio finance",
    title: "The napkin-math killer.",
    intro: "The module most booking tools skip entirely: the studio’s money tracked inside the scheduler, per transaction, per perspective, down to a locked, printable month.",
    featureIds: [35, 36, 37, 40, 41],
    visual: "ledger",
  },
  {
    num: "04",
    id: "clients",
    kicker: "Clients & reputation",
    title: "Know every client. Earn the next visit.",
    intro: "Profiles with booking history and Instagram handles, live no-show and retention stats, and a review loop that turns a post-visit thank-you into a repeat booking.",
    featureIds: [18, 19, 65, 67, 63],
  },
  {
    num: "05",
    id: "pwa",
    kicker: "Notifications & PWA",
    title: "Built for the chair, not the office.",
    intro: "Push, in-app and email triggers for every event that matters — with staff tiers so nobody’s phone rings itself hoarse, and offline mode for when the studio drops the connection.",
    featureIds: [55, 56, 54, 74, 75],
    visual: "phone",
  },
  {
    num: "06",
    id: "tenants",
    kicker: "Multi-location & multi-tenant",
    title: "One account, many studios.",
    intro: "Each site keeps its own timezone and currency; tenants stay strictly isolated by rule. Run two studios from one login without a single data leak.",
    featureIds: [43, 44, 45],
    visual: "tenant",
  },
  {
    num: "07",
    id: "admin",
    kicker: "Admin & paperwork",
    title: "Everything configured in one place.",
    intro: "Hours, roles, services, chairs, sites, forms and ledgers — one settings suite. Paperwork (intake, consent) happens before the chair, not during it.",
    featureIds: [71, 59, 60, 69],
    visual: "matrix",
  },
];

export const differentIntro = {
  kicker: "Proof of difference",
  title: "What the other tools don’t have.",
  sub: "Booksy, Phorest, Square, Vagaro, Zenoti — none of these ship the next ten. These are the features that make Team Calendar a different animal, not a me-too scheduler.",
};

// Punch lines shown on the 10 differentiator cards; the full text comes from features.json.
export const differentPunch: Record<number, string> = {
  1: "The “who owes what” answer, automatic — per transaction.",
  2: "Books the chair, not just the person.",
  3: "The artist sees exactly what to draw before the client sits down.",
  4: "No login, no back-and-forth — and the studio sets the rules.",
  5: "Review → 10% off → Instagram → Google, one tracked loop.",
  6: "Knows which artist, which time, which chair will free up.",
  7: "An installable app that works offline and lets you dial the pings.",
  8: "One account across studios, isolated by rule.",
  9: "A social-first client base, right in the record.",
  10: "Multi-region, without manual conversion.",
};

export const inventoryIntro = {
  kicker: "The full inventory",
  title: "All 81 features, filterable.",
  sub: "The complete list — what each feature does, who it’s for, and exactly how far along it is. Filter by area, status or role, or search for a specific capability.",
};

export const legend = [
  { key: "live", mark: "✅", label: "Live", desc: "Built and in production." },
  { key: "progress", mark: "🟡", label: "In progress", desc: "Code present; known issues or partial backend." },
  { key: "pending", mark: "🔶", label: "Deploy pending", desc: "Implemented + tested, awaiting deployment." },
  { key: "planned", mark: "⏳", label: "Planned", desc: "Roadmap / spec only, not yet built." },
  { key: "verify", mark: "⚠️", label: "Verify", desc: "UI in repo; matching Cloud Function unverified." },
];

export const roadmap = {
  kicker: "What’s next",
  title: "On the roadmap.",
  sub: "Planned, not yet built — flagged ⏳ in the inventory above.",
  soon: [
    { id: 42, label: "Stripe deposits & payments at booking" },
    { id: 60, label: "Client-facing intake / consent forms (next step)" },
    { id: 57, label: "Automated 24h / 1h reminders (unverified)" },
    { id: 49, label: "Client onboarding wave (composite client model)" },
    { id: 48, label: "Branded public booking URL per studio" },
  ],
  later: [
    { id: null, label: "Internal team messaging" },
    { id: null, label: "Advanced reporting & analytics" },
    { id: null, label: "Block-out time slots" },
    { id: 80, label: "Multi-language (i18n)" },
    { id: 81, label: "Customizable themes / branding" },
    { id: null, label: "Public API" },
    { id: 58, label: "Client-facing notifications" },
  ],
};

export const honestyNote =
  "Status flags reflect the repository state as of 2026-08-29 (commit edbc187). Features marked in-progress or verify are real UI, but their backend is still landing — the inventory above keeps that honest."

export const footer = {
  tagline: "The studio scheduler that retires the sheet, the chat, and the napkin.",
  github: "https://github.com/Ibaliqbal/codrops-barbajs-page-transition",
};

