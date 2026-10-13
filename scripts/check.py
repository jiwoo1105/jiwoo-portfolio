#!/usr/bin/env python3
"""Check the generated site independently of its content and template."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
issues = []


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs, self.lang, self.h1 = [], [], None, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.lang = a.get('lang')
        if tag == 'h1':
            self.h1 += 1
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'img' and 'alt' not in a:
            issues.append(f'{current}: image missing alt')
        for key in ('src', 'href', 'poster'):
            if key in a:
                self.refs.append((a[key], tag, 'data-language-link' in a))


pages = {}
for current in sorted(ROOT.rglob('*.html')):
    page = Page()
    page.feed(current.read_text())
    pages[current] = page
    expected = 'en' if current.relative_to(ROOT).parts[0] == 'en' else 'ko'
    if page.lang != expected or page.h1 != 1:
        issues.append(f'{current}: language or main heading mismatch')
    for ident, count in Counter(page.ids).items():
        if count > 1:
            issues.append(f'{current}: duplicate ID {ident}')

for current, page in pages.items():
    for ref, tag, language_switch in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        target = (current.parent / unquote(url.path)).resolve() if url.path else current
        if target.is_dir():
            target /= 'index.html'
        if not target.is_file():
            issues.append(f'{current}: missing {ref}')
        elif target in pages:
            if url.fragment and url.fragment not in pages[target].ids:
                issues.append(f'{current}: missing fragment {ref}')
            if tag == 'a' and not language_switch and page.lang != pages[target].lang:
                issues.append(f'{current}: navigation crosses languages: {ref}')
    if page.lang == 'ko':
        alternate = ROOT / 'en' / current.relative_to(ROOT)
        if alternate not in pages or set(page.ids) != set(pages[alternate].ids):
            issues.append(f'{current}: counterpart missing or section IDs differ')

for issue in issues:
    print(issue)
print(f'Checked {len(pages)} pages and {sum(len(p.refs) for p in pages.values())} references: {len(issues)} issues.')
raise SystemExit(bool(issues))
