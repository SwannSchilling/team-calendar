#!/bin/bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
for q in "$@"; do
  echo "##### $q"
  curl -s -m 25 -A "$UA" --compressed "https://lite.duckduckgo.com/lite/?q=$(python -c "import sys,urllib.parse;print(urllib.parse.quote_plus(sys.argv[1]))" "$q")" \
  | python -c "
import sys,re,urllib.parse
t=sys.stdin.read()
seen=[]
for u in re.findall(r'/l/\?uddg=([^&\"]+)',t):
    d=urllib.parse.unquote(u)
    if d not in seen: seen.append(d)
bad=('duckduckgo.com','w3.org','schema.org','favicon','/assets/','/dist/')
seen=[s for s in seen if not any(b in s for b in bad)]
for i,s in enumerate(seen[:16],1): print(f'{i}. {s}')
"
  sleep 1
done
