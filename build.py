#!/usr/bin/env python3
"""Static site generator for the Runout Rank marketing site.

There is no framework and no build step in production: this script writes plain
.html files into this directory (English at the root, each other language into
its own subdirectory) and those files are what gets deployed.

    python3 build.py

The split of responsibilities is:

    common.py     constants, the locale registry, and copy helpers
    locales/*.py  all page copy, one module per language
    build.py      this file — layout, <head>, hreflang, sitemap. No copy.

To add a language, add an entry to common.LOCALES and a matching module in
locales/. Nothing here needs to change.

Change SITE_URL in common.py if the site moves to another domain; sitemap.xml,
canonical tags, hreflang and og:url all derive from it.
"""

import html
import importlib
import os
import re
from datetime import date

from common import (
    AUTHOR_NAME, DEFAULT_LOCALE, LASTMOD, LOCALES, LOGO_SVG, SITE_NAME, SITE_URL,
    SITEMAP_PAGES, breadcrumb, breadcrumb_schema, locale_by_code, page_url,
)

HERE = os.path.dirname(os.path.abspath(__file__))


def module_name(locale):
    """locales module for a locale code: "zh-Hans" -> locales.zh_hans."""
    return "locales." + locale["code"].lower().replace("-", "_")


def up(locale):
    """Relative prefix from a page in this locale back to the site root."""
    return "../" * locale["path"].count("/")


def cross_link(locale, other, slug):
    """Relative href from a page in `locale` to the same page in `other`."""
    return up(locale) + other["path"] + slug


# --------------------------------------------------------------------------
# Layout
# --------------------------------------------------------------------------

def header(locale, ui, current):
    items = "\n".join(
        '          <li><a href="{href}"{cur}>{label}</a></li>'.format(
            href=href,
            label=label,
            cur=' aria-current="page"' if href == current else "",
        )
        for href, label in ui["nav"]
    )
    return f"""  <a class="skip-link" href="#main">{ui["skip_link"]}</a>
  <header class="site-header">
    <div class="container">
      <a class="brand" href="index.html">
        {LOGO_SVG}
        Runout&nbsp;Rank
      </a>
      <nav class="site-nav" aria-label="{ui["nav_aria"]}">
        <ul>
{items}
        </ul>
      </nav>
    </div>
  </header>"""


def lang_switch(locale, ui, slug):
    """Footer language picker. Every locale carries every page, so each link is direct."""
    links = []
    for other in LOCALES:
        if other["code"] == locale["code"]:
            links.append(
                f'          <li><span aria-current="true" lang="{other["code"]}">{other["label"]}</span></li>')
        else:
            href = cross_link(locale, other, slug)
            links.append(f'          <li><a href="{href}" hreflang="{other["code"]}" '
                         f'lang="{other["code"]}">{other["label"]}</a></li>')
    joined = "\n".join(links)
    return f"""      <nav class="lang-switch" aria-label="{ui["lang_aria"]}">
        <h4>{ui["lang_current"]}</h4>
        <ul>
{joined}
        </ul>
      </nav>"""


