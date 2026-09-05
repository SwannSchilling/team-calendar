// German (dedicated) tour copy for the Team Calendar showcase — /de/ route.
// Structure mirrors ./tour.ts (EN); feature ids reference ./features.de.json.

import type { StoryBeat, Pillar, UiStrings, MockCopy } from "./tour";

export const hero = {
  kicker: "Studio-Verwaltung · PWA",
  title: "Schluss mit Zetteln und guten Vorsätzen.",
  titleA: "Schluss mit",
  titleB: "Zetteln und guten Vorsätzen.",
  sub: "Team Calendar ist der Kalender für Tattoo-Studios — er ersetzt Chat-Nachrichten und Zettel, die zwischen zwei Terminen verloren gehen. Mit geführter Kundenbuchung, einem Teamkalender für Stühle und Kunden, einer Abrechnung, die nie den Überblick verliert, und einer App, die auch ohne WLAN weiterläuft.",
  ctaPrimary: { label: "Einen Tag miterleben", href: "#story" },
  ctaSecondary: { label: "Alle 81 Funktionen", href: "#inventory" },
  stats: [
    { value: "81", label: "Funktionen erfasst" },
    { value: "55", label: "live im Einsatz" },
    { value: "11", label: "Arbeitsbereiche" },
    { value: "4", label: "Rollen, eine App" },
  ],
};

export const storyIntro = {
  kicker: "Ein Tag im Studio",
  title: "Fünf Momente, die bisher auf Hoffnung liefen.",
  sub: "Jeder dieser Punkte ist eine Stelle, an der Studios heute Zeit, Geld oder Kund:innen verlieren. So löst Team Calendar jeden davon — und welche Features dahinterstecken.",
};

export const storyBeats: StoryBeat[] = [
  {
    time: "09:41",
    title: "\u201eKann ich meinen Termin verschieben?\u201d",
    pain: "Er kommt als DM, Anruf oder Zettel. Iemand jongliert mit zwei Handys und einem Papierkalender, findet einen \u201efreien\u201c Termin, der es nicht ist — und der Stuhl wird nie aktualisiert.",
    fix: "Dein Kunde tippt auf einen sicheren Einmal-Link zum Verschieben — ohne Login, ohne App-Installation. Termine werden aus den echten Arbeitszeiten, Abwesenheiten und Verschiebe-Fenstern der Künstler:in berechnet. Das Studio legt die Regeln fest: Wie weit wird gesucht, wie viele Termine, wie lange der Link lebt.",
    featureIds: [11, 12, 13],
    visual: "link",
  },
  {
    time: "11:05",
    title: "Zwei Künstler:innen, ein Stuhl.",
    pain: "Die meisten Buchungstools buchen Menschen. Niemand prüft, ob der Stuhl frei ist — also landen zwei Künstler:innen am Stuhl 2, und eine:r wird kurzfristig verschoben.",
    fix: "Arbeitsplätze sind buchbare Ressourcen mit eigener Kapazität und Puffer. Die Konfliktprüfung läuft pro Stuhl — Künstler:in, Abwesenheit und Arbeitszeiten werden geprüft — bevor ein Termin angenommen wird. Die Tagesansicht zeigt ein Raster pro Stuhl, damit Kollisionen sichtbar sind, nicht erst im Nachhinein.",
    featureIds: [16, 3, 15],
    visual: "grid",
  },
  {
    time: "14:30",
    title: "\u201eIch hab dir die Vorlage geschickt.\u201d",
    pain: "Vergraben unter 400 DMs, manchmal in schlechter Auflösung, manchmal die falsche — und weg ist sie, wenn der Kunde auf dem Stuhl sitzt.",
    fix: "Motiv- und Vorher/Nachher-Bilder hängen direkt am Termin. Automatisch verkleinert beim Hochladen, löschbar und im anstehenden Kalender der Künstler:innen und im Profil sichtbar — genau das, was gezeichnet wird, noch bevor der Kunde den Raum betritt.",
    featureIds: [10, 9],
    visual: "refs",
  },
  {
    time: "20:00",
    title: "Die Abrechnung am Tagesende.",
    pain: "Wer hat was bekommen? Splits auf der Servie ausgerechnet, Anzahlen diskutiert, doppelt in die Tabelle eingegeben — und zum Monatsende traut niemand mehr den Zahlen.",
    fix: "Jeder Buchungsposten trägt die pro Transaktion kalkulierte Künstler-/Studio-Verteilung. Checkout sperrt die Einträge; der Monatsabschluss überträgt den Saldo und sperrt den Monat. Wenn die Buchhaltung fragt, gibt es einen druckbaren Bericht — EN/DE.",
    featureIds: [35, 36, 37, 40],
    visual: "ledger",
  },
  {
    time: "22:15",
    title: "Totes Wi-Fi, lautes Studio.",
    pain: "Die Studio-Verbindung bricht ab. Der Kalender lebt auf dem Laptop an der Theke. Das Handy, das gerade klingelt, ist genau das, das die App nicht erreicht.",
    fix: "Es ist eine PWA: auf den Home-Bildschirm installiert, offline lauffähig, synchronisiert bei zurückkehrender Verbindung — und die App-Icon-Badge zeigt, was zu erledigen ist. Push-Stufen lassen jede:r Künstler:in entscheiden, wie oft das Handy piepen darf.",
    featureIds: [74, 75, 54, 56],
    visual: "phone",
  },
];

