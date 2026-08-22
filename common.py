#!/usr/bin/env python3
"""Shared constants and copy-independent helpers for the Runout Rank site.

This module holds everything that is the same in every language (URLs, dates,
the logo, the locale registry) plus the small helpers the per-language content
modules in locales/ need. It deliberately imports nothing from build.py or from
locales/, so the content modules can import it without a cycle.
"""

import json
import re

SITE_URL = "https://mylesieong.github.io/products/runout-rank/"
SITE_NAME = "Runout Rank"

# Every page carries a visible byline and machine-readable dates. FIRST_PUBLISHED is
# when the site went up; UPDATED is the date of the current copy. Individual pages can
# override either through the "published"/"updated" keys in a locale's PAGES.
AUTHOR_NAME = "Sai Ieong"
AUTHOR_URL = SITE_URL + "index.html"
FIRST_PUBLISHED = "2026-08-20"
UPDATED = "2026-08-22"
LASTMOD = UPDATED

PLAY_URL = "https://play.google.com/store/apps/details?id=com.municornio.app.tableinfinite"

LOGO_SVG = """<svg width="30" height="30" viewBox="0 0 64 64" aria-hidden="true" focusable="false">
      <rect width="64" height="64" rx="14" fill="#111413"/>
      <g transform="rotate(-14 32 32)">
        <rect x="-8" y="22" width="80" height="20" fill="#1B5E3B"/>
        <rect x="-8" y="20.4" width="80" height="1.6" fill="#404942"/>
        <rect x="11.6" y="27.6" width="8.8" height="8.8" transform="rotate(45 16 32)" fill="none" stroke="#E8DCC8" stroke-width="3.4"/>
        <rect x="43.6" y="27.6" width="8.8" height="8.8" transform="rotate(45 48 32)" fill="none" stroke="#E8DCC8" stroke-width="3.4"/>
        <rect x="26.5" y="26.5" width="11" height="11" transform="rotate(45 32 32)" fill="#F7BE1D"/>
      </g>
    </svg>"""

# --------------------------------------------------------------------------
# Locales
# --------------------------------------------------------------------------
# code     the hreflang value, and the key used everywhere in the build
# path     directory the locale is written into, relative to the site root
#          ("" is the root locale, which is also the x-default target)
# og       the og:locale value
# label    the language's own name, used in the language switcher
# The site ships one Chinese variant (Simplified) and European Portuguese.

LOCALES = [
    dict(code="en",      path="",     og="en_GB", label="English"),
    dict(code="zh-Hans", path="zh/",  og="zh_CN", label="简体中文"),
    dict(code="vi",      path="vi/",  og="vi_VN", label="Tiếng Việt"),
    dict(code="pt-PT",   path="pt/",  og="pt_PT", label="Português"),
    dict(code="ko",      path="ko/",  og="ko_KR", label="한국어"),
]

DEFAULT_LOCALE = "en"

# Pages that exist in every locale, in sitemap order, with their sitemap priority.
# 404.html is generated too but deliberately kept out of the sitemap.
SITEMAP_PAGES = [
    ("index.html", "1.0"),
    ("how-it-works.html", "0.9"),
    ("fargo-rate-alternative.html", "0.9"),
    ("pool-rating-without-a-league.html", "0.9"),
    ("absolute-vs-relative-pool-rating.html", "0.8"),
    ("levels.html", "0.8"),
    ("practice.html", "0.8"),
    ("runout-pro.html", "0.7"),
    ("pool-skill-level-test.html", "0.7"),
    ("faq.html", "0.6"),
    ("privacy-policy.html", "0.3"),
]


def locale_by_code(code):
    for loc in LOCALES:
        if loc["code"] == code:
            return loc
    raise KeyError(code)


def page_url(locale, slug):
    """Absolute URL of a slug within a locale. index.html is served as the bare directory."""
    return SITE_URL + locale["path"] + ("" if slug == "index.html" else slug)


# --------------------------------------------------------------------------
# Copy helpers used by the per-language content modules
# --------------------------------------------------------------------------

def pretty_date(ui, iso):
    """2026-08-22 -> the visible byline form, in the locale's own convention."""
    y, m, d = (int(part) for part in iso.split("-"))
    return ui["date_format"].format(y=y, m=m, d=d, month=ui["months"][m - 1])


