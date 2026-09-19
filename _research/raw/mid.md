# Mid-tier competitor dossier — Team Calendar (tattoo-studio management PWA)

Deep-research subagent report. **All URLs accessed 2026-09-19.** Outbound access was via a plain-HTTP fetcher (`_research/fetch.py`), Bing results (`_research/search.py`), the iTunes Search/Lookup API (official App Store metadata = primary), and the Wayback CDX API + `web.archive.org` snapshots.

## Method, limits and honesty notes
- **Network OK.** First probe: `idcheck.py https://tattoomanager.de/` → `final=https://tattoomanager.de/ ctype=text/html; charset=utf-8 textlen=820 keyword-hits={'tattoo':3,'termin':4,'kalender':2}`. Not BLOCKED.
- **`web_search` tool and firecrawl were NOT used** (per instructions).
- **Vendor bundles contain real UI strings.** TattooManager, InkLinka and Linework ship their product as JS single-page apps whose HTML embeds full i18n/catalogues. Strings from those bundles are marked **Verified (product bundle)** — they are official first-party artifacts, but they prove *the feature exists as code/UI*, not that it is polished or enabled for every plan. Marketing-page quotes are marked **Claimed (advertised)**.
- **German text is quoted exactly as fetched**, including the vendors' own misspellings (e.g. `Einverständiserklärungen`, `Tätowierer`, `Rollen & Rechte`), because I verified the raw HTML byte-for-byte contains them (e.g. `grep -o "Terminplan[^<]*" _research/raw/tm_home_raw.html` → `Terminplanung, Kunden, Einverständiserklärungen, Kommunikation und mehr.`).
- **"not found" ≠ absent**. Where I could not see a feature I write **"not found in sources checked"** and list which sources.
- **Play Store could not be read**: `play.google.com/store/apps/details?id=…` returns JS/CSS only for a plain HTTP client (verified: `<title>` empty, body = `@font-face{font-family:'Roboto'…}`). Play package names are therefore reported as *advertised by the vendor site* and Play-side dates as **not found in sources checked**. App Store metadata is used as the primary app-age source.
- Raw captures of everything cited live in `_research/raw/`, `_research/raw2/`, `_research/raw_lw/`, `_research/raw_an/`.

