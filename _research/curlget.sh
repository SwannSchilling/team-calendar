#!/usr/bin/bash
# curlget.sh URL [maxchars] -> cleaned text (curl UA)
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
curl -sSL -m 25 -A "$UA" -H "Accept-Language: en-US,en;q=0.9" "$1" | python htmlx.py "${2:-6000}"
