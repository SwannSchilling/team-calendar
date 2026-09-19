#!/usr/bin/env python3
# Reddit Atom (rss) reader: works when .json is blocked. Use search.rss / new.rss.
# usage: rss.py SUBREDDIT 'query' [limit]   |  rss.py --feed URL [limit]
#        rss.py --post r/tattoo/comments/ID   (comments feed)
import sys, re, gzip, zlib, html as _h, urllib.request, urllib.parse, time, random
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

def _get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                b = r.read(); e = (r.headers.get("Content-Encoding") or "").lower()
                if "gzip" in e:
                    try: b = gzip.decompress(b)
                    except Exception: pass
                elif "deflate" in e:
                    try: b = zlib.decompressobj(b).read()
                    except Exception: pass
                return b.decode("utf-8", "replace")
        except Exception as ex:
            code = getattr(ex, "code", None)
            if code in (429, 403, 503, 429):
                time.sleep(3 + attempt * 4 + random.random()); continue
            if code is None and attempt < 2:
                time.sleep(2); continue
            return f"__ERR__ {type(ex).__name__} {getattr(ex,'code','')} {ex}"
    return "__ERR__ retries exhausted"

def _clean(t):
    t = re.sub(r"(?is)<a href=\"([^\"]+)\"[^>]*>.*?</a>", r" \1 ", t or "")
    t = re.sub(r"(?is)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", _h.unescape(t)).strip()

def entries(xml):
    if xml.startswith("__ERR__"):
        print(xml); return []
    out = []
    for blk in re.findall(r"(?is)<entry>(.*?)</entry>", xml):
        def g(tag):
            m = re.search(rf"(?is)<{tag}[^>]*>(.*?)</{tag}>", blk)
            return m.group(1) if m else ""
        link = ""
        for m in re.finditer(r"(?is)<link[^>]*href=\"([^\"]+)\"", blk):
            link = m.group(1)
        title = _clean(g("title")); content = g("content") or g("summary")
        d = g("updated") or g("published")
        out.append({"title": title, "link": _h.unescape(link), "date": d[:10],
                    "body": _clean(content)[:1400]})
    return out

def main():
    a = sys.argv[1:]
    if not a:
        print("usage: rss.py SUB QUERY [n] | --feed URL [n] | --post PATH"); return
    if a[0] == "--feed":
        url = a[1]; n = a[2] if len(a) > 2 else "25"
    elif a[0] == "--post":
        url = f"https://www.reddit.com/{a[1].lstrip('/')}/.rss?limit=100"
        n = a[2] if len(a) > 2 else "60"
    else:
        sub, q = a[0], urllib.parse.quote_plus(a[1])
        n = a[2] if len(a) > 2 else "25"
        url = f"https://www.reddit.com/r/{sub}/search.rss?q={q}&restrict_sr=1&sort=relevance&limit={n}"
    print("URL:", url)
    es = entries(_get(url))
    print(f"N={len(es)}")
    for e in es:
        print("-" * 70)
        print("TITLE:", e["title"], "|", e["date"])
        print("LINK:", e["link"])
        if e["body"]: print("BODY:", e["body"])
    time.sleep(1.2)

if __name__ == "__main__":
    main()
