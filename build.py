#!/usr/bin/env python3
"""Builds the UltraVena site.

    python3 build.py

Reads content/*.md and content/home.json and writes the pages into docs/.
Images, PDFs, styles and 3D models live in docs/assets/ and are left alone.
GitHub Pages serves docs/ as it is, so there is no build step on GitHub's side.
Needs Python 3 and the 'markdown' package (pip install markdown).
"""
import html, json, re
from pathlib import Path
import markdown

ROOT = Path(__file__).parent
SRC, OUT = ROOT / 'content', ROOT / 'docs'
SITE = 'UltraVena'
MONTHS = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()


def esc(s):
    return html.escape(str(s), quote=True)


def nice_date(iso):
    y, m, d = iso.split('-')
    return f'{int(d)} {MONTHS[int(m) - 1]} {y}'


def read_page(path):
    text = path.read_text(encoding='utf-8')
    meta = {}
    if text.startswith('---'):
        head, text = text[3:].split('\n---', 1)
        for line in head.strip().splitlines():
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip()
    meta['slug'] = path.stem
    meta['order'] = int(meta.get('order', 99))
    return meta, text.lstrip('\n')


def render_md(text):
    md = markdown.Markdown(extensions=['tables', 'toc', 'attr_list', 'md_in_html', 'sane_lists'],
                           extension_configs={'toc': {'permalink': False, 'toc_depth': '2-3'}})
    body = md.convert(text)
    # task lists
    body = re.sub(r'<li>(\s*<p>)?\[ \] ', r'<li class="task">\1<span class="box" aria-hidden="true"></span>', body)
    body = re.sub(r'<li>(\s*<p>)?\[x\] ', r'<li class="task done">\1<span class="box" aria-hidden="true"></span>', body, flags=re.I)
    body = body.replace('<ul>\n<li class="task', '<ul class="tasks">\n<li class="task')
    # wide tables scroll inside their own box
    body = body.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
    # outside links open in a new tab
    body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', body)
    # pictures: lazy, and a paragraph holding only a picture becomes a figure with its alt text as caption
    def fig(m):
        attrs = m.group(1)
        alt = re.search(r'alt="([^"]*)"', attrs)
        cls = re.search(r'class="([^"]*)"', attrs)
        cap = f'<figcaption>{alt.group(1)}</figcaption>' if alt and alt.group(1) else ''
        return f'<figure class="{cls.group(1) if cls else "plain"}"><img loading="lazy" {attrs}>{cap}</figure>'
    body = re.sub(r'<p><img ([^>]*?)\s*/?></p>', fig, body)
    toc = [(t['id'], t['name']) for t in md.toc_tokens if t['level'] == 2]
    return body, toc


def shell(title, desc, current, pages, main, scripts=''):
    nav = ''.join(
        f'<a href="{"index" if p["slug"] == "index" else p["slug"]}.html"'
        f'{" aria-current=\"page\"" if p["slug"] == current else ""}>{esc(p["nav"])}</a>'
        for p in pages)
    full = SITE if current == 'index' else f'{title} · {SITE}'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/cad-iso.png">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="top-in">
    <a class="brand" href="index.html"><span class="dot" aria-hidden="true"></span>UltraVena</a>
    <input type="checkbox" id="menu" class="menu-toggle" aria-label="Open the menu">
    <label for="menu" class="menu-btn" aria-hidden="true"><span></span><span></span><span></span></label>
    <nav class="nav" aria-label="Main">{nav}</nav>
  </div>
</header>
<main id="main">
{main}
</main>
<footer class="foot">
  <div class="foot-in">
    <p><span class="dot" aria-hidden="true"></span>UltraVena · Team 7, Electrical and Systems Engineering, University of Pennsylvania</p>
    <p class="small">A student research prototype. It is not a medical device and has not been tested on patients.</p>
  </div>