def footer(locale, ui, slug):
    def links(entries):
        return "\n".join(f'            <li><a href="{href}">{label}</a></li>'
                         for href, label in entries)

    guides = links(ui["footer_links_guides"])
    copyright_line = ui["footer_copyright"].format(year=date.today().year, author=AUTHOR_NAME)
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="brand" href="index.html">{LOGO_SVG} Runout&nbsp;Rank</a>
          <p style="margin-top:12px;max-width:24rem">{ui["footer_blurb"]}</p>
        </div>
        <div>
          <h4>{ui["footer_col_app"]}</h4>
          <ul>
{links(ui["footer_links_app"])}
          </ul>
        </div>
        <div>
          <h4>{ui["footer_col_guides"]}</h4>
          <ul>
{guides}
            <li><a href="{up(locale)}sitemap.xml">{ui["footer_sitemap"]}</a></li>
          </ul>
        </div>
      </div>
{lang_switch(locale, ui, slug)}
      <div class="footer-bottom">
        <span>{copyright_line}</span>
        <span>Part of <a href="https://mylesieong.github.io/">Sai vs. Reality</a></span>
        <span>{ui["footer_platforms"]}</span>
      </div>
      <p class="disclaimer">{ui["footer_disclaimer"]}</p>
    </div>
  </footer>"""


def alternates(slug):
    """hreflang set. Every page exists in every language, so the set is always complete."""
    out = []
    for other in LOCALES:
        out.append(f'  <link rel="alternate" hreflang="{other["code"]}" '
                   f'href="{page_url(other, slug)}">')
    default = locale_by_code(DEFAULT_LOCALE)
    out.append(f'  <link rel="alternate" hreflang="x-default" href="{page_url(default, slug)}">')
    return "\n".join(out) + "\n"


def page(locale, ui, slug, title, description, body, extra_schema=None, noindex=False,
         keywords=None, published=None, updated=None, dated=False):
    from common import FIRST_PUBLISHED, UPDATED
    root = up(locale)
    canonical = page_url(locale, slug)
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    published = published or FIRST_PUBLISHED
    updated = updated or UPDATED
    schema = ""
    if extra_schema:
        for blk in extra_schema:
            schema += f'  <script type="application/ld+json">\n{blk}\n  </script>\n'
    kw = f'  <meta name="keywords" content="{html.escape(keywords)}">\n' if keywords else ""
    dates = "" if not dated else f"""  <meta name="author" content="{AUTHOR_NAME}">
  <meta name="date" content="{published}">
  <meta name="last-modified" content="{updated}">
  <meta property="article:author" content="{AUTHOR_NAME}">
  <meta property="article:published_time" content="{published}">
  <meta property="article:modified_time" content="{updated}">
"""
    alts = "" if noindex else alternates(slug)
    return f"""<!DOCTYPE html>
<html lang="{locale["code"]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
{kw}  <meta name="robots" content="{robots}">
  <meta name="theme-color" content="#111413">
  <meta name="color-scheme" content="dark">
  <link rel="canonical" href="{canonical}">
{alts}  <link rel="stylesheet" href="{root}assets/css/style.css">
  <link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="{root}assets/img/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="{root}assets/img/apple-touch-icon.png">
  <link rel="manifest" href="{root}site.webmanifest">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE_URL}assets/img/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{html.escape(ui["og_image_alt"])}">
  <meta property="og:locale" content="{locale["og"]}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(description)}">
  <meta name="twitter:image" content="{SITE_URL}assets/img/og-image.png">
{dates}{schema}</head>
<body>
{header(locale, ui, slug)}
  <main id="main">
{fix_asset_paths(body, root)}
  </main>
{footer(locale, ui, slug)}
</body>
</html>
"""


def fix_asset_paths(body, root):
    """Page bodies are written with root-relative asset paths; subdirectories need a prefix."""
    if not root:
        return body
    return re.sub(r'(src|href)="(assets/)', rf'\1="{root}\2', body)


# --------------------------------------------------------------------------
# Markdown (privacy policy)
# --------------------------------------------------------------------------

def markdown_to_html(md):
    """A deliberately small Markdown subset: headings, lists, tables, bold, code, links, rules."""
    out = []
    lines = md.split("\n")
    i = 0
    in_ul = False

    def inline(t):
        t = html.escape(t, quote=False)
        t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
        t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
        t = re.sub(r"(?<![\"=>])\b(https?://[^\s<)|]+)", r'<a href="\1">\1</a>', t)
        return t

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("      </ul>")
            in_ul = False

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()
        if not stripped:
            close_ul()
            i += 1
            continue
        if stripped.startswith("|"):
            close_ul()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], rows[2:] if len(rows) > 2 else []
            out.append('      <div class="table-wrap"><table>')
            out.append("        <thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>")
            out.append("        <tbody>")
            for r in body:
                out.append("          <tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("        </tbody></table></div>")
            continue
        if stripped.startswith("---"):
            close_ul()
            out.append('      <hr class="rule">')
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            close_ul()
            level = len(m.group(1))
            # The document's H1 is already rendered in the page head.
            if level > 1:
                out.append(f"      <h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue
        if stripped.startswith("- "):
            if not in_ul:
                out.append('      <ul>')
                in_ul = True
            out.append(f"        <li>{inline(stripped[2:])}</li>")
            i += 1
            continue
        close_ul()
        out.append(f"      <p>{inline(stripped)}</p>")
        i += 1
    close_ul()
    return "\n".join(out)


def privacy_source(locale):
    """Per-language privacy policy Markdown, falling back to English if one is missing."""
    code = locale["code"].lower().replace("-", "_")
    for name in (f"privacy-policy.{code}.md", "privacy-policy.md"):
        path = os.path.join(HERE, "content", name)
        if os.path.exists(path):
            return path
    raise FileNotFoundError("no privacy policy markdown found")


def privacy_body(locale, ui):
    with open(privacy_source(locale), encoding="utf-8") as fh:
        md = fh.read()
    return f"""  <section class="page-head">
    <div class="container">
{breadcrumb(ui, ui["privacy_breadcrumb"])}
      <h1>{ui["privacy_h1"]}</h1>
      <p class="lead">{ui["privacy_lead"]}</p>
    </div>
  </section>

  <section>
    <div class="container prose">
{markdown_to_html(md)}
    </div>
  </section>
