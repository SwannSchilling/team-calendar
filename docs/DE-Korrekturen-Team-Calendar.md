# Prüfung der deutschen Texte: Team Calendar (Tattoo-Studio-Kalender)

## 0. Prüfumfang und Kontext

Geprüft wurden die im Projekt vorhandenen deutschen Texte der Produktseite für **Team Calendar**, insbesondere:

- `src/data/tour.de.ts`
- `src/data/features.de.json`
- `dist/de/index.html` als generierter DE-Build

**Hinweis zum Link:** In der aktuellen Nachricht war kein konkreter, eindeutig übermittelbarer URL enthalten. Die Prüfung erfolgte daher anhand des lokalen DE-Builds und der DE-Datenquellen im Projekt. Wenn du den exakten Live-Link hast, kann ich die dort ausgelieferten Texte zusätzlich 1:1 gegen die Quelltexte vergleichen.

**Zielgruppe:** Tätowierer:innen, Studio-Inhaber:innen, Admins und Empfangsteams in Tattoo-Studios, die ihr Zeitmanagement, ihre Terminplanung, ihre Kundenkommunikation und ihre Abrechnung klarer, schneller und fehlerärmer organisieren wollen.

---

## 1. Kerninteressen der Zielgruppe: Tattoo-Studios denken in Zeit, Stühlen, Geld und Motiven

Die Käufer:innen dieser App denken nicht in Feature-Listen, sondern in konkreten Studio-Situationen. Die Texte sollten deshalb sofort die praktischen Fragen beantworten, die im Alltag Geld, Zeit und Nerven kosten.

### 1.1 Kernfragen der Zielgruppe

| Kernfrage der Zielgruppe | Was wirklich gemeint ist | Antwort / USP von Team Calendar | Copy-Baustein |
|---|---|---|---|
| Verhindert die App Doppelbuchungen am Stuhl? | Nicht nur Personen werden gebucht, sondern konkrete Arbeitsplätze: Stuhl 1, Stuhl 2, Kabine. | Arbeitsplätze sind eigene buchbare Ressourcen mit Konfliktprüfung, Kapazität und Pufferzeit. | „Stuhl gebucht, Konflikt gecheckt.“ |
| Wie reduziere ich No-Shows und kurzfristige Absagen? | Verlorene Arbeitszeit, unsichere Auslastung, frustrierte Kund:innen. | Geführte Buchung, Warteliste, Terminstatus, geplante Erinnerungen und Anzahlungen als Umsatzsicherung. | „Weniger Leerlauf im Kalender, mehr gebuchte Auslastung.“ |
| Wie rechne ich Künstler:in und Studio sauber ab? | Wer schuldet wem was? Splits, Checkout, Monatsabschluss, Steuerberatung. | Honoraranteil pro Transaktion, Checkout-Sperrung, Saldo-Übertrag, gesperrte Monate, druckbarer Bericht EN/DE. | „Die Abrechnung rechnet, die Zahlen stimmen.“ |
| Wo ist die Vorlage, wenn ich sie brauche? | Motiv, Flash, Cover-up, Vorher-/Nachher, keine Suche in 400 DMs. | Motivvorlagen direkt am Termin, automatisch komprimiert, im Kalender und Profil sichtbar. | „Vorlage sichtbar, Motiv klar, Künstler:in informiert.“ |
| Funktioniert das auch am Tattoo-Arbeitsplatz, bei schwachem WLAN? | Empfang im Studio ist oft mangelhaft, der Arbeitsfluss darf nicht gestört werden. | PWA, installierbar, offline lauffähig, Sync bei Verbindung, App-Badge, Push-Stufen. | „Offline nicht offline — sondern nur vertagt.“ |
| Können Kund:innen selbst buchen und verschieben? | Chat-Overload, Hin und Her, Ticket-Chaos. | Geführter Buchungsprozess, sicherer Einmal-Link, echte Verfügbarkeit, keine Anmeldung erforderlich. | „Ohne Anmeldung, ohne Chat, ohne Chaos.“ |
| Wie behalte ich mein Team im Blick? | Rollen, Rechte, Abwesenheiten, Arbeitszeiten, Dienstleistungen. | Teamkalender, Farbcodierung, Rollenmodell, Statusleiste, Konfliktprüfung. | „Wer sieht was, wenn wer wo wann was bucht?“ |
| Wie wird aus einem Besuch eine Wiederholungsbuchung? | Social Proof, Google-Bewertungen, Instagram, Kundenbindung. | Bewertungs-Loop, 10-%-Rabattcode, Instagram-Funnel, Kundenprofil mit Historie. | „Ein Like, ein Follow, ein Folgetermin.“ |
| Sind die Kundendaten DSGVO-sicher getrennt? | Einwilligung, Löschung, Export, mehrere Studios. | Versionierte Einwilligung, Datenexport, Datenlöschung, strikte Tenant-Isolation. | „Deine Daten, deine Rechte, dein Studio.“ |
| Kann ich mehrere Standorte sauber führen? | Zeitzone, Währung, Tenants, Studio-Branding. | Standorte, Zeitzone, Währung, Multi-Tenant, Studio wechseln. | „Ein Login, mehrere Studios, keine Verwirrung.“ |

