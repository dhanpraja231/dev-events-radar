#!/usr/bin/env python3
"""Cheap daily HTTP link check. Updates link_status/link_checked in data/events.json for upcoming events.
ok=2xx/3xx; broken=404/410/5xx/DNS/conn error/parked; uncertain=401/403/429/999/timeout. 'fixed' is kept if still ok.
Usage: python3 scripts/linkcheck.py [--all]   (prints events that need an LLM fix)"""
import json,re,sys,datetime,concurrent.futures as cf,requests
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36','Accept':'text/html,*/*','Accept-Language':'en-US,en'}
PARK=re.compile(r'domain (is )?for sale|buy this domain|parked (free|domain)|sedoparking|hugedomains|This domain may be for sale',re.I)
def chk(u):
  if not u: return 'broken'
  try:
    r=requests.get(u,headers=UA,timeout=20,allow_redirects=True);c=r.status_code
    if c in (404,410) or c>=500: return 'broken'
    if c in (401,403,429,999): return 'uncertain'
    if PARK.search(r.text[:20000]): return 'broken'
    return 'ok' if c<400 else 'uncertain'
  except requests.exceptions.ConnectionError: return 'broken'
  except Exception: return 'uncertain'
P='data/events.json';ev=json.load(open(P))
today=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5,minutes=30))).date().isoformat()
todo=[e for e in ev if '--all' in sys.argv or e['end_date']>=today]
with cf.ThreadPoolExecutor(16) as ex: res=list(ex.map(lambda e:chk(e['url']),todo))
for e,s in zip(todo,res):
  e['link_status']='fixed' if (s=='ok' and e.get('link_status')=='fixed') else s; e['link_checked']=today
json.dump(ev,open(P,'w'),indent=1,ensure_ascii=False)
from collections import Counter;print(Counter(res))
for e in todo:
  if e['link_status']=='broken': print('BROKEN',e['id'],e['url'])
