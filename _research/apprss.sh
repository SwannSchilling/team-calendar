#!/usr/bin/bash
# apprss.sh NAME ID  -> raw/appreviews/appstore_NAME.xml
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
mkdir -p raw/appreviews
curl -sS --compressed -m 25 -A "$UA" "https://itunes.apple.com/rss/customerreviews/direct/rssfeed?id=$2&country=us&limit=200" -o "raw/appreviews/appstore_$1.xml" -w "$1 %{http_code} %{size_download}\n"
