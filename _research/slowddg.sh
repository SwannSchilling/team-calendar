#!/bin/bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
OUT="_research/raw/_q/ddg_out.txt"
: > "$OUT"
while IFS= read -r q; do
  [ -z "$q" ] && continue
  got=0
  for try in 1 2 3 4; do
    eng="lite"; [ $((RANDOM % 2)) -eq 0 ] && eng="html"
    curl -s -m 30 -A "$UA" --compressed "https://${eng}.duckduckgo.com/${}/?q=$(python -c "import sys,urllib.parse;print(urllib.parse.quote_plus(sys.argv[1]))" "$q")" < /dev/null -o _research/raw/_q/ddgpage.html
    if grep -q 'result-link' _research/raw/_q/ddgpage.html; then got=1; break; fi
    sleep 25
  done
  echo "##### $q" >> "$OUT"
  if [ "$got" = "1" ]; then python _research/ddgparse.py < /dev/null >> "$OUT"; else echo "  (empty)" >> "$OUT"; fi
  sleep 20
done < "$1"
echo "ALLDONE" >> "$OUT"
