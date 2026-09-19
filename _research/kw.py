#!/usr/bin/env python3
import sys,re,os,glob
for _n in ("stdout","stderr"):
    try: getattr(sys,_n).reconfigure(encoding="utf-8",errors="replace")
    except Exception: pass
dirs=sys.argv[1].split(',')
kws=sys.argv[2:]
files=[]
for d in dirs:
    files+=sorted(glob.glob(os.path.join(d,'*.txt')))
for kw in kws:
    rx=re.compile(r'[^<>{}"]{0,70}'+re.escape(kw)+r'[^<>{}"]{0,90}',re.I)
    hits=[];seen=set()
    for f in files:
        t=open(f,encoding="utf-8",errors="replace").read()
        for m in rx.finditer(t):
            s=re.sub(r'\s+',' ',m.group(0)).strip()
            if len(s)<12: continue
            k=s.lower()[:70]
            if k in seen: continue
            seen.add(k); hits.append((os.path.basename(f)[:38],s))
            if len(hits)>=3: break
        if len(hits)>=3: break
    print(f"### {kw} :: {len(hits)}")
    for f,s in hits: print(f"   [{f}] {s}")