def byline(ui, published, updated):
    """Visible authorship line. The <time> elements carry the machine-readable dates."""
    updated_part = ""
    if updated != published:
        updated_part = (f' <span aria-hidden="true">&middot;</span> {ui["byline_updated"]} '
                        f'<time datetime="{updated}">{pretty_date(ui, updated)}</time>')
    return f"""      <p class="byline">
        {ui["byline_by"]} <span class="byline-author">{AUTHOR_NAME}</span>{ui["byline_sep"]}
        {ui["author_title"]} <span aria-hidden="true">&middot;</span>
        {ui["byline_published"]} <time datetime="{published}">{pretty_date(ui, published)}</time>{updated_part}
      </p>"""


def breadcrumb(ui, label):
    return f"""      <nav class="breadcrumb" aria-label="{ui["breadcrumb_label"]}">
        <ol>
          <li><a href="index.html">{ui["nav_home"]}</a></li>
          <li>{label}</li>
        </ol>
      </nav>"""


def store_block(ui, centred=False):
    style = ' style="justify-content:center"' if centred else ""
    return f"""<div class="store-links"{style}>
        <a class="store-link" href="{PLAY_URL}"><span>{ui["store_get_it_on"]}</span><span>Google Play</span></a>
        <div class="store-link store-link--pending" aria-label="{ui["store_review_aria"]}"><span>{ui["store_in_review"]}</span><span>App Store</span></div>
      </div>"""


def faq_body(items):
    return "\n".join(
        f"""      <div class="faq-item">
        <h3>{q}</h3>
        <p>{a}</p>
      </div>"""
        for q, a in items
    )


def _plain(s):
    s = s.replace("&mdash;", "—").replace("&ldquo;", "“").replace("&rdquo;", "”")
    s = s.replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"<[^>]+>", "", s)


def faq_schema(items):
    entries = ",\n".join(
        '    {\n'
        '      "@type": "Question",\n'
        f'      "name": {json.dumps(_plain(q))},\n'
        f'      "acceptedAnswer": {{"@type": "Answer", "text": {json.dumps(_plain(a))}}}\n'
        '    }'
        for q, a in items
    )
    return f"""{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{entries}
  ]
}}"""


# --------------------------------------------------------------------------
# Structured data shared by every language
# --------------------------------------------------------------------------

AUTHOR_SCHEMA_TEMPLATE = """{{
      "@type": "Person",
      "name": "{name}",
      "jobTitle": {job},
      "url": "{url}"
    }}"""


def author_schema(ui):
    return AUTHOR_SCHEMA_TEMPLATE.format(
        name=AUTHOR_NAME, job=json.dumps(ui["author_title"]), url=AUTHOR_URL)


def article_schema(locale, ui, headline, description, slug, published, updated):
    return f"""{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {json.dumps(headline)},
  "description": {json.dumps(description)},
  "image": "{SITE_URL}assets/img/og-image.png",
  "author": {author_schema(ui)},
  "publisher": {{
    "@type": "Organization",
    "name": "{SITE_NAME}",
    "url": "{SITE_URL}"
  }},
  "datePublished": "{published}",
  "dateModified": "{updated}",
  "inLanguage": "{locale["code"]}",
  "mainEntityOfPage": "{page_url(locale, slug)}"
}}"""


def breadcrumb_schema(locale, ui, label, slug):
    return f"""{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": {json.dumps(ui["nav_home"])}, "item": "{SITE_URL}{locale["path"]}"}},
    {{"@type": "ListItem", "position": 2, "name": {json.dumps(_plain(label))}, "item": "{page_url(locale, slug)}"}}
  ]
}}"""


def app_schema(locale, ui):
    features = ",\n".join(f"    {json.dumps(f)}" for f in ui["app_features"])
    return f"""{{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Runout Rank",
  "applicationCategory": "SportsApplication",
  "applicationSubCategory": "Billiards training",
  "operatingSystem": "Android, iOS",
  "url": "{SITE_URL}{locale["path"]}",
  "image": "{SITE_URL}assets/img/og-image.png",
  "inLanguage": "{locale["code"]}",
  "description": {json.dumps(ui["app_description"])},
  "featureList": [
{features}
  ],
  "offers": {{
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "description": {json.dumps(ui["app_offer"])}
  }}
}}"""


def site_schema(locale, ui):
    return f"""{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "{SITE_NAME}",
  "url": "{SITE_URL}{locale["path"]}",
  "inLanguage": "{locale["code"]}",
  "description": {json.dumps(ui["tagline"])}
}}"""
