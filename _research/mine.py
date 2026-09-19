#!/usr/bin/env python3
# Mine the local reddit corpus for a theme. usage: mine.py REGEX [max] [--field body|title|all]
import sys, os, re, json
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
OUT = os.path.join(os.path.dirname(__file__), "raw", "reddit", "corpus.jsonl")
pat = sys.argv[1]; mx = int(sys.argv[2]) if len(sys.argv) > 2 else 12
rx = re.compile(pat, re.I)
import html as _H
def tidy(t):
    t = _H.unescape(t)
    t = re.sub(r"(?is)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).strip()
rows = [json.loads(l) for l in open(OUT, encoding="utf-8") if l.strip()]
for r in rows:
    r["title"] = tidy(r.get("title","")); r["body"] = tidy(r.get("body",""))
print(f"corpus={len(rows)} pattern={pat}")
n = 0
for r in rows:
    txt = (r.get("title","") + " || " + r.get("body",""))
    m = rx.search(txt)
    if not m: continue
    n += 1
    if n > mx: break
    a = max(0, m.start()-260); b = min(len(txt), m.end()+340)
    print("-"*68)
    print(f"[{r['sub']}|{r['date']}] {r['title'][:150]}")
    print(f"URL {r['link']}  (query={r.get('query','')})")
    print("..." + txt[a:b] + "...")
print(f"MATCHED={n}")