### 1.2 Empfohlene Tonalität

- **Du-Ansprache**, weil Tattoo-Studios persönlich, handschriftlich, kreativ und direkt arbeiten.
- **Locker-professionell**: keine Behördensprache, keine Konzernsprache, keine Fachsprache ohne Erklärung.
- **Fachbegriffe nur dort**, wo sie erklären helfen: „Honoraranteil“, „Pufferzeit“, „PWA“, „Tenant“.
- **Gendergerechte Formulierungen**: Tätowierer:innen, Künstler:innen, Kund:innen.
- **Priorität der USPs**: erst Stuhl, dann Kunden, dann Geld, dann Kommunikation, dann Technik.

---

## 2. Harte Korrekturen: Rechtschreibung, Grammatik, Zeichensetzung

> Jede Korrektur steht in einer eigenen Entität / Tabellenzeile.  
> Die Spalte „Fundstelle“ zeigt, wo der Text steht. Die Spalte „Korrektur“ zeigt, wie der Text stehen soll.

| ID | Fundstelle / Datei | Betroffene Passage | Korrektur / Vorschlag | Begründung |
|---:|---|---|---|---|
| HC-01 | `src/data/tour.de.ts`, Zeile 32 | `Iemand jongliert` | `Jemand jongliert` | Großschreibung und Wortanfang: „jemand“ schreibt sich mit J. „jonglieren“ schreibt sich mit ie. |
| HC-02 | `src/data/tour.de.ts`, Zeile 56 | `Splits auf der Servie ausgerechnet` | `Splits auf der Serviette ausgerechnet` | Wortfehler: „Serviette“ statt „Servie“. |
| HC-03 | `src/data/tour.de.ts`, Zeile 56 | `Anzahlen diskutiert` | `Anzahlungen diskutiert` | Kontext: Gemeint sind Anzahlungen / Deposits, nicht bloße Zahlen. |
| HC-04 | `src/data/tour.de.ts`, Zeile 57 | `gibt es einen druckbaren Bericht` | `gibt es einen druckbaren Bericht` | Tippfehler: „gibt es“ statt „gibt es“. |
| HC-05 | `src/data/tour.de.ts`, Zeile 63 | `Totes Wi-Fi, lautes Studio.` | `Totes WLAN, lautes Studio.` | Terminologie: Im deutschen Text ist „WLAN“ klarer als „Wi-Fi“. |
| HC-06 | `src/data/tour.de.ts`, Zeile 65 | `auf den Home-Bildschirm installiert` | `auf dem Startbildschirm installiert` | Kasus und Idiomatik: „auf dem Startbildschirm installiert“. „Startbildschirm“ statt Denglisch. |
| HC-07 | `src/data/tour.de.ts`, Zeile 65 | `die App-Icon-Badge` | `der App-Badge` | Genus und Verständlichkeit: „Badge“ ist im Deutschen meist „der/das Badge“; „App-Icon-Badge“ ist sperrig. |
| HC-08 | `src/data/tour.de.ts`, Zeile 92 | `damit nichts sich überschneidet` | `damit sich nichts überschneidet` | Wortstellung: Reflexivpronomen vor Negation: „sich nichts“. |
| HC-09 | `src/data/tour.de.ts`, Zeile 101 | `zwischen Shop und Artist aufgeteilt` | `zwischen Studio und Künstler:in aufgeteilt` | Partizip: „aufgeteilt“. Fachsprache: Studio/Künstler:in statt Shop/Artist. |
| HC-10 | `src/data/tour.de.ts`, Zeile 101 | `jede Abrechnung ist einzeln einsehbar` | `jede Abrechnung ist einzeln einsehbar` | Rechtschreibung: „einzeln“ schreibt sich mit h. |
| HC-11 | `src/data/features.de.json`, Zeile 221 | `jeden Stuhl einzeln` | `jeden Stuhl einzeln` | Rechtschreibung: „einzeln“ statt „einzeln“. |
| HC-12 | `src/data/features.de.json`, Zeile 244 | `Sperre einzelner Zeitfenster` | `Sperre einzelner Zeitfenster` | Rechtschreibung: „einzelner“ mit h. |
| HC-13 | `src/data/features.de.json`, Zeile 921 | `Eine asynchrone, robuste Zustellung` | `Eine asynchrone, robuste Zustellung` | Rechtschreibung: „asynchrone“ mit ä. |
| HC-14 | `src/data/features.de.json`, Zeile 744 | `Verknüpft mit dem geplanten` | `Verknüpft mit dem geplanten` | Rechtschreibung: „verknüpft“, nicht „verknüpft“. |
| HC-15 | `src/data/features.de.json`, Zeile 1010 | `noch nicht mit einem echten Studio verknüpft` | `noch nicht mit einem echten Studio verknüpft` | Rechtschreibung: „verknüpft“, nicht „verknüpft“. |
| HC-16 | `src/data/tour.de.ts`, Zeile 165 | `suche eine bestimmte Funktion` | `suche eine bestimmte Funktion` | Rechtschreibung: „bestimmte“ mit zwei m. |
| HC-17 | `src/components/TourPage.astro` in Verbindung mit `features.de.json` | Notiz-Schlüssel enden teilweise auf `:`, z. B. `Notiz:`, `Status:`; die Komponente ergänzt zusätzlich `: `, dadurch erscheint `Notiz::` bzw. `Status::`. | Notiz-Schlüssel ohne Doppelpunkt pflegen: `"Notiz"` statt `"Notiz:"`, `"Status"` statt `"Status:"`, `"Verifizieren"` statt `"Verifizieren:"`. Alternativ die Komponente so anpassen, dass sie keinen zusätzlichen Doppelpunkt ergänzt. | Zeichensetzungslehre / UI-Text: Der Doppelpunkt wird doppelt gesetzt, was er nicht werden soll. |
| HC-18 | `src/utils/text.ts`, Zeile 56 | `Deployment ausstehend` | `Bereitstellung ausstehend` oder `Deployment steht aus` | Verständlichkeit: „Deployment ausstehend“ ist holprig. Als Badge ist „Bereitstellung ausstehend“ oder „Deployment steht aus“ klarer. |

