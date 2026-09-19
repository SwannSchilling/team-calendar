#!/usr/bin/env python3
import sys, json, urllib.request, urllib.parse, gzip, zlib
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass
UA="Mozilla/5.0"
def _get(url, timeout=30):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept-Encoding":"gzip, deflate"})
    with urllib.request.urlopen(req,timeout=timeout) as r:
        b=r.read(); e=(r.headers.get("Content-Encoding") or "").lower()
        if "gzip" in e:
            try: b=gzip.decompress(b)
            except Exception: pass
        elif "deflate" in e:
            try: b=zlib.decompressobj(b).read()
            except Exception: pass
        return b.decode("utf-8","replace")
def search(term, country="us", limit=12):
    u=f"https://itunes.apple.com/search?term={urllib.parse.quote_plus(term)}&entity=software&country={country}&limit={limit}"
    try: d=json.loads(_get(u))
    except Exception as e: print(f"  [{term}] ERR {e}"); return
    rs=d.get("results",[])
    if not rs: print(f"  [{term}] -> no App Store software results for term in {country}"); return
    for r in rs:
        print(f"  [{term}] {r.get('trackName')!r} | seller={r.get('sellerName')!r} bundle={r.get('bundleId')!r}")
        print(f"        id={r.get('trackId')} releaseDate={r.get('releaseDate')} curVerRel={r.get('currentVersionReleaseDate')} ratingCount={r.get('userRatingCount')} price={r.get('formattedPrice')} url={r.get('trackViewUrl')}")
        print(f"        descSnippet={(r.get('description') or '')[:140]!r}")
def lookup(track_ids, country="us"):
    ids = track_ids if isinstance(track_ids,(list,tuple)) else [track_ids]
    u=f"https://itunes.apple.com/lookup?id={','.join(map(str,ids))}&country={country}"
    try: d=json.loads(_get(u))
    except Exception as e: print(f"  lookup ERR {e}"); return
    for r in d.get("results",[]):
        print("=====")
        print("trackName       :", r.get("trackName"))
        print("sellerName      :", r.get("sellerName"), "| artistName:", r.get("artistName"))
        print("bundleId        :", r.get("bundleId"))
        print("trackId         :", r.get("trackId"))
        print("releaseDate     :", r.get("releaseDate"), "| curVerRelease:", r.get("currentVersionReleaseDate"), "| version:", r.get("version"))
        print("price           :", r.get("formattedPrice"), "| currency:", r.get("priceCurrency"))
        print("ratingCount     :", r.get("userRatingCount"), "| avgRating:", round(r.get("averageUserRating") or 0,2))
        print("genres          :", r.get("genres"))
        print("url             :", r.get("trackViewUrl"))
        print("--- FULL DESCRIPTION ---")
        print((r.get("description") or "").strip())
if __name__=="__main__":
    country="us"; args=sys.argv[1:]
    if args and args[0].startswith("--country="): country=args[0].split("=",1)[1]; args=args[1:]
    if args and args[0]=="--ids":
        lookup(args[1].split(","), country); raise SystemExit
    for t in args:
        print(f"== query {t!r} country={country} =="); search(t,country)
