#!/usr/bin/env python3
# Play Store product page -> description + review-ish strings. usage: playrev.py NAME=BUNDLE
import sys, os, re, json, gzip, zlib, html as _h, urllib.request, urllib.parse
try: sys.stdout.reconfigure(encoding="utf-8",errors="replace")
except Exception: pass
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
OUT=os.path.join(os.path.dirname(__file__),"raw","appreviews")
def _get(url, timeout=30):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html,*/*","Accept-Language":"en-US,en;q=0.9","Accept-Encoding":"gzip, deflate"})
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
        return "__ERR__ "+type(ex).__name__+" "+str(getattr(ex,"code",""))+" "+str(ex)[:70]
os.makedirs(OUT,exist_ok=True)
for spec in sys.argv[1:]:
    name,_,bundle=spec.partition("=")
    url="https://play.google.com/store/apps/details?id="+bundle
    h=_get(url)
    if h.startswith("__ERR__"):
        print("!!",name,h); continue
    m=re.search(r'<meta name="description" content="([^"]*)"',h)
    desc=_h.unescape(m.group(1)) if m else ""
    am=re.search(r'itemprop="description">([^<]{40,})',h)
    long=_h.unescape(am.group(1)) if am else ""
    # review bodies: long escaped strings in the data blob
    _pat = "((?:" + chr(91) + "[^" + chr(34) + chr(92)*2 + "]|" + chr(92)*2 + ".)" + "{80,1600}?)" + chr(34)
    cands=re.findall(_pat, h)
    keep=[]
    for c in cands:
        try: t=json.loads('"'+c+'"')
        except Exception: continue
        if not re.search(r'[a-z]{20}',t): continue
        if re.search(r'(http|www\.|function|var |\.js|\.css|rgba|#[0-9a-f]{6}|play.google.com|_,\[\[)',t): continue
        if not re.search(r"\b(the|and|to|of|is|for|with|my|we)\b",t): continue
        keep.append(t)
    seen=set(); uniq=[]
    for t in keep:
        k=t[:60]
        if k in seen: continue
        seen.add(k); uniq.append(t)
    head=("APP: "+name+" | BUNDLE "+bundle+chr(10)+"SOURCE-URL: "+url+chr(10)+
          "ACCESSED: 2026-09-19"+chr(10)+"META-DESC: "+desc+chr(10)+"LONG-DESC: "+long[:2500]+chr(10)+
          "CANDIDATE-STRINGS: "+str(len(uniq))+chr(10)+chr(10))
    body=head+chr(10).join("--- s"+str(i+1)+chr(10)+t for i,t in enumerate(uniq[:90]))
    fn=os.path.join(OUT,"play_"+re.sub("[^a-z0-9]+","_",name.lower().strip())+".txt")
    open(fn,"w",encoding="utf-8").write(body)
    print("ok",name,"strings=",len(uniq),"desc=",len(desc),"->",os.path.basename(fn))
