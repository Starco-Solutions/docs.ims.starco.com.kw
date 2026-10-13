#!/usr/bin/env python3
"""Offline documentation checks only. Does not run or contact IMS applications."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json, re, sys, xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
errors=[]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.ids=set();self.refs=[];self.tags={};self.canon=[];self.json=False;self.json_text=''
    def handle_starttag(self, tag, attrs):
        a=dict(attrs);self.tags[tag]=self.tags.get(tag,0)+1
        if 'id' in a:
            if a['id'] in self.ids:errors.append(f'{self.path}: duplicate id {a["id"]}')
            self.ids.add(a['id'])
        for attr in ['href','src']:
            if a.get(attr):self.refs.append(a[attr])
        if tag=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href'))
        if tag=='script' and a.get('type')=='application/ld+json':self.json=True;self.json_text=''
    def handle_data(self,data):
        if self.json:self.json_text+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.json:
            try:json.loads(self.json_text)
            except ValueError as ex:errors.append(f'{self.path}: invalid structured JSON: {ex}')
            self.json=False
pages={}
for f in ROOT.rglob('*.html'):
    if '.git' in f.parts:continue
    p=Page();p.path=f.relative_to(ROOT).as_posix();p.feed(f.read_text());pages[p.path]=p
manifest=json.loads((ROOT/'maintainer/site-manifest.json').read_text());origin=manifest['origin'].rstrip('/')
listed=[x['path'] for x in manifest['pages']]
if len(listed)!=len(set(listed)) or set(listed)!=set(pages):errors.append('Manifest coverage differs from HTML corpus')
for name,p in pages.items():
    for tag in ['html','head','body','main','h1']:
        if p.tags.get(tag)!=1:errors.append(f'{name}: expected exactly one {tag}')
    if p.canon!=[origin+'/' + ('' if name == 'index.html' else name)]:errors.append(f'{name}: canonical does not match manifest origin')
    for href in p.refs:
        u=urlsplit(href)
        if u.scheme or u.netloc:continue
        target=((ROOT/name).parent/unquote(u.path)).resolve() if u.path else ROOT/name
        if u.path.startswith('/'):target=ROOT/unquote(u.path.lstrip('/'))
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'{name}: missing local target {href}');continue
        if u.fragment and target.suffix=='.html':
            rel=target.relative_to(ROOT).as_posix()
            if unquote(u.fragment) not in pages[rel].ids:errors.append(f'{name}: missing fragment {href}')
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls=[e.text for e in ET.parse(ROOT/'sitemap.xml').findall('s:url/s:loc',ns)]
expected={origin+'/'+name for name in pages}
if len(urls)!=len(expected) or set(urls)!=expected:errors.append('Sitemap coverage/origin mismatch')
llms=re.findall(r'^- (https://\S+) — ',(ROOT/'llms.txt').read_text(),re.M)
if len(llms)!=len(expected) or set(llms)!=expected:errors.append('AI index coverage/origin mismatch')
if origin+'/sitemap.xml' not in (ROOT/'robots.txt').read_text():errors.append('Robots sitemap mismatch')
for f in ROOT.rglob('*.json'):
    if '.git' not in f.parts:
        try:json.loads(f.read_text())
        except ValueError as ex:errors.append(f'{f.relative_to(ROOT)}: invalid JSON {ex}')
css=(ROOT/'assets/css/docs.css').read_text()
if 'body.searching .search-hidden' not in css:errors.append('Fallback search hide selector missing')
print(f'Checked {len(pages)} HTML pages: local targets/fragments, basic document structure, JSON, manifest, canonical, sitemap, llms, robots, search selector.')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('PASS (static checks; no rendered UI, external-link reachability or application behavior validation)')