export const pillarsIntro = {
  kicker: "Die Werkzeugkiste",
  title: "Elf Arbeitsbereiche. Sieben, die du täglich nutzt.",
  sub: "Alles unten steht in der vollständigen Liste — filterbar nach Bereich, Status oder Rolle. Das sind die Säulen, die ein Studio täglich berührt.",
};

export const pillars: Pillar[] = [
  {
    num: "01",
    id: "booking",
    kicker: "Buchung",
    title: "Buchen ohne Hin-und-Her.",
    intro: "Der Kunde bekommt einen geführten Weg — ein empfohlener Termin mit Match-Score oder die volle Kontrolle über Dienstleistung, Künstler:in, Datum und Uhrzeit. Die Theke bucht in einem Durchgang, auch für brandneue Kund:innen.",
    featureIds: [1, 2, 3, 4, 10],
    visual: "flow",
  },
  {
    num: "02",
    id: "calendar",
    kicker: "Teamkalender",
    title: "Die Hauptfläche.",
    intro: "Tages-, Wochen- und Monatsansichten, rollenbezogen gefiltert. Nur dein eigener Kalender, Abwesenheiten mit Grund und Pufferzeiten pro Stuhl als Dämpfer.",
    featureIds: [7, 8, 14, 15, 16, 6],
    visual: "grid",
  },
  {
    num: "03",
    id: "finance",
    kicker: "Studio-Finanzen",
    title: "Der Servien-Math-Killer.",
    intro: "Das Modul, das die meisten Buchungstools komplett überspringen: Das Geld des Studios wird im Kalender mitverwaltet — pro Transaktion, pro Perspektive, bis zum gesperrten, druckbaren Monat.",
    featureIds: [35, 36, 37, 40, 41],
    visual: "ledger",
  },
  {
    num: "04",
    id: "clients",
    kicker: "Kunden & Reputation",
    title: "Jeden Kunden kennen. Den nächsten Besuch verdienen.",
    intro: "Profile mit Buchungshistorie und Instagram-Handles, Live-Statistiken zu No-Shows und Bindung, und ein Bewertungs-Loop, der ein Danke nach dem Besuch in eine Wiederholungsbuchung verwandelt.",
    featureIds: [18, 19, 65, 67, 63],
  },
  {
    num: "05",
    id: "pwa",
    kicker: "Benachrichtigungen & PWA",
    title: "Gebaut für den Stuhl, nicht fürs Büro.",
    intro: "Push-, In-App- und E-Mail-Trigger für jedes Event, das zählt — mit Stufen für das Team, damit kein Handy sich hoarsch piept, und Offline-Modus, falls das Studio die Verbindung verliert.",
    featureIds: [55, 56, 54, 74, 75],
    visual: "phone",
  },
  {
    num: "06",
    id: "tenants",
    kicker: "Multi-Location & Multi-Tenant",
    title: "Ein Konto, viele Studios.",
    intro: "Jede Location hat eigene Zeitzone und Währung; Tenants bleiben strikt getrennt. Zwei Studios aus einem Login bedienen, ohne ein einziges Datenleck.",
    featureIds: [43, 44, 45],
    visual: "tenant",
  },
  {
    num: "07",
    id: "admin",
    kicker: "Admin & Papiere",
    title: "Alles an einem Ort eingestellt.",
    intro: "Zeiten, Rollen, Dienstleistungen, Stühle, Locations, Formulare und Bücher — eine einzige Einstellungen-Suite. Papiere (Anamnese, Consent) passieren vor dem Stuhl, nicht während.",
    featureIds: [71, 59, 60, 69],
    visual: "matrix",
  },
];

