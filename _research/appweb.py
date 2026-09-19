#!/usr/bin/env python3
# Extract App Store product page description + embedded review bodies (no tricky regex).
import sys, os, re, json, gzip, zlib, html as _h, urllib.request
BS = chr(92)
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
        return "__ERR__ " + type(ex).__name__ + " " + str(getattr(ex,"code","")) + " " + str(ex)[:90]
def scan(h, key):
    """Return list of JSON string values for "key":"...." occurrences."""
    out=[]; needle = chr(34)+key+chr(34)+":"+chr(34)
    i=0
    while True:
        j=h.find(needle,i)
        if j<0: break
        k=j+len(needle); buf=[]
        while k < len(h):
            c=h[k]
            if c==BS:
                nxt=h[k+1:k+2]
                buf.append(BS+nxt); k+=2; continue
            if c==chr(34): break
            buf.append(c); k+=1
        raw="".join(buf)
        try: val=json.loads(chr(34)+raw+chr(34))
        except Exception: val=_h.unescape(raw).replace(BS+"n"," ")
        out.append(val)
        i=k
        if len(out)>=120: break
    return out
os.makedirs(OUT,exist_ok=True)
for spec in sys.argv[1:]:
    name,_,tid=spec.partition("=")
    url="https://apps.apple.com/us/app/x/id"+tid
    h=_get(url)
    if h.startswith("__ERR__"):
        print("!!", name, h); continue
    dm=re.search(chr(60)+"meta name="+chr(34)+"description"+chr(34)+" content="+chr(34)+"([^"+chr(34)+"]*)", h)
    desc=_h.unescape(dm.group(1)) if dm else ""
    bodies=scan(h,"reviewBody"); titles=scan(h,"title")
    cnt=re.search("ratingCount"+BS+"s*:"+BS+"s*("+BS+"d+)", h)
    avg=re.search("averageUserRating"+BS+"s*:"+BS+"s*([0-9.]+)", h)
    head=("APP: "+name+" | TRACK-ID "+tid+chr(10)+
          "SOURCE-URL: "+url+chr(10)+"ACCESSED: 2026-09-19"+chr(10)+
          "RATING_COUNT: "+(cnt.group(1) if cnt else "?")+" | AVG: "+(avg.group(1) if avg else "?")+chr(10)+
          "PAGE-DESC: "+desc+chr(10)+"REVIEW-BODIES: "+str(len(bodies))+chr(10)+chr(10))
    body=head
    for idx,b in enumerate(bodies):
        t = titles[idx] if idx < len(titles) else ""
        body += "--- review "+str(idx+1)+": "+t+chr(10)+b+chr(10)+chr(10)
    fn=os.path.join(OUT, re.sub("[^a-z0-9]+","_",name.lower().strip())+".txt")
    open(fn,"w",encoding="utf-8").write(body)
    print("ok",name,"reviews=",len(bodies),"desc_len=",len(desc),"->",os.path.basename(fn))
