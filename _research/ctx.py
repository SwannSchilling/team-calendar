#!/usr/bin/env python3
import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f,kw=sys.argv[1],sys.argv[2]
w=int(sys.argv[3]) if len(sys.argv)>3 else 400
n=int(sys.argv[4]) if len(sys.argv)>4 else 3
t=open(f,encoding="utf-8",errors="replace").read()
c=0
for m in re.finditer(re.escape(kw),t,re.I):
    a=max(0,m.start()-w); b=min(len(t),m.end()+w)
    print("----",m.start()); print(re.sub(r'\s+',' ',t[a:b]))
    c+=1
    if c>=n: break
