#!/usr/bin/env python3
# Wayback CDX: earliest/latest capture + total count (any status & 200-only).
import sys, json, urllib.request, urllib.parse, gzip, zlib
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
UA="Mozilla/5.0"
def _get(url, timeout=40):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept-Encoding":"gzip, deflate"})
    with urllib.request.urlopen(req,timeout=timeout) as r:
        b=r.read(); e=(r.headers.get("Content-Encoding") or "").lower()
        if "gzip" in e:
            try: b=gzip.decompress(b)
            except Exception: pass
        elif "deflate" in e:
            try: b=zlib.decompressobj(b).read()
            except Exception: pass
        return b.decode("utf-8","replace")
def _ts(t): return f"{t[0:4]}-{t[4:6]}-{t[6:8]}" if len(t)>=8 else t
def _rows(txt):
    try: d=json.loads(txt)
    except Exception: return []
    return [r for r in d if isinstance(r,list) and r and isinstance(r[0],str) and r[0].isdigit()]
def _one(target, mt, extra=""):
    t=urllib.parse.quote_plus(target)
    url=f"https://web.archive.org/cdx/identification?url={t}&output=json&fl=timestamp&sort=asc&limit=1&matchType={mt}{extra}"
    return _rows(_get(url))
def query(target):
    out={}
    for mt in ("exact","domain","prefix"):
        try:
            r=_one(target,mt); out[mt]=_ts(r[0][0]) if r else None
        except Exception as e:
            out[mt]=f"ERR"
    # total any-status count
    try:
        t=urllib.parse.quote_plus(target)
        cnt=len(_rows(_get(f"https://web.archive.org/cdx/identification?url={t}&output=json&fl=timestamp&matchType=domain")))
    except Exception: cnt=-1
    firsts=[v for v in out.values() if v and v!="ERR"]
    first=min(firsts) if firsts else "NO SNAPSHOT"
    print(f"{target:34s} first={first:12s} exact={out['exact']} domain={out['domain']} prefix={out['prefix']} n_captures~{cnt}")
if __name__=="__main__":
    for a in sys.argv[1:]: query(a)