---

## 3. Sinnvolle Umformulierungen: locker, professionell, USP-sicher

Diese Vorschläge sind nicht nur Rechtschreibungskorrekturen, sondern Conversion- und Verständlichkeitsoptimierungen.

| ID | Abschnitt | Betroffene Passage / Status | Vorschlag | Ziel |
|---:|---|---|---|---|
| SC-01 | Hero / Tagline | `Der Studio-Kalender, der Zettel, Chat und Serviette ablöst.` | `Der Studio-Kalender für Tattoo-Studios — vorbei mit unübersichtlicher Zettelwirtschaft.` | direkter Nutzen, Zielgruppenansprache, charmant |
| SC-02 | Hero / Subline | `Team Calendar ist der Kalender für Tattoo-Studios ...` | `Team Calendar ist der Kalender für Tattoo-Studios: geführte Kundenbuchung, Stuhl-Planung mit Konfliktprüfung, Honorarabrechnung ohne Zahlen-Chaos und eine PWA, die auch ohne WLAN weiterläuft.` | kürzer, klarer, mehr USP |
| SC-03 | Hero CTA | `Einen Tag miterleben` | `Einen Studio-Tag miterleben` | konkreter, bildlicher, alltagsnah |
| SC-04 | Story 09:41 Pain | `Jemand jongliert mit zwei Handys ...` | `Jemand jongliert zwischen zwei Handys, Papierkalender und 400 DMs. Der vermeintlich freie Termin ist längst vergeben — und der Stuhl bleibt ungebucht.` | Problem scharf, bildlich, klar |
| SC-05 | Story 09:41 Fix | `Dein Kunde tippt auf einen sicheren Einmal-Link ...` | `Kund:in tippt auf einen sicheren Einmal-Link — ohne Login, ohne App. Team Calendar prüft echte Arbeitszeiten, Abwesenheiten und Verschiebe-Fenster. Das Studio legt die Regeln fest.` | Gender, Nutzen, Kontrolle |
| SC-06 | Story 11:05 Pain | `Die meisten Buchungstools buchen Menschen ...` | `Viele Tools buchen Menschen. Niemand prüft, ob der Stuhl frei ist. Dann stehen zwei Künstler:innen an Stuhl 2 — und eine Person muss weichen.` | Doppelbuchung konkret und verständlich |
| SC-07 | Story 11:05 Fix | `Die Konfliktprüfung läuft pro Stuhl ...` | `Stühle sind buchbare Ressourcen mit eigener Kapazität und Puffer. Die Konfliktprüfung läuft pro Stuhl: Künstler:in, Abwesenheiten, Arbeitszeiten — bevor ein Termin angenommen wird.` | Mehrzahl und Reihung der Prüffunktionen |
| SC-08 | Story 14:30 Fix | `Motiv- und Vorher/Nachher-Bilder hängen direkt am Termin.` | `Motiv- und Vorher-/Nachher-Bilder sind fest am Termin. Automatisch komprimiert, im anstehenden Kalender der Künstler:in sichtbar.` | Was der Zeichner wissen muss |
| SC-09 | Story 20:00 Pain | `Splits auf der Servie ausgerechnet ...` | `Splits auf der Serviette, Anzahlungen diskutiert, doppelt in die Tabellen — am Monatsende traut niemand den Zahlen.` | Abrechnung als Drama, aber lesbar |
| SC-10 | Story 20:00 Fix | `Jeder Buchungsposten trägt die pro Transaktion kalkulierte Künstler-/Studio-Verteilung.` | `Jeder Buchungsposten trägt die pro Transaktion kalkulierte Künstler:in-/Studio-Aufteilung. Checkout sperrt, Monatsabschluss überträgt den Saldo, Monat sperrt. Für Steuerberater:innen: druckbarer Bericht EN/DE.` | Abrechnung für Einsteiger:innen |
| SC-11 | Story 22:15 Title | `Totes Wi-Fi, lautes Studio.` | `Totes WLAN, lautes Studio.` | verständlich, handlich, deutsch |
| SC-12 | Story 22:15 Pain | `Ausgerechnet das Handy, das jetzt klingelt ...` | `Ausgerechnet das Handy, das gerade klingelt, erreicht die App nicht.` | natürlicher, weniger sperrig |
| SC-13 | Story 22:15 Fix | `Es ist eine PWA: auf den Home-Bildschirm installiert ...` | `Eine PWA: auf dem Startbildschirm installiert, offline lauffähig, synchronisiert bei wiederhergestellter Verbindung.` | PWA für Einsteiger:innen |
| SC-14 | PWA / Punch | `und die App-Icon-Badge zeigt ...` | `Der App-Badge zeigt, was zu erledigen ist. Push-Stufen steuert jede:r Künstler:in selbst: Das Handy darf piepen — so laut, so selte, so sinnvoll.` | Feature-Highlight mit charmantem Unterton |
| SC-15 | Pillars Intro | `Die vollständige Liste unten ...` | `Die vollständige Liste lässt sich nach Bereich, Status und Rolle filtern. Das sind die Werkzeuge für den Studioalltag.` | Vollständigkeit und Übersicht |
| SC-16 | Pillar Buchen | `Der Kunde bekommt einen geführten Weg` | `Kund:in bekommt einen geführten Buchungsprozess` | Kundenperspektive, nicht Kundenverwirrung |
| SC-17 | Pillar Teamkalender | `Du siehst nur deine eigene Ansicht ...` | `Du siehst rollengerecht, was dich betrifft: eigene Termine, Abwesenheiten mit Grund, Pufferzeiten pro Stuhl — damit sich nichts überschneidet.` | Rollen und Rechte |
| SC-18 | Pillar Finanzen | `Kommissionen werden automatisch zwischen Shop und Artist aufgeteilt` | `Honoraranteile werden automatisch zwischen Studio und Künstler:in aufgeteilt. Jede Abrechnung ist einzeln einsehbar — pro Person oder fürs ganze Studio — bis hin zum gesperrten, druckbaren Monatsabschluss.` | Fachsprache verständlich |
| SC-19 | Pillar Kunden | `Live-Statistiken zu No-Shows und Bindung` | `Live-Kennzahlen zu No-Shows und Kundenbindung` | Kundenbindung konkret |
| SC-20 | Pillar PWA | `Push-, In-App- und E-Mail-Trigger für jedes Event, das zählt ...` | `Push-, In-App- und E-Mail-Trigger für jedes Event — mit Stufen, damit nicht jedes Handy ununterbrochen piept.` | weniger ist mehr |
| SC-21 | Pillar Admin | `Anamnese und Einverständniserklärungen werden erledigt ...` | `Anamnese und Einverständnis sind vor dem Termin erledigt — nicht am Stuhl.` | Zeitersparnis, Schmerzgrenze |
| SC-22 | Differentiator Motiv | `bevor der Kunde den Raum betritt` | `bevor die Kundin oder der Kunde am Stuhl sitzt` | Zielgruppen-Sicht |
| SC-23 | Differentiator PWA | `die Pieper-Einstellung in der Hand` | `die Benachrichtigungsregeln in der Hand` | verständliche Fachbegriffe |
| SC-24 | Differentiator Kundenbasis | `Eine social-first-Kundenbasis` | `Eine Social-first-Kundenbasis` | Adjektivschreibung bei englischen Bestandteilen |
| SC-25 | Inventory Intro | `Filter nach Bereich, Status oder Rolle, oder suche eine bestimmte Funktion.` | `Filter nach Bereich, Status und Rolle — oder suche eine bestimmte Funktion.` | Übersichtlichkeit |
| SC-26 | Feature #1 | `Ersetzt das mühsame Hin und Her per Direktnachricht` | `Ersetzt das mühsame Hin und Her per Chat` | natürlich, einfach, klar |
| SC-27 | Feature #3 | `So wird nie derselbe Stuhl oder dieselbe Person doppelt gebucht` | `So wird nie derselbe Stuhl oder dieselbe Person doppelt gebucht — ein Konflikt fällt sofort auf.` | sofort und verständlich |
| SC-28 | Feature #57 | `Der wirkungsvollste Hebel gegen No-Shows.` | `Der wirksamste Hebel gegen No-Shows.` | „wirksam“ statt „wirkungsvoll“ |

