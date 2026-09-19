#!/usr/bin/env python3
# Dependency-free page/text fetch helper for research (urllib + stdlib only).
import sys as _S
for _n in ("stdout","stderr"):
    try: getattr(_S,_n).reconfigure(encoding="utf-8",errors="replace")
    except Exception: pass
import sys, re, gzip, zlib, html as _html, urllib.request, urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

def _read_body(resp):
    data = resp.read()
    enc = (resp.headers.get("Content-Encoding") or "").lower()
    if "gzip" in enc:
        try: data = gzip.decompress(data)
        except Exception: pass
    elif "deflate" in enc:
        try: data = zlib.decompressobj(data).read()
        except Exception: pass
    return data

def fetch(url, timeout=30, raw=False, links=False, maxbytes=400000):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw_bytes = _read_body(resp)[:maxbytes]
        ctype = (resp.headers.get("Content-Type") or "").lower()
        final = resp.geturl()
    try: text = raw_bytes.decode("utf-8", "replace")
    except Exception: text = raw_bytes.decode("latin-1", "replace")
    out = {"finalurl": final, "ctype": ctype}
    if raw or ("json" in ctype):
        out["text"] = text; return out
    if links:
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', text, flags=re.I)
        hrefs = [h for h in hrefs if not re.match(r'^(#|javascript:|mailto:|tel:|data:)', h, re.I)]
        seen, abs_links = set(), []
        for h in hrefs:
            try: a = urllib.parse.urljoin(final, h)
            except Exception: a = h
            if a not in seen: seen.add(a); abs_links.append(a)
        out["links"] = abs_links
    out["text"] = _html2text(text)
    return out

def _html2text(text):
    text = re.sub(r'(?is)<(script|style|noscript|svg|head)[^>]*>.*?</\1>', ' ', text)
    text = re.sub(r'(?is)<!--.*?-->', ' ', text)
    text = re.sub(r'(?is)<br\s*/?>', '\n', text)
    text = re.sub(r'(?is)</(p|div|li|tr|h[1-6]|section|article)>', '\n', text)
    text = re.sub(r'(?is)<[^>]+>', ' ', text)
    text = _html.unescape(text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n\s*', '\n', text)
    lines = [l.strip() for l in text.split('\n')]
    lines = [l for l in lines if l and not re.match(r'^[.,;:\-–—|·•*\s]*$', l)]
    return '\n'.join(lines)

def main():
    if len(sys.argv) < 2:
        print("usage: fetch.py URL [--raw] [--links] [--max N]"); return
    url = sys.argv[1]
    raw = '--raw' in sys.argv
    links = '--links' in sys.argv
    mx = 400000
    if '--max' in sys.argv: mx = int(sys.argv[sys.argv.index('--max')+1])
    try: out = fetch(url, raw=raw, links=links, maxbytes=mx)
    except Exception as e:
        print(f"ERROR fetching {url}: {type(e).__name__}: {e}"); return
    print(f"### FINAL-URL: {out.get('finalurl')}")
    print(f"### CONTENT-TYPE: {out.get('ctype')}")
    if 'links' in out:
        print("### LINKS:")
        for l in out['links'][:120]: print(l)
    print("### TEXT:")
    print(out.get('text'))

if __name__ == '__main__':
    main()
