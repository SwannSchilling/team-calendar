#!/usr/bin/env python3
import sys, os, re
sys.path.insert(0, os.path.dirname(sys.argv[0]))
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
from fetch import fetch
KW = ("tattoo","tätowierzenie","tattooing","booking","buchung","termin","appointment","termin",
      "station","stool","arbeitsplatz","chair","deposit","anzahlung","commission","provision",
      "offline","calendar","kalender","waitlist","warteliste","aftercare","ink","pwa","flash","consent")
def check(url):
    try:
        out = fetch(url, maxbytes=120000)
    except Exception as e:
        print(f"URL: {url}\n  FETCH-ERROR: {type(e).__name__}: {e}\n"); return
    txt = out.get("text","")
    low = txt.lower()
    hits = {k: low.count(k) for k in KW if low.count(k)>0}
    sample = re.sub(r"\s+"," ", txt.strip())[:280]
    print(f"URL: {url}\n  final={out.get('finalurl')}\n  ctype={out.get('ctype')}\n  textlen={len(txt)}\n  keyword-hits={hits}\n  sample={sample!r}\n")
for u in sys.argv[1:]:
    check(u)