---

## 4. Empfohlene Neufassung der wichtigsten Textblöcke

### 4.1 Hero

**Empfohlene Fassung:**

> **Vorbei mit unübersichtlicher Zettelwirtschaft.**  
> Team Calendar ist der Kalender für Tattoo-Studios: geführte Kundenbuchung, Stuhl-Planung mit Konfliktprüfung, Honorarabrechnung ohne Zahlen-Chaos und eine PWA, die auch ohne WLAN weiterläuft.

**Warum besser:** Die Zielgruppe erkennt in fünf Sekunden, wen die App anspricht, welches Problem sie löst und worin der Nutzen besteht.

### 4.2 CTA-Paare

| Alt | Neu | Begründung |
|---|---|---|
| `Einen Tag miterleben` | `Einen Studio-Tag miterleben` | konkreter, bildlicher |
| `Alle 81 Funktionen` | `Alle 81 Funktionen entdecken` | Handlungsanreiz |
| `Einen Tag miterleben ↓` | `Studio-Tag live erleben ↓` | lockere Tonalität |

### 4.3 „Ein Tag im Studio“ — USP-Story

**Einleitung:**

> **Fünf Momente, in denen Studios auf Glück hoffen.**  
> Jeder dieser Punkte kostet Zeit, Geld oder Nerven. Team Calendar macht sie planbar.