export const differentIntro = {
  kicker: "Beweis des Unterschieds",
  title: "Was die anderen Tools nicht haben.",
  sub: "Booksy, Phorest, Square, Vagaro, Zenoti — keine dieser Tools bietet die nächsten zehn. Das sind die Features, die Team Calendar zu einem anderen Tier machen, nicht zu einem weiteren Kalender.",
};

// Einzeiler für die 10 Differentiator-Karten; der Volltext stammt aus features.de.json.
export const differentPunch: Record<number, string> = {
  1: "Die Antwort auf \u201eWer schuldet was?\u201c — automatisch, pro Transaktion.",
  2: "Bucht den Stuhl, nicht nur den Menschen.",
  3: "Die Künstler:in sieht genau, was zu zeichnen ist, bevor der Kunde sitzt.",
  4: "Kein Login, kein Hin-und-Her — und das Studio legt die Regeln fest.",
  5: "Bewertung \u2192 10 % Rabatt \u2192 Instagram \u2192 Google, ein getrackter Loop.",
  6: "Weiß, welche:r Künstler:in, zu welcher Zeit, an welchem Stuhl frei wird.",
  7: "Eine installierbare App, die offline läuft — und die Pieper-Einstellung in der Hand hat.",
  8: "Ein Konto quer durch Studios, getrennt per Regel.",
  9: "Eine social-first-Kundenbasis, direkt im Datenbestand.",
  10: "Mehrfach-Regionen, ohne manuelles Umrechnen.",
};

export const inventoryIntro = {
  kicker: "Das komplette Inventar",
  title: "Alle 81 Features, filterbar.",
  sub: "Die vollständige Liste — was jede Funktion kann, für wen sie ist und wie weit sie steht. Filter nach Bereich, Status oder Rolle, oder suche eine bestimmte Funktion.",
};

export const legend = [
  { key: "live", mark: "✅", label: "Live", desc: "Gebaut und in Produktion." },
  { key: "progress", mark: "🟡", label: "In Arbeit", desc: "Code vorhanden; bekannte Issues oder teilweises Backend." },
  { key: "pending", mark: "🔶", label: "Deployment ausstehend", desc: "Implementiert + getestet, wartet auf Deployment." },
  { key: "planned", mark: "⏳", label: "Geplant", desc: "Roadmap / Spezifikation, noch nicht gebaut." },
  { key: "verify", mark: "⚠️", label: "Verifizieren", desc: "UI im Repo; passende Cloud Function unbestätigt." },
];

