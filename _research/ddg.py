#!/usr/bin/env python3
import sys,re,html,urllib.request,urllib.parse,gzip,zlib,json,time
try: sys.stdout.reconfigure(encoding="utf-8",errors="replace")
except Exception: pass
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
def _get(url,timeout=30):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html","Accept-Language":"en-US,en;q=0.9,de;q=0.8","Accept-Encoding":"gzip, deflate"})
    with urllib.request.urlopen(req,timeout=timeout) as r:
        b=r.read(); e=(r.headers.get("Content-Encoding") or "").lower()
        if "gzip" in e:
            try: b=gzip.decompress(b)
            except Exception: pass
        elif "deflate" in e:
            try: b=zlib.decompressobj(b).read()
            except Exception: pass
    return b.decode("utf-8","replace")
SKIP=("duckduckgo.com","w3.org","schema.org","favicon","opensearch","/assets/","/dist/","bing.com","microsoft.com")
def srch(q):
    t=_get("https://lite.duckduckgo.com/lite/?q="+urllib.parse.quote_plus(q)+"&kl=us-en")
    res=[]
    for m in re.finditer(r'(?is)<div class="result results-link([^"]*)">(.*?)</div>\s*</div>',t):
        blk=m.group(2)
        a=re.search(r'href="(/l/\?uddg=([^"&]+))',blk)
        if not a: continue
        u=urllib.parse.unquote(a.group(2))
        ti=re.search(r'(?is)<a[^>]*>(.*?)</a>',blk)
        title=html.unescape(re.sub(r'(?is)<[^>]+>','',ti.group(1))) if ti else ""
        sn=re.search(r'(?is)<div class="result-snippet[^"]*">(.*?)</div>',blk)
        snip=html.unescape(re.sub(r'(?is)<[^>]+>',' ',sn.group(1))) if sn else ""
        res.append((re.sub(r'\s+',' ',title).strip(),u,re.sub(r'\s+',' ',snip).strip()))
    return res
for q in sys.argv[1:]:
    print(f"\n##### DDG: {q}")
    try: rs=srch(q)
    except Exception as e: print(f"  ERR {type(e).__name__}: {e}"); continue
    if not rs:
        t=_get("https://lite.duckduckgo.com/lite/?q="+urllib.parse.quote_plus(q))
        urls=[urllib.parse.unquote(u) for u in re.findall(r'/l/\?uddg=([^&"]+)',t)]
        rs=[("",u,"") for u in dict.fromkeys(urls)]
    for i,(ti,u,sn) in enumerate(rs[:14],1):
        if any(s in u for s in SKIP): continue
        print(f"{i}. {ti} | {u}\n    {sn[:230]}")
    time.sleep(1.2)