**09:41 — Verschieben ohne Chat-Chaos:**

> Kund:in tippt auf einen sicheren Einmal-Link — ohne Login, ohne App. Team Calendar prüft echte Arbeitszeiten, Abwesenheiten und Verschiebe-Fenster. Das Studio legt die Regeln fest.

**11:05 — Ein Stuhl, zwei Künstler:innen:**

> Stühle sind buchbare Ressourcen mit eigener Kapazität und Puffer. Die Konfliktprüfung läuft pro Stuhl — bevor ein Termin angenommen wird.

**14:30 — Motivvorlage am Termin:**

> Motive und Vorher-/Nachher-Bilder sind fest am Termin. Automatisch komprimiert, im anstehenden Kalender sichtbar. Was gezeichnet wird, ist vor dem Termin klar.

**20:00 — Abrechnung, aber sicher:**

> Die pro Transaktion kalkulierte Künstler:in-/Studio-Aufteilung wird mitprotokolliert. Checkout sperrt, Monatsabschluss überträgt den Saldo, Monat sperrt. Für die Buchhaltung: druckbarer Bericht EN/DE.

**22:15 — PWA, offline, Push:**

> Eine PWA: auf dem Startbildschirm installiert, offline lauffähig, synchronisiert bei wiederhergestellter Verbindung. Der App-Badge zeigt, was zu erledigen ist. Push-Stufen steuert jede:r Künstler:in selbst.