"""


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------

def build_locale(locale):
    mod = importlib.import_module(module_name(locale))
    ui = mod.UI
    out_dir = os.path.join(HERE, locale["path"]) if locale["path"] else HERE
    os.makedirs(out_dir, exist_ok=True)
    written = []

    def write(slug, markup):
        with open(os.path.join(out_dir, slug), "w", encoding="utf-8") as fh:
            fh.write(markup)
        written.append(locale["path"] + slug)

    for spec in mod.PAGES:
        slug = spec["slug"]
        write(slug, page(locale, ui, slug, spec["title"], spec["description"], spec["body"],
                         spec["schema"], keywords=spec.get("keywords"),
                         published=spec.get("published"), updated=spec.get("updated"),
                         dated=spec.get("dated", False)))

    write("privacy-policy.html", page(
        locale, ui, "privacy-policy.html", ui["privacy_title"], ui["privacy_description"],
        privacy_body(locale, ui),
        [breadcrumb_schema(locale, ui, ui["privacy_breadcrumb"], "privacy-policy.html")]))

    write("404.html", page(locale, ui, "404.html", ui["not_found_title"],
                           ui["not_found_description"], mod.NOT_FOUND, None, noindex=True))
    return written


def sitemap():
    """One <url> per language per page, each listing the whole hreflang set."""
    entries = []
    for slug, priority in SITEMAP_PAGES:
        alts = "\n".join(
            f'    <xhtml:link rel="alternate" hreflang="{loc["code"]}" href="{page_url(loc, slug)}"/>'
            for loc in LOCALES)
        default = locale_by_code(DEFAULT_LOCALE)
        alts += (f'\n    <xhtml:link rel="alternate" hreflang="x-default" '
                 f'href="{page_url(default, slug)}"/>')
        for loc in LOCALES:
            entries.append(f"""  <url>
    <loc>{page_url(loc, slug)}</loc>
{alts}
    <lastmod>{LASTMOD}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(entries)}
</urlset>
"""


def main():
    written = []
    for locale in LOCALES:
        written += build_locale(locale)

    with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(sitemap())
    written.append("sitemap.xml")

    with open(os.path.join(HERE, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}sitemap.xml
""")
    written.append("robots.txt")

    with open(os.path.join(HERE, "site.webmanifest"), "w", encoding="utf-8") as fh:
        fh.write("""{
  "name": "Runout Rank",
  "short_name": "Runout Rank",
  "description": "Absolute pool skill rating test and training app for Android and iOS. A 0-100 rating from one ten-table session, with no league required.",
  "start_url": "./",
  "display": "standalone",
  "background_color": "#111413",
  "theme_color": "#111413",
  "icons": [
    { "src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "assets/img/apple-touch-icon.png", "sizes": "180x180", "type": "image/png" },
    { "src": "assets/img/favicon-32.png", "sizes": "32x32", "type": "image/png" }
  ]
}
""")
    written.append("site.webmanifest")

    print(f"wrote {len(written)} files across {len(LOCALES)} languages:\n  "
          + "\n  ".join(written))


if __name__ == "__main__":
    main()
