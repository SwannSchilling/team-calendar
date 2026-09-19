#!/usr/bin/env python3
# Theme tally over the corpus. usage: tally.py
import json, re, os, sys
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
OUT=os.path.join(os.path.dirname(__file__),"raw","reddit","corpus.jsonl")
rows=[json.loads(l) for l in open(OUT,encoding="utf-8") if l.strip()]
def uniq(rows): return rows
THEMES={
 "IG/DM booking overload": r"instagram dm|insta dm|\bdms?\b|instagram (is|messages|booking)|through instagram|via instagram|dm'?s (are|is) (full|insane|chaos)|answ(er|ing) (dm|dms|messages)",
 "WhatsApp/email chaos": r"whatsapp|\bemail\b|e-mails|inbox|messages (back and forth|everywhere)|different apps",
 "Paper calendar / Zettelwirtschaft": r"paper (planner|calendar|diary|book)|pen and paper|handwritten|paper schedule|notebook|zettel|paper form",
 "Double-booking / chair conflicts": r"double.?book|booked (twice|two (clients|appointments))|same (time|slot)|overlapping|clash|conflict(ed)? (with|in) (the )?(calendar|schedul)",
 "Empty chairs / idle time": r"empty chair|no (tattoo )?appointments|slow (season|week|month)|gap(s)? in (my|the) (book|calendar|schedul)|not booked|booked out (is over|no more)|quiet (season|period)|dead (weeks|months)",
 "No-shows / late cancellations": r"no.?show|didn'?t (show|turn up)|never showed|ghost(ed|ing)?\b|cancellat|cancel(ed)? (my|the|last)|last[- ]minute",
 "Deposit chasing / non-payment": r"deposit|down payment|didn'?t pay|never paid|unpaid|balance (due|owed)|chasing (a )?payment",
 "Reference images lost in chat": r"reference (image|photo|picture)s?|inspo|brief|screenshots|images (got|are) (lost|buried)|found (the|a) (reference|photo)|in (the )?(dm|chat|messages) (again|separately)",
 "Commission split / month-end settlement": r"commission|split (is|of|the) (revenue|work)|\b\d{1,2}%|% (take|cut|of the)|payout|pay ?day|settle(ment)?|bookkeep|accountant|tax(?:es)? report|spread ?sheet.*(revenue|commission)",
 "Guest / resident artist scheduling": r"guest spot|guest artist|resident artist|chair rent|rent(?:a|ing)? (a |the )?chair|booth rent",
 "Offline / bad in-studio internet": r"offline|wi-?fi|internet (is |was )?(down|out|bad)|connection (issues|problems|outage)|no internet",
 "Multiple locations": r"multiple (locations|studios|shops)|second (location|studio|shop)|other (location|studio) of ours|all (our )?locations|multi-?location",
 "Client retention / repeat bookings": r"repeat (client|customer|booking)|retention|come back|rebook|re-?book|loyal|lost (a )?client|never (come|came) back",
 "Admin time burden": r"admin|paperwork|paper ?work|book(ing)? (admin|work)|hours? (on|of) (admin|paperwork)|so much (admin|paperwork)|nights.*(admin|answering)|data entry",
 "Consent / paperwork / compliance": r"consent|waiver|health (form|questionnaire)|medical (form|history|intake)|intake form|liabilit|gdpr|hygiene (form|document)|release form",
 "Reminders": r"remind(er|ers|ing)|text (me )?(a )?reminder|appointment reminder|forget (their|the|about) (appointment|their app)",
 "Waitlist / fill openings": r"waitlist|wait ?list|last[- ]minute (opening|slot)|fill (a |the )?(slot|spot|opening)|opening (in my |my )?(schedule|book|calendar)",
 "Software/tool complaints & switching": r"software|app (is|for|that) |platform|subscri(ption|be)|monthly fee|too expensive|migrat|switch(ing)? (to|from)|spread ?sheet",
}
print("corpus rows:",len(rows))
res=[]
for th,pat in THEMES.items():
    rx=re.compile(pat,re.I)
    hits=[r for r in rows if rx.search(r.get("title","")+" "+r.get("body",""))]
    subs={}
    for h in hits: subs[h["sub"]]=subs.get(h["sub"],0)+1
    res.append((len(hits),th,subs,hits))
for n,th,subs,hits in sorted(res,reverse=True):
    print(f"{n:5d}  {th}   {subs}")
