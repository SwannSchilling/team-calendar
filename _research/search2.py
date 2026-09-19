#!/usr/bin/env python3
import sys, re, html as _h, urllib.request, urllib.parse, urllib.error, gzip, zlib
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

def _get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent":UA,"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        b = r.read()
        e = (r.headers.get("Content-Encoding") or "").lower()
        if "gzip" in e:
            try: b = gzip.decompress(b)
            except Exception: pass
        elif "deflate" in e:
            try: b = zlib.decompressobj(b).read()
            except Exception: pass
        return b.decode("utf-8","replace")

def _clean(t):
    t = re.sub(r"(?is)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", _h.unescape(t)).strip()

def _bing_url(href):
    if not href: return href
    m = re.search(r"[?&]url=([^&]+)", href)
    if m:
        try: return urllib.parse.unquote(m.group(1))
        except Exception: pass
    return href if href.startswith("http") else None

def search(query, count=25):
    q = urllib.parse.quote_plus(query)
    out = []
    # try RSS first
    try:
        xml = _get(f"https://www.bing.com/search?q={q}&count={count}&setmkt=en-US")
        items = re.findall(r"(?is)<item>(.*?)</item>", xml)
        for it in items:
            link = re.search(r"(?is)<link>(.*?)</link>", it)
            title = re.search(r"(?is)<title>(.*?)</title>", it)
            desc  = re.search(r"(?is)<description>(.*?)</description>", it)
            u = _clean(link.group(1)) if link else None
            if not u: continue
            if re.search(r"(bing|microsoft|msn)\.", u, re.I): continue
            out.append(((_clean(title.group(1)) if title else ""), u, _clean(desc.group(1)) if desc else ""))
    except Exception as e:
        out = []
    if not out:
        try:
            xml = _get(f"https://www.bing.com/search?q={q}&count={count}&setmkt=en-US")
            for blk in re.findall(r'(?is)<li class="b_algo.*?(?=<li class="b_algo|</ol>|<nav|<aside)', xml):
                a = re.search(r'(?is)<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', blk)
                if not a: continue
                u = _bing_url(_h.unescape(a.group(1)))
                if not u or re.search(r"(bing|microsoft|msn)\.", u, re.I): continue
                sn = re.search(r'(?is)<p class="b_[^"]*">(.*?)</p>', blk)
                out.append((_clean(a.group(2)), u, _clean(sn.group(1)) if sn else ""))
        except Exception as e:
            print(f"SEARCH ERROR: {type(e).__name__}: {e}")
    return out

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: search.py 'query' [count]"); raise SystemExit
    query = sys.argv[1]; count = int(sys.argv[2]) if len(sys.argv)>2 else 25
    for i,(t,u,s) in enumerate(search(query,count),1):
        print(f"{i}. {t}\n   URL: {u}\n   {s[:220]}")
