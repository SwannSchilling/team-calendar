#!/usr/bin/env python3
# stdin html -> text on stdout. usage: curl -s URL | python htmlx.py [maxchars]
import sys,re,html as _h
try: sys.stdin.reconfigure(encoding="utf-8",errors="replace"); sys.stdout.reconfigure(encoding="utf-8",errors="replace")
except Exception: pass
t=sys.stdin.read()
t=re.sub(r"(?is)<(script|style|noscript|svg|head)[^>]*>.*?</\1>"," ",t)
t=re.sub(r"(?is)<!--.*?-->"," ",t)
t=re.sub(r"(?is)<br\s*/?>",chr(10),t)
t=re.sub(r"(?is)</(p|div|li|tr|h[1-6]|section|article|figcaption)>",chr(10),t)
t=re.sub(r"(?is)<[^>]+>"," ",t)
t=_h.unescape(t)
t=re.sub(r"[ \t]+"," ",t)
mx=int(sys.argv[1]) if len(sys.argv)>1 else 6000
lines=[l.strip() for l in t.split(chr(10)) if l.strip()]
out=chr(10).join(lines)
print(out[:mx])
