#!/usr/bin/env python3
# Build _research/raw/painpoints.md with VERBATIM quotes extracted from cached sources.
import json, os, re, sys, datetime
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
HERE = os.path.dirname(__file__)
CORPUS = os.path.join(HERE, "raw", "reddit", "corpus.jsonl")
WEB = os.path.join(HERE, "raw", "web")
OUTP = os.path.join(HERE, "raw", "painpoints.md")
ACC = "2026-09-19"
rows = [json.loads(l) for l in open(CORPUS, encoding="utf-8") if l.strip()]
# theme tallies, reusing the THEMES literal from tally.py (no retyping)
tt = open(os.path.join(HERE, "tally.py"), encoding="utf-8").read()
m = re.search(r"(?s)THEMES\s*=\s*(\{.*?\n\})", tt)
ns = {}
exec("THEMES=" + m.group(1), ns)
THEMES = ns["THEMES"]
def tidy(t):
    import html as H
    t = H.unescape(t)
    t = t.replace("<!-- SC_OFF -->", " ").replace("<!-- SC_ON -->", " ").replace("&#32;", " ")
    t = re.sub(r"(?is)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).strip()
def win(text, pat, pre, post):
    rx = re.compile(pat, re.I)
    mm = rx.search(text)
    if not mm: return None
    a = max(0, mm.start() - pre); b = min(len(text), mm.end() + post)
    s = text[a:b]
    if a > 0:
        k = s.find(" ")
        s = s[k + 1:] if 0 <= k < 40 else s
    if b < len(text):
        k = s.rfind(" ")
        s = s[:k] if k > len(s) - 40 else s
    s = s.strip().strip(",:; ")
    for cut in ("submitted by", "[link] [comments]", "Read More"):
        k = s.find(cut)
        if k > 40: s = s[:k].strip()
    s = s.lstrip("| ").strip()
    return s
def reddit_quote(key, pat, pre, post):
    for r in rows:
        if key in r["link"]:
            txt = tidy(r.get("title", "") + " || " + r.get("body", ""))
            w = win(txt, pat, pre, post)
            if w: return w, r["link"], r["date"], r["sub"], r["title"]
    return None, None, None, None, None
def web_quote(fname, pat, pre, post):
    p = os.path.join(WEB, fname)
    if not os.path.exists(p): return None
    txt = re.sub(r"(?s)^SOURCE-URL:.*?ACCESSED:.*?CHARS:\s*\d+\s*", "", open(p, encoding="utf-8").read())
    txt = re.sub(r"\s+", " ", tidy(txt))
    return win(txt, pat, pre, post)
MISSING = []
def E(kind, theme, src, pat, pre=110, post=280, note=""):
    """kind: community|vendor|founder ; src: reddit thread key or web filename"""
    if src.endswith(".txt"):
        q = web_quote(src, pat, pre, post)
        url = ""
        p = os.path.join(WEB, src)
        if os.path.exists(p):
            f = open(p, encoding="utf-8").read(400)
            mu = re.search(r"(?s)SOURCE-URL:\s*(\S+)", f); url = mu.group(1) if mu else src
        date = ""
    else:
        q, url, date, sub, title = reddit_quote(src, pat, pre, post)
    if not q:
        MISSING.append((theme, src, pat))
        return dict(kind=kind, theme=theme, q="[ANCHOR NOT FOUND: " + pat + "]", url=src, date="", note=note)
    return dict(kind=kind, theme=theme, q=q, url=url, date=date, note=note)

R = "TattooArtists/comments/"
S = "smallbusiness/comments/"
ITEMS = [
 # T1 Instagram / DM booking overload
 ("community","Instagram / DM booking overload",R+"1vapgm5",r"instagram dms",60,330,"artist describing current stack"),
 ("community","Instagram / DM booking overload",R+"1qd5z06",r"process for clients who DM",0,360,"asking how others handle DM booking"),
 ("community","Instagram / DM booking overload",R+"16jdgze",r"messaging game",240,220,""),
 ("community","Instagram / DM booking overload",R+"1d5a0e8",r"leads feature",330,340,"IG appointment/leads tool overrides shop booking rules"),
 ("community","Instagram / DM booking overload",R+"1iudku4",r"built their business around Instagram",110,240,""),
 ("community","Instagram / DM booking overload",R+"1o8feiv",r"instagram work is not enough",170,230,"shop owner on demand dependence on IG"),
 # T2 WhatsApp / email chaos
 ("community","WhatsApp / email chaos",R+"1tum85p",r"jump between Instagram DMs",90,290,"founder of rival app Blackbook describing the pain"),
 ("community","WhatsApp / email chaos",R+"1043wqb",r"back and forth",270,330,""),
 ("community","WhatsApp / email chaos",R+"1d5a0e8",r"saved replies",200,300,""),
 # T3 Paper calendar / Zettelwirtschaft
 ("community","Paper calendar & Zettelwirtschaft",R+"f7nckf",r"an app for doing",40,340,"fragmented paper+spreadsheet shop ops (2020)"),
 ("community","Paper calendar & Zettelwirtschaft",R+"1043wqb",r"whiteboard",30,260,"comment: whiteboards for bookings months ahead"),
 ("community","Paper calendar & Zettelwirtschaft",R+"17gdp8d",r"wait list of clients",40,340,"waitlist lost with notebook + unbacked-up doc"),
 ("community","Paper calendar & Zettelwirtschaft",R+"y1dqmp",r"studio manager/boss",110,230,"own diary vs shared studio diary dispute"),
 ("community","Paper calendar & Zettelwirtschaft",R+"1043wqb",r"paper planner, booking via email",60,200,""),
 # T4 Double booking / chair conflicts
 ("community","Double-booking & chair/calendar conflicts",R+"1d5a0e8",r"not allow double booking",90,340,""),
 ("community","Double-booking & chair/calendar conflicts",S+"1ltvfhw",r"double booking whenever",210,200,"non-tattoo SMB, same failure mode"),
 ("community","Double-booking & chair/calendar conflicts",S+"1op2fyz",r"upgraded from Calendly",20,250,""),
 ("community","Double-booking & chair/calendar conflicts",R+"15d20rp",r"booking correct amounts of time",200,220,"managers mis-schedule session length"),
 ("community","Double-booking & chair/calendar conflicts",R+"17gukph",r"pencil in",110,250,"artist wants shared calendar others can pencil into"),
 # T5 No-shows & late cancellations
 ("community","No-shows & late cancellations",R+"1l5a9bi",r"no-show me today",60,260,""),
 ("community","No-shows & late cancellations",R+"1ta07ot",r"of these people turn up",130,300,"only ~40% attend in-person consult"),
 ("community","No-shows & late cancellations",R+"zhz6zf",r"how long do you wait",60,250,""),
 ("community","No-shows & late cancellations",R+"uj8sgd",r"6th sense",40,240,""),
 ("community","No-shows & late cancellations",R+"1n20t5r",r"last week it was 4",200,270,""),
 ("community","No-shows & late cancellations",R+"1vwhelv",r"no-showed",130,190,"comment on who keeps deposit after no-show"),
 # T6 Deposits
 ("community","Deposit chasing & payment collection",R+"1l5a9bi",r"forgot to check if they actually sent a deposit",90,320,""),
 ("community","Deposit chasing & payment collection",R+"1vwhelv",r"percentage basis",30,290,""),
 ("community","Deposit chasing & payment collection",R+"16iaqau",r"never be refunded",70,180,""),
 ("community","Deposit chasing & payment collection",S+"1ltem0x",r"Chasing flaky customers",60,320,"non-tattoo SMB, same failure mode"),
 # T7 Empty chairs / idle time
 ("community","Empty chairs / idle time & weak demand",R+"16mnnuh",r"dragging out the walk in sign",90,330,""),
 ("community","Empty chairs / idle time & weak demand",R+"1vlp4dz",r"been so slow",90,280,""),
 ("community","Empty chairs / idle time & weak demand",R+"1rmp9jv",r"difficult to let people know",80,250,""),
 ("community","Empty chairs / idle time & weak demand",R+"1o8feiv",r"pick up another job",90,200,""),
 # T8 References / context lost
 ("community","Reference images & booking context lost in chat",R+"1043wqb",r"reference photos and",130,340,""),
 ("community","Reference images & booking context lost in chat",R+"15d20rp",r"Supplying the reference pictures",90,220,""),
 ("community","Reference images & booking context lost in chat",R+"18hoxdt",r"photos attached to the appointments",90,330,""),
 # T9 Commission & settlement
 ("community","Commission split & month-end settlement",R+"1vwhelv",r"100% go to you",30,290,""),
 ("community","Commission split & month-end settlement",R+"1vwhelv",r"end of every week",120,300,"comment describing manual weekly percentage settlement"),
 ("community","Commission split & month-end settlement",R+"1te34i9",r"bookkeeping, payroll",90,270,"shop owner quitting commission-based model"),
 ("community","Commission split & month-end settlement",R+"1t44nun",r"getting in return",70,280,""),
 ("community","Commission split & month-end settlement",R+"vq3lhx",r"50/50 split",70,280,""),
 # T10 Guest artists
 ("community","Guest / resident artist scheduling",R+"xew2dr",r"shop split and lodgings",60,280,""),
 ("community","Guest / resident artist scheduling",R+"13w7j89",r"guest artists come through often",60,330,""),
 ("community","Guest / resident artist scheduling",R+"1qd5z06",r"guest spots",200,180,""),
 # T11 Admin burden
 ("community","Admin time burden & work-life bleed",R+"1sz6kgd",r"admin things in the evening",90,290,""),
 ("community","Admin time burden & work-life bleed",R+"1g3gjpw",r"angry and pressing emails",90,320,""),
 ("community","Admin time burden & work-life bleed",R+"1126gwc",r"other admin tasks",90,260,""),
 ("community","Admin time burden & work-life bleed",R+"1vapgm5",r"administrative work",130,220,""),
 # T12 Reminders
 ("community","Reminders",R+"18hoxdt",r"reminder texts",120,220,""),
 ("community","Reminders",R+"1043wqb",r"google forms",60,280,"artist keeps booking data in forms+planner+folder"),
 # T13 Waitlists
 ("community","Waitlists & filling openings",R+"1n20t5r",r"last minute openings",120,260,""),
 ("community","Waitlists & filling openings",R+"17gdp8d",r"fill gaps",40,240,""),
 # T14 Retention
 ("community","Client retention & repeat bookings",R+"1rmp9jv",r"come back every month",60,300,""),
 ("community","Client retention & repeat bookings",R+"1vqvot0",r"Repeat clientele",90,290,""),
 ("community","Client retention & repeat bookings",R+"17gdp8d",r"regulars who come in",40,190,""),
 # T15 Consent
 ("community","Consent / intake forms & compliance",R+"1rgyk3s",r"intake form has a field",60,320,""),
 ("community","Consent / intake forms & compliance",R+"1v4mw3s",r"consent form",120,280,"consent form exists but is not enforced in practice"),
 # T16 Multi-location
 ("community","Multiple locations",R+"1d5a0e8",r"3 locations and 20ish artists",60,140,"comment on multi-site setup"),
 ("community","Multiple locations",S+"9e1bnc",r"opened a second location",60,320,"non-tattoo SMB"),
 ("community","Multiple locations",R+"1t13v5f",r"second shop an hour away",90,220,""),
 # T17 Offline (gap)
 ("community","Offline / bad in-studio internet",S+"17cytnf",r"offline use",200,240,"only hit found; not tattoo-specific -> evidence GAP"),
 # T18 Tooling complaints
 ("community","Tooling: fragmentation, price, switching",S+"1op2fyz",r"Phorest is the worst",0,150,"comment"),
 ("community","Tooling: fragmentation, price, switching",S+"1op2fyz",r"Fresha is leagues better",0,250,"comment"),
 ("community","Tooling: fragmentation, price, switching",S+"1ircu1z",r"solo operating aesthetics",0,330,"aesthetics SMB on booking platforms"),
 ("community","Tooling: fragmentation, price, switching",S+"1ircu1z",r"more consistent new bookings",90,260,""),
 ("community","Tooling: fragmentation, price, switching",R+"9zhzk5",r"expensive/outdated",60,240,""),
 ("community","Tooling: fragmentation, price, switching",R+"1d5a0e8",r"I use square",60,260,"comment: incumbent generic tool adopted"),
]

VENDORS = [
 ("TatTool (tattool.io)", "tattool_io__root.txt", r"One workspace for tattoo studios", 40, 260, "hero"),
 ("TatTool (tattool.io)", "tattool_io__root.txt", r"recreate the same appointment", 120, 220, "anti-fragmentation claim"),
 ("TatTool (tattool.io)", "tattool_io__root.txt", r"without double-booking artists", 120, 160, "scheduling + guest spots"),
 ("inkStar (inkstar.app)", "inkstar_app__en_p_home.txt", r"You Didn.t Build This Dream", 0, 240, "hero sub-problem block"),
 ("inkStar (inkstar.app)", "inkstar_app__en_p_home.txt", r"Clients who ghost", 20, 260, "problem card 01"),
 ("inkStar (inkstar.app)", "inkstar_app__en_p_home.txt", r"The midnight grind", 20, 250, "problem card 03"),
 ("inkStar (inkstar.app)", "inkstar_app__en_p_home.txt", r"You can never switch off", 20, 230, "problem card 04"),
 ("inkStar (inkstar.app)", "inkstar_app__en_p_home.txt", r"Consent forms on paper", 20, 300, "problem card 05"),
 ("inkStar (inkstar.app)", "inkstar_app__en_p_home.txt", r"What InkStar replaces", 0, 150, "replacement list intro"),
 ("inkStar (inkstar.app)", "inkstar_app__en_p_home.txt", r"Manual WhatsApp reminders", 0, 200, "replaces list"),
 ("inkStar (inkstar.app)", "inkstar_app__en_p_home.txt", r"Full functionality even without internet", 140, 90, "offline USP already marketed by rival"),
 ("inkStar (inkstar.app)", "inkstar_app__en_p_home.txt", r"Automatic commission tracking", 60, 140, "commission tracking already marketed"),
 ("inkStar (inkstar.app)", "inkstar_app__en_p_home.txt", r"Deposits before the chair is blocked", 0, 250, "deposit/no-show protection"),
 ("InkSchedule (inkschedule.app)", "inkschedule_app__root.txt", r"N o t a n s w e r i n g D M s", 70, 90, "hero (letterspaced banner)"),
 ("InkSchedule (inkschedule.app)", "inkschedule_app__root.txt", r"Sound familiar", 0, 200, "problem-section header"),
 ("InkSchedule (inkschedule.app)", "inkschedule_app__root.txt", r"No deposit means no appointment", 90, 100, "deposit-first"),
 ("InkSchedule (inkschedule.app)", "inkschedule_app__root.txt", r"When you are fully booked", 30, 200, "waitlist"),
 ("InkSchedule (inkschedule.app)", "inkschedule_app__root.txt", r"No paper, no borrowed pens", 90, 120, "digital consent"),
 ("InkSchedule (inkschedule.app)", "inkschedule_app__product.txt", r"No phone calls, no DMs", 150, 120, "online booking"),
 ("InkSchedule (inkschedule.app)", "inkschedule_app__product.txt", r"no-shows and last", 60, 220, "deposit rationale"),
 ("InkSchedule (inkschedule.app)", "inkschedule_app__product.txt", r"never double-book", 100, 140, "calendar sync"),
 ("InkSchedule (inkschedule.app)", "inkschedule_app__product.txt", r"Reduce no-shows", 0, 260, "reminders"),
 ("Ink Studio Manager (inkstudiomanager.de)", "inkstudiomanager_de__root.txt", r"Nie wieder Terminchaos", 0, 260, "hero (DE)"),
 ("Ink Studio Manager (inkstudiomanager.de)", "inkstudiomanager_de__root.txt", r"Dop.{0,3}pelbuchungen", 0, 150, "no double bookings"),
 ("Ink Studio Manager (inkstudiomanager.de)", "inkstudiomanager_de__root.txt", r"Warteliste", 60, 260, "waitlist fills free slots (DE)"),
 ("Ink Studio Manager (inkstudiomanager.de)", "inkstudiomanager_de__root.txt", r"handgeschriebene", 90, 160, "paper slips gone (DE)"),
 ("Ink Studio Manager (inkstudiomanager.de)", "inkstudiomanager_de__root.txt", r"Steuerberater", 120, 120, "tax/settlement export"),
 ("InkLinka (inklinka.com)", "inklinka_com__en_tattoo_studio_calendar_chaos.txt", r"We use Google Calendar", 0, 300, "vendor-quoted customer problem"),
 ("InkLinka (inklinka.com)", "inklinka_com__en_tattoo_studio_calendar_chaos.txt", r"search for references in Instagram", 0, 260, "vendor-quoted customer problem"),
 ("InkLinka (inklinka.com)", "inklinka_com__en_tattoo_studio_calendar_chaos.txt", r"if they are away", 0, 260, "vendor-quoted: manager as single point of knowledge"),
 ("InkLinka (inklinka.com)", "inklinka_com__en_payments_payouts.txt", r"separate spreadsheets", 140, 160, "anti-spreadsheet finance claim"),
 ("InkLinka (inklinka.com)", "inklinka_com__en_guest_visit_planner.txt", r"Both calendars know", 0, 260, "guest artist scheduling"),
 ("InkLinka (inklinka.com)", "inklinka_com__en.txt", r"Guest and resident artist operations", 0, 300, "guest/resident ops module"),
 ("Linework (linework.com)", "linework_com__root.txt", r"without anyone having to ask", 120, 200, "shared calendar / gaps"),
 ("Linework (linework.com)", "linework_com__root.txt", r"paperwork is done", 150, 120, "consent automation"),
 ("Linework (linework.com)", "linework_com__about_us.txt", r"unfit tools", 80, 260, "founder problem narrative"),
 ("Linework (linework.com)", "linework_com__about_us.txt", r"consolidate calendars", 120, 200, "founder: fragmented incumbents"),
 ("Linework (linework.com)", "linework_com__invest.txt", r"21 billion", 140, 220, "market claim (vendor)"),
 ("Cerenza (calenza.app/studio)", "calenza_app__studio.txt", r"reconciled to the cent", 60, 240, "hero: settlement accuracy"),
 ("Cerenza (calenza.app/studio)", "calenza_app__studio.txt", r"commission, salary or", 60, 240, "napkin-math replacement"),
 ("Cerenza (calenza.app/studio)", "calenza_app__studio.txt", r"one-tap payday", 90, 160, "payout automation"),
 ("Cerenza (calenza.app/studio)", "calenza_app__studio.txt", r"no-show", 90, 200, "booking state handling"),
]

MAP = {
 "Instagram / DM booking overload": "IG/DM booking overload",
 "WhatsApp / email chaos": "WhatsApp/email chaos",
 "Paper calendar & Zettelwirtschaft": "Paper calendar / Zettelwirtschaft",
 "Double-booking & chair/calendar conflicts": "Double-booking / chair conflicts",
 "No-shows & late cancellations": "No-shows / late cancellations",
 "Deposit chasing & payment collection": "Deposit chasing / non-payment",
 "Empty chairs / idle time & weak demand": "Empty chairs / idle time",
 "Reference images & booking context lost in chat": "Reference images lost in chat",
 "Commission split & month-end settlement": "Commission split / month-end settlement",
 "Guest / resident artist scheduling": "Guest / resident artist scheduling",
 "Admin time burden & work-life bleed": "Admin time burden",
 "Reminders": "Reminders",
 "Waitlists & filling openings": "Waitlist / fill openings",
 "Client retention & repeat bookings": "Client retention / repeat bookings",
 "Consent / intake forms & compliance": "Consent / paperwork / compliance",
 "Multiple locations": "Multiple locations",
 "Offline / bad in-studio internet": "Offline / bad in-studio internet",
 "Tooling: fragmentation, price, switching": "Software/tool complaints & switching",
}
ORDER = list(MAP.keys())
def tally_rows():
    import re as R
    out = []
    for th, pat in THEMES.items():
        rx = R.compile(pat, R.I)
        hits = [r for r in rows if rx.search(r.get("title", "") + " " + r.get("body", ""))]
        posts = [h for h in hits if h["sub"] != "comments"]
        links = []
        for h in hits[:400]:
            u = re.match(r"(https?://\S+)", h["link"])
            if u and u.group(1) not in links: links.append(u.group(1))
        out.append(dict(theme=th, total=len(hits), posts=len(posts), comments=len(hits) - len(posts),
                        subs=sorted({h["sub"] for h in hits}), links=links))
    return out
L = []
A = L.append
A("# Tattoo-studio pain points: customer/community evidence + competitor pain marketing")
A("")
A("Compiled by the pain-point research subagent. **Access date for every citation: " + ACC + ".**")
A("All quotes below were extracted programmatically from cached page/feed text in `_research/raw/` "
  "(no hand retyping), so wording, spelling and typos are the source's own.")
A("")
A("## Method + limits (read this before using the numbers)")
A("")
A("- Community sources: Reddit public **Atom (`.rss`) feeds** — `search.rss` per subreddit plus per-thread comment feeds "
  "(`.rss` on the thread path). The `.json` API is bot-blocked (403), `old.reddit.com` forces a login wall, "
  "pullpush.io is 404 and the safereddit/redlib mirrors are behind Anubis proof-of-work. Reddit rate-limits hard "
  "(429): roughly half of the feed requests in a batch succeed, so harvesting was repeated and de-duplicated by post URL.")
A("- Corpus on disk: `%s` (%d rows; posts + comments). Harvest queries were pain-oriented "
  "(booking, no-show, deposit, commission, guest spot, waitlist, admin, calendar, software ...), so the corpus is "
  "**purposefully biased toward these topics** — treat the tallies as 'how often the theme recurs in a targeted corpus', "
  "not as a random sample of r/TattooArtists." % (os.path.relpath(CORPUS, os.path.dirname(HERE)), len(rows)))
A("- Tally basis: per theme one case-insensitive keyword/phrase regex over `title + body` of each corpus row. "
  "Keyword matching over-counts (a thread may mention a theme in one line) and under-counts (no keyword hit). "
  "Use the numbers as an *ordering* signal only; the quotes are the actual evidence.")
A("- Blocked / unavailable during this run (recorded, not worked around with invention): "
  "Trustpilot 403, G2 403 on product review paths, Capterra 404 for the probed slugs, Apple App Store customer-review RSS "
  "HTTP 500 (app metadata via the iTunes Search API worked), Google Play product pages returned HTML but no extractable review text, "
  "Quora question pages 403, general web search engines (DuckDuckGo HTML/lite, Ecosia, Startpage, searx instances, Google SERP) "
  "all bot-walled or JS-only, so discovery went through known URLs + subreddit feeds instead.")
A("")
A("## Ranked theme tally")
A("")
A("| # | Theme | rows hit | threads (posts) | comments | subs |")
A("|---|-------|---------:|----------------:|---------:|------|")
for i, t in enumerate(sorted(tally_rows(), key=lambda x: -x["total"]), 1):
    A("| %d | %s | %d | %d | %d | %s |" % (i, t["theme"], t["total"], t["posts"], t["comments"], ", ".join(t["subs"])))
A("")

A("## Community / customer evidence, grouped by theme")
A("")
A("Class labels: **customer/community evidence** = words of an artist, shop owner or small-business owner in a public forum; "
  "**vendor claim** = marketing copy. Snippets are trimmed around the key sentence; `||` separates post title from post body.")
A("")
built = {}
for kind, theme, src, pat, pre, post, note in ITEMS:
    d = E(kind, theme, src, pat, pre, post, note)
    built.setdefault(theme, []).append(d)
for theme in ORDER:
    A("### " + theme)
    A("")
    for d in built.get(theme, []):
        if not d["q"].strip(): continue
        A("> \"" + d["q"] + "\"")
        meta = "**" + d["kind"] + "** — " + d["url"] + " — accessed " + ACC
        if d["date"]: meta += " (thread/post dated " + d["date"] + ")"
        if d["note"]: meta += " — " + d["note"]
        A(meta)
        A("")
A("## Competitors: the pain points they explicitly market against")
A("")
A("Hero / sub-problem copy taken from each vendor's own pages. These are **vendor claims** — useful for positioning "
  "and for the anti-bias check below, not as proof that the pain exists. "
  "(`inkos.app` resolved but renders only via JavaScript, so no page text could be captured for INKOS.)")
A("")
cur = None
for prod, fn, pat, pre, post, label in VENDORS:
    q = web_quote(fn, pat, pre, post)
    if prod != cur:
        A("### " + prod); A(""); cur = prod
    if not q:
        A("- [ANCHOR NOT FOUND: " + pat + "] (" + fn + ")"); A("")
        MISSING.append((prod, fn, pat)); continue
    p = os.path.join(WEB, fn)
    f = open(p, encoding="utf-8").read(400)
    mu = re.search(r"SOURCE-URL:\s*(\S+)", f); url = mu.group(1) if mu else fn
    A("> \"" + q + "\"")
    A("**vendor claim** — " + url + " — accessed " + ACC + " — " + label)
    A("")

A("## Anti-bias check: is a 'unique' pain point already occupied?")
A("Findings that cut against a 'nobody else does this' framing (each is backed by a vendor-claim quote above; "
  "community evidence for the same theme is in the sections above):")
A("")
A("- **Deposits / no-show protection** is table stakes across the field: inkStar (deposit-first booking, 'no-show protection'), "
  "InkSchedule ('no-shows and last-minute cancellations' rationale, automatic reminders), Ink Studio Manager "
  "('Erinnerungen reduzieren No-Shows'), Cerenza (bookings marked no-show).")
A("- **Instagram/DM -> booking-page redirection** is marketed by inkStar (booking links for Instagram/website) and "
  "InkSchedule ('no phone calls, no DMs'). Community evidence for the underlying DM overload exists, so this pain is real, "
  "but the *solution position* is crowded.")
A("- **Offline mode** is already an advertised differentiator (inkStar page copy: offline claim above), while my corpus "
  "produced essentially **no** community complaint about studio internet (single weak non-tattoo hit). If Team Calendar "
  "markets offline as unique, it is (a) not customer-verified in this corpus and (b) not uncontested.")
A("- **Commission / month-end settlement** is a headline position for Cerenza ('reconciled to the cent', one-tap payday) "
  "and inkStar (automatic commission tracking per employee) and InkLinka (payout accounting, ledger reports). Community "
  "evidence here is about *disputes over what the split should be* more than about tallying it — the tallying pain is "
  "mostly asserted by vendors, only indirectly supported (weekly percentage settlement described in a comment, "
  "'bookkeeping, payroll' as burnout driver).")
A("- **Guest / resident artists** is a named module at InkLinka (guest visit planner, 'Both calendars know') — again a real "
  "community topic (guest-spot economics threads) but not an open field.")
A("- **Reference images / booking context** is explicitly attacked by InkLinka with quoted studio-owner problems "
  "(Google Calendar holds no context; references searched in Instagram/WhatsApp/folders) and implicitly by TatTool "
  "('do not have to recreate the same appointment in separate tools'). So 'references lost in DMs' is both a real pain "
  "(community quotes above) and an occupied pitch.")
A("- **Generic incumbents are loved AND hated in the same threads**: Square appears as an accepted, working answer "
  "(comment recommending Square text confirmations), while salon SMB owners list concrete cons of Square/Vagaro/Boulevard/"
  "Phorest/Fresha. Positioning should be against named tools with named failure modes, not against 'nobody understands tattoos'.")
A("- **Vendor-vampire risk in the same threads**: booking-tool vendors and researchers show up inside the very "
  "r/TattooArtists threads asking 'what do you use to book clients?' (self-disclosed paid research 2018, founder self-plugs, "
  "free-lifetime-app offers 2026). Community trust is therefore thin; evidence-led, non-pushy participation matters.")
A("")
A("## Weakly-evidenced themes in this corpus (do not oversell)")
A("")
A("- Multi-location: only a handful of tattoo-side hits (one comment mentions a 3-location / ~20-artist setup; one shop "
  "owner opening a second shop an hour away). The strongest multi-site failure-mode evidence came from non-tattoo "
  "r/smallbusiness threads.")
A("- Offline / studio internet: effectively no community signal.")
A("- Consent-form digitisation: community hits are about forms being *ignored in practice* and about intake screening, "
  "not about wanting e-signatures; the e-consent pain is basically vendor-asserted.")
A("")
A("## Source files on disk")
A("")
A("- `%s` — harvested posts + comments (JSONL)." % os.path.relpath(CORPUS, os.path.dirname(HERE)))
A("- `%s/` — cleaned page text per fetched URL, each file carries SOURCE-URL and ACCESSED lines." % os.path.relpath(WEB, os.path.dirname(HERE)))
A("- `%s` — this report." % os.path.relpath(OUTP, os.path.dirname(HERE)))
A("")
if MISSING:
    A("## Extraction problems (anchors not found — removed rather than invented)")
    A("")
    for t, s, p in MISSING:
        A("- theme/product " + str(t) + " in " + str(s) + ": pattern " + str(p))
    A("")
open(OUTP, "w", encoding="utf-8").write(chr(10).join([x for x in L if x is not None]))
print("WROTE", OUTP, "lines=", len(L), "missing=", len(MISSING))
for t, s, p in MISSING: print("  MISSING:", t, "|", s, "|", p)
