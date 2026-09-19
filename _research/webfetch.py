#!/usr/bin/env python3
# Fetch competitor/marketing/press pages into plain text files under raw/web/.
# usage: webfetch.py URL [URL...]
import sys, os, re, hashlib, urllib.request, urllib.parse, gzip, zlib, html as _h, time
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
OUT = os.path.join(os.path.dirname(__file__), "raw", "web")

def _get(url, timeout=35):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
        "Accept": "text/html,application/xhtml,application/json;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,de;q=0.8", "Accept-Encoding": "gzip, deflate",
        "Connection": "close"})
    for a in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                b = r.read()[:1200000]; final = r.geturl()
                e = (r.headers.get("Content-Encoding") or "").lower()
                if "gzip" in e:
                    try: b = gzip.decompress(b)
                    except Exception: pass
                elif "deflate" in e:
                    try: b = zlib.decompressobj(b).read()
                    except Exception: pass
                return b.decode("utf-8", "replace"), final, None
        except Exception as ex:
            err = f"{type(ex).__name__} {getattr(ex,'code','')} {ex}"
            time.sleep(1 + a)
    return None, url, err

def to_text(t):
    t = re.sub(r"(?is)<(script|style|noscript|svg|head)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?is)<!--.*?-->", " ", t)
    t = re.sub(r"(?is)<br\s*/?>", "\n", t)
    t = re.sub(r"(?is)</(p|div|li|tr|h[1-6]|section|article|figcaption)>", "\n", t)
    t = re.sub(r"(?is)<[^>]+>", " ", t)
    t = _h.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    lines = [l.strip() for l in t.split("\n")]
    return "\n".join([l for l in lines if l])

def main():
    os.makedirs(OUT, exist_ok=True)
    for url in sys.argv[1:]:
        if not re.match(r"https?://", url): url = "https://" + url
        txt, final, err = _get(url)
        if err:
            print(f"!! {url}\n   ERR {err}")
            continue
        body = to_text(txt) if re.search(r"html|xml", final) or "<html" in txt[:2000].lower() else txt
        slug = re.sub(r"[^a-z0-9]+", "_", re.sub(r"^www\.", "", urllib.parse.urlparse(final).netloc)).strip("_")[:40]
        tail = re.sub(r"[^a-z0-9]+", "_", urllib.parse.urlparse(final).path).strip("_")[:60]
        fn = os.path.join(OUT, f"{slug}__{tail or 'root'}.txt")
        with open(fn, "w", encoding="utf-8") as f:
            f.write(f"SOURCE-URL: {final}\nACCESSED: 2026-09-19\nCHARS: {len(body)}\n\n{body}")
        print(f"ok {final}\n   -> {os.path.basename(fn)} chars={len(body)}")
        time.sleep(0.6)

if __name__ == "__main__":
    main()
