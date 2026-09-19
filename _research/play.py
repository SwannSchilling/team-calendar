#!/usr/bin/env python3
import sys,re,html
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
sys.path.insert(0,'_research')
from fetch import fetch
for pid in sys.argv[1:]:
    u=f"https://play.google.com/store/apps/details?hl=en&gl=US&id={pid}"
    try: o=fetch(u,maxbytes=900000)
    except Exception as e: print(pid,"ERR",e); continue
    t=o["text"]
    def g(pat,n=1):
        m=re.findall(pat,t,re.I)
        return [html.unescape(x)[:200] for x in m[:n]]
    print("###",pid)
    print("  title:",g(r'<title[^>]*>(.*?)</title>')[:1])
    print("  desc:",g(r'itemprop="description"[^>]*>(.*?)</div>',1)[:1])
    print("  valid:",("Wellness" if False else None))
    body=re.sub(r'(?is)<style.*?</style>',' ',t)
    body=re.sub(r'(?is)<script[^>]*>.*?</script>',' ',body)
    txt=re.sub(r'(?is)<[^>]+>',' ',body)
    txt=html.unescape(re.sub(r'\s+',' ',txt))
    i=txt.find('App description')
    print("  body:",txt[i:i+700] if i>0 else txt[:400])
    for k in ["Updated on","Downloads","Offers In-App Purchases","Verified email address","Developer Email","Developer Address"]:
        j=txt.find(k)
        if j>0: print("   ",k,"->",txt[j:j+120])