</footer>
{scripts}
</body>
</html>
'''


def doc_page(meta, text, pages):
    body, toc = render_md(text)
    side = ''
    if len(toc) > 2:
        links = ''.join(f'<li><a href="#{i}">{esc(html.unescape(n))}</a></li>' for i, n in toc)
        side = f'<aside class="toc"><p class="toc-h">On this page</p><ol>{links}</ol></aside>'
    bits = [f'Updated {nice_date(meta["updated"])}'] if meta.get('updated') else []
    if meta.get('pdf'):
        bits.append(f'<a href="{meta["pdf"]}">Download as PDF</a>')
    main = f'''<div class="doc{" has-toc" if side else ""}">
{side}
<article class="prose">
<header class="doc-head">
<h1>{esc(meta["title"])}</h1>
<p class="lede">{esc(meta.get("summary", ""))}</p>
<p class="meta">{" · ".join(bits)}</p>
</header>
{body}
</article>
</div>'''
    scripts = ''
    if meta.get('scripts') == 'viewer':
        scripts = ('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n'
                   '<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>\n'
                   '<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>\n'
                   '<script src="assets/js/viewer.js"></script>')
    return shell(meta['title'], meta.get('summary', ''), meta['slug'], pages, main, scripts)


def latest_updates(text, n=3):
    items = []
    for block in re.split(r'(?m)^## ', text)[1:]:
        head, _, rest = block.partition('\n')
        date, _, title = head.partition(' · ')
        para = next((p.strip() for p in rest.split('\n\n') if p.strip()), '')
        items.append((date.strip(), title.strip(), para))
    return items[:n]


def home_page(h, pages, docs, updates):
    stats = ''.join(f'<div class="stat"><dt>{esc(s["l"])}</dt><dd>{esc(s["n"])}</dd></div>' for s in h['stats'])
    steps = ''.join(f'<li><h3>{esc(a)}</h3><p>{esc(b)}</p></li>' for a, b in h['steps'])
    label = {'done': 'Done', 'progress': 'In progress', 'todo': 'Not started'}
    status = ''.join(f'<li class="{s}"><span class="pill">{label[s]}</span><div><h3>{esc(a)}</h3><p>{esc(b)}</p></div></li>'
                     for a, s, b in h['status'])
    cards = ''.join(f'<a class="card" href="{d["slug"]}.html"><h3>{esc(d["title"])}</h3><p>{esc(d.get("summary", ""))}</p>'
                    f'<span class="go" aria-hidden="true">Read</span></a>' for d in docs)
    ups = ''.join(f'<li><time>{esc(d)}</time><div><h3>{esc(t)}</h3><p>{esc(p)}</p></div></li>' for d, t, p in updates)
    people = ''.join(f'<li><strong>{esc(n)}</strong><span>{esc(r)}</span></li>' for n, r in h['team']['people'])
    main = f'''<section class="hero">
  <div class="hero-text">
    <p class="eyebrow">{esc(h["tagline"])}</p>
    <h1>A machine that finds the vein and marks the spot.</h1>
    <p class="lede">{esc(h["lede"])}</p>
    <p class="stage"><span class="dot" aria-hidden="true"></span>{esc(h["stage"])}</p>
    <p class="actions"><a class="button" href="hardware.html">Read the hardware brief</a><a class="button ghost" href="cad.html">Turn the 3D model</a></p>
  </div>
  <figure class="hero-fig"><img src="assets/img/cad-hero.png" alt="CAD render of the UltraVena rig: an aluminium frame with three walls, a slanted front panel carrying an iPad and a red stop button, and an overhead gantry holding an ultrasound probe above an arm rest" width="1026" height="821"><figcaption>CAD version 7, Butterfly iQ3 version</figcaption></figure>
</section>
<section class="band"><dl class="stats">{stats}</dl></section>
<section class="block">
  <h2>How one scan runs</h2>
  <ol class="steps">{steps}</ol>
</section>
<section class="block">
  <h2>Where the project stands</h2>
  <ul class="status">{status}</ul>
</section>
<section class="block">
  <h2>The documents</h2>
  <div class="cards">{cards}</div>
</section>
<section class="block two">
  <div>
    <h2>Latest updates</h2>
    <ol class="updates">{ups}</ol>
    <p><a href="updates.html">All updates</a></p>
  </div>
  <div>
    <h2>The team</h2>
    <p>{esc(h["team"]["intro"])}</p>
    <ul class="people">{people}</ul>
  </div>
</section>'''
    return shell(SITE, h['lede'], 'index', pages, f'<div class="home">{main}</div>')


def main():
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob('*.html'):
        old.unlink()
    (OUT / '.nojekyll').write_text('')
    docs = sorted((read_page(p) for p in SRC.glob('*.md')), key=lambda x: x[0]['order'])
    pages = [{'slug': 'index', 'nav': 'Overview'}] + [m for m, _ in docs]
    for meta, text in docs:
        (OUT / f'{meta["slug"]}.html').write_text(doc_page(meta, text, pages), encoding='utf-8')
    home = json.loads((SRC / 'home.json').read_text(encoding='utf-8'))
    ups = latest_updates(next(t for m, t in docs if m['slug'] == 'updates'))
    cards = [m for m, _ in docs if m['slug'] not in ('updates', 'downloads')]
    (OUT / 'index.html').write_text(home_page(home, pages, cards, ups), encoding='utf-8')
    lost = '<div class="doc"><article class="prose"><header class="doc-head"><h1>Page not found</h1><p class="lede">That page does not exist. <a href="index.html">Go to the overview</a>.</p></header></article></div>'
    (OUT / '404.html').write_text(shell('Page not found', '', '', pages, lost), encoding='utf-8')
    print(f'Built {len(docs) + 2} pages into {OUT}')


if __name__ == '__main__':
    main()
