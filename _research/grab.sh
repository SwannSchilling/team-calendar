#!/bin/bash
# usage: grab.sh OUTDIR URL [URL...]
out="$1"; shift; mkdir -p "$out"
for u in "$@"; do
  slug=$(echo "$u" | sed -e 's#https://##' -e 's#[?#].*##' -e 's#/#__#g' -e 's#[^A-Za-z0-9._-]#_#g')
  f="$out/${slug:0:150}.txt"
  python _research/fetch.py "$u" --max 600000 > "$f" 2>&1
  echo "$(wc -c < "$f") $u"
done
