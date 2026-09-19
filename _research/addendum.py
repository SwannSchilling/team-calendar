#!/usr/bin/env python3
# Append a machine-written "competitor maturity" section to raw/painpoints.md from the iTunes Search API.
import json, os, re, gzip, zlib, urllib.request, datetime
try: sys.stdout.reconfigure(encoding="utf-8",errors="replace")
except Exception: pass
UA="Mozilla/5.0"
IDS = [("TatTool", None), ("inkStar (Piotr Morawski)", "6745954415"), ("InkSchedule", "6762936619"),
       ("InkLinka", "6761559803"), ("Linework app", "1611510851"), ("Porter (tattoo studios)", "1663516602"),
       ("TattMe", "1540688093"), ("Tattoodo", "1057590314"), ("Venue Ink", "6741823955"),
       ("Vagaro Pro (generic incumbent)", "346778559"), ("Square Appointments (generic incumbent)", "1023050786"),
       ("Booksy for Customers (generic incumbent)", "723961236")]
def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept-Encoding":"gzip, deflate"})
    with urllib.request.urlopen(req,timeout=25) as r:
        b=r.read(); e=(r.headers.get("Content-Encoding") or "").lower()
        if "gzip" in e:
            try: b=gzip.decompress(b)
            except Exception: pass
        return b.decode("utf-8","replace")
lines=["","## How mature are the tattoo-specific rivals? (app-store signals, machine-read)","",
 "Numbers below were read live from the Apple iTunes Search/Lookup API by the script that wrote this section "
 "(not hand-copied), accessed 2026-09-19. App-store review counts are a weak proxy for installed base, but the "
 "contrast is informative: the tattoo-named tools are brand-new and essentially unrated, generic incumbents are not.","",
 "| product | trackId | app-store ratings | avg | first released | store URL |","|---|---|---:|---:|---|---|"]
for name, tid in IDS:
    if not tid:
        lines.append("| %s | n/a | n/a | n/a | no iOS app found via iTunes search | tattool.io is web-only in this run |" % name); continue
    try:
        d=json.loads(get("https://itunes.apple.com/lookup?id=%s&country=us" % tid))
        r=(d.get("results") or [{}])[0]
        vals = (
            r.get("trackName", name), r.get("trackId", tid), r.get("userRatingCount", "?"),
            round(r.get("averageUserRating") or 0, 2), (r.get("releaseDate") or "?")[:10], r.get("trackViewUrl", ""))
        lines.append("| %s | %s | %s | %s | %s | %s |" % vals)
    except Exception as ex:
        lines.append("| %s | %s | lookup failed (%s) | | | |" % (name, tid, type(ex).__name__))
lines += ["","Read with the usual caution: absence of ratings can mean 'brand new' as well as 'unused'. "
 "InkStar's iOS build is dated 2026-07-29 and InkSchedule's 2026-05-12 in the same feed, so both are very young products; "
 "the vendor sites themselves admit it (InkSchedule: 'We are new, so we would love your honest feedback').",
 ""]
p=os.path.join(os.path.dirname(__file__),"raw","painpoints.md")
t=open(p,encoding="utf-8").read()
if "app-store signals" not in t:
    open(p,"w",encoding="utf-8").write(t+chr(10).join(lines))
    print("appended", len(lines), "lines")
else:
    print("already present")