### 4.4 Toolkit / Pillars — USP in einem Satz

| Bereich | USP |
|---|---|
| Buchen | „Geführte Buchung statt Chat-Discussion.“ |
| Teamkalender | „Stuhl statt Irrtum, Termine statt Fehler.“ |
| Finanzen | „Die Abrechnung rechnet, die Zahlen stimmen.“ |
| Kunden | „Aus einem Danke nach dem Besuch wird eine Wiederholungsbuchung.“ |
| PWA | „Offline nicht offline — sondern nur vertagt.“ |
| Multi-Tenant | „Ein Login, mehrere Studios, keine Verwirrung.“ |
| Admin | „Von Anfang an klar, für alle Beteiligten.“ |

### 4.5 Unterschied / Features

> **Was andere Tools nicht haben:** Team Calendar bucht nicht nur Menschen, sondern auch Stühle. Mit Motivvorlage am Termin, Honoraranteil pro Transaktion, PWA offline und sicherem Einmal-Link.

---

## 5. Direkte Antworten für die Zielgruppe

Diese Fragen sollten auf der Seite sichtbar, klar und ohne Umwege beantwortet werden.

### 5.1 Zeitmanagement

**Frage:** Spart die App wirklich Zeit?

**Antwort:** Ja. Der Kalender ersetzt Papier, Chat und Zettel. Termine, Abwesenheiten, Pufferzeiten und Stühle laufen dort zusammen, was zusammengehört.

### 5.2 Doppelbuchungen

**Frage:** Wie wird verhindert, dass zwei Künstler:innen denselben Stuhl bekommen?

**Antwort:** Arbeitsplätze sind eigene buchbare Ressourcen. Team Calendar prüft Stuhl, Künstler:in, Arbeitszeiten und Abwesenheiten, bevor ein Termin angenommen wird.

### 5.3 No-Shows

