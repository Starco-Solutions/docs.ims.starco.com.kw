#!/usr/bin/env python3
"""Rebuild documentation discovery from one reviewed manifest; no network calls."""
import json, re
from pathlib import Path
from xml.sax.saxutils import escape
ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'maintainer/site-manifest.json').read_text())
origin = manifest['origin'].rstrip('/')
for entry in manifest['pages']:
    path = ROOT / entry['path']
    source = path.read_text()
    # Restrict replacement to known documentation origins, never API/example endpoints.
    source = source.replace('https://ims.starco.com.kw/', origin + '/')
    path.write_text(source)
lines = ['# IMS Documentation', '', '> Source-backed user and technical documentation. See the source baseline for version and verification limits.']
section = None
for entry in manifest['pages']:
    group = entry['path'].split('/')[0] if '/' in entry['path'] else 'Overview'
    if group != section:
        lines.extend(['', '## ' + group.replace('-', ' ').title()])
        section = group
    lines.append(f"- {origin}/{entry['path']} — {entry['summary']}")
(ROOT / 'llms.txt').write_text('\n'.join(lines) + '\n')
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f"  <url><loc>{escape(origin + '/' + e['path'])}</loc></url>\n" for e in manifest['pages']) + '</urlset>\n')
(ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + origin + '/sitemap.xml\n')
print(f"Updated discovery for {len(manifest['pages'])} pages at {origin}")
