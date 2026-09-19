#!/usr/bin/env python3
# Harvest reddit posts via public Atom (.rss) feeds into a local JSONL corpus.
# usage: harvest.py jobsfile   where jobsfile is TSV: sub<TAB>query[<TAB>limit]
import sys, os, re, json, gzip, zlib, html as _h, urllib.request, urllib.parse, time, random
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
OUT = os.path.join(os.path.dirname(__file__), "raw", "reddit", "corpus.jsonl")

def _get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"})
    for attempt in range(3):
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
            if code in (429, 403, 503, 408, 451) or code is None:
                time.sleep(3 + attempt * 4 + random.random() * 2); continue
            return f"__ERR__ {type(ex).__name__} {code} {ex}"
    return "__ERR__ retries exhausted"

def _clean(t):
    t = re.sub(r"(?is)<a href=\"([^\"]+)\"[^>]*>\s*\[comments\]\s*</a>", " ", t or "")
    t = re.sub(r"(?is)<a href=\"([^\"]+)\"[^>]*>\s*\[link\]\s*</a>", r" \1 ", t or "")
    t = re.sub(r"(?is)<[^>]+>", " ", t)
    t = _h.unescape(t)
    t = t.replace("&#32;", "").replace("<!-- SC_OFF -->", "").replace("<!-- SC_ON -->", "")
    return re.sub(r"\s+", " ", t).strip()

def entries(xml):
    if xml.startswith("__ERR__"):
        return None, xml
    out = []
    for blk in re.findall(r"(?is)<entry>(.*?)</entry>", xml):
        def g(tag):
            m = re.search(rf"(?is)<{tag}[^>]*>(.*?)</{tag}>", blk)
            return m.group(1) if m else ""
        link = ""
        for m in re.finditer(r"(?is)<link[^>]*href=\"([^\"]+)\"", blk):
            link = m.group(1)
        author = ""
        am = re.search(r"(?is)<name>(.*?)</name>", blk)
        if am: author = _clean(am.group(1))
        out.append({"title": _clean(g("title")), "link": _h.unescape(link),
                    "date": (g("updated") or g("published"))[:10], "author": author,
                    "body": _clean(g("content") or g("summary"))[:2500]})
    return out, None

def main():
    jobs = sys.argv[1]
    only = sys.argv[2] if len(sys.argv) > 2 else None
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    seen = set()
    if os.path.exists(OUT):
        for ln in open(OUT, encoding="utf-8"):
            try: seen.add(json.loads(ln)["link"])
            except Exception: pass
    fout = open(OUT, "a", encoding="utf-8")
    tot = 0
    for line in open(jobs, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line or line.startswith("#"): continue
        parts = line.split("\t")
        sub, q = parts[0], parts[1]
        n = parts[2] if len(parts) > 2 else "25"
        key = f"{sub}|{q}"
        if only and only not in key: continue
        url = (f"https://www.reddit.com/r/{sub}/search.rss?q={urllib.parse.quote_plus(q)}"
               f"&restrict_sr=1&sort=relevance&limit={n}")
        es, err = entries(_get(url))
        if err:
            print(f"!! {key}: {err}"); time.sleep(2); continue
        new = 0
        for e in es:
            e["sub"] = sub; e["query"] = q
            if e["link"] in seen: continue
            seen.add(e["link"]); new += 1
            fout.write(json.dumps(e, ensure_ascii=False) + "\n")
        fout.flush()
        tot += new
        print(f"ok {key}: feed={len(es)} new={new}")
        time.sleep(1.8 + random.random())
    fout.close()
    print(f"TOTAL NEW={tot} CORPUS={len(seen)}")

if __name__ == "__main__":
    main()