**Frage:** Was tun gegen No-Shows?

**Antwort:** Geführte Buchung, Terminstatus, Warteliste, geplante Erinnerungen und Anzahlungen. Im Roadmap-Bereich sind automatische 24-h/1-h-Erinnerungen und Stripe-Anzahlungen vorgesehen.

### 5.4 Abrechnung

**Frage:** Wie rechne ich Honorare ab?

**Antwort:** Pro Transaktion automatisch. Mit Checkout, Saldo, Monatsabschluss, Sperre und druckbarem Bericht EN/DE.

### 5.5 Motivvorlagen

**Frage:** Wo sehe ich die Vorlage vor dem Termin?

**Antwort:** Direkt am Termin. Kund:innen oder Team laden Motive hoch. Bilder werden automatisch komprimiert und sind im Kalender sichtbar.

### 5.6 WLAN

**Frage:** Was passiert, wenn die Verbindung weg ist?

**Antwort:** Die App ist eine PWA. Sie läuft offline, speichert lokal und synchronisiert bei wiederhergestellter Verbindung.

### 5.7 Kundenbuchung

**Frage:** Können Kund:innen selbst buchen oder verschieben?

**Antwort:** Ja — geführte Buchung und sicherer Einmal-Link, ohne Login, ohne App-Installation.

### 5.8 Multi-Studio

**Frage:** Kann ich mehrere Studios führen?

**Antwort:** Ja, mit einem Konto. Tenants bleiben strikt getrennt, Zeitzone und Währung je Standort werden berücksichtigt.

---

## 6. Was korrekt ist und nicht korrigiert werden sollte

Einige Begriffe wirken auf den ersten Blick falsch, sind aber korrekt und sollten nicht „repariert“ werden.

| Begriff | Status | Anmerkung |
|---|---|---|
| `Benachrichtigungen` | korrekt | Rechtschreibung: `Benachricht` + `igungen`. Kein „Benachricht“. |
| `verliert` | korrekt | Kommt von „verlieren“: „die Abrechnung verliert nie den Überblick“. |
| `Teamkalender` | korrekt | Zusammengesetzte Substantivierung: Team + Kalender. |
| `traut` | korrekt | „Traut niemand den Zahlen“ ist die korrekte Form von „trauen“. |
| `einzeln` | korrekt | „einzeln“ schreibt sich mit einem h. |
| `i18n` | korrekt | Abkürzung für Internationalization, nicht „i18n“. |

---

## 7. Umsetzungs-Hinweise

### 7.1 Nur Text, kein Code-Pfusch

Diese Datei ist ein Korrekturbericht. Die Korrekturen können direkt in den Quelldateien umgesetzt werden:

- `src/data/tour.de.ts`
- `src/data/features.de.json`
- ggf. `src/components/TourPage.astro` für die Doppelpunkt-Korrektur in der Notiz-Renderung
- ggf. `src/utils/text.ts` für Statuslabels

### 7.2 Empfohlener Workflow

```bash
node scripts/parse-inventory.mjs
node scripts/check-i18n.mjs
npm run build
node scripts/verify-i18n-dist.mjs
```

### 7.3 Qualitätscheck vor Commit

- Rechtschreibung: alle harten Korrekturen übernommen.
- Grammatik: Kasus, Kongruenz, Kommas, Partizipien geprüft.
- Sinnlichkeit: Zielgruppe kann, Zielgruppe versteht.
- Tonalität: locker, professionell, nicht lehrerhaft.
- USPs: klar, deutlich, gemeint.

---

## 8. Fazit: Das ist das Wichtigste

Die Zielgruppe will keine Feature-Liste, sondern einen Weg durch den Studio-Alltag. Die Texte sollten nicht fragen: „Was hat die App?“ — sondern sagen: „Was machst du mit der App?“

**Drei Sätze für die Startseite:**

1. **Vorbei mit unübersichtlicher Zettelwirtschaft.**
2. **Stuhl gebucht, Konflikt gecheckt, Abrechnung geregelt.**
3. **Motiv sichtbar, Kunde informiert, Studio organisiert.**
