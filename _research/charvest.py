#!/usr/bin/env python3
# Harvest comment feeds for thread paths into corpus.jsonl
# usage: charvest.py threads.txt   (one path per line: r/Sub/comments/ID or full URL)
import sys, os, re, json, gzip, zlib, html as _h, urllib.request, time, random
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
OUT=os.path.join(os.path.dirname(__file__),"raw","reddit","corpus.jsonl")
def _get(url, timeout=30):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"*/*","Accept-Encoding":"gzip, deflate"})
    for a in range(3):
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
            code=getattr(ex,"code",None)
            if code in (429,403,503,None):
                time.sleep(3+a*4); continue
            return "__ERR__ "+type(ex).__name__+" "+str(code)
    return "__ERR__ retries"
def clean(t):
    t=_h.unescape(t); t=re.sub(r"(?is)<[^>]+>"," ",t)
    return re.sub(r"\s+"," ",t).strip()
seen=set()
for ln in open(OUT,encoding="utf-8"):
    try: seen.add(json.loads(ln)["link"])
    except Exception: pass
out=open(OUT,"a",encoding="utf-8")
tot=0
for line in open(sys.argv[1],encoding="utf-8"):
    p=line.strip()
    if not p or p.startswith("#"): continue
    p=re.sub(r"^https?://(www\.|old\.)?reddit\.com/","",p)
    p=p.split("?")[0]
    url="https://www.reddit.com/"+p.strip("/")+"/.rss?limit=100"
    xml=_get(url)
    if xml.startswith("__ERR__"):
        print("!!",p,xml); time.sleep(2); continue
    n=0
    for blk in re.findall(r"(?is)<entry>(.*?)</entry>", xml):
        tm=re.search(r"(?is)<title>(.*?)</title>", blk)
        lm=""
        for m in re.finditer(r'(?is)<link[^>]*href="([^"]+)"', blk): lm=m.group(1)
        cm=re.search(r"(?is)<content[^>]*>(.*?)</content>", blk)
        dt=re.search(r"(?is)<updated>(.*?)</updated>", blk)
        title=clean(tm.group(1)) if tm else ""
        body=clean(cm.group(1)) if cm else ""
        link=_h.unescape(lm)
        if link in seen: continue
        body=re.sub(r"<!-- SC_OFF -->|<!-- SC_ON -->|&#32;","",body)
        seen.add(link); n+=1
        out.write(json.dumps({"title":title[:200],"link":link,"date":(dt.group(1) if dt else "")[:10],
            "body":body[:2200],"sub":"comments","query":p.split("/")[2]},ensure_ascii=False)+chr(10))
    tot+=n
    print("ok",p.split("/")[2],"comments=",n); time.sleep(1.6+random.random())
out.close()
print("TOTAL NEW=",tot)