## Verdict legend (used in every checklist)
`Y-V` = yes, verified on an official current page (or in that vendor's own shipped app bundle) · `Y-C` = advertised, depth unverifiable from outside (advertised-unverified) · `ROADMAP` = planned/not enabled yet, per the vendor's own wording · `HIST` = present historically, current state unconfirmed · `UNVER` = only third-party evidence · `NO-E` = vendor states the negative · `NF` = not found in sources checked.

---

# 1. TattooManager

## 1.1 Identity, operator, country
| Field | Finding | Class | Evidence |
|---|---|---|---|
| Legal operator | "TattooManager umgesetzt durch CutiDesign / Inhaber: **Daniel Cuti** / Mülheimerstraße 48 / 53909 Zülpich / **Deutschland**" (sic, as fetched); "Verantwortlich für den Inhalt gemäß § 55 Abs. 2 RStV: Daniel Cuti" | Y-V | `https://tattoomanager.de/impressum/` |
| Brand owner line | "TattooManager ist eine Software von CutiDesign"; "TattooManager Connect" is the same vendor's artist/studio marketplace ("Komplett gratis!") | Y-V | `https://tattoomanager.de/preise/` |
| App seller | **No App Store app by CutiDesign found.** iTunes term search `TattooManager` (US) and `--country=de` return only unrelated apps; the closest hit `'Tattoo Manager' seller='Peter Yermakov' bundle='com.tattoo-manager.tattoomanager' releaseDate=2023-02-26` is a **different Russian-language product**, not this one | Y-V (iTunes lookup) | `https://itunes.apple.com/search?term=TattooManager&entity=software`; `…?country=de` |
| Backend/hosting | "Wir verwenden **Supabase** als Backend-Service … Allerdings ist unser Serverstandort in einem deutschen hochsicherheits Rechenzentrum in **Frankfurt**."; "Server in Deutschland"; "DSGVO & GoDV Konform" | Y-V | `https://tattoomanager.de/datenschutz/`; `https://tattoomanager.de/` |
| Payment rail | "9. Zahlungen und Abonnements über **PayPal**" … "die Zahlungsabwicklung über den Zahlungsdienstleister PayPal (Europe) S.à r.l. et Cie … Luxemburg" | Y-V | `https://tattoomanager.de/datenschutz/` |

## 1.2 Geography & target market
DACH / Germany-first. Evidence: German-only site + `.de`, Impressum in Zülpich (DE), "Server in Deutschland", GDPR/GoDD/eIDAS compliance framing, EUR pricing "ohne Ausweis der Umsatzsteuer … gemäß § 19 UStG", testimonials named after German-language studios ("Hendrik K. vom Studio Elite Tattoo 57", "Michael H. vom Studio 368Inkz"), Instagram/TikTok `@tattoomanager.de`. Target segments are explicit: solo artist → small studio → large multi-location studio ("Für Solo-Artists / Für kleine Studios / Für große Studios", `tattoomanager.de/`).

## 1.3 Product age (evidence, no guessing)
- Earliest Wayback capture of `tattoomanager.de` = **2025-01-07** (`20250107102526`, then `20250107123847`, `20250107131353`; 2025-01-08 for `www.`). CDX: `https://web.archive.org/cdx/identification?url=tattoomanager.de&matchType=domain&output=json&fl=timestamp&sort=asc&limit=3`.
- First capture carrying HTTP **200** = `20250321111037`; the snapshot body (fetched with `…/20250321111037id_/https://tattoomanager.de/`) shows a **solo-artist product**: "Du bist Tattoowierer? Oder Shop-Manager?", "14 Tage kostenlos testen / Keine Kreditkarte notwendig", modules "Deine Kundendaten / Deine Tattoos / Deine Dokumente / Dein Dashboard / Deine Termine / Deine Einnahmen / Deine Ausgaben / Deine Notizen & Bestellungen / Dein Einverständniserklärungen".
- Earliest capture of the app host `tattoomanager.online` = **2025-01-14** (`20250114094316`).
- On-site founder statement (no date): "Der TattooManager entstand nicht am Reißbrett – sondern aus dem echten Studioalltag. … 'Auf dem Markt gab es einfach nichts Vergleichbares - und da ich gelernter Programmierer bin, habe ich es selbst gebaut.'" — signed "Daniel Cuti, Gründer des TattooManagers".
- HTML metadata of the live homepage: `datePublished 2025-04-29`, `dateModified 2026-09-18`.
- **Statement:** Exact launch date not established from primary sources; earliest evidence: **2025-01-07** (Wayback CDX, `tattoomanager.de`), first substantive product snapshot **2025-03-21** (Wayback `id_` snapshot), i.e. the product is ≈2 years old and was **solo-artist-first**, studio/multi-site tiers arriving later.

## 1.4 Current status
**Live**, actively developed. Homepage modified `2026-09-18`; blog cadence into Sept 2026 ("Hygieneplan im Tattoo-Studio" 16. September 2026, "Tattoo-Studio-Kosten kalkulieren" 13. September 2026, "Tattoo-Nachsorge digital begleiten" 9. September 2026); 30-day free trial "Ohne Zahlungsdaten · Keine automatische Verlängerung". Two shipped bundles: marketing WordPress/Elementor site, and the product at `https://www.tattoomanager.online` (React SPA shell + `/assets/D_5n5ooe.js`, 878 KB).

## 1.5 Source keys (cited in the table as `[X]`)
| key | URL | accessed |
|---|---|---|
| `[TM-H]` | https://tattoomanager.de/ (incl. `#funktionen`, FAQ, testimonials) | 2026-09-19 |
| `[TM-P]` | https://tattoomanager.de/preise/ (6 price cards + full feature-comparison table + Connect) | 2026-09-19 |
| `[TM-I]` | https://tattoomanager.de/impressum/ | 2026-09-19 |
| `[TM-D]` | https://tattoomanager.de/datenschutz/ | 2026-09-19 |
| `[TM-A]` | https://tattoomanager.de/artikel/ | 2026-09-19 |
| `[TM-APP]` | https://www.tattoomanager.online + `/assets/CBfKiyVQ.webmanifest` + `/assets/D_5n5ooe.js` (shipped product bundle) | 2026-09-19 |
| `[TM-WB1]` | http://web.archive.org/web/20250321111037id_/https://tattoomanager.de/ | 2026-09-19 |
| `[TM-WBCDX]` | https://web.archive.org/cdx/identification?url=tattoomanager.de&matchType=domain&output=json&fl=timestamp&sort=asc&limit=3 | 2026-09-19 |
| `[TM-ITUNES]` | https://itunes.apple.com/search?term=TattooManager&entity=software (US + DE) | 2026-09-19 |

## 1.6 Feature checklist
| Feature | Verdict | Evidence |
|---|---|---|
| online booking | **Y-V** | "Online Terminkalender", "Online Buchungen … Deine Kunden tragen sich ihre Termine ganz einfach selbst über deinen persönlichen Buchungslink ein" `[TM-H]`; row "Online-Buchungskalender – ✓ ✓ ✓ ✓ ✓" `[TM-P]` |
| client self-booking | **Y-V** | "Kunden tragen sich ihre Termine ganz einfach selbst über deinen persönlichen Buchungslink ein"; "100% in deinem gewünschten Look" `[TM-H]`; Kundenportal screenshots `termin-kalender`, `terminkalender` `[TM-H]` |
| appointment/artist/shared calendar | **Y-V** | "Übersichtliche Tages-, Wochen- und Monatsansichten für dein gesamtes Studio"; "Gemeinsamer Studio-Kalender ✓" `[TM-P]` |
| station/chair/workstation booking | **Y-V (count-based)** | "Verwalte Künstler, Piercer, Standorte, **Arbeitsplätze**, Aufgaben …" `[TM-H]`; plan rows "3 Standorte & **10 Arbeitsplätze**", "5 Standorte & 20 Arbeitsplätze", table row "Standorte & Arbeitsplätze … 3 / 10 … 5 / 20", "Standort- & Aufenthaltsplaner" `[TM-P]`. Caveat: presented as *counts per plan* + planner; no public proof of named per-station booking screens |
| resource conflict checking | **Y-V** | "Weniger Doppelbuchungen — **Räume, Artists und Zeiten bleiben sauber koordiniert**" `[TM-H]` |
| buffer/setup time | partial **Y-V** | "Flexible Planung — Termine, **Pausen** und Ressourcen schnell verschieben"; "Termin-Lücken-Füller" `[TM-H]`,`[TM-P]`. Explicit per-service buffer/setup field: NF |
| working hours/holidays/absences | **NF** | No working-hours/holiday UI text in `[TM-H]/[TM-P]`; bundle contains no `Urlaub`/`Feiertag` strings found |
| time-off | **NF** | as above |
| guest/resident artists | **Y-V** | "Gast-Künstler Funktion" (Ultra/Ultra+), table "Gast-Künstler-Funktion – – ✓ – ✓ ✓"; plus separate `TattooManager Connect` marketplace "Finde deinen nächsten Guest Spot" `[TM-P]` |
| walk-ins | **NF** | no `Walk-in`/`Spontan` string in `[TM-H]/[TM-P]`/bundle |
| recurring/multi-session | **Y-C (multi-session)** | "Kunden & Tattoos … Tattoo-Projekte", "Fotos zu Tattoos hinzufügen" `[TM-P]`; 2025 snapshot: "Dokumentiere jedes Tattoo-Projekt … Designs, Platzierungen und Fortschritte" `[TM-WB1]`. Explicit recurring-series engine: NF |
| waitlist | **NF** | no `Warteliste` string in `[TM-H]/[TM-P]`/bundle |
| client profiles/history | **Y-V** | "Kundendaten und Tattoo-Projekte übersichtlich an einem Ort"; "Tattoo-Historie im Kundenportal" `[TM-H]`,`[TM-P]` |
| notes | **Y-V** | "Bestellungen & Notizen … persönliche Notizen direkt in der App" `[TM-H]` |
| reference images | **Y-V** | "Fotos zu Tattoos hinzufügen ✓" `[TM-P]`; "Speichere Designs, Platzierungen und Fortschritte" `[TM-WB1]` |
| consultation | **NF** | no consultation/`Beratung` booking type found |
| consent forms | **Y-V** | "Einverständniserklärung ✓", "Gesundheits- & Anamnesefragebogen", "Datenschutzerklärung", "Einverständnis für Minderjährige", "Risiko- & Aufklärungsbogen", "Digitale Unterschriften", "Unterschriften werden eIDAS-Konform gespeichert" `[TM-P]`,`[TM-H]` |
| aftercare | **Y-V** | "Pflege- & Aftercare-Hinweise ✓"; "Automatische Aftercare-Nachrichten" `[TM-P]`; article "Tattoo-Nachsorge digital begleiten" `[TM-A]` |
| deposits | **Y-V** | "Anzahlungen verwalten ✓"; screenshots `finanzen-terminzahlungen`, `finanzen-zahlungsuebersicht` `[TM-P]`,`[TM-H]` |
| payments/POS | **Y-V** | "Kassenbücher", "Automatische **Kassenschubladen-Öffnung**" `[TM-P]`; bundle string `"Das Kassenmodul ist momentan offline."` `[TM-APP]` (POS module exists in the shipped app) |
| artist commissions & artist/shop split | **Y-V ⚠** | "Berechnung der **Künstler Provisionen**" (Ultimate), table "Künstler-Provisionen berechnen – – ✓", "**Platzmieten** abrechnen ✓", "Tagesabrechnungen ✓" `[TM-P]` → **this directly contradicts a 'unique commission ledger' claim** |
| invoicing | **Y-V** | "Automatische Rechnungen & Belege ✓" all tiers; screenshot `finanzen-rechnung-pdf` `[TM-P]`,`[TM-H]` |
| monthly closing / locked months | partial **Y-V** | "Monats- & Jahresbilanzen exportieren ✓"; "Kassenbücher", "Tagesabrechnungen" `[TM-P]`. Period **locking** (`gesperrt`/`Monat abschliessen`) NF |
| financial reports | **Y-V** | "Statistiken & Bilanzen — Verfolge den Umsatz, analysiere das Wachstum und exportiere Bilanzen für den Steuerberater"; "Studio- & Künstlerstatistiken" `[TM-H]`,`[TM-P]` |
| roles/permissions | **Y-V** | "Rollen & Rechte", "Rechte jedes Mitarbeiters frei anpassbar", "Individuelle Mitarbeiterrechte", "Rollen- & Rechteverwaltung" `[TM-H]`,`[TM-P]` |
| multi-staff | **Y-V** | tiers "Bis zu 3 / 5 / 10 / 20 Künstler"; "Für Teams von 3 bis 20 Personen - jeder mit seinem eigenem Zugang" `[TM-P]` |
| multi-room | partial **Y-V** | "Räume … bleiben sauber koordiniert" `[TM-H]`; room count field NF |
| multi-location | **Y-V** | table "Standorte & Arbeitsplätze … 3 / 10 … 5 / 20"; "Mehrere Standorte" `[TM-P]`,`[TM-H]` |
| multi-tenant | **Y-C** | SaaS with per-studio accounts + Supabase backend, `register/connect` onboarding `[TM-D]`,`[TM-APP]`; the word "mandant" not published |
| studio branding | **Y-V** | "Individuell anpassbare Studio-Webseite ✓", "Online-Buchung 100% in deinem gewünschten Look", "Alles individuell nach deinen Wünschen anpassbar" `[TM-P]`,`[TM-H]` |
| email | **Y-V** | "Automatische E-Mail-Erinnerungen", "Eigene E-Mail- & SMS-Vorlagen", "Emails & SMS inklusive" `[TM-P]` |
| SMS | **Y-V** | "Automatische SMS-Erinnerungen", "Nachrichtenverlauf & **SMS-Antworten**"; Wayback article path `artikel/automatische-sms-erinnerungen-im-tattoomanager-jetzt-kostenlos-in-jedem-plan/` `[TM-A]` |
| WhatsApp | weak **Y-C** | marketing sells against it ("Keine 1.000 WhatsApp-Chats mehr") `[TM-H]`; app bundle contains 2 `WhatsApp` strings, no marketing feature page → depth unclear |
| Instagram | **NF as feature** | only their own social profile link in footer `[TM-H]` |
| unified inbox | partial **Y-C** | screenshot `kommunikation-posteingang` + "Nachrichtenverlauf & SMS-Antworten" `[TM-H]`,`[TM-P]` |
| campaigns | **NF** | birthday automation only ("Automatische Geburtstagsnachrichten", "Geburtstags-Spins") `[TM-P]` |
| review requests | **NF** | none found |
| flash/flash-days | **NF** | none found |
| stencil tools | **NF** | no `Stencil` string in `[TM-APP]` |
| ink registration | **NF** | no ink-brand/`Tinte` registry string found (`Tinte` matches were minifier false positives) |
| inventory | **Y-V** | "Material-Verwaltung — Du kannst alle Materialien erfassen und dann zusammen mit jedem Tattoo das verwendete Material verbuchen"; "Verwalte Materialbestellungen, Lieferungen" `[TM-H]`; 2025 snapshot already had "Materialkosten" `[TM-WB1]` |
| gift cards | **Y-V** | "Gutscheine verwalten ✓" `[TM-P]` |
| PWA | **Y-V** | `/assets/CBfKiyVQ.webmanifest`: `"display":"standalone"`, `"id":"tattoomanager"`, android chrome icons; `"Keine Installation nötig"` `[TM-APP]`,`[TM-H]` |
| offline mode | **NO-E leaning / NF** | bundle throws `"Could not process request. Application offline."` and `"Das Kassenmodul ist momentan offline."` `[TM-APP]` → these are **failure strings**, i.e. the app *detects* being offline; no offline-work capability published |
| sync | **Y-V** | FAQ: "plattformübergreifend nutzbar … Deine Daten sind immer **synchronisiert** und überall verfügbar" `[TM-H]` |
| mobile app (iOS/Android) | **NO/NF** | No App Store listing for this vendor `[TM-ITUNES]`; site sells "Smartphone, Tablet, Desktop" + installable web manifest `[TM-H]`,`[TM-APP]` → treat "app" wording in testimonials ("die App ist perfekt gemacht") as colloquial for the web app |
| browser app | **Y-V** | "Mehr Überblick. Auf großem Bildschirm. Die Web-Oberfläche im Detail." + `App-Login` nav `[TM-H]` |
| API | **NF** | no public API/dev docs found |
| Google Calendar | **Y-V** | "Google Kalender Integration … Termine automatisch mit dem Google Kalender zu synchronisieren" `[TM-D]`; table rows "Google-Kalender-Synchronisierung ✓", "**Apple**-Kalender-Synchronisierung ✓" `[TM-P]` |
| accounting/Stripe/payment providers | **Y-V** (PayPal) | "Daten werden nur weitergegeben … z. B. an Zahlungsdienstleister wie PayPal" + §9 PayPal agreements `[TM-D]`; "exportiere Bilanzen für den Steuerberater" `[TM-H]`; **Stripe not found**; DATEV/Lexware not found |
| analytics (revenue/utilization/no-shows/retention/artist perf.) | partial **Y-V** | "Weniger No-Shows" `[TM-H]`, "Statistiken über das Studio & jeden Künstler" `[TM-P]`, "Auslastung" appears only in an annotation label `Termine, Artists und Auslastung` `[TM-H]`. Retention: closest = "Stammkunden-Status & Tattoo-Statistik", "Treuepunkte" `[TM-P]` |

## 1.7 Positioning
Hero: **"Digitale Dokumente — DSGVO-konform • Server in Deutschland • Keine Installation nötig"** / **"Terminplanung, Kunden, Einverständiserklärungen, Kommunikation und mehr. Alles in einer Software."** / **"Dein Studio. Einfach organisiert."** Sub-brand line: **"Deine Kunst. Deine Ordnung. Deine Zeit."** Differentiators = German compliance posture + paperlessness + one-person founder authenticity ("Entwickelt von einem, der es selbst lebt … Von Studios. Für Studios.").

## 1.8 Pain points they market against (verbatim)
- "Viele Tätowierer verlieren täglich wertvolle Stunden durch Chaos im Studio. Zeit, die eigentlich in ihre Kunst fließen sollte."
- "Kein Terminstress mehr — Keine 1.000 WhatsApp-Chats mehr. Kunden tragen sich ihre Termine ganz einfach selbst über deinen persönlichen Buchungslink ein."
- "Alle Daten perfekt sortiert — … Keine Zettel, keine verlorenen Notizen."
- "100% Digitale Dokumente — … Endlich kein Papierchaos mehr!"
- "Dein Kalender füllt sich. **Nicht dein Postfach.**"
- "Räume, Artists und Zeiten bleiben sauber koordiniert" (their word for double-booking pain).
- Founder quote vs the market: "Auf dem Markt gab es einfach nichts Vergleichbares".

## 1.9 Pricing (official pricing page)
`[TM-P]` — "Alle Preise verstehen sich gemäß § 19 UStG ohne Ausweis der Umsatzsteuer … jederzeit kündbar"; all tiers "Kostenloses 30-tägiges Testabo".
Basic **€19,99**/mo (1 artist) · Pro **€49,99**/mo (1 artist + online booking + customer portal) · Studio **€99,99**/mo (bis zu 3 Künstler) · Ultimate **€179,99**/mo (bis zu 5 Künstler, provisions + chair rent billing) · Ultra **€299,99**/mo (bis zu 10 Künstler, 3 Standorte/10 Arbeitsplätze, Gast-Künstler) · Ultra+ **€399,99**/mo (bis zu 20 Künstler, 5 Standorte/20 Arbeitsplätze). Homepage teaser simplifies to "ab 19,99 / ab 99,99 / ab 299,99 €". **Note:** seats are capped per tier — the pricing model is tier-by-artist-count + location/workstation counts, not usage-based.

## 1.10 Advertised USPs
1. German data posture: "Server in Deutschland / Sicheres Serverzentrum in Frankfurt", "DSGVO & GoDV Konform", eIDAS-conform signatures, paperless archive `[TM-H]`.
2. Tattoo-specific document stack: consent + health/anamnesis + minors + risk disclosure + aftercare templates with digital signatures `[TM-P]`.
3. Studio-tier economics including **artist commission calculation, chair/booth rent billing, daily settlements, cash books** + "Standorte & Arbeitsplätze" + "Gast-Künstler-Funktion" `[TM-P]`; plus loyalty gamification in the client portal (Glücksrad, Slotmachine, Quiz, Treuepunkte) `[TM-P]`; plus free artist↔studio marketplace "TattooManager Connect".

## 1.11 Claims I tried to falsify
| Claim given to me | Result |
|---|---|
| "150+ artists" | **NOT FOUND / Unverified.** Whole fetched homepage HTML searched for `150`, `Künstlern`, counter widgets — every `150…` hit is CSS/SVG/base64 noise (e.g. `contain-intrinsic-size:3000px 1500px`, `…,150))},hide:function`). Public proof instead is *lower*: named studio testimonials are 5 named studio owners (`Studio Elite Tattoo 57`, `Eternal Ink`, `Basti Taff`, `368Inkz`, `JanINKa_Tattoos`) plus "Einige zufriedene Kunden & Benutzer der Software" — deliberately **no** user count published. If Team Calendar quotes "150+ artists" as *their* number, fine; as a TattooManager claim it is unsupported by `[TM-H]`. |
| "Terminplanung, Kunden, Einverständiserklärungen, Kommunikation, Finanzen" | **Verified** — hero line verbatim (see § Method grep) `[TM-H]`. |
| iOS/Android app exists | **Not established.** `[TM-ITUNES]` shows no CutiDesign listing; vendor sells a browser/PWA install (`display:standalone`) instead `[TM-APP]`. |
| Team Calendar uniqueness probes | **station booking** → TattooManager publishes "Standorte & Arbeitsplätze" + "Standort- & Aufenthaltsplaner" as paid features ⇒ do **not** claim station booking as unique. **offline mode** → no evidence; their own strings treat offline as an error state ⇒ safest differentiator, but verify no competitor ships it (InkLinka also has none found). **commission ledger w/ month close** → TattooManager publishes "Künstler-Provisionen berechnen" + "Platzmieten abrechnen" + "Tagesabrechnungen" + "Kassenbücher" + "Monats- & Jahresbilanzen exportieren" ⇒ do **not** claim a commission ledger as unique; the *locked/signed monthly close* is the part not evidenced here. |

---

# 2. InkLinka

## 2.1 Identity, operator, country
| Field | Finding | Class | Evidence |
|---|---|---|---|
| Legal operator | "**InkLinka is owned and operated by Inklinka Technologies OÜ**. … Registered office: Harju maakond, Tallinn, Kesklinna linnaosa, Tuukri tn 19-202, 10120, **Estonia**" (Estonian OÜ = private limited company); "Service operator: Inklinka Technologies OÜ"; footer "© 2026 Inklinka Technologies OÜ. All rights reserved."; "Owned and operated by Inklinka Technologies OÜ" | Y-V | https://inklinka.com/en/terms ; /en/privacy ; /en/contact |
| App Store seller | `trackName='InkLinka'`, `sellerName='Inklinka Technologies OU'`, `bundleId='com.inklinka.app'`, `trackId=6761559803`, `version 1.0.9`, `ratingCount=0` | Y-V (iTunes lookup) | `https://itunes.apple.com/lookup?id=6761559803` |
| Android | link `https://play.google.com/store/apps/details?id=com.inklinka.app` on the site; Play page unreadable via plain HTTP | Y-C / NF | https://inklinka.com/en |
| Role | self-limiting platform clause: "InkLinka provides software, hosting, workflow tools, integrations, and technical infrastructure only … not … a clinic, studio operator, **merchant of record**, employer … or records custodian" | Y-V | /en/terms |
| Payments | "When you connect a **Stripe** account … you are the seller and merchant responsible … InkLinka supplies software and may collect the platform fee disclosed for your plan"; "Paid plans are completed securely in Stripe" | Y-V | /en/terms; /en/pricing |

## 2.2 Geography & target market
Estonian-registered, EU-oriented SaaS: support hours "Mon-Fri: 9:00 AM - 6:00 PM (**CET**)"; nine storefront locales `en,pl,ru,es,he,sv,de,nl,fr`; EUR pricing; DATEV-facing string present in the money module (see checklist); political statement in footer "We love Ukraine and stand with Ukraine." Market = independent tattoo artists + studios + "multi-location teams" ("Built for every stage of your tattoo business: Independent artists · Tattoo studios · Multi-location teams"). Positioning explicitly against spa software and against "other tattoo software".

## 2.3 Product age
- **App Store first release `releaseDate=2026-04-17T07:00:00Z`**, current version released 2026-08-31, v1.0.9, 0 ratings → primary, hard evidence.
- Terms of Service header: "**Last updated: April 14, 2026**".
- **Zero Wayback coverage**: CDX `matchType=domain|exact|prefix` all return `[]` (e.g. `https://web.archive.org/cdx/identification?url=inklinka.com&matchType=domain&output=json&fl=timestamp`) → the site has never been crawled/kept, consistent with a 2026 launch.
- Asset cache-busting stamps on the site itself (`site.webmanifest?v=20260319`, `favicon.ico?v=20260820`) bracket first public release Mar 2026 → Aug 2026 activity.
- **Statement:** Exact launch date not established from primary sources beyond the store record; earliest evidence: **App Store releaseDate 2026-04-17** (iTunes lookup, id 6761559803) with legal pages dated **April 14, 2026** (/en/terms). ⇒ InkLinka is **~5 months old** at the access date.

## 2.4 Current status
**Live but early / partly beta.** Proof of maturity gaps in their own UI copy: `business-analyst: { "betaLabel":"Beta version", "betaDescription":"You can already use and test the Business Analyst, but it is still being improved and expanded." }` and the stencil module `"meta":{"description":"Generate **beta** stencil drafts, clean them manually, and export PNG/SVG."}`. Case-lifecycle strings admit unfinished migration: `"caseTrackingPending":"Case tracking will be available after the case-lifecycle migration and the next snapshot."` Ratings: `ratingCount=0` on iOS. Verdict: shipping product, public beta features.

## 2.5 Source keys
| key | URL | accessed |
|---|---|---|
| `[IK-H]` | https://inklinka.com/en | 2026-09-19 |
| `[IK-P]` | https://inklinka.com/en/pricing | 2026-09-19 |
| `[IK-T]` | https://inklinka.com/en/terms | 2026-09-19 |
| `[IK-D]` | https://inklinka.com/en/privacy | 2026-09-19 |
| `[IK-C]` | https://inklinka.com/en/contact | 2026-09-19 |
| `[IK-FA]` | https://inklinka.com/en/faqs | 2026-09-19 |
| `[IK-PP]` | https://inklinka.com/en/payments-payouts | 2026-09-19 |
| `[IK-PC]` | https://inklinka.com/en/guest-visit-planner · /en/sms-email-automation · /en/website-booking-tools · /en/aftercare-merch-sales · /en/business-analytics · /en/tattoo-stencil-maker · /en/studio-efficiency-check · /en/guest-artist-software · /en/tattoo-business-control · /en/tattoo-studio-essentials · /en/tattoo-studio-calendar-software · /en/tattoo-deposit-management · /en/tattoo-booking-software · /en/tattoo-studio-crm · /en/tattoo-artist-crm · /en/tattoo-studio-management-software · /en/tattoo-studio-calendar-chaos · /en/why-inklinka | 2026-09-19 |
| `[IK-APP]` | shipped React/Next bundles embedded in the above pages (i18n catalogues incl. `inbox`, `consent`, `stencil-vectorizer`, `business-analyst`, `team`, `payments`) + `https://inklinka.com/site.webmanifest?v=20260319` | 2026-09-19 |
| `[IK-ITUNES]` | https://itunes.apple.com/lookup?id=6761559803 | 2026-09-19 |
| `[IK-WBCDX]` | https://web.archive.org/cdx/identification?url=inklinka.com&matchType=domain&output=json&fl=timestamp | 2026-09-19 |

## 2.6 Feature taxonomy (their nav → normalized buckets)
| Their label | Bucket | Notes (verbatim anchor text where available) |
|---|---|---|
| Guest Planner for Studios | People/resourcing — guest & resident artists | "artist invitations, guest planner, visit dates, calendar sync, guest-only availability, cooperation terms, rates, revenue share and fixed compensation" `[IK-H]` |
| Payments & Payouts | Finance ledger | "deposits, invoices, vouchers, expenses, Stripe payments, artist debt, payouts and ledger-based reports" `[IK-H]`, `[IK-PP]` |
| SMS & Email Automation | Communications | "Built around sessions, not generic campaigns." `[IK-PC]` |
| Forms, Widgets & AI Chat | Customer-facing front end | "booking widgets and personal links", "Website chat with AI agent" `[IK-FA]`,`[IK-P]` |
| Aftercare & Merch Sales | Point of sale | "products, stock, mixed appointment checkout, orders, receipts and product reporting" `[IK-PC]` |
| AI Business Analyst | Analytics (beta) | see `[IK-APP]` `business-analyst` |
| Universal Stencil Maker | Production tool (beta) | "Generate beta stencil drafts … export PNG/SVG" |
| Studio Efficiency Check | Diagnostics/telemetry | marketing landing page |
| Multi-studio teams / ownership rules | Access control & multi-tenancy | "each studio keeps its own team, access, clients, calendar and working rules separate" `[IK-H]` |

## 2.7 Feature checklist
| Feature | Verdict | Evidence |
|---|---|---|
| online booking | **Y-V** | "Can clients book appointments online? **Yes.** Studios can use booking widgets and personal links so clients can send requests or book available time" `[IK-FA]` |
| client self-booking | **Y-V** | same; + "slot reservation and deposit rules" `[IK-H]` |
| appointment/artist/shared calendar | **Y-V** | "Connected studio calendar — Link every booking to its project, artist, client, deposit and session history"; iOS app: "Calendar and appointments: track your schedule and daily workload" `[IK-H]`,`[IK-ITUNES]` |
| station/chair/workstation booking | partial **Y-V (capacity only) ⚠** | `[IK-APP]` settings field `"workstationsCount":"Number of Workstations"`, `"workstationsCountDescription":"Used to calculate studio load"`, calendar `"load":"Load: {visits}/{workstations} ({percentage}%)"`, and validator `"Cannot create visit: number of guests exceeds number of workstations ({workstations}) on dates: {dates}"` → workstations are a **numeric capacity constraint + load metric**, *not* named bookable station entities. Named-station booking: not found |
| resource conflict checking | **Y-V** | `"preventOverlaps"`, `"eventOverlap":"Event overlaps with another"`, `"alreadyPlanned":"A visit is already planned for {date}"`, `"datesCovered":"Selected dates are already covered by existing visits"` `[IK-APP]` |
| buffer/setup time | **NF** | no `buffer`/setup-duration string found |
| working hours/holidays/absences | **Y-V** | `"Working Hours"` + onboarding validation `"workingHoursRequired":"Working hours are required"` + tip "Set your studio's working hours. In the calendar, the working hours space will be highlighted in white, which will help visually distinguish working and non-working…" `[IK-PC]` |
| time-off | **Y-V** | `"Please enter vacation start date"`, `"Error: start date is required for Vacation"` `[IK-H]` bundle |
| guest/resident artists | **Y-V** | "Guest and resident artist operations — Handle artist invitations, guest planner, visit dates, calendar sync, guest-only availability, cooperation terms, rates, revenue share and fixed compensation" `[IK-H]`; Basic plan lists "Guest visits & guest planner" `[IK-P]` |
| walk-ins | partial **Y-V** | form field `"Walk-in name (optional)"` `[IK-P]`; a walk-in booking flow/waitlist module not found |
| recurring/multi-session | **Y-V (multi-session)** | "Multi-session tattoo history — References, placement, style, cover-up and color details, planned sessions, stages, progress, artist notes, healing notes, media and next steps live inside the project" `[IK-H]`; recurring-series scheduler: NF |
| waitlist | **NF** | no waitlist string found |
| client profiles/history | **Y-V** | "Client profiles — Keep contact details, visit history and essential records together"; "Client profile / Tattoo idea / Body placement / Approximate size / Preferred style / Reference images" `[IK-H]`,`[IK-PC]` |
| notes | **Y-V** | "artist notes, healing notes"; "Latest artist handoff"; "Artist note" `[IK-H]`,`[IK-APP]` |
| reference images | **Y-V** | "Tattoo booking forms — Collect references, placement, style and availability before the consultation" `[IK-H]` |
| consultation | **Y-V** | "Tattoo project lifecycle — Connect the request, **consultation**, sessions, healing and completion" `[IK-H]` |
| consent forms | **Y-V** | `[IK-APP]` `consent` module: "Client Consent Form", `"signature":"Client Signature"`, "I confirm that I have read and agree to all terms of the consent form"; seeded text includes an age/legal-capacity clause "I confirm that I am 18 years old or older (or have written consent from a parent/guardian)" `[IK-H]` |
| aftercare | **Y-V** | "tattoo or piercing aftercare message templates" `[IK-H]`; "Automatic aftercare instructions provided by the artist, including: Regular cleaning and treatment…" `[IK-H]` |
| deposits | **Y-V** | "Deposits, payments and payouts — Connect deposits … directly to tattoo work"; analyst case types `appointment_missing_deposit`, `no_show_deposit_forfeited` `[IK-H]`,`[IK-APP]` |
| payments/POS | **Y-V** | "One finance center for studio payments, payouts, and control … deposits, session payments, team payouts, and expenses … connected payment services, invoices, and vouchers"; POS: "Sell a service and products in one clear checkout. Track Orders, payments, receipts, ledger" `[IK-PP]`,`[IK-PC]` |
| artist commissions & artist/shop split | **Y-V ⚠⚠ (strongest counter-evidence in this dossier)** | `[IK-APP]` payments UI: `"compensationNoOpenRuns":"No closed unpaid monthly compensation cycles are available yet."`, `"compensationRunCycle":"Monthly cycle"`, `"compensationRunOutstanding":"Outstanding balance"`, `"fixedCompensationOverviewTooltip":"Closed unpaid fixed compensation cycles due right now. Current cycles and advances are shown separately."`, `"compensationAdvanceBalance":"Available advance credit"`, `"artistAdvancesReceivable":"Artist advances receivable"`; marketing: "Transparent team payouts — Keep payout accounting for each team member with a clear, transparent history" `[IK-PP]`; plan feature "revenue share" and "fixed compensation plan" with currency-migration guard "Disable every active fixed compensation plan before changing currency". ⇒ a **fixed/monthly artist-compensation ledger with closed cycles + advances + payout creation** is implemented |
| invoicing | **Y-V** | "Invoice creation (20/100/Unlimited)" per tier `[IK-P]`; webhook event sample `invoice.payment_failed` `[IK-PC]` |
| monthly closing / locked months | partial **Y-V ⚠** | Closed/unbounded monthly compensation cycles are computed and tracked as *unpaid* runs (`"compensationRunSelect":"Select an unpaid monthly cycle"`). A general period-**lock**/"close the month" control for the whole ledger: not found |
| financial reports | **Y-V** | "ledger-based reports"; "Report generation" (Basic+) `[IK-H]`,`[IK-P]`; "Financial clarity for the studio … Only the studio owner controls financial reporting. The owner can create reports whenever they are needed." `[IK-PP]` |
| roles/permissions | **Y-V** | "Assign roles and permissions", "Manage permissions per user"; roles `owner/manager/front_desk/artist`; "1 manager seat", "4 manager seats" per plan; "Studio and artist ownership rules — InkLinka separates ownership of clients, payments, appointments, notes and creative projects" `[IK-APP]`,`[IK-P]`,`[IK-H]` |
| multi-staff | **Y-V** | "Solo master mode (1 team member)" → "Up to 3 / 20 team members" → "Unlimited team members" `[IK-P]` |
| multi-room | **NF** | no room entity found (workstation count is capacity, see above) |
| multi-location | **Y-C ⚠** | marketing segments "Independent artists · Tattoo studios · **Multi-location teams**"; onboarding option "Large studio or network — A large team, multiple managers or locations"; the shipped model is **multi-tenant-per-studio** with artists shared across tenants ("Artists can be members of several studios, while each studio keeps its own team, access, clients, calendar and working rules separate") ⇒ "multi-location" ≈ several studios under one artist, not one tenant with N locations |
| multi-tenant | **Y-V** | legal vocabulary: "your account, **workspace, tenant, or organization**"; "Tenant slug not available yet"; "tenant attributions" `[IK-T]`,`[IK-APP]` |
| studio branding | **Y-V** | "Branding & Design" settings, `"studioLogo":"Studio Logo"`, "Changes apply to your tenant and update branding across the app"; widget appearance config (position, colour, avatar, greeting) `[IK-PC]`,`[IK-FA]` |
| email | **Y-V** | "Integrations: Email, SMS" `[IK-P]`; "Use IMAP/SMTP credentials for any provider." + "Inbox actions do not delete the original emails from your connected mailbox provider" `[IK-APP]` |
| SMS | **Y-V** | "Tenant-funded SMS delivery. Each studio uses its own **Infobip** account and balance. Connect your Infobip account to enable SMS sending." (provider config incl. `Infobip API Base URL`, `Infobip API Key`) `[IK-APP]` |
| WhatsApp | **Y-C** | "Messenger integrations (WhatsApp, Telegram)"; `whatsappTitle`, "WhatsApp Business" strings `[IK-APP]`; no pricing-page line item ⇒ depth unclear |
| Instagram | **Y-V (field, not integration)** | onboarding field `"instagram":{"label":"Instagram","placeholder":"@studio_name"}`; feature "Personal artist links" for social posts `[IK-APP]`,`[IK-P]` |
| unified inbox | **Y-V** | `[IK-APP]` `inbox`: "Messages from email and connected channels in one place. Deleted conversations stay recoverable for at least 24 hours…"; "Replies are available only for email conversations right now" (limitation!) |
| campaigns | **NO-E (deliberate) / NF** | their copy: "Built around sessions, **not generic campaigns**." `[IK-PC]` — marketing automation for arbitrary client segments is not the product's centre of gravity |
| review requests | **NF** | only `staffReview`/`review` strings for internal case review, no public review-request pipeline found |
| flash/flash-days | partial **Y-V** | "Flash claim — Quick form for flash designs." `[IK-PC]`; no flash-day calendar module |
| stencil tools | **Y-V (beta)** | "Universal Stencil Maker … Make a tattoo stencil in seconds … Control the exact millimeter size" + full tool UI (`pencil`, `eraser`, `contour`, `wrap`, `a4Sheet`, PNG/SVG export, "Stencil AI Neurons per month" quota) `[IK-H]`,`[IK-APP]`,`[IK-P]` |
| ink registration | **NF** | no ink-brand registry found |
| inventory | **Y-V** | "Organize Products, variants, categories, prices and stock"; "Recognize product cost and reduce the **inventory asset** when goods are sold", `inventoryAssetAccount` `[IK-PC]`,`[IK-APP]` |
| gift cards | **Y-V** | "Gift certificates and vouchers are available only on paid plans. Create and manage gift certificates. The voucher is considered a gift certificate. Revenue from the sale will be recorded in payments as income" `[IK-APP]`,`[IK-P]` |
| PWA | **Y-V** | `https://inklinka.com/site.webmanifest?v=20260319` → `"display":"standalone"` `[IK-APP]` |
| offline mode | **NF / effectively NO** | only chat-widget string `"offlineMessage":"Offline Message"` placeholder "We are currently offline…" `[IK-APP]` — a widget status message, not an offline working mode |
| sync | **Y-V** | guest-planner "calendar sync"; migration guard "The active plan conflicts with the studio financial settings. Its historical currency will not be changed automatically" `[IK-H]`,`[IK-APP]` |
| mobile app (iOS/Android) | **Y-V iOS / Y-C Android** | iOS: App Store id 6761559803, "InkLinka is the mobile workspace for tattoo studios, managers, and artists who already use InkLinka … Sign in with your existing credentials to access your workspace and role-based permissions"; site badge "Download on the App Store / GET IT ON Google Play" `[IK-ITUNES]`,`[IK-H]` |
| browser app | **Y-V** | "web panel for studio, online booking for clients" `[IK-APP]` |
| API | **Y-V (partial)** | Terms cover "hosted applications, **APIs**, communication features, integrations"; developer UI "Dashboard: Developers → **Webhooks** → select endpoint → Send test webhook (event: invoice.payment_failed)"; SMS provider API keys. A public open REST API document: not found |
| Google Calendar | **Y-V (import)** | `"Google Calendar import"`, `"Scan, review, and apply Google Calendar events into InkLinka appointments."`, `"Google Calendar"` `[IK-APP]`; privacy policy: "If a user … chooses to connect a **Google account**, InkLinka may access Google user data strictly to provide the email features requested" `[IK-D]` |
| accounting/Stripe/payment providers | **Y-V** | Stripe (merchant-of-record disclaimer + "Stripe refund required" reconciliation hint + "Payment service configuration error"); DATEV-visibility toggle in the money module: `"Show DATEV in payments"`, `"DATEV enabled in payments."` `[IK-T]`,`[IK-PC]`,`[IK-APP]`; multi-currency guard "Available commissions are split across multiple currencies. Request one currency at a time." |
| analytics (revenue/utilization/no-shows/retention/artist perf.) | **Y-V (broad) + ROADMAP ⚠** | shipped `business-analyst` (beta): case types `paid_not_completed`, `no_show_follow_up`, `completed_appointment_balance_due`, `appointment_missing_deposit`, `project_recovery`, `client_rebooking`, `lead_rescue`, `data_quality`; metrics "Outstanding balance", "Unfinished paid sessions", "Clients", "Projects", "Data to finish"; "Weekly Owner Report"; filters incl. artist/client/category/priority. **Roadmap:** `"forecasting":{ "description":"The Business Analyst is collecting evidence only. Forecasts, probability scores, automated messages, and automatic assignments remain **disabled**." }` with targets `weekly_revenue_forecast`, `capacity_gap_forecast`, `client_rebooked_90d`, `no_show_refund_risk`; status labels `collecting`, `readyForOfflineCalibration`. Utilization KPIs are marketing copy only: "Maximize studio utilization", "forecast demand" `[IK-APP]` |

## 2.8 Positioning
Hero: **"The AI-Powered Operating System for Tattoo Studios."** Sub: "InkLinka delivers real results: more bookings, more returning clients, and better service." Anti-positioning headline: **"Stop paying for spa software built around generic appointments"**, followed by a 14-row comparison table with columns `Spa software | Other tattoo software | InkLinka` in which most competitor cells are `—` `[IK-H]`. Secondary slogan (SEO landing set): "Tattoo studio calendar software with project context" `/en/tattoo-studio-calendar-software`; footer: "Professional Studio Management — Tattoo studio CRM and management software for bookings, projects, clients and payments."

## 2.9 Pain points they market against (verbatim)
- "Why many studios feel overloaded even with a full calendar." → **Context is scattered**: "Bookings in messengers, references on phones and payment notes in separate chats create constant context switching and errors."; **Planning is fragile**: "When one schedule change is not synchronized for everyone, the studio loses time to manual coordination and avoidable conflicts."; **Finances are hard to control**: "Deposits, payouts and balances become unclear when they are not directly linked to appointments, clients and team agreements." `[IK-H]`
- "Tired of `<chaos>`schedule chaos`</chaos>`, `<missed>`missed clients`</missed> and `<manual>`manual management`</manual>?" `[IK-APP]`
- Numbers they attach to those pains (their own KPI copy, unverified): "increases profit by 30%", "Free up to 10 hours per week", "Reduce missed sessions by 40%", "attracts 25% more new clients", "Join hundreds of studios already using InkLinka" — all **Y-C** (no methodology published).

## 2.10 Pricing (official)
`[IK-P]` Monthly | Yearly toggle ("Save up to 0%" as shipped): **Free** (20 clients, 20 appointments/mo, 15 payments, 1 team member, 60,000 stencil-AI "Neurons", 50 MB) · **Basic €15/mo** (80 appts, 200 clients, 3 members, products/stock, deposits, 20 invoices, guest planner, 1 widget, "5% platform fee on online product payments", Email+SMS, gift certificates, 1 GB) · **Pro AI €29/mo** ("Popular"; 300 appts, 1,000 clients, 20 members + 1 manager seat, AI chat agent, 100 invoices, 3% platform fee, 5 GB) · **Expert AI €49/mo** ("For every need"; unlimited appts/clients/members, 4 manager seats, unlimited invoices, 1% platform fee, 10 GB). "No credit card required for Free", "Cancel anytime", "No hidden fees"; paid plans checkout "securely in Stripe". ⇒ flat fee + **transaction-volume platform fee** + **metered AI quota**; capacity limits (appointments/clients/payments/storage) are the real throttle.

## 2.11 Advertised USPs
1. Tattoo-domain object model instead of generic appointments: project lifecycle request → consultation → sessions → healing → completion, multi-session history with references/placement/stages/media `[IK-H]`.
2. Money as a first-class citizen: deposits, session payments, team payouts, expenses, invoices, vouchers, "ledger-based reports" all keyed to the appointment/project they belong to `[IK-H]`,`[IK-PP]`.
3. Cross-studio artist identity with separated ownership/permissions + guest/resident artist planning with revenue share **and** fixed compensation `[IK-H]`.
4. Artist-facing production tool: Universal Stencil Maker (AI, mm-precise, PNG/SVG) `[IK-H]`,`[IK-P]`.
5. AI Business Analyst as a case queue with owner/manager/front-desk/artist workflow `[IK-APP]`.

## 2.12 Uniqueness probes
- **station booking**: partial — capacity counter + overlap validators + load %, **no named bookable stations/rooms found** ⇒ Team Calendar may still claim named station/room entities, but must not claim "workstation awareness" as unique.
- **offline mode**: not found ⇒ no conflict detected (neither for InkLinka nor for the claim).
- **commission ledger w/ month close**: **found** (`Closed unpaid … compensation cycles`, monthly cycle, outstanding balance, advances receivable, payout creation) ⇒ do not claim uniqueness of an artist/shop commission ledger; the differentiator must move to *immutable/locked* months, per-station attribution of revenue, or audit trail.

---

# 3. Linework

## 3.1 Identity, operator, country
| Field | Finding | Class | Evidence |
|---|---|---|---|
| Legal operator | "**Linework Inc. is a Delaware corporation**" ; footer "© 2026 Linework Inc."; governing law "the laws of the State of New York" [sic]; late-interest clause cites "the Norwegian Late Payment Interest Act" (Act no. 100 of 17 December 1976) | Y-V | https://www.linework.com/general-terms-of-service |
| Origin/brand | footer "**Made by Norwegians, launched in USA.**"; nav brand badge renders a Norwegian flag glyph next to "Linework" | Y-V | /features /studios /artists /pricing /about-us /magazine |
| Team | "Kai Robin Ree — Founder & CEO", "Marius W. Haaverstad — CPO", "Mads Lundgaard — CTO", "Nicolai Karlsvik — COO US", "Amalie Baltzer Glenne — CCO/COO", "Ronja Kruus — Account manager, Sweden", "Daro Navaratnam — Board member and founder of Dintero", "Thomas Hansteen — Legal", "Andreas Øwre — Advisor & investor", "Thorvald H. Steen — Business advisor" (all names as fetched) | Y-V | /about-us |
| Founder domain | "Tattoo artist and studio owner **Kai Ree** has been in the game for over 17 years … has owned his own studio and **managed four shops simultaneously**" | Y-V | /about-us, /magazine ("Linework Founder Kai Ree Tells All") |
| App Store | `trackName='Linework app'`, `sellerName='Linework Inc.'`, `bundleId='com.linework'`, `trackId=1611510851`, `releaseDate=2022-03-13T08:00:00Z`, `version 6.8.4`, `curVerRel=2026-09-17`, `ratingCount=4`, `avgRating 3.75`, genres Business/Utilities | Y-V (iTunes lookup) | `https://itunes.apple.com/lookup?id=1611510851` |
| Support | "Email us at hello@linework.com … Mon–Fri, 9am–6pm **ET**" | Y-V | /contact-us |

## 3.2 Geography & target market
USA-first go-to-market of a Norwegian-founded company: pricing in **USD**, payment rails "Visa, Mastercard, Amex, Apple Pay, Google Pay, **Klarna**", payouts via Stripe, support in ET, "tax-ready reports for your **CPA**", "Does Linework help with **health department** requirements?" (US health-department consent forms), NY governing law + Norwegian interest statute ⇒ dual-legal DACH-expansion is not their market. Their own editorial line: "Where is Linework available?" is an FAQ whose answer is client-side rendered and therefore **not found in sources checked** (server HTML contains only the question; the `<div data-state="closed" … hidden>` panel body is empty).

## 3.3 Product age (this is the item where the 2000-era domain must be rejected)
- `https://web.archive.org/cdx/identification?url=linework.com&matchType=domain&output=json&fl=timestamp&sort=asc&limit=2` → `20000620210815`, `20011128071859`; the snapshot calendar UI of that domain reports "**142 captures — 20 Jun 2000 – 08 Feb 2026**". **The 2000 captures are a different prior use of the domain and are not evidence of this product's age.** Sampled `20190128222751` → body is an Internet-Archive media-item frame ("Internet Archive Audio … Live Music … Grateful Dead"), i.e. not the tattoo product.
- **`20211211064908`** (`http://web.archive.org/web/20211211064908/http://linework.com/`) → visible text of the archived page is literally: **"linework.com — Coming soon."** ⇒ the tattoo product was **not yet published** at 2021-12-11.
- **`20220424222408`** → archived page already ships the product: nav "Studios / Artists", banner "Note : To use Linework on your phone you must first register on a computer" ⇒ first positive evidence of the live tattoo product on the web = **2022-04-24**.
- `20221107135412` adds "Want a demo? : Book an appointment with our onboarding specialist".
- Legal record: General Terms of Service — "**Last updated October 26, 2023** . **Effective date: June 1, 2023**" (`/general-terms-of-service`) — with the Norwegian-interest wording and the AWS/Stripe subcontractor clause ("such as software from Amazon Web Services, Stripe etc.").
- App Store record: **first released 2022-03-13** (`[LW-ITUNES]`), still maintained (`2026-09-17`).
- **Statement:** The 2000 Wayback captures are a *different prior use of the domain* and are excluded. Product age established from primary sources: **"Coming soon." placeholder 2021-12-11 (Wayback) → first product page 2022-04-24 (Wayback) → iOS app first released 2022-03-13 (iTunes) → ToS effective 2023-06-01 (official)**. No on-site founding date exists (`/about-us` narrates the story but publishes no year) ⇒ **Exact launch date not established from primary sources; earliest evidence: 2021-12-11 ("Coming soon" placeholder, Wayback), earliest live product evidence 2022-04-24 (Wayback), earliest machine-readable release 2022-03-13 (App Store).**

## 3.4 Current status
**Live, actively maintained.** iOS build 6.8.4 released 2026-09-17 (iTunes); every marketing page carries "© 2026 Linework Inc."; persistent banner "Want a demo? Book one with our onboarding specialist — 30 minutes, no commitment."; free tier is open ("Create free account", "Every feature included"). No beta markers found.

## 3.5 Source keys
| key | URL | accessed |
|---|---|---|
| `[LW-H]` | https://www.linework.com/ | 2026-09-19 |
| `[LW-F]` | https://www.linework.com/features | 2026-09-19 |
| `[LW-S]` | https://www.linework.com/studios | 2026-09-19 |
| `[LW-A]` | https://www.linework.com/artists | 2026-09-19 |
| `[LW-P]` | https://www.linework.com/pricing (full "What's included?" matrix + FAQ headings) | 2026-09-19 |
| `[LW-AB]` | https://www.linework.com/about-us | 2026-09-19 |
| `[LW-TOS]` | https://www.linework.com/general-terms-of-service | 2026-09-19 |
| `[LW-M]` | https://www.linework.com/magazine ; /contact-us ; /demo | 2026-09-19 |
| `[LW-APP]` | https://app.linework.com/ + `/manifest.json` + `/static/js/main.08050fb2.js` (4 MB bundle fetched; keyword sweep for `workplace`, `workstation`, `walk-in`, `waitlist`, `offline` returned no match in the served chunk) | 2026-09-19 |
| `[LW-ITUNES]` | https://itunes.apple.com/lookup?id=1611510851 ; search term `Linework` | 2026-09-19 |
| `[LW-WB0]` | http://web.archive.org/web/20211211064908/http://linework.com/ ("Coming soon.") | 2026-09-19 |
| `[LW-WB1]` | http://web.archive.org/web/20220424222408/https://linework.com/ | 2026-09-19 |
| `[LW-WB2]` | http://web.archive.org/web/20221107135412/https://linework.com/ | 2026-09-19 |
| `[LW-WBCDX]` | https://web.archive.org/cdx/identification?url=linework.com&matchType=domain&output=json&fl=timestamp (2000/2001 first; 2019-01-28; 2021-12-11; 2022-04-24; 2023-01-29) | 2026-09-19 |

## 3.6 Feature checklist (their pricing matrix is unusually explicit, so most rows are Y-V)
| Feature | Verdict | Evidence |
|---|---|---|
| online booking | **Y-V** | "Booking flow — Clients book — you confirm. Share your personal booking link. Clients pick a service and a time, and pay their deposit online. You confirm with one tap." `[LW-F]` |
| client self-booking | **Y-V** | "Online booking page with your own link ✓ ✓" `[LW-P]` |
| appointment/artist/shared calendar | **Y-V** | "Shared calendar & shop overview ✓ ✓"; "See the whole floor in a single week"; "Every artist's week in one view, or filter down to one" `[LW-P]`,`[LW-S]`; "Day, 3-day and week views" `[LW-A]` |
| station/chair/workplace booking | **Y-V ⚠ (semantic)** | "When you book an appointment or take a deposit you choose **which workplace it belongs to**, and the appointments you have at a studio can also be managed by that studio's manager." `[LW-P]` ⇒ a *workplace* is an assignable object of an appointment. Named-station UI not seen; keyword sweep of `[LW-APP]` bundle for `workstation`/`station`: no match |
| resource conflict checking | **NF** | not stated in fetched copy; "Managers create and manage appointments on an artist's behalf" implies central control, not validated |
| buffer/setup time | **NF** | not found |
| working hours/holidays/absences | partial **Y-V** | "block out time" ("Calendar — See every appointment in day, week and month view. Manage bookings, **block out time** and get push notifications right on your phone.") `[LW-F]`; dedicated working-hours/holiday registry: not found |
| time-off | **NF** | not found (`block out time` is the closest) |
| guest/resident artists | **Y-V** | "Guest artist support ✓ ✓" `[LW-P]`; FAQ heading "Does Linework work for guest artists?" `[LW-P]` |
| walk-ins | **NF** | keyword sweep in `[LW-F/S/A/P/M]` and `[LW-APP]`: no match; closest analogue "Cash sale tracking" `[LW-P]` |
| recurring/multi-session | **NF** | "Tattoo requests (inquiry flow) ✓ ✓" and "Consultation bookings ✓ ✓" exist; no recurring-series or multi-session project object found |
| waitlist | **NF** | no match |
| client profiles/history | **Y-V** | "Client profiles & payment history ✓ ✓" `[LW-P]` |
| notes | **NF** | not found as a listed feature |
| reference images | **Y-V (adjacent)** | "Flash gallery with images ✓ ✓" `[LW-P]`; explicit client-reference image store not found |
| consultation | **Y-V** | "Consultation bookings ✓ ✓" `[LW-P]` |
| consent forms | **Y-V** | "Consent forms (digitally signed) ✓ ✓"; "Health history forms ✓ ✓"; FAQ "Does Linework help with health department requirements?" `[LW-P]` |
| aftercare | **Y-V** | "Aftercare instructions (automatic) ✓ ✓" `[LW-P]` |
| deposits | **Y-V** | "Deposits at booking ✓ ✓" `[LW-P]` |
| payments/POS | **Y-V** | "Online payments via Stripe", "Visa, Mastercard, Amex, Apple Pay, Google Pay, Klarna", "**Cash sale tracking**", "Point of sale for cash and card", "Tipping at checkout" `[LW-P]`,`[LW-A]` |
| artist commissions & artist/shop split | **Y-V ⚠⚠ (directly contradicts uniqueness)** | "Automatic **commission split** ✓ ✓"; "Commission split per artist"; "Set the split, the **card-fee share** and the **tax on rent** per artist"; "Commission-based rent — an agreed share of each artist's sales / Fixed rent — a set amount, and the artist keeps 100% of their sales" `[LW-P]`,`[LW-S]` |
| invoicing | **Y-V** | "**Flat booth rent with automatic invoicing** ✓ ✓"; "Client invoices with payment link", "Custom due dates", "Net 10, 15 or 30 due dates", "Email it directly from the platform" `[LW-P]`,`[LW-F]` |
| monthly closing / locked months | partial **Y-V ⚠** | "**Settlements** — Studio rent, settled from real sales. Squaring up with your artists is normally a spreadsheet job at the end of every month. Linework builds it from the sales that already happened — commissions tracked per artist, invoiced properly, and collected." + "Settlements & payout statements ✓ ✓" `[LW-S]`,`[LW-P]`. An explicit *lock-the-month* control: not found |
| financial reports | **Y-V** | "Tax-ready reports ✓ ✓"; "Complete sales history … Tax-ready reports for your CPA" `[LW-P]`,`[LW-A]` |
| roles/permissions | **Y-V (thin)** | account model: artist accounts vs studio accounts holding "**manager seats**"; "Managers … never carry their own appointments" `[LW-P]`. Fine-grained ACL: not found |
| multi-staff | **Y-V** | "1 manager seat included", "Extra manager seats ✓ ✓" `[LW-P]` |
| multi-room | **NF** | not found |
| multi-location | **NF ⚠** | no multi-location claim in fetched copy; their scaling axis is instead "**connect to as many studios as you like**" / "connect to one or more studios" (artist federates across studios) `[LW-P]` |
| multi-tenant | **Y-C** | SaaS "delivery of the SaaS" with "Customer Data … deleted from Lineworks' servers" `[LW-TOS]` |
| studio branding | **Y-V** | "Make it look like you — Give your booking page a personal touch. Pick from different themes … so it matches your style and your brand"; "Themes for your booking page ✓ ✓"; "Dark mode — your style, your call" `[LW-F]`,`[LW-P]`,`[LW-A]` |
| email | **Y-V** | "Unlimited email notifications ✓ ✓"; "Receipts by text & email" `[LW-P]` |
| SMS | **Y-V** | "Unlimited text notifications ✓ ✓"; "Booking confirmations by text & email"; "Automatic client reminders" `[LW-P]`,`[LW-F]` |
| WhatsApp | **NF** | not found (their pain copy targets "no more DM back-and-forth" `[LW-A]`) |
| Instagram | **NF** | not found |
| unified inbox | **NF** | not found |
| campaigns | **NF** | not found |
| review requests | **NF** | not found |
| flash/flash-days | **Y-V** | "Flash gallery with images ✓ ✓" `[LW-P]`; "Assign open requests from the studio's booking page to an artist" `[LW-S]` |
| stencil tools | **NF** | not found |
| ink registration | **NF** | not found |
| inventory | **NF** | "Retail product sales ✓ ✓" exists; stock/warehouse tracking not found |
| gift cards | **NF** | not found |
| PWA | **Y-V** | `https://app.linework.com/manifest.json` → `"name":"Linework Dashboard"`, `"display":"standalone"`, `"orientation":"landscape"`; marketing copy "Web browser ✓ ✓" `[LW-APP]`,`[LW-P]` |
| offline mode | **NF** | no match for `offline` in fetched copy or in the 4 MB served bundle chunk `[LW-APP]` |
| sync | **Y-V** | "With Linework, **all elements synchronize automatically**"; "Your whole schedule, always current"; "Full portability (your data follows you) ✓ ✓" `[LW-AB]`,`[LW-F]`,`[LW-P]` |
| mobile app (iOS/Android) | **Y-V iOS / Y-V (matrix)** | "iPhone app (iOS) ✓ ✓", "Android app ✓ ✓" `[LW-P]`; "iOS and Android apps" `[LW-F]`; App Store `Linework app` v6.8.4, first released 2022-03-13 `[LW-ITUNES]` |
| browser app | **Y-V** | "Manager app (web-based) ✓ ✓" `[LW-P]` |
| API | **NF** | not found |
| Google Calendar | **NF** | not found (Google sign-in client and Apple auth are wired in the app shell, `[LW-APP]`, which is authentication, not calendar sync) |
| accounting/Stripe/payment providers | **Y-V** | "Online payments via Stripe"; ToS §4 "facilitate electronic payment handling … through third-party payment vendors, like e.g. Stripe" + "automatic distribution of payments from the Customer's customers to the Customer and its business partners" (= split payments) `[LW-P]`,`[LW-TOS]` |
| analytics | partial **Y-V** | "Sales & reports — Know exactly what you earned … reports and full sales history"; "real-time revenue" `[LW-S]`,`[LW-A]`. Utilization/no-show/retention/artist-performance KPIs: not found |

## 3.7 Positioning
Hero taglines (by page): `/` "Bookings, payments and shop management — all in one place. **Built by tattooers, for tattooers.**" · `/features` "Everything your tattoo business needs" · `/studios` "Tattoo studio software for busy shops — … Commission split or flat booth rent. Shared calendar, automatic invoicing and real-time revenue." · `/artists` "Tattoo business software for artists — Your own booking page, automatic reminders and deposits — **no more DM back-and-forth**." · `/about-us` "**About us — Taking Back an Overlooked Industry**". Differentiator = domain-native vertical (vs. horizontal spa/salon tools) + integrated payments + zero-config pricing ("Every plan includes every feature. The only thing the price changes is the transaction fee.").

## 3.8 Pain points they market against (verbatim)
- "Kai was forced to utilize **unfit tools and solutions made for other industries**." / "this vast **technological chasm** often rendered Kai's business inefficient" `[LW-AB]`
- "Today's general solutions consist mostly of elements that **don't communicate or consolidate calendars, accounting systems, and card terminals/cash registers**." `[LW-AB]`
- "you won't need old, outdated systems **designed for hair dressers** or other industries completely unlike our own." `[LW-AB]`
- "With a lack of knowledge, time, and supporting tools, tattoo artists and studio owners are unable to meet the increasing demands from both clients and authorities." `[LW-AB]`
- "no more DM back-and-forth." `[LW-A]` ; "Squaring up with your artists is normally a **spreadsheet job** at the end of every month." `[LW-S]`

## 3.9 Pricing (official)
`[LW-P]`: "Artist or studio, free or paid — **the same features either way**. Start free with a **6% transaction fee**, or go **Pro for $19/mo** and pay only **Stripe's fee (2.9% + 30¢)**. Pass the fee on to your client or cover it yourself — your choice." Four cards: Artist Free $0 (6%/txn) · Artist Pro $19/mo · Studio Free $0 (6%/txn) · Studio Pro $19/mo; "The only thing the price changes is the transaction fee"; payout modes "Next-day payouts ✓ / Weekly payouts (free) / 2-day rolling payouts (free)". FAQ headings (answers client-side, not fetched): "How do Linework's fees work?", "How do payments and payouts to the artist work?", "What about cash sales…", "Does Linework help with health department requirements?", "How does the commission split between shop and artist work?", "Does Linework work for guest artists?", "Where is Linework available?", "How fast can we get started?"

## 3.10 Advertised USPs
1. **Vertical-native**: "Built by tattooers, for tattooers." + founder is a 17-year tattooer/multi-shop owner `[LW-H]`,`[LW-AB]`.
2. **Feature-parity pricing**: every tier ships every feature; monetisation is a transaction fee, not a feature gate `[LW-P]`.
3. **Money-split automation**: automatic commission split / flat booth rent with automatic invoicing, settlement statements, next-day payouts, tax-ready reports `[LW-P]`,`[LW-S]`.

## 3.11 Uniqueness probes
- **station booking** → *found*: appointments are assignable to a "workplace" `[LW-P]` (also "Flat booth rent" implies bookable booths) ⇒ do not claim station assignment as unique.
- **offline mode** → not found in any source checked (incl. the shipped JS bundle) ⇒ claim is safe so far, subject to my own verification of the four shipped apps' offline capabilities on device.
- **commission ledger w/ month close** → *found*: "Automatic commission split", "Settlements & payout statements", "Squaring up with your artists … at the end of every month. Linework builds it from the sales that already happened — commissions tracked per artist, invoiced properly, and collected." ⇒ do not claim the concept; the *locked/immutable close + audit trail* is not evidenced.

---

# 4. Anolla

## 4.1 Identity, operator, country
| Field | Finding | Class | Evidence |
|---|---|---|---|
| Legal operator | "**The owner and operator of the Anolla platform is Booklux OÜ**, a company founded and registered in **Estonia** (registry code: 12127160, VAT: EE102000843)" … "Our only legal entity is **Booklux OÜ**, based in Estonia" (their own note on third-party data portals that may show other statuses) | Y-V | https://anolla.com/en/about-us |
| App Store seller | `trackName='Anolla'`, `sellerName='Booklux OU'`, `bundleId='com.agado.agado'` (legacy Agado package), `trackId=1570020265`, `releaseDate=2021-06-10`, `curVerRel=2025-10-28`, `userRatingCount=0` (US storefront) | Y-V (iTunes lookup) | `https://itunes.apple.com/lookup?id=1570020265` |
| Leadership | "Meelis and Tarko Koger lead the company. Meelis focuses on product development and the technical side. Tarko is responsible for strategic direction …" | Y-V | /en/about-us |
| Brand history | "Our journey began in **2011** under the name **Otsiabi OÜ**. From that, the booking software **Booklux** was created … We later developed the **Agado** client app … That's how **ANOLLA** was born … officially registered with the European Union Intellectual Property Office." | Y-V | /en/about-us |
| Independence claim | "14+ Years of active development · 30+ Countries · AA+ Credit rating · 100% Independent"; "without external funding" | Y-C | /en/about-us |

## 4.2 Geography & target market
Estonian platform operator, EU-wide/self service: "**Official languages (26)**" enumerated (Čeština … Malti), "Available in **30+ countries**", "Support for 25+ Languages", "1M+ Bookings Annually", "over **200 service categories**". Vertical landing pages are *sector* pages (`/en/salon-software`, `/en/tattoo-software`, `/en/healthcare-software`, `/en/automotive-software`, `/en/construction-services-software`, `/en/pet-software`, `/en/real-estate-services-software`, `/en/rental-software`, `/en/sports-software`, `/en/wellness-software`, `/en/schedule-software`, `/en/website-booking-software`, …, plus 26 localised tattoo paths e.g. `/de/tatowierstudio-software`, `/cs/software-pro-tetovaci-studia`, `/ru/programmnoe-obespecenie-dlia-tatu-salonov`). **Not tattoo-specific**: the tattoo page reuses the generic platform copy; testimonials are from other verticals ("For years I was looking for a system that could handle **group classes, personal training sessions, and workshops**", "We have **five locations** …", "Proactive **inventory management** and resource planning…").

## 4.3 Product age vs. tattoo positioning (two clocks)
- Platform/company: "Founded in **2011**" (about-us claim, Y-C) + App Store `releaseDate=2021-06-10` (Y-V) + domain archived since **2018** (per tasking brief; my own CDX probes this session were aimed at the tattoo paths) ⇒ company/platform is old, **treat separately from the product positioning**.
- **Tattoo positioning is recent:** `https://web.archive.org/cdx/identification?url=anolla.com/en/tattoo-software&matchType=exact&output=json&fl=timestamp&sort=asc` → **`20260213035432`** (then `20260309120431`); the sibling `/en/salon-software` first capture **`20260213130220`**. A CDX regex-filter sweep `filter=original:.*tattoo.*` over the `anolla.com/` prefix returned `[]` (tool-level filter artefact), so I verified the tattoo landing page by direct capture instead.
- On-page methodology block: every metric is stamped "**Last updated: 31.07.2026**" (Official languages 26; in-app rating 4.8/5; measured platform uptime 99.96%; AI-resolved support chats 79.3%; core feature coverage in mobile apps 99%; full online payment flow with prepayment 100%) ⇒ the tattoo landing page is maintained in 2026.
- **Statement:** Exact date of first tattoo-specific positioning not established from primary sources; earliest evidence **2026-02-13** (Wayback capture of `/en/tattoo-software`), while the platform itself is attested since 2011 (vendor claim) and its mobile app since 2021-06-10 (App Store).

## 4.4 Current status
**Live.** Free self-service signup ("Create Free Account"), shipping mobile apps ("The iOS and Android app brings 100% of the web functionality"), "measured platform uptime 99.96%", public review "4.8 (1708 ratings)", plus "Anolla ratings on Capterra" [sic — the fetched name of the review portal as rendered] 5.0/5 ease of use, 5.0/5 features, 4.7/5 value. Some intelligence features are explicitly *not* enabled: "our development focus is to make these capabilities increasingly proactive".

## 4.5 Source keys
| key | URL | accessed |
|---|---|---|
| `[AN-T]` | https://anolla.com/en/tattoo-software | 2026-09-19 |
| `[AN-F]` | https://anolla.com/en/features (module catalogue with "Activate …" strings) | 2026-09-19 |
| `[AN-AB]` | https://anolla.com/en/about-us | 2026-09-19 |
| `[AN-H]` | https://anolla.com/en ; https://anolla.com/en/salon-software | 2026-09-19 |
| `[AN-PR]` | https://anolla.com/en/pricing (soft-404: identical template to /en — see §4.9) | 2026-09-19 |
| `[AN-WBCDX]` | https://web.archive.org/cdx/identification?url=anolla.com/en/tattoo-software&matchType=exact&output=json&fl=timestamp&sort=asc (→20260213035432) | 2026-09-19 |
| `[AN-ITUNES]` | https://itunes.apple.com/search?term=Anolla&entity=software&country=us&limit=12 ; lookup id 1570020265 | 2026-09-19 |

## 4.6 Module structure (as published)
`[AN-F]` preamble: "**Activate paid features as needed.** Some features may require other paid features. **VAT will be added** to the prices. **The exact price and terms are shown in the detailed view of each feature.**"
- Core: `Core features` (auto email confirmations; prerequisite for paid add-ons), `Business profile`, `Billing`, `Help Center`, `Real-time statistics`, `Users`, `Clients`, `Services`, `Schedules`, `Calendar`, `Client notifications`, `Translations`, `Link Manager`.
- Business/finance: `Transactions` ("Consolidate payments and **cash register** activity into one view … **virtual point-of-sale** system … overview of the cash balance, turnover, and payment methods"), `Products` ("product inventory and stock movements … by **service location**"), `Customer invoices` ("generates an invoice or payment document as a PDF").
- Marketing/loyalty: `Memberships`, `Passes` (punch cards, period passes), `Mailchimp` ("synchronize customer contacts and customer groups … targeted campaigns and automated marketing workflows"), `Special service pricing` ("prices that differ … based on the date, time, day of the week, schedule, service, duration, or customer membership").
- Comms: `SMS notifications`, `IFTTT Switches API` (name as fetched — "Automate smart devices based on booking start and end times … control lighting, heating, or other connected devices").
- Payments: `Stripe payments` ("collect advance payments … automatically confirm paid bookings … recurring card payments for supported passes").
- Channels/CMS: `Client booking` (web/iOS/Android), `Wordpress plugin` [sic], `Wix integration`, `Large-Screen View`, `Minimum advance booking time`, `Add-on Service Booking`.
- `Schedules` definition (verbatim): "Manage the availability of **employees, rooms, equipment, and other bookable resources** from one place. Define **regular working hours and date-specific exceptions** so customers are always shown up-to-date bookable times."
- Tattoo vertical overlay `[AN-T]`: "Multi-Resource Booking — Set up multi-tattoo resource booking – let customers reserve **several tattoo artists, booths, workstations or equipment sets in one transaction**"; "Resource Management — link **workstations, booths, laser removal devices and special equipment** to specific tattoo artists and services, **avoiding double use**"; "Schedules … set regular working hours, **vacations, guest spots**, and exceptions"; "Time Blocking — create one-time or **recurring blocks** … using precise date, time and weekday filters"; "Automated **Waitlist**"; "Group Bookings … **recurring group sessions such as flash tattoo days** and special studio events"; "Dynamic pricing … campaigns, VIP prices, **flash-day offers**"; "Recurring Subscriptions"; "Passes and Tickets"; "Quotes and orders"; "Service marketplace"; "Interactive Business Profile … buy **gift cards**"; "IoT Ecosystem … **access control**, automated lighting … **24/7 self-service**"; "Tattoo shop scheduling software — Helps shop owners manage **workstations**, artist schedules, and client documentation (**consent forms**)".

## 4.7 Feature checklist
| Feature | Verdict | Evidence |
|---|---|---|
| online booking | **Y-V** | "Client booking — Provide customers with seamless, mobile-first self-service … find, book, and manage a suitable service and time themselves" `[AN-F]` |
| client self-booking | **Y-V** | "clients book consultations and tattoo sessions online" `[AN-T]` |
| appointment/artist/shared calendar | **Y-V** | "Calendar — Manage all bookings and related actions from one central view … participants, statuses, notifications, and **change history**"; "color-coded artist calendars in day, week or month view" `[AN-F]`,`[AN-T]` |
| station/chair/workstation booking | **Y-V ⚠⚠ (strongest counter-evidence for station booking)** | "Multi-Resource Booking — let customers reserve several tattoo artists, **booths, workstations or equipment sets** in one transaction"; "Resource Management — link **workstations, booths**, laser removal devices and special equipment to specific tattoo artists and services" `[AN-T]` |
| resource conflict checking | **Y-V** | "…**avoiding double use** and increasing studio throughput"; "Role-based permissions and real-time updates keep schedules accurate, **prevent conflicts**" `[AN-T]` |
| buffer/setup time | partial **Y-V** | "**Minimum advance booking time** — Give sufficient notice for services that require more preparation, transportation, or **setup time**" `[AN-F]`; "Variable-Duration Services … minimizes **idle gaps**" `[AN-T]`. Inter-appointment buffer field: not found |
| working hours/holidays/absences | **Y-V** | "Define **regular working hours and date-specific exceptions**"; "Coordinate artists' **working hours, studio closures**, private events, rooms, equipment and other resources from one calendar" `[AN-F]`,`[AN-T]` (literal `holiday`/`absence` keywords not present) |
| time-off | **Y-V** | "set regular working hours, **vacations**, guest spots, and exceptions" `[AN-T]` |
| guest/resident artists | **Y-V** | "**guest spots**"; "guest artists"; "assign different permissions to studio managers, front-desk staff, apprentices, and **guest artists**" `[AN-T]` |
| walk-ins | **Y-V (as a segment)** | "hybrid tattoo studios that handle both short **walk-in** pieces and long, multi-session planned projects"; pricing rules per "customer segments – for example regular clients, new clients, **walk-ins** or large projects" `[AN-T]`. No walk-in booking module per se |
| recurring/multi-session | **Y-V** | "**Recurring** blocks"; "**Recurring Subscriptions** — automatically renewing … ideal for … multi-session sleeves carried out step by step"; "hourly and multi-day … simultaneously" `[AN-T]`,`[AN-F]` |
| waitlist | **Y-V** | "**Automated Waitlist** — … Clients receive notifications when suitable times open up"; "manage real-time attendee lists and **waitlists**" `[AN-T]`; "Replace fragmented calendar apps, email exchanges and **manual waiting lists** with one powerful solution" `[AN-T]` |
| client profiles/history | **Y-V** | "Clients — customer database … updated automatically from bookings … contact details, notes, groups, and memberships"; CRM "consolidates each client's **tattoo history**, ideas, style preferences, consultation notes and photos" `[AN-F]`,`[AN-T]` |
| notes | **Y-V** | "contact details, **notes**, groups" `[AN-F]` |
| reference images | **Y-V** | "…consultation **notes and photos** into a single real-time updated database"; "browse artist **portfolios**" `[AN-T]` |
| consultation | **Y-V** | "Manage **consultations**, tattoo sessions, project stages, design approvals, automatic reminders and activity logs from one clear dashboard" `[AN-T]` |
| consent forms | **Y-C ⚠** | appears only as SEO copy: "client documentation (**consent forms**)" `[AN-T]`; no `Consent` module in the catalogue `[AN-F]` (the only `consent` strings concern **marketing consent** for Mailchimp contacts) ⇒ advertised-unverified |
| aftercare | **Y-C** | "strategic **aftercare** and repeat booking offers"; "**automatic aftercare instructions**" (paid plans); "from first enquiry to aftercare" `[AN-T]` — not a named module |
| deposits | **Y-V** | "Online payments — Let clients pay a secure **deposit** when booking tattoo appointments. Appointments are confirmed once payment is received, helping **reduce no shows**" `[AN-T]`; `Stripe payments` "collect **advance payments**" `[AN-F]`; metric "Full online payment flow with prepayment — **100%** … confirmed only after the full booking fee has been paid" `[AN-T]` |
| payments/POS | **Y-V** | "`Transactions` … **virtual point-of-sale** … cash balance, turnover, and payment methods" `[AN-F]`; "Manage online bookings, **payments, point of sale** and marketing automation in one system" `[AN-T]` |
| artist commissions & artist/shop split | **NF ⚠⚠ (important negative)** | keyword sweep over all fetched Anolla pages: **`commission` n=0, `payout` n=0, `booth rent` n=0, `staff split` n=0**. Closest: "average **revenue per artist**" (statistics), "per-studio … **turnover**". ⇒ **no artist-/shop commission ledger evidenced** ⇒ this is where Team Calendar's ledger concept stays defensible against Anolla (but see Linework/InkLinka/TattooManager) |
| invoicing | **Y-V** | "`Customer invoices` — … generates an **invoice** or payment document as a **PDF** … downloadable from the booking details" `[AN-F]` |
| monthly closing / locked months | **NF** | no period-close/lock statement found; `Billing` covers "subscription, payments, and invoices … top up SMS credit" only |
| financial reports | **Y-V** | "`Real-time statistics` — … **bookings, turnover, transactions, services, and new customers** for the selected period"; "export … to **Excel, Google Sheets** or directly into BI and AI tools" `[AN-F]`,`[AN-T]` |
| roles/permissions | **Y-V** | "`Users` — … assign their **permissions** for features, bookings, schedules, and service locations"; "**Flexible role- and location-based access control (RBAC)** … studio managers, front-desk staff, apprentices, and guest artists" `[AN-F]`,`[AN-T]` |
| multi-staff | **Y-V** | "Manage **unlimited** … users, services, and clients"; "add an unlimited number of … artist profiles, and administrators" `[AN-T]` |
| multi-room | **Y-V** | "`Schedules`: employees, **rooms**, equipment, and other bookable resources"; "larger shop with **multiple rooms** and guest artists" `[AN-F]`,`[AN-T]` |
| multi-location | **Y-V** | "**unlimited tattoo studios** … in one place"; "tattoo studio operating as a **chain** … centralized dashboard to manage all artists, booths, queues and bookings"; "manage **physical, region-based, and online service locations**"; "track sales … by **service location**" `[AN-T]`,`[AN-F]` |
| multi-tenant | **Y-C** | "Thousands of businesses, hundreds of industries … one unified platform"; per-account subscription model `[AN-AB]`; the word "multi-tenant" is not published |
| studio branding | **Y-V** | "`Business profile` — Set the **brand name**, primary business activity, country, time zone, and currency"; "preserve your tattoo studio's **brand voice**" `[AN-F]`,`[AN-T]` |
| email | **Y-V** | "`Client notifications` — … **booking confirmations, reminders**, and other supported booking-related email notifications"; "Multilingual messages are managed securely and **documented**" `[AN-F]`,`[AN-T]` |
| SMS | **Y-V** | "`SMS notifications` — Reduce **missed appointments** … even when they are not using email or the app" (paid, "top up SMS credit" in `Billing`) `[AN-F]` |
| WhatsApp | **NF** | keyword sweep: `WhatsApp n=0` |
| Instagram | partial **Y-V** | "Create and share separate booking links and QR codes … every **Instagram** portfolio post, TikTok video description, 'Book a tattoo' button … becomes a direct booking funnel"; "Add a link to your Instagram profile" `[AN-T]`,`[AN-F]` |
| unified inbox | **NF** | only "forum My conversations" in the client shell (a user-side view) `[AN-H]`; no unified inbox of channels documented |
| campaigns | **Y-V** | "`Mailchimp` — … **targeted campaigns** and automated marketing workflows … only contacts with appropriate **marketing consent**"; "one of the market's most powerful solutions for creating **campaigns**, VIP prices, flash-day offers" `[AN-F]`,`[AN-T]` |
| review requests | **Y-V** | "**Automatic feedback collection** — Automatically collect **ratings and comments** after every completed client visit"; "4.8 (1708 ratings)"; "Anolla ratings on Capterra" `[AN-T]`,`[AN-H]` |
| flash/flash-days | **Y-V** | "recurring group sessions such as **flash tattoo days**"; "**flash-day offers**"; "quick small-symbol **flash** sessions" `[AN-T]` |
| stencil tools | **NF** | `stencil n=0` |
| ink registration | **NF** | no ink registry found |
| inventory | **Y-V** | "`Products` — Keep **product inventory and stock movements** under control … catalog, groups, prices, and units … sales, purchases, and stock movements by service location" `[AN-F]` |
| gift cards | **Y-V** | "buy **gift cards**"; "collect deposits and booking fees or sell gift cards as part of the online booking process" `[AN-T]` |
| PWA | **Y-V** | "Our mobile apps **primarily serve as interfaces for the main PWA platform**" `[AN-AB]`; "The platform has an intuitive mobile-friendly user interface. It uses **cloud synchronization**. It provides instant app notifications." `[AN-H]` |
| offline mode | **NF / effectively NO** | `offline n=0`; "cloud-based access … Your data stays **synchronized automatically**"; "works on the web, iOS, and Android"; SMS value proposition: "text messages reach clients quickly **even when they do not have internet access**" (the *client's* device, not the app) ⇒ offline working is not documented |
| sync | **Y-V** | "**Schedules** automatically sync artists' and studio booth availability with the online booking calendar"; "real-time updates"; "Cloud-based access … synchronized automatically" `[AN-T]`,`[AN-F]`,`[AN-H]` |
| mobile app (iOS/Android) | **Y-V** | "Admin app — A mobile app for studio owners and tattoo artists (**iOS and Android**) that offers **100% of the web version's functionality**"; "Client app (iOS, Android, web)"; App Store lookup id 1570020265 (`sellerName='Booklux OU'`, `bundleId='com.agado.agado'`, first released 2021-06-10) `[AN-T]`,`[AN-ITUNES]` |
| browser app | **Y-V** | "Cross-platform ecosystem … runs smoothly on Mac/PC, iOS and Android"; "browser and mobile" `[AN-T]`,`[AN-H]` |
| API | **Y-V** | "We built the platform **API-first**"; "includes a powerful **API** and integration options with other systems"; "`IFTTT Switches API`" `[AN-AB]`,`[AN-T]`,`[AN-F]` |
| Google Calendar | **NF** | only "Google Analytics, Google Tag Manager and Meta Pixel" + "export to Excel, **Google Sheets**"; no calendar interchange with Google Calendar found |
| accounting/Stripe/payment providers | **Y-V** | "`Stripe payments`" module; "For payment processing there is a direct integration with **Stripe**"; "integration options with other systems used by the studio such as **accounting software**, marketing automation, loyalty programmes or website CMS platforms"; "For payment processing, we use **certified and internationally recognized providers**" `[AN-F]`,`[AN-T]`,`[AN-AB]`. A named accounting product (DATEV/Lexware/etc.): not found |
| analytics (revenue/utilization/no-shows/retention/artist perf.) | **Y-V (broad)** | "track booked tattoo sessions, **average revenue per artist**, the most popular styles and body areas in real time"; "**Customer Loyalty Analytics** … who your most valuable tattoo enthusiasts are, how often they plan new tattoos … to … **maximise studio occupancy**"; "real-time dashboard displays **revenue, booked slots, repeat bookings, new clients and cancellations**"; "measure booking sources, **campaign ROI**"; "analyse **artist occupancy**, style popularity and average booking value" `[AN-T]` (note: "Customer Loyalty" [sic] as fetched) |

## 4.8 Positioning
H1: "**Tattoo studio management software**" / second H2 "Tattoo shop management software". Deck: "Anolla helps tattoo studios manage online bookings, artist calendars, client records and appointments in one flexible system. Automate routine admin, coordinate studio resources and let clients book consultations and tattoo sessions online." Second deck: "Build a workflow that fits your tattoo business with **modular tools and detailed configuration options** … a system that can evolve with your studio and support your team with **AI-powered features**." About-us vision: "Anolla is **evolving service booking from a static calendar into an intelligent experience**" / "We're building something fundamentally different: infrastructure that gets better over time at predicting needs, recommending optimal times, and personalizing communication." Differentiation from generic calendar apps is explicit: "Many booking tools only handle time selection and calendar organization" and "Unlike many beauty service booking systems, Anolla does not force you to choose only between an hourly or a day-based booking model."

## 4.9 Pricing (official)
**Model = free core + metered/usage-based + per-feature "activate paid" add-ons; no euro amount is published on any fetched page.**
- `[AN-T]`: "**Flexible pricing** … a transparent **usage-based model** with no hidden fees that scales from a solo tattoo artist to a small named studio or a larger shop with multiple rooms and guest artists"; "**Free software** — Start for free … **0€**"; "Start with free software and **activate paid features as needed**"; "Anolla's pricing is based on **actual usage**, so you only pay for the features your tattoo studio needs"; FAQ: "How does Anolla's **usage-based pricing** help reduce a tattoo studio's business risk? … **Software costs scale in proportion to the actual booking volume and system usage.**"
- `[AN-F]`: "Activate paid features as needed. Some features may require other paid features. **VAT will be added** to the prices. **The exact price and terms are shown in the detailed view of each feature.**" ⇒ prices are gated behind login/in-app; **not publicly disclosed**.
- `[AN-H]`: "Join for free … There are no sign-up or monthly fees"; "A fee applies only after the job is confirmed. The **Boost** service and additional integrations are optional paid modules."
- Methodological note (adversarial): `https://anolla.com/en/pricing`, `/en/service-providers` and `/en/modules` all return the **same template** (`textlen ≈ 14.9–15.7 k`, identical nav/footer) ⇒ these are **soft-404s**; I therefore did **not** treat their content as a pricing page. Also the "metrics" block on `[AN-T]` is self-published: "**Anonymized** … **do not guarantee results for any individual tattoo studio**", each with "Source and method" — treat as vendor claims (Y-C).

## 4.10 Advertised USPs
1. **Modularity + configurability**: "Activate over **20 ready-to-use modules** instantly"; "Add-on modules … Enable add-ons with one click"; "12 Advanced features activated via self-service" `[AN-H]`,`[AN-T]`.
2. **AI as support staff, not as a feature**: "24/7 Contextual AI support … **AI-resolved support chats 79.3%**"; "Unedited AI-generated support responses 52.4%"; "The 24/7 end-customer support is like hiring two full-time employees for free" (customer testimonial) `[AN-T]`.
3. **Resources and multi-location at scale**: "unlimited … booths, workstations or equipment sets", "unlimited tattoo studios, users, services, and clients", "1M+ Bookings Annually", "30+ countries" `[AN-T]`,`[AN-H]`.
4. **Language/rollout moat**: "26 languages … user interface, notifications, AI assistance, and customer support workflows"; "multi-currency and time zones" `[AN-T]`.
5. **Physical-world integrations**: "IoT Ecosystem … access control, automated lighting … **24/7 self-service**; door control solutions (self check-in for regular clients); equipment rental management; sensors that help the studio monitor **workspace usage**" `[AN-T]`.

## 4.11 Uniqueness probes
- **station booking** → **found, twice** ("booths, workstations or equipment sets in one transaction"; "Resource Management — link workstations, booths, laser removal devices…avoiding double use"). Team Calendar must **not** present station/resource booking as unique against Anolla. What *is* not evidenced anywhere in the fetched copy: a station-level **conflict-queue/hold-resolution UI** named as such, or per-station revenue attribution in a ledger.
- **offline mode** → **not found**; the platform is described as cloud-synchronised only ⇒ the offline claim is uncontested by Anolla.
- **commission ledger w/ month close** → **not found** (commission/payout/booth-rent keywords: zero matches) ⇒ uncontested by Anolla — but *contested* by Linework (`[LW-P]` `[LW-S]`), TattooManager (`[TM-P]`) and InkLinka (`[IK-APP]`).

---

# 5. Cross-competitor matrix (the "is Team Calendar unique?" scorecard)

| Team-Calendar "unique" candidate | TattooManager | InkLinka | Linework | Anolla | Verdict for Team Calendar |
|---|---|---|---|---|---|
| **Online booking / client self-booking** | Y-V | Y-V | Y-V | Y-V | **Not unique.** Commodity. |
| **Station / chair / workstation booking** | **Y-V** ("Standorte & Arbeitsplätze", "Standort- & Aufenthaltsplaner", plan counts 3/10, 5/20) | partial (workstation **count** = capacity + load %, guest-capacity validator) | **Y-V** ("choose which workplace it belongs to"; "Flat booth rent") | **Y-V** ("booths, workstations or equipment sets in one transaction"; "avoiding double use") | **Not unique as a capability.** Narrow the claim to *named, bookable station entities with a station-level conflict queue and per-station utilisation/ledger attribution*, and evidence it. |
| **Resource conflict checking** | Y-V ("Räume, Artists und Zeiten bleiben sauber koordiniert") | Y-V (`preventOverlaps`, `eventOverlap`, `datesCovered`) | NF | Y-V ("avoiding double use", "prevent conflicts") | Not unique. |
| **Working hours / holidays / time-off** | NF | Y-V (Working Hours + Vacation start/end) | partial ("block out time") | Y-V (working hours + date-specific exceptions + vacations) | Not unique. |
| **Guest/resident artists** | Y-V ("Gast-Künstler-Funktion" + Connect marketplace) | Y-V (Guest Planner, invitations, rates, revenue share) | Y-V ("Guest artist support") | Y-V ("guest spots", "guest artists") | Not unique. |
| **Walk-ins** | NF | partial ("Walk-in name (optional)") | NF | Y-C (walk-ins as a pricing segment) | Potentially differentiating *as a first-class flow*; nobody documents a walk-in booking module. |
| **Waitlist** | NF | NF | NF | **Y-V** ("Automated Waitlist") | **Not unique** (Anolla has it). |
| **Consent forms + digital signature** | **Y-V** (6 form types, eIDAS-conform signatures) | **Y-V** (Client Consent Form + signature pad) | **Y-V** ("Consent forms (digitally signed)", "Health history forms") | Y-C (only SEO copy) | Not unique. |
| **Deposits** | Y-V | Y-V (incl. no-show deposit forfeiture cases) | Y-V | Y-V (100 % prepayment metric) | Not unique. |
| **Payments / POS / cash register** | Y-V (Kassenbücher, cash-drawer opening) | Y-V (checkout, receipts, mixed-appointment checkout) | Y-V (POS for cash and card, cash sale tracking, tipping) | Y-V ("virtual point-of-sale", cash register view) | Not unique. |
| **Artist/shop commission ledger (+ monthly close)** | **Y-V** ("Künstler-Provisionen berechnen", "Platzmieten abrechnen", "Tagesabrechnungen", "Kassenbücher", "Monats- & Jahresbilanzen exportieren") | **Y-V** ("Closed unpaid … monthly compensation cycles", outstanding balance, advances receivable, payouts, ledger-based reports) | **Y-V** ("Automatic commission split", "Settlements & payout statements", "end of every month … commissions tracked per artist, invoiced properly, and collected") | **NF** (commission/payout keywords: 0 matches) | **Not unique in concept; three of four competitors ship it.** Remaining defensible ground: *immutable period lock + audit trail + per-station attribution*, none of which is documented by any competitor. |
| **Multi-location / multi-tenant** | Y-V (up to 5 locations) | Y-C (multi-studio *federation*, one tenant per studio) | NF (artist federates across studios instead) | Y-V (unlimited locations, RBAC) | Not unique. |
| **PWA / installable web app** | Y-V (`display:standalone`) | Y-V (`display:standalone`) | Y-V (`display:standalone`, landscape dashboard) | Y-V ("interfaces for the **main PWA platform**") | **Not unique — PWA is table stakes.** |
| **Offline mode** | NF (offline ⇒ error strings) | NF (offline ⇒ chat-widget status) | NF | NF (cloud-sync only) | **This is Team Calendar's strongest uncontested axis in the checklist** — subject to verification of the four shipped apps' offline capabilities on device. |
| **Native mobile apps** | **no App Store app** (PWA only) | iOS Y-V (2026-04-17, v1.0.9, 0 ratings) | iOS Y-V (2022-03-13, v6.8.4, 4 ratings, 3.75★) | iOS Y-V (2021-06-10, com.agado.agado) | All have native apps except TattooManager (PWA-only) → *mobile is not a differentiator, but "one installable offline-capable PWA for iOS **and** Android" is unusual*. |
| **Stencil tooling** | NF | **Y-V (beta, AI, mm-exact, PNG/SVG, quota-metered "Neurons")** | NF | NF | Unique to InkLinka among these four — do not compete on it. |
| **Analytics: utilisation / no-shows / retention / artist performance** | Y-V (partial) | Y-V case-queue + **ROADMAP** for forecasts ("…remain disabled") | partial (sales/revenue only) | **Y-V (broad: revenue per artist, occupancy, loyalty cohorts, ROI)** | Not unique; Anolla is the strongest generic analyst here. |
| **Flash / flash-days** | NF | partial ("Flash claim" form) | Y-V ("Flash gallery with images") | Y-V ("flash tattoo days", "flash-day offers") | Not unique. |
| **Inventory / merch sales** | Y-V (Material-Verwaltung, orders/deliveries) | Y-V (products, stock, inventory asset account) | partial ("Retail product sales") | Y-V (Products module, stock movements by location) | Not unique. |
| **Gift cards / vouchers** | Y-V ("Gutscheine verwalten") | Y-V ("Gift certificates … only on paid plans", revenue-recognition wording) | NF | Y-V ("buy gift cards") | Not unique. |
| **Google Calendar sync** | **Y-V** (Google + Apple calendar, OAuth, privacy-policy §10) | Y-V (Google Calendar **import**) | NF | NF (analytics only) | Not unique. |
| **WhatsApp** | Y-C (2 bundle strings) | Y-C ("Messenger integrations (WhatsApp, Telegram)") | NF | **NF (0 matches)** | Weakly differentiating at best; verify before advertising. |
| **Unified inbox** | Y-C (Posteing screenshot) | **Y-V** (email + contact-form channels, 24 h retention) | NF | NF (only user-side "My conversations") | Semi-differentiating vs 2 of 4. |

## 5.1 Top-3 advertised USPs per competitor (as advertised; unverified unless noted)
- **TattooManager** — (1) German compliance/PWA posture: "Server in Deutschland · DSGVO & GoDV Konform · Keine Installation nötig" (Y-V); (2) tattoo document suite with eIDAS signatures (Y-V); (3) studio economics: commissions, chair rent, daily settlements, workstation/location tiers (Y-V) + free artist↔studio marketplace "Connect".
- **InkLinka** — (1) "The AI-Powered Operating System for Tattoo Studios" / "Stop paying for spa software" 14-row comparison table (Y-V for existence of the claim, Y-C for its truth); (2) request→client→appointment→project automation (Y-V in bundle); (3) Universal Stencil Maker, AI-metered (Y-V, beta).
- **Linework** — (1) "Built by tattooers, for tattooers" (Y-V); (2) "Every plan includes every feature. The only thing the price changes is the transaction fee." 6 % free / $19 + Stripe fees (Y-V); (3) money-split automation: commission split, booth-rent invoicing, next-day payouts, tax-ready reports (Y-V).
- **Anolla** — (1) "modular … activate over 20 ready-to-use modules", usage-based pricing, 0 € free core (Y-V for the model, prices undisclosed); (2) 24/7 AI support (79.3 % resolved by AI) + "26 official languages" (Y-C self-measurement with published methodology); (3) unlimited resources/multi-location RBAC + IoT self-service (Y-V for the claims, depth unclear).

## 5.2 Age ranking (oldest → youngest, by *earliest evidence actually seen*)
1. **Anolla** — platform "Founded in 2011" (vendor claim), app 2021-06-10, **tattoo landing page first captured 2026-02-13**.
2. **Linework** — "Coming soon." 2021-12-11 → live product 2022-04-24 → app 2022-03-13 → ToS effective 2023-06-01. *(Domain captures from 2000-06-20 belong to a prior, unrelated use and are excluded.)*
3. **TattooManager** — first capture 2025-01-07; first substantive snapshot 2025-03-21; app store: none.
4. **InkLinka** — legal pages dated 2026-04-14; App Store release 2026-04-17; **zero Wayback coverage**; app v1.0.9 with 0 ratings. ⇒ a 5-month-old product in open beta, with at least two features self-labelled "beta" and one analytics feature whose predictive functions are explicitly disabled.

## 5.3 Where Team Calendar can still stand out (after contradiction)
1. **Offline-first** — nobody in these four documents offline operation; every one of them treats "offline" as an error/edge case, and Anolla describes itself as cloud-synchronised only. Highest-value, uncontested axis.
2. **Locked/immutable accounting periods with an audit trail** — competitors compute commissions and settlements (TattooManager, InkLinka, Linework) but none documents a *month lock*, a period-sealed ledger, or tamper-evident history. (Anolla's `Calendar` documents only a "change history".)
3. **Per-station attribution inside the ledger** — station/resource booking exists at three competitors, but no competitor attributes revenue, utilisation or no-shows *per named station*; they attribute per artist, per client, per service location.
4. **Walk-in as a first-class booking flow** — only segment-level mentions; no walk-in module documented.
5. Caveats: do **not** advertise PWA, online booking, consent forms, deposits, guest artists, waitlists, gift cards, Google-Calendar sync, analytics dashboards or AI assistants as unique — all are documented at one or more of these four.
