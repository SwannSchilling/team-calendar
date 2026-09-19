import re,html,urllib.parse,sys
t=open('_research/raw/_q/ddgpage.html',encoding='utf-8',errors='replace').read()
n=0
for m in re.finditer(r"(?is)<a rel=.nofollow. href=.(?://duckduckgo\.com)?/l/\?uddg=([^&\"']+)&?[^\"']*.\s+class=.result-link.>(.*?)</a>(.*?)(?=<a rel=.nofollow|$)",t):
    u=urllib.parse.unquote(m.group(1))
    title=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
    rest=m.group(3)
    sn=re.search(r"(?is)<td class=.result-snippet.>(.*?)</td>",rest)
    snip=html.unescape(re.sub(r'<[^>]+>',' ',sn.group(1))) if sn else ''
    n+=1
    print(f"{n}. {re.sub(r'\s+',' ',title).strip()} | {u}")
    print(f"    {re.sub(r'\s+',' ',snip).strip()[:230]}")
    if n>=13: break
if n==0: print("  (no results parsed; bytes=%d)"%len(t))