export const roadmap = {
  kicker: "Was als Nächstes kommt",
  title: "Auf der Roadmap.",
  sub: "Geplant, noch nicht gebaut — im Inventar oben mit ⏳ markiert.",
  soon: [
    { id: 42, label: "Stripe-Anzahlungen & -zahlungen bei der Buchung" },
    { id: 60, label: "Kunden-Anamnese / Consent-Formulare (nächster Schritt)" },
    { id: 57, label: "Automatisierte 24h / 1h-Erinnerungen (unbestätigt)" },
    { id: 49, label: "Kunden-Onboarding-Welle (komposit-Kundenmodell)" },
    { id: 48, label: "Branded öffentliche Buchungs-URL pro Studio" },
  ],
  later: [
    { id: null, label: "Internes Team-Messaging" },
    { id: null, label: "Erweiterte Reports & Analysen" },
    { id: null, label: "Sperre von Zeitfenstern" },
    { id: 80, label: "Mehrsprachigkeit (i18n)" },
    { id: 81, label: "Individuelle Themes / Branding" },
    { id: null, label: "Öffentliche API" },
    { id: 58, label: "Kunden-Benachrichtigungen" },
  ],
};

export const honestyNote =
  "Die Status-Flags spiegeln den Zustand des Repos vom 29.08.2026 (Commit edbc187). Features mit \u201eIn Arbeit\u201c oder \u201eVerifizieren\u201c sind echte UI, aber ihr Backend steht noch aus — das Inventar oben behält das ehrlich."

export const footer = {
  tagline: "Der Studio-Kalender, der Zettel, Chat und Serviette ablöst.",
  github: "https://github.com/SwannSchilling/team-calendar",
};

export const meta = {
  title: "Team Calendar — der Studio-Kalender, der Zettel, Chat und Serviette ablöst",
  description: "Ein Feature-Tour durch Team Calendar, die Tattoo-Studio-Verwaltungs-PWA: geführte Buchung, Stuhl-Planung, Honorarbuch, Kunden-Bewertungen und Offline-PWA. 81 Funktionen, 11 Arbeitsbereiche, filterbares Inventar.",
};

export const ui: UiStrings = {
  showing: "Zeige {n} von {total} Funktionen",
  empty: "Keine Funktionen entsprechen diesen Filtern — weite die Suche an.",
  allAreas: "Alle Arbeitsbereiche",
  searchPlaceholder: "Funktionen suchen … (z. B. \u201eHonorar\u201c, \u201eWaitlist\u201d)",
  searchAria: "Funktionen suchen",
  catAria: "Nach Arbeitsbereich filtern",
  statusAria: "Nach Status filtern",
  roleAria: "Nach Rolle filtern",
  roles: [
    { key: "Owner", label: "Inhaber" },
    { key: "Admin", label: "Admin" },
    { key: "Artist", label: "Künstler" },
    { key: "Client", label: "Kunde" },
  ],
  whatLabel: "Was sie kann",
  whoLabel: "Für wen",
  beatBefore: "Vorher",
  beatAfter: "Mit Team Calendar",
  soonHead: "Als Nächstes",
  laterHead: "Später",
  sourceRepo: "Quellcode",
  inventoryMeta: "Feature-Inventar ·",
  builtWith: "Gebaut mit Astro · Noise-Load-in mit three.js + GSAP",
  frameKind: "Studio-Verwaltung · PWA",
  nav: [
    { href: "#story", label: "Ein Tag" },
    { href: "#features", label: "Toolkit" },
    { href: "#different", label: "Unterschied" },
    { href: "#inventory", label: "Inventar" },
    { href: "#roadmap", label: "Roadmap" },
  ],
  github: "GitHub",
  differentiator: "Unterscheidungsmerkmal",
};

