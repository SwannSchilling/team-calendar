#!/usr/bin/env python3
# Search via searx (disroot) + startpage HTML. usage: ds.py 'query' [n]
import sys, re, gzip, zlib, html as _h, urllib.request, urllib.parse
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
def _get(url, timeout=25):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml,*/*","Accept-Language":"en-US,en;q=0.9","Accept-Encoding":"gzip, deflate","Connection":"close"})
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
        return f"__ERR__ {type(ex).__name__} {getattr(ex,'code','')} {str(ex)[:70]}"
def _txt(t):
    t=re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>"," ",t); t=re.sub(r"(?is)<[^>]+>"," ",t)
    return re.sub(r"\s+"," ",_h.unescape(t)).strip()
BAD=re.compile(r'(startpage|searx|disroot|ads\..*|go\.startpage|www\.startpage|bing\.com|microsoft|duckduckgo)',re.I)
def searx(q,n):
    u=f"https://search.disroot.org/search?q={urllib.parse.quote_plus(q)}&format=json"
    h=_get(u)
    if h.startswith("__ERR__"): return [("ERR",h,"")]
    try:
        import json; d=json.loads(h)
        return [(r.get('url',''), _txt(r.get('title','')), _txt(r.get('content',''))) for r in d.get('results',[])[:n]]
    except Exception: pass
    out=[]
    for blk in re.findall(r'(?is)<div[^>]+class="[^"]*result[^"]*"[^>]*>(.*?)(?=</div>\s*<div[^>]+class="[^"]*result|$)', h)[:n*3]:
        m=re.search(r'(?is)<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>', blk)
        if not m: continue
        u2,label=m.group(1),_txt(m.group(2))
        sn=re.search(r'(?is)<div[^>]+class="[^"]*(content|snippet|description)[^"]*"[^>]*>(.*?)</div>', blk)
        if BAD.search(u2) or len(label)<10: continue
        out.append((u2,label,_txt(sn.group(2)) if sn else ""))
        if len(out)>=n: break
    return out
def startpage(q,n):
    u=f"https://www.startpage.com/sp-search/search?query={urllib.parse.quote_plus(q)}&num=20"
    h=_get(u)
    if h.startswith("__ERR__"): return [("ERR",h,"")]
    out=[]; 
    for m in re.finditer(r'(?is)<h3[^>]*>\s*<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>', h):
        u2,label=m.group(1),_txt(m.group(2))
        if BAD.search(u2) or len(label)<10: continue
        i=h.find(m.group(0))
        tail=h[i:i+3000]
        sn=re.search(r'(?is)<div class="[^"]*(sMw3td|lPkkUc|SSoMe)[^"]*"[^>]*>(.*?)</div>', tail)
        out.append((u2,label,_txt(sn.group(2)) if sn else ""))
        if len(out)>=n: break
    return out
if __name__ == "__main__":
    a=sys.argv[1:]; n=int(a[-1]) if a and a[-1].isdigit() else 8
    q=" ".join(a[:-1] if a and a[-1].isdigit() else a)
    print("Q:",q)
    for name,fn in (("searx",searx),("startpage",startpage)):
        res=fn(q,n)
        print(f"== {name}: {len(res)}")
        for u,t,s in res:
            print(f"   - {t[:120]}\n     {u[:170]}")
            if s: print(f"     {s[:260]}")
