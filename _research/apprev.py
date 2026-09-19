#!/usr/bin/env python3
# Pull App Store customer review RSS into raw/appreviews/. usage: apprev.py NAME=ID [NAME=ID...]
import sys, os, re, gzip, zlib, html as _h, urllib.request, urllib.parse
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
OUT=os.path.join(os.path.dirname(__file__),"raw","appreviews")
def _get(url, timeout=30):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"*/*","Accept-Encoding":"gzip, deflate"})
    try:
        with urllib.request.urlopen(req,timeout=timeout) as r:
            b=r.read(); e=(r.headers.get("Content-Encoding") or "").lower()
            if "gzip" in e:
                try: b=gzip.decompress(b)
                except Exception: pass
            elif "deflate" in e:
                try: b=zlib.decompressobj(b).read()
                except Exception: pass
            return b.decode("utf-8","replace")
    except Exception as ex:
        return f"__ERR__ {type(ex).__name__} {getattr(ex,'code','')} {str(ex)[:90]}"
def clean(t):
    t=_h.unescape(t); t=re.sub(r"(?is)<[^>]+>"," ",t); return re.sub(r"\s+"," ",t).strip()
os.makedirs(OUT,exist_ok=True)
for spec in sys.argv[1:]:
    name,_,tid = spec.partition("=")
    url=f"https://itunes.apple.com/rss/customerreviews/direct/rssfeed?id={tid}&country=us&limit=150"
    xml=_get(url)
    if xml.startswith("__ERR__"):
        print(f"!! {name}: {xml}"); continue
    rows=[]
    for blk in re.findall(r"(?is)<entry>(.*?)</entry>", xml):
        def g(t):
            m=re.search(rf"(?is)<{t}[^>]*>(.*?)</{t}>", blk); return clean(m.group(1)) if m else ""
        rating=re.search(r'name="[^"]*ratingvalue"[^/]*rating="(\d)"', blk)
        rows.append({"rating": rating.group(1) if rating else "?", "title": g("title"),
                      "body": g("content"), "author": g("author"), "date": g("updated")})
    body=f"APP: {name}  TRACK-ID: {tid}\nSOURCE-URL: {url}\nACCESSED: 2026-09-19\nREVIEWS: {len(rows)}\n\n"
    for r in rows:
        body+=f"--- {r['rating']}★ [{r['date']}] {r['author']}\nTITLE: {r['title']}\n{r['body']}\n\n"
    fn=os.path.join(OUT, re.sub(r"[^a-z0-9]+","_",name.lower().strip())+".txt")
    open(fn,"w",encoding="utf-8").write(body)
    print(f"ok {name}: reviews={len(rows)} -> {os.path.basename(fn)}")
