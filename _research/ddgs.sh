#!/bin/bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
for q in "$@"; do
  echo "##### $q"
  ok=0
  for try in 1 2 3; do
    curl -s -m 30 -A "$UA" --compressed "https://lite.duckduckgo.com/lite/?q=$(python -c "import sys,urllib.parse;print(urllib.parse.quote_plus(sys.argv[1]))" "$q")" -o _research/raw/_q/ddgpage.html
    if grep -q 'result-link' _research/raw/_q/ddgpage.html; then ok=1; break; fi
    sleep 4
  done
  if [ "$ok" = "1" ]; then python _research/ddgparse.py; else echo "  (empty after retries)"; fi
  sleep 2
done