export const mock: MockCopy = {
  dayGrid: {
    aria: "Mockup: Tagesansicht des Teamkalenders",
    title: "Teamkalender · Heute, Tagesansicht",
    live: "Echtzeit",
    chairs: ["Stuhl 1", "Stuhl 2", "Stuhl 3"],
    clients: { alex: "Alex M.", sam: "Sami T.", lena: "Lena P." },
    buffer: "Puffer",
    timeoff: "Abwesenheit",
    services: { custom: "Custom", flash: "Flash", coverup: "Cover-Up" },
    refTitle: "Motivvorlage angehängt",
  },
  ledger: {
    aria: "Mockup: Honorarbuch",
    title: "Finanzen · Juli-Buch",
    view: "Künstler-Ansicht",
    jobs: [
      { job: "Custom Rückenstück", meta: "Alex M. · Stuhl 1 · 6h" },
      { job: "Ärmel, Session 3", meta: "Sami T. · Stuhl 2 · 5h" },
      { job: "Kleine Linienarbeit", meta: "Ines B. · vorbezahlt" },
    ],
    splitA: "Künstler",
    splitB: "Studio",
    ok: "✓ abgerechnet",
    lock: "🔒 Juni geschlossen · gesperrt",
    print: "Druckbericht · EN/DE",
    amounts: ["€1.200", "€950", "€240"],
  },
  phone: {
    aria: "Installierbare PWA auf dem Smartphone",
    app: "Team Calendar",
    now: "jetzt",
    ago: "2 h",
    n1t: "Neuer Termin",
    n1b: "Alex M. · Sa 14:00 · Stuhl 1 — Motivvorlagen angehängt",
    n2t: "Termin geändert",
    n2b: "Sami T. auf So 18:00 verschoben",
    offline: "Offline — Änderungen werden synchronisiert, sobald die Verbindung zurückkommt",
  },
  flow: {
    aria: "Kunden-Buchungs-Flow",
    title: "Kundenweg · geführte Buchung",
    steps: [
      { t: "Dienstleistung wählen", d: "Jede Studio-Dienstleistung als Pill, mit Dauer & Preis" },
      { t: "Quick Book oder selbst wählen", d: "Empfohlener Termin mit Match-Score — oder eigene Filter" },
      { t: "Bestätigen", d: "Konfliktgeprüft: Künstler:in, Zeiten, Abwesenheit, Stuhl" },
      { t: "Alle werden informiert", d: "Push + In-App + E-Mail-Queue feuern bei Anlage" },
      { t: "Bewertung → 10 % Rabatt", d: "Nachbesuch-Bewertung schaltet den Code für den nächsten Besuch frei" },
    ],
    foot: "Kein Login fürs Verschieben — einmaliger sicherer Link",
  },
  tenant: {
    aria: "Ein Konto, zwei Studios, strikte Isolation",
    title: "Multi-Tenant · ein Konto, zwei Studios",
    user: "Ein Login",
    userMeta: "owner@studio.example · Magic Link oder Passwort",
    member: "in 2 Studios",
    meta: [
      ["Berlin · EUR · 4 Künstler", "3 Stühle · eigene Arbeitszeiten"],
      ["Hamburg · EUR · 2 Künstler", "1 Stuhl · eigene Arbeitszeiten"],
    ],
    lock: "Firestore-Regeln erzwingen strikte Tenant-Isolation — kein Datenleck zwischen Studios, Studiowechsel in der App.",
  },
  matrix: {
    aria: "Was jede Rolle sieht",
    title: "Rollen · wer was sieht",
    cols: ["Kalender", "Kunden", "Finanzen", "Admin"],
    rows: [
      { role: "Inhaber", cells: ["✓", "✓", "✓", "✓"] },
      { role: "Admin", cells: ["✓", "✓", "lesen", "✓"] },
      { role: "Künstler", cells: ["meine", "eigenes Buch", "eigener Split", "—"] },
      { role: "Kunde", cells: ["eigene Termine", "eigene", "—", "—"] },
    ],
  },
  link: {
    aria: "Einmal-Link zum Verschieben",
    from: "Ink Haven Studio",
    text: "Hallo Alex — soll dein Termin Sa 14:00 bei Mara verschoben werden? Wähle einfach einen neuen Termin, ohne Login. Der Link läuft 48 h.",
    urlLabel: "einmalig · 48 h",
  },
  refs: {
    aria: "Termin mit Motivvorlagen",
    appt: "Alex M. · Custom Rückenstück",
    pill: "Sa 14:00 · Stuhl 1",
    more: "+1 weitere",
    note: "📌 3 Motivvorlagen · automatisch verkleinert beim Hochladen · sichtbar im Kalender der Künstler:in",
  },
};
