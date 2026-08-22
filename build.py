#!/usr/bin/env python3
"""Static site generator for the Runout Rank marketing site.

There is no framework and no build step in production: this script writes plain
.html files into this same directory, and those files are what gets deployed.
Re-run it after editing PAGES below:

    python3 build.py

Change SITE_URL if the site moves to another domain; sitemap.xml, canonical
tags and og:url all derive from it.
"""

import html
import json
import os
import re
from datetime import date

SITE_URL = "https://mylesieong.github.io/products/runout-rank/"
SITE_NAME = "Runout Rank"
TAGLINE = "Absolute pool skill rating test and training app for Android and iOS"

# Every page carries a visible byline and machine-readable dates. FIRST_PUBLISHED is
# when the site went up; UPDATED is the date of the current copy. Individual pages can
# override either through the "published"/"updated" keys in PAGES.
AUTHOR_NAME = "Sai Ieong"
AUTHOR_TITLE = "Creator of Runout Rank"
AUTHOR_URL = SITE_URL + "index.html"
FIRST_PUBLISHED = "2026-08-20"
UPDATED = "2026-08-22"
LASTMOD = UPDATED

HERE = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Home"),
    ("how-it-works.html", "How it works"),
    ("levels.html", "Levels"),
    ("practice.html", "Practice"),
    ("fargo-rate-alternative.html", "vs Fargo Rate"),
    ("runout-pro.html", "Runout Pro"),
    ("faq.html", "FAQ"),
]

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

PLAY_URL = "https://play.google.com/store/apps/details?id=com.municornio.app.tableinfinite"

STORE_BLOCK = f"""<div class="store-links">
        <a class="store-link" href="{PLAY_URL}"><span>Get it on</span><span>Google Play</span></a>
        <div class="store-link store-link--pending" aria-label="In review for the App Store"><span>In review</span><span>App Store</span></div>
      </div>"""


def pretty_date(iso):
    """2026-08-22 -> 22 August 2026, the form used in the visible byline."""
    y, m, d = (int(part) for part in iso.split("-"))
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return f"{d} {months[m - 1]} {y}"


def byline(published, updated):
    """Visible authorship line. The <time> elements carry the machine-readable dates."""
    updated_part = ""
    if updated != published:
        updated_part = (f' <span aria-hidden="true">&middot;</span> Updated '
                        f'<time datetime="{updated}">{pretty_date(updated)}</time>')
    return f"""      <p class="byline">
        By <span class="byline-author">{AUTHOR_NAME}</span>,
        {AUTHOR_TITLE} <span aria-hidden="true">&middot;</span>
        Published <time datetime="{published}">{pretty_date(published)}</time>{updated_part}
      </p>"""


AUTHOR_SCHEMA = f"""{{
      "@type": "Person",
      "name": "{AUTHOR_NAME}",
      "jobTitle": "{AUTHOR_TITLE}",
      "url": "{AUTHOR_URL}"
    }}"""


def article_schema(headline, description, slug, published, updated):
    return f"""{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {json.dumps(headline)},
  "description": {json.dumps(description)},
  "image": "{SITE_URL}assets/img/og-image.png",
  "author": {AUTHOR_SCHEMA},
  "publisher": {{
    "@type": "Organization",
    "name": "{SITE_NAME}",
    "url": "{SITE_URL}"
  }},
  "datePublished": "{published}",
  "dateModified": "{updated}",
  "inLanguage": "en",
  "mainEntityOfPage": "{SITE_URL}{slug}"
}}"""


def header(current):
    items = "\n".join(
        '          <li><a href="{href}"{cur}>{label}</a></li>'.format(
            href=href,
            label=label,
            cur=' aria-current="page"' if href == current else "",
        )
        for href, label in NAV
    )
    return f"""  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container">
      <a class="brand" href="index.html">
        {LOGO_SVG}
        Runout&nbsp;Rank
      </a>
      <nav class="site-nav" aria-label="Primary">
        <ul>
{items}
        </ul>
      </nav>
    </div>
  </header>"""


FOOTER = f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="brand" href="index.html">{LOGO_SVG} Runout&nbsp;Rank</a>
          <p style="margin-top:12px;max-width:24rem">An absolute pool rating from a ten-table run-out
          test on your own table. A 0&ndash;100 number in one sitting &mdash; no league, no 200-game wait,
          no account, no internet needed.</p>
        </div>
        <div>
          <h4>The app</h4>
          <ul>
            <li><a href="how-it-works.html">How it works</a></li>
            <li><a href="levels.html">The six levels</a></li>
            <li><a href="practice.html">Practice &amp; training log</a></li>
            <li><a href="runout-pro.html">Runout Pro</a></li>
          </ul>
        </div>
        <div>
          <h4>Guides</h4>
          <ul>
            <li><a href="fargo-rate-alternative.html">Fargo Rate alternative</a></li>
            <li><a href="pool-rating-without-a-league.html">A rating without a league</a></li>
            <li><a href="absolute-vs-relative-pool-rating.html">Absolute vs relative ratings</a></li>
            <li><a href="pool-skill-level-test.html">Pool skill level test guide</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="privacy-policy.html">Privacy policy</a></li>
            <li><a href="sitemap.xml">Sitemap</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; {date.today().year} Runout Rank. Written and built by {AUTHOR_NAME}.</span>
        <span>Android &amp; iOS &middot; Dark mode only, like the app</span>
      </div>
      <p class="disclaimer">Fargo Rate and FargoRate are trademarks of their respective owner.
      Runout Rank is an independent app and is not affiliated with, endorsed by, or connected to
      FargoRate, the BCA, the APA or any league operator. Comparisons on this site describe published
      behaviour of those systems and are offered for the reader&rsquo;s own judgement.</p>
    </div>
  </footer>"""


CTA = f"""  <section class="cta band">
    <div class="container">
      <p class="eyebrow">Get the number</p>
      <h2>Ten tables. One attempt each. One honest rating.</h2>
      <p class="lead" style="max-width:38rem;margin:0 auto 28px">Set the layouts up on the table you
      already play on. The app scores the run-outs and tells you which level to train at next.</p>
      {STORE_BLOCK.replace('class="store-links"', 'class="store-links" style="justify-content:center"')}
    </div>
  </section>"""


def page(slug, title, description, body, extra_schema=None, noindex=False, keywords=None,
         published=None, updated=None, dated=False):
    canonical = SITE_URL + ("" if slug == "index.html" else slug)
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    published = published or FIRST_PUBLISHED
    updated = updated or UPDATED
    schema = ""
    if extra_schema:
        for block in extra_schema:
            schema += f'  <script type="application/ld+json">\n{block}\n  </script>\n'
    kw = f'  <meta name="keywords" content="{html.escape(keywords)}">\n' if keywords else ""
    dates = "" if not dated else f"""  <meta name="author" content="{AUTHOR_NAME}">
  <meta name="date" content="{published}">
  <meta name="last-modified" content="{updated}">
  <meta property="article:author" content="{AUTHOR_NAME}">
  <meta property="article:published_time" content="{published}">
  <meta property="article:modified_time" content="{updated}">
"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
{kw}  <meta name="robots" content="{robots}">
  <meta name="theme-color" content="#111413">
  <meta name="color-scheme" content="dark">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE_URL}assets/img/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Runout Rank — how good are you at pool, really?">
  <meta property="og:locale" content="en_GB">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(description)}">
  <meta name="twitter:image" content="{SITE_URL}assets/img/og-image.png">
{dates}{schema}</head>
<body>
{header(slug)}
  <main id="main">
{body}
  </main>
{FOOTER}
</body>
</html>
"""


def breadcrumb(label):
    return f"""      <nav class="breadcrumb" aria-label="Breadcrumb">
        <ol>
          <li><a href="index.html">Home</a></li>
          <li>{label}</li>
        </ol>
      </nav>"""


def breadcrumb_schema(label, slug):
    return f"""{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE_URL}"}},
    {{"@type": "ListItem", "position": 2, "name": "{label}", "item": "{SITE_URL}{slug}"}}
  ]
}}"""


APP_SCHEMA = f"""{{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Runout Rank",
  "applicationCategory": "SportsApplication",
  "applicationSubCategory": "Billiards training",
  "operatingSystem": "Android, iOS",
  "url": "{SITE_URL}",
  "image": "{SITE_URL}assets/img/og-image.png",
  "description": "Runout Rank is an absolute billiards skill-rating app. Take a ten-table run-out test on a real pool table, get a 0-100 rating and a tier from Rookie to Master in a single session, then practise at the level that beats you. The rating measures you against fixed layouts rather than against local opponents, so it needs no league, no 200-game history and no opponents at all. All data stays on your device.",
  "featureList": [
    "Absolute rating: measured against fixed generated layouts, not against local opponents",
    "A full 0-100 rating from one ten-table session, with no minimum game count to serve out",
    "Portable between cities, leagues and countries because the yardstick never changes",
    "Ten-table Rating Test with a 0-100 rating and a named tier",
    "Six challenge levels from Rookie to Master",
    "Fixed level constraints, so the same rating means the same thing anywhere",
    "Endless randomly generated practice layouts",
    "Training log with favourites",
    "Lifetime run-out rate, streaks and per-level statistics",
    "Works fully offline with no account"
  ],
  "offers": {{
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "description": "Free to download. Optional Runout Pro subscription unlocks progress history and CSV export."
  }}
}}"""

SITE_SCHEMA = f"""{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "{SITE_NAME}",
  "url": "{SITE_URL}",
  "description": "{TAGLINE}"
}}"""


# --------------------------------------------------------------------------
# Page bodies
# --------------------------------------------------------------------------

INDEX = f"""  <section class="hero">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow">Absolute pool rating &middot; Android &amp; iOS</p>
        <h1>Your pool rating. <span class="accent">Tonight</span>, not in 200 games.</h1>
        <p class="lead">League ratings need hundreds of matches before the number means anything, and
        what you get depends on who your city happens to have. Runout Rank measures you against the
        table instead: ten layouts, one attempt each, a 0&ndash;100 rating in one session.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="{PLAY_URL}">Get it on Google Play</a>
          <a class="btn btn--ghost" href="how-it-works.html">How the test works</a>
        </div>
        <p class="hero-note">No league &middot; No opponents &middot; No account &middot; Works offline</p>
      </div>
      <div class="hero-shot">
        <div class="phone">
          <img src="assets/img/screen-home.png" width="1080" height="2400"
               alt="Runout Rank home screen on a phone, offering to start the ten-table Rating Test."
               fetchpriority="high" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <section class="tight band">
    <div class="container">
      <div class="grid grid--4">
        <div><span class="stat">10</span><p class="dim">tables per test, one attempt each</p></div>
        <div><span class="stat">1</span><p class="dim">session to a full rating, not a 200-game wait</p></div>
        <div><span class="stat">0&ndash;100</span><p class="dim">rating and a tier, the moment you finish</p></div>
        <div><span class="stat">0</span><p class="dim">leagues, opponents and accounts required</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Why bother</p>
        <h2>A league rating costs a season <span class="accent">and still moves with your city.</span></h2>
      </div>
      <div class="compare">
        <div class="card pain">
          <h3>200 games before it is real</h3>
          <p>FargoRate treats 200 games as the minimum for an established rating. That is a league, a
          season and a set of fees before you find out where you stand.</p>
          <p><a href="pool-rating-without-a-league.html">A rating without a league &rarr;</a></p>
        </div>
        <div class="card pain">
          <h3>Your number describes your postcode</h3>
          <p>A relative rating is anchored to the players around you, so a thin or isolated local scene
          drifts against the rest of the world.</p>
          <p><a href="absolute-vs-relative-pool-rating.html">Absolute vs relative &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">The answer</p>
        <h2>Measure the player against the <span class="accent">table</span>, not the room.</h2>
        <p class="lead">Every level fixes exactly what makes it hard &mdash; ball count, ball in hand,
        how tightly the balls are packed, blockers. Those constraints are the yardstick, and they are
        the same for everyone. Beat them and the number goes up. Nothing else moves it.</p>
      </div>
      <div class="grid grid--3">
        <div class="card">
          <h3>Absolute, not relative</h3>
          <p>No opponent pool to be strong or weak, and nothing to drift against.</p>
        </div>
        <div class="card">
          <h3>One session, not one season</h3>
          <p>About an hour at the table, and you finish with a real rating rather than a placeholder.</p>
        </div>
        <div class="card">
          <h3>Nothing to memorise</h3>
          <p>Layouts are generated fresh for every test, so you meet the level, never a drill you have
          already learned the answer to.</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="fargo-rate-alternative.html">The full comparison with Fargo Rate &rarr;</a></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">How it works</p>
        <h2>Three steps, one sitting</h2>
      </div>
      <div class="grid grid--3 steps">
        <div class="card step">
          <h3>Rack what the app draws</h3>
          <p>Each table is drawn top-down, so you can set the exact layout up in front of you.</p>
        </div>
        <div class="card step">
          <h3>Play it once</h3>
          <p>Run out or miss, then record it with one tap. No retries, no skips.</p>
        </div>
        <div class="card step">
          <h3>Get a rating and a plan</h3>
          <p>A score, a rating, your tier &mdash; and the level that is beating you, to practise at next.</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="how-it-works.html">Read the full explanation &rarr;</a></p>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-test.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="A Rating Test in progress: table 6 of 10 drawn top-down with four numbered object balls on the cloth, and the Ran out and Missed buttons below."></div>
        </div>
        <div>
          <p class="eyebrow">The table</p>
          <h3>This is what a table looks like.</h3>
          <p>Each one is drawn top-down, to scale, so you can rack it on the cloth in front of you and
          play the real shot. It stays on screen for the whole attempt, so you can rebuild the layout
          if you knock it about.</p>
          <ul class="ticks">
            <li><strong>The numbers are the order</strong> you have to pot them in &mdash; not ball values</li>
            <li><strong>Blockers</strong> are drawn drab and unnumbered: in your way, not in the sequence</li>
            <li><strong>The cue ball</strong> appears from Advanced up. Below that you have ball in hand</li>
          </ul>
        </div>
      </div>

      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-result.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="Test result screen showing 7 out of 10, a rating of 58, the League tier, and what to do next."></div>
        </div>
        <div>
          <p class="eyebrow">The result</p>
          <h3>A rating, and the level that <span class="gold">beats you</span>.</h3>
          <p>Seven out of ten clears a level. You get the score, the 0&ndash;100 rating, your tier and
          how far the number has moved since last time &mdash; then the level currently beating you,
          with practice at it one tap away.</p>
        </div>
      </div>

      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-progress.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="The progress screen showing rating, tier, lifetime metrics and per-level breakdown."></div>
        </div>
        <div>
          <p class="eyebrow">Progress</p>
          <h3>See whether practice is working.</h3>
          <p>Rating, tier, cleared level, lifetime run-out rate and best streak &mdash; free,
          permanently. <a href="runout-pro.html">Runout Pro</a> adds the history: every test plotted
          over time and CSV export.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--3">
        <div class="card">
          <h3>Six levels, none locked</h3>
          <p>Rookie to Master. Test at any of them &mdash; a strong player never grinds up from the
          bottom. <a href="levels.html">Compare the levels &rarr;</a></p>
        </div>
        <div class="card">
          <h3>Practice at your edge</h3>
          <p>Endless generated layouts at the level that beat you, with a log of everything you have
          run. <a href="practice.html">More on practice &rarr;</a></p>
        </div>
        <div class="card">
          <h3>Your record stays yours</h3>
          <p>No account, no server, works offline. Everything lives on your device.
          <a href="privacy-policy.html">Privacy policy &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

HOW = f"""  <section class="page-head">
    <div class="container">
{breadcrumb("How it works")}
      <h1>How the Runout Rank rating works</h1>
      <p class="lead">Ten generated tables, one attempt each, scored into a 0&ndash;100 rating and a
      named tier &mdash; and a clear instruction about what to do next.</p>
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>1. Pick a level and start the test</h2>
      <p>A Rating Test is ten tables at a single level. You choose the level: the app suggests one, but
      nothing is locked, so a strong player can start at Competitor rather than grinding up from
      Rookie. If you have never been rated, the test is one tap from the home screen &mdash; there is
      nothing to configure first.</p>
      <p>If you would rather warm up, you can generate a single practice table instead and take the
      test later.</p>

      <h2>2. Set each table up on a real table</h2>
      <p>Every table is drawn top-down with the cue ball, the object balls, and any blocker balls in
      place. Blockers are drawn deliberately drab and unnumbered so they never read as part of the
      potting order. You rack what you see, on the table you already play on. The illustration stays on
      screen for the whole attempt, so you can rebuild the layout if you disturb it.</p>

      <h2>3. Play it once, record it once</h2>
      <p>Run out, or do not. One tap records the result and moves you to the next table. The header
      always shows which table you are on out of ten, and the strip above the table shows which of the
      played tables were run-outs and which were misses.</p>
      <p><strong>There is exactly one attempt per table. No retries, no skips.</strong> That
      restriction is the whole reason the number at the end is worth anything.</p>
      <div class="note">Interrupted? Leave the test and come back later &mdash; it resumes at the exact
      table you stopped on. Deliberately quitting asks for a confirmation first, and tells you that a
      part-finished run cannot be scored.</div>

      <h2>4. Read the result</h2>
      <p>The moment the tenth table is recorded you get:</p>
      <ul>
        <li><strong>A score out of ten</strong> &mdash; how many of the ten you ran out.</li>
        <li><strong>A 0&ndash;100 rating</strong> and the <strong>tier</strong> that goes with it.</li>
        <li><strong>Cleared or not.</strong> Seven of ten clears the level.</li>
        <li><strong>Your rating delta</strong> &mdash; how far the number moved since your last test.</li>
        <li><strong>Your edge level</strong> &mdash; the level currently beating you, with a
        plain-language explanation of what to do about it.</li>
      </ul>
      <p>From that screen, practising at your edge level is one tap.</p>

      <h2>Why random layouts still produce a comparable score</h2>
      <p>Every test is generated fresh, so there are no answers to memorise and no drill you can
      rehearse in advance. Two players never meet the same ten tables &mdash; and they do not need to.</p>
      <p>What is fixed is the <strong>level</strong>. Ball count, whether you get ball in hand, the
      minimum spacing between balls and the number of blockers are defined constants, identical for
      everyone on both platforms. A Level&nbsp;4 test always asks a Level&nbsp;4 question. Ten tables
      is enough for the difficulty to average out, which is why the test is ten and not one.</p>
      <p>So the thing being measured is you against the level&rsquo;s constraints, not you against ten
      particular tables. That is what makes one player&rsquo;s 58 mean the same as another&rsquo;s.</p>

      <h2>Why the rating is absolute</h2>
      <p>No opponent appears anywhere in that calculation. League systems such as Fargo Rate are
      <em>relative</em> &mdash; your number is derived from results against other rated players, which
      is why they need a large game history before the rating settles, and why a weakly connected
      local scene can sit high or low against the rest of the network. Runout Rank compares you to a
      fixed standard instead. The level constraints are the same everywhere, so the rating is the same
      measurement everywhere, from the very first test.</p>
      <p>The one local variable is your equipment. Pocket cut, table size and cloth speed change how
      hard a run-out is, so take the test on the table you actually play on and compare your own
      numbers over time.</p>
      <p><a href="absolute-vs-relative-pool-rating.html">Absolute vs relative pool ratings &rarr;</a></p>

      <h2>What the rating is not</h2>
      <p>It is a measurement of your run-out ability on generated layouts, taken under a no-retry rule.
      It is not a handicap system, not a governing-body rating, and it does not talk to any league
      database. If you need a number to handicap a match, that is what a league rating is for &mdash;
      see <a href="fargo-rate-alternative.html">how the two compare</a>. This is an honest number you
      can take yourself, on your own table, whenever you want a fresh one.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="levels.html">See the six levels</a>
        <a class="btn btn--ghost" href="fargo-rate-alternative.html">Compared with Fargo Rate</a>
      </div>
    </div>
  </section>

{CTA}
"""

LEVELS = f"""  <section class="page-head">
    <div class="container">
{breadcrumb("Levels")}
      <h1>Six levels, from Rookie to Master</h1>
      <p class="lead">Difficulty is a ladder, not a slider. Each rung changes something concrete about
      the layouts you are asked to run &mdash; and none of them are locked.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="table-wrap">
        <table>
          <caption class="sr-only">The six Runout Rank levels and what changes at each rung</caption>
          <thead>
            <tr>
              <th scope="col">Level</th>
              <th scope="col">Name</th>
              <th scope="col">Object balls</th>
              <th scope="col">Ball in hand</th>
              <th scope="col">Minimum ball spacing</th>
              <th scope="col">Blockers</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>1</strong></td><td><strong>Rookie</strong></td><td>2</td><td>Yes</td><td>8&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>2</strong></td><td><strong>Regular</strong></td><td>3</td><td>Yes</td><td>6&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>3</strong></td><td><strong>League</strong></td><td>4</td><td>Yes</td><td>4&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>4</strong></td><td><strong>Competitor</strong></td><td>5</td><td>Yes</td><td>2.25&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>5</strong></td><td><strong>Advanced</strong></td><td>5</td><td>No</td><td>2.25&Prime;</td><td>&mdash;</td></tr>
            <tr><td><strong>6</strong></td><td><strong>Master</strong></td><td>5</td><td>No</td><td>2.25&Prime;</td><td>2</td></tr>
          </tbody>
        </table>
      </div>
      <p class="dim" style="margin-top:16px">Spacing is a <em>minimum</em> centre-to-centre distance, so a
      bigger number means a more spread-out, more forgiving layout. 2.25&Prime; is one ball diameter &mdash; the
      floor, below which balls would physically overlap. The same figures are shown inside the app on each level card.</p>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Reading the ladder</p>
        <h2>Four dials, turned up one rung at a time</h2>
      </div>
      <div class="grid grid--4">
        <div class="card"><h3>Ball count</h3><p>Two balls at Rookie, rising to five from Competitor upward. Every extra ball is another position decision that has to come off.</p></div>
        <div class="card"><h3>Ball in hand</h3><p>Levels 1&ndash;4 let you place the cue ball. From Advanced it goes where the layout puts it, and you start from what you are given.</p></div>
        <div class="card"><h3>Packing</h3><p>The minimum gap between balls shrinks from 8&Prime; to one ball diameter. Tightly packed balls block angles and kill position play.</p></div>
        <div class="card"><h3>Blockers</h3><p>Master alone adds two. They are not part of the potting order &mdash; drawn drab and unnumbered &mdash; and exist only to be in your way.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-levels.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="The levels screen with the League level expanded, showing best test score and recent practice rate."></div>
        </div>
        <div>
          <p class="eyebrow">Your standing, per rung</p>
          <h3>Every level knows how you are doing on it</h3>
          <p>Expand any level to see your best test score there, your recent practice run-out rate, and
          how many attempts that rate is based on &mdash; so you can tell a real weakness from a bad
          evening. Passed levels are marked, and your <span class="gold">edge</span> &mdash; the level
          currently beating you &mdash; is called out in gold.</p>
          <ul class="ticks ticks--gold">
            <li>Start a Rating Test at any level, not only the next one</li>
            <li>Retake a level you have already tested to confirm or improve it</li>
            <li>Start free practice at any level directly from the ladder</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

PRACTICE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb("Practice")}
      <h1>Practice, and a log of everything you have run</h1>
      <p class="lead">The test tells you which level beats you. Practice is where you do something
      about it &mdash; an endless stream of generated layouts at exactly that level.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-practice.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="A practice session with a generated four-ball layout and the prompt asking whether you ran out."></div>
        </div>
        <div>
          <p class="eyebrow">A session</p>
          <h3>Never run out of material, never memorise a layout</h3>
          <p>Practice tables are generated on demand at whatever level you pick, and your attempts
          count toward that level's statistics. The illustration stays on screen for the whole
          attempt, so you can re-rack it if the layout gets disturbed.</p>
          <ul class="ticks">
            <li>One tap logs a success or a failure, with confirmation that it was recorded</li>
            <li>Skip a layout you do not want to play, rather than stalling the session</li>
            <li>Retry the exact same layout to drill it until you own it</li>
            <li>Generate the next table straight after recording &mdash; a loop, not a menu tree</li>
            <li>Reopen the last table you generated from the home screen after closing the app</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">The training log</p>
        <h2>A complete record of the work you have put in</h2>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>Every table you have played</h3><p>Browse the lot, with the date, the level, and how many attempts you ran out.</p></div>
        <div class="card"><h3>Favourites</h3><p>Star the layouts worth repeating and filter the log to favourites only, building a personal library of drills.</p></div>
        <div class="card"><h3>Continue from anywhere</h3><p>Pick any table in the log and carry on training from it. Revisiting an old layout is one tap.</p></div>
      </div>
      <p class="dim" style="margin-top:20px">An empty log tells you how to fill it rather than showing you a blank screen.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-progress.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="The Rank screen showing the current rating, tier, lifetime metrics and per-level breakdown."></div>
        </div>
        <div>
          <p class="eyebrow">Where you stand &mdash; free, always</p>
          <h3>The numbers that answer &ldquo;am I getting better?&rdquo;</h3>
          <p>Your 0&ndash;100 rating and tier, the highest level you have cleared, your edge level, and
          the rating change since your last test. Underneath: lifetime attempts, total run-outs,
          overall run-out rate and best streak, plus a plain-language read of the ratio &mdash;
          &ldquo;you are running out 1 in every N tables&rdquo;.</p>
          <p>Retaking the test at your edge level is one tap from the same screen.</p>
          <p><a href="runout-pro.html">What Runout Pro adds on top &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

{CTA}
"""

PRO = f"""  <section class="page-head">
    <div class="container">
{breadcrumb("Runout Pro")}
      <h1>Runout Pro</h1>
      <p class="lead">One boundary, one sentence: <strong>where you stand is free, how you got there
      is Pro.</strong></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--2">
        <div class="card">
          <p class="eyebrow">Free, permanently</p>
          <h3>Where you stand</h3>
          <ul class="ticks">
            <li>Your 0&ndash;100 rating and tier</li>
            <li>The level you have cleared and the level that beats you</li>
            <li>Rating delta since your last test</li>
            <li>Per-level breakdown: best test score and recent practice rate</li>
            <li>Lifetime attempts, run-outs, run-out rate and best streak</li>
            <li>Unlimited Rating Tests and unlimited practice at every level</li>
          </ul>
          <p class="dim">None of this is a trial. The app is fully useful without paying.</p>
        </div>
        <div class="card card--gold">
          <p class="eyebrow eyebrow--gold">Runout Pro</p>
          <h3>How you got here</h3>
          <ul class="ticks ticks--gold">
            <li>Your rating plotted across every test you have ever taken</li>
            <li>Score progression at each level &mdash; every test, not just your best</li>
            <li>Run-out rate over time, and your session history</li>
            <li>A full test log: level, score, date and rating change for every run</li>
            <li>CSV export of your entire history</li>
          </ul>
          <p class="dim">Subscribe monthly or annually. Your whole past history unlocks immediately
          &mdash; there is no fresh collection period to wait out.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">How the upsell behaves</p>
        <h2>One honest card, not padlocks down the page</h2>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>No pitch on day one</h3><p>A brand-new player with no test history is shown no sales pitch at all. A paywall for something you cannot yet imagine wanting is just noise.</p></div>
        <div class="card"><h3>A preview of your own data</h3><p>Once you have enough history to unlock something, you see your own progress curve with the values obscured &mdash; not a generic advert.</p></div>
        <div class="card"><h3>One boundary, at the bottom</h3><p>The Rank screen has exactly one Pro card. Scattering lock icons through a screen makes every free feature feel like a sample.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Billing, restoring and cancelling</h2>
      <ul>
        <li>Prices are shown live from the App Store or Google Play, with the annual saving calculated
        against them, so what you see is what your store will charge in your currency.</li>
        <li>Already bought it? <strong>Restore purchase</strong> brings it back after a reinstall or on
        a second device &mdash; a reinstall never costs you twice.</li>
        <li>Manage or cancel any time in your Apple or Google account. Refunds and billing questions are
        handled by the store under its own terms.</li>
        <li>The Terms of Use and the <a href="privacy-policy.html">privacy policy</a> are readable
        before you subscribe, not after.</li>
        <li><strong>Pro keeps working offline.</strong> A bad signal in a pool hall never locks you out
        of what you paid for.</li>
      </ul>
      <p>Payments are processed entirely by Apple and Google. Runout Rank never sees or stores your
      card details.</p>
    </div>
  </section>

{CTA}
"""

GUIDE_TITLE = "How to test your pool skill level (and get a number you can trust)"
GUIDE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb("Pool skill level test")}
      <h1>How to test your pool skill level</h1>
      <p class="lead">Most players can tell you who they beat. Very few can tell you how good they
      are. Here is what separates a skill test worth taking from a drill you happen to like.</p>
{byline(FIRST_PUBLISHED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Why &ldquo;how good am I?&rdquo; is so hard to answer</h2>
      <p>Match results measure your opponents as much as they measure you. A good night against a weak
      field and a bad night against a strong one can produce identical scorelines. Practice feels
      productive whether or not it is working, because you naturally spend it on shots you already
      like. And the drills most players run are the ones they have run before &mdash; which is exactly
      why they get easier.</p>
      <p>A useful skill test has to do three things that casual practice does not.</p>

      <h2>1. It has to measure a whole skill, not a single shot</h2>
      <p>Potting a long straight blue tells you about one stroke. Clearing a table tells you about
      pattern reading, position play, speed control, safety judgement and nerve, in the order the
      table demands them. That is why the run-out &mdash; the whole table, start to finish &mdash; is
      the right unit of measurement for a skill test, and why Runout Rank scores tables rather than
      shots.</p>

      <h2>2. It has to be unpredictable</h2>
      <p>Any fixed set of layouts decays into a memory test. The tenth time you set up the same drill
      you are not measuring run-out ability, you are measuring how well you remember the answer to
      that particular table. A test worth repeating has to generate its layouts, so the pattern in
      front of you is genuinely new each time.</p>

      <h2>3. Its difficulty has to be defined, not improvised</h2>
      <p>Here is the tension: randomness makes a test honest, and it also threatens to make two scores
      incomparable. If your ten tables were harder than mine, our scores mean different things.</p>
      <p>The fix is to <strong>fix the constraints rather than the layouts</strong>. Define precisely
      what a difficulty level means &mdash; how many object balls, whether you get ball in hand, the
      minimum spacing between balls, how many blockers &mdash; and generate freely inside those rules.
      Every layout is new, every layout is the same difficulty, and enough tables in a row average out
      whatever luck is left. In Runout Rank those constants are published on the
      <a href="levels.html">levels page</a> and are identical on Android and iOS.</p>
      <p>That is what makes a score portable: it says you cleared seven of ten at Level&nbsp;4, and
      Level&nbsp;4 means the same thing for everyone.</p>

      <h2>The rules that make a score honest</h2>
      <ul>
        <li><strong>One attempt per table.</strong> Best-of-three measures your best day, not your
        standard.</li>
        <li><strong>No skipping.</strong> The layouts you would rather avoid are precisely the ones
        carrying the information.</li>
        <li><strong>A fixed number of tables.</strong> Ten is enough to average out one unlucky roll,
        short enough to finish in a single sitting at a real table.</li>
        <li><strong>A stated pass mark.</strong> Seven out of ten clears a level in Runout Rank.
        Knowing the bar before you start is part of the test.</li>
        <li><strong>Record it immediately.</strong> A result you write down an hour later is a result
        you have already flattered.</li>
      </ul>

      <h2>What to do with the number</h2>
      <p>A rating on its own is trivia. The number is only useful if it points somewhere, which is why
      the important output of a test is not the score but the <strong>edge level</strong> &mdash; the
      rung you cannot yet clear. That is where practice pays, because it is the only level where the
      layouts are still asking you a question you cannot answer.</p>
      <p>The practical loop looks like this:</p>
      <ol>
        <li>Test at a level you think you can clear.</li>
        <li>If you clear it, test the level above until one beats you.</li>
        <li>Practise at that edge level, logging attempts so the run-out rate is real.</li>
        <li>Retest the same level when the rate has moved. Compare the ratings, not the feelings.</li>
      </ol>

      <h2>How often to retest</h2>
      <p>Often enough that the number tracks reality, rarely enough that each retest reflects actual
      work. For most players putting in a couple of table sessions a week, every two to four weeks is
      about right. Retesting after every session mostly measures noise; retesting twice a year tells
      you nothing you can act on.</p>

      <h2>Why this beats waiting for a league rating to settle</h2>
      <p>The alternative most players are pointed at is a relative rating earned through league play,
      which needs a large history of games against other rated players before it means much &mdash;
      FargoRate, for instance, treats 200 games as the minimum for an established rating. A run-out
      test gives you the answer in one sitting because it measures you against the layouts rather than
      against the room, which also means it does not shift with the strength of your local scene.
      Further reading:</p>
      <ul>
        <li><a href="fargo-rate-alternative.html">A Fargo Rate alternative that does not need 200 league games</a></li>
        <li><a href="pool-rating-without-a-league.html">How to get a pool rating without joining a league</a></li>
        <li><a href="absolute-vs-relative-pool-rating.html">Absolute vs relative pool ratings</a></li>
      </ul>

      <div class="note">Runout Rank does all of this on the table you already play on: it generates
      the layouts, scores the run-outs, keeps the history on your device, and names the level to train
      at next. <a href="how-it-works.html">See exactly how the test works &rarr;</a></div>
    </div>
  </section>

{CTA}
"""

# --------------------------------------------------------------------------
# Positioning pages: the two pain points a relative league rating leaves open
# --------------------------------------------------------------------------

FARGO_DISCLAIMER = """      <p class="disclaimer">Runout Rank is independent and is not affiliated with, endorsed by or
      connected to FargoRate. Everything said here about Fargo Rate is drawn from
      <a href="https://www.fargorate.com/" rel="nofollow">FargoRate&rsquo;s own published material</a>
      and is described as fairly as we know how; it is a good system, and this page is about where its
      design does and does not fit a particular kind of player.</p>"""

FARGO_ALT_TITLE = "A Fargo Rate alternative that does not need 200 league games"
FARGO_ALT = f"""  <section class="page-head">
    <div class="container">
{breadcrumb("Fargo Rate alternative")}
      <h1>A Fargo Rate alternative for players who will never play 200 league games</h1>
      <p class="lead">Fargo Rate is the best relative rating pool has. But relative is exactly the
      thing that makes it slow to earn and sensitive to where you live. Here is what an absolute
      rating does differently, and which of the two you actually want.</p>
{byline(UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>First, credit where it is due</h2>
      <p>Fargo Rate put amateurs and world champions on one scale and made pool handicapping something
      you can argue about with numbers instead of reputations. If you play league matches every week
      against other rated players, it works, and this page is not going to pretend otherwise. Keep it.</p>
      <p>The question this page is about is narrower: <strong>what do you do if you are not that
      player?</strong> If you practise alone, play casually with friends, travel, or simply want to
      know how good you are without signing up to a season of matches, a relative rating has two
      structural problems &mdash; and they are structural, not bugs.</p>

      <h2>Pain point one: the number is not real until 200 games</h2>
      <p>FargoRate calls the size of your game history <em>robustness</em>, and states plainly that a
      robustness of 200 games is the minimum for it to consider a rating
      &ldquo;established&rdquo;. Under that threshold your official rating is a blend of your actual
      performance and a <em>starter rating</em> &mdash; an initial guess &mdash; with the guess losing
      influence as you close the gap to 200.</p>
      <p>Count what 200 rated games costs a normal person. It means finding a league that reports to
      the system, paying its fees, being free on the same evening every week, and playing out most of
      a season or two &mdash; before the number in the app is a measurement of you rather than a
      weighted opinion. A player who wants a single honest answer to &ldquo;how good am I?&rdquo; has
      to buy a year of commitment to get it.</p>
      <p>And there is no way to shortcut it, because there is nothing to shortcut: a relative system
      genuinely cannot know anything about you until you have generated enough results against people
      it already knows.</p>
      <p><a href="pool-rating-without-a-league.html">How to get a pool rating without joining a league &rarr;</a></p>

      <h2>Pain point two: your rating partly describes your city</h2>
      <p>A relative rating is computed from who beat whom. That means your number is only as anchored
      as the chain of games connecting your local players to the rest of the rated world. Where that
      chain is thick &mdash; big cities, strong touring scenes, players who travel to open events
      &mdash; ratings line up well. Where it is thin, a local group can settle at a level that does
      not match the same numbers elsewhere.</p>
      <p>This is not an outsider&rsquo;s complaint. FargoRate&rsquo;s own writing describes two nearly
      isolated groups of players, one rated too high relative to the other, as a particularly vexing
      problem &mdash; one that only corrects itself through a lot of cross-play over a long time. Its
      definition of a reliable rating likewise notes that games against opponents with established
      ratings count for more.</p>
      <p>So if your region is packed with strong players, or barely connected to the wider network, or
      new to the system, the number you carry is telling you something about your surroundings as well
      as about you. Move somewhere else and it may not mean what it meant at home.</p>
      <p><a href="absolute-vs-relative-pool-rating.html">Absolute vs relative ratings, explained &rarr;</a></p>

      <h2>What an absolute rating does instead</h2>
      <p>Runout Rank removes opponents from the measurement altogether. Instead of asking who you beat,
      it puts a defined layout on the table and asks whether you can run it out.</p>
      <p>You play ten generated tables at one level, one attempt each, no retries and no skips, and
      record each as a run-out or a miss. Ten answers become a score, a 0&ndash;100 rating and a tier
      from Rookie to Master. Seven of ten clears the level. The whole thing takes about an hour on the
      table you already play on.</p>
      <p>Because the layouts are the yardstick and the yardstick never changes, the number means the
      same thing whoever else is in the room, and the same thing next year as this year. It is earned
      from the first session, not accumulated over a season.</p>

      <h2>Side by side</h2>
      <div class="table-wrap">
        <table>
          <caption class="sr-only">Relative league ratings compared with the Runout Rank absolute rating</caption>
          <thead>
            <tr>
              <th scope="col"></th>
              <th scope="col">Relative rating (Fargo Rate and similar)</th>
              <th scope="col">Runout Rank</th>
            </tr>
          </thead>
          <tbody>
            <tr><th scope="row">What it measures</th><td>Results against other rated players</td><td>Run-outs against fixed generated layouts</td></tr>
            <tr><th scope="row">Before it means something</th><td>200 games for an established rating; a starter rating is blended in below that</td><td>One ten-table test, roughly an hour</td></tr>
            <tr><th scope="row">What you need</th><td>A reporting league or rated events, opponents, fees, a schedule</td><td>A pool table and a phone</td></tr>
            <tr><th scope="row">Effect of your local scene</th><td>Real: connectivity and the strength of your player pool influence the number</td><td>None: no opponents are involved</td></tr>
            <tr><th scope="row">Portability</th><td>Travels within the network; weakly connected regions can drift</td><td>The same level constraints everywhere, on Android and iOS</td></tr>
            <tr><th scope="row">Good for</th><td>Handicapping matches, tournament brackets, league eligibility</td><td>Knowing your own standard and what to practise next</td></tr>
            <tr><th scope="row">Not for</th><td>Answering &ldquo;how good am I?&rdquo; on day one</td><td>Handicapping a match against someone else &mdash; it is not a handicap system</td></tr>
            <tr><th scope="row">Cost and account</th><td>League membership; an online profile</td><td>Free app, no account, works fully offline</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Be clear about what Runout Rank is not</h2>
      <p>It does not replace a league rating for handicapping, and it will not get you seeded in a
      tournament. No governing body recognises it. It is also honest about its own variable: you are
      playing on your own equipment, so a tight-pocketed table with slow cloth will read differently
      from a bar box. Take the test on the table you actually compete on, and compare like with like
      over time.</p>
      <p>What it gives you is the thing a relative system cannot give you cheaply: a real number today,
      from your own play, that does not depend on anyone else.</p>

      <h2>The obvious answer: use both</h2>
      <p>They measure different things and they do not conflict. If you play league, keep your Fargo
      Rate for matches, and use Runout Rank between them to tell you which part of your game is behind
      &mdash; a run-out test names the level that beats you and hands you practice at it, which a
      match-result rating cannot do. If you do not play league, Runout Rank is the number you can
      actually have.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="how-it-works.html">See how the test works</a>
        <a class="btn btn--ghost" href="pool-rating-without-a-league.html">Get a rating without a league</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

NO_LEAGUE_TITLE = "How to get a pool rating without joining a league"
NO_LEAGUE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb("A rating without a league")}
      <h1>How to get a pool rating without joining a league</h1>
      <p class="lead">Every established rating system asks for the same entry fee: hundreds of matches
      against other rated players. If that is not your life, you are not unratable &mdash; you just
      need a rating that measures the table instead of the room.</p>
{byline(UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>Why casual players end up with no number at all</h2>
      <p>The usual advice is: join a league that reports to a rating system, play a season, and your
      rating will settle. That is sound advice, and for a lot of players it is also impossible. It asks
      for a fixed evening every week, membership fees, a venue that runs a reporting league, and enough
      opponents who are themselves rated.</p>
      <p>Then there is the volume. FargoRate treats 200 games as the minimum robustness for calling a
      rating established; below that, part of what you are looking at is the starter rating the system
      assigned you rather than what you did. Two hundred rated games is a season or more for most
      league players and a fantasy for everyone else.</p>
      <p>So the honest position for a casual player is this: the effort of earning a relative rating is
      larger than the value of knowing it. Most people quietly give up and go back to guessing from
      who they beat down the club.</p>

      <h2>What you are actually trying to find out</h2>
      <p>Strip the systems away and there are usually three questions underneath:</p>
      <ul>
        <li><strong>Where do I stand?</strong> Am I a decent club player, or better than I think, or
        worse?</li>
        <li><strong>Am I improving?</strong> Not &ldquo;did I feel good tonight&rdquo; &mdash; is the
        curve moving?</li>
        <li><strong>What should I practise?</strong> Which part of the game is actually holding the
        rest back?</li>
      </ul>
      <p>None of those three questions require an opponent. They require a fixed, repeatable task that
      is hard enough to fail and a record of how often you complete it.</p>

      <h2>The test that answers them</h2>
      <p>A run-out is the right unit: clearing a table exercises pattern reading, position, speed
      control and nerve in the order the table demands them, which a single potting drill does not.
      Make it ten tables at one difficulty level, one attempt each, no retries and no skips, and you
      have a measurement instead of a practice session.</p>
      <p>That is what Runout Rank does. The app draws each layout top-down, you rack it on your own
      table, play it once and tap run-out or miss. At the end you get a score out of ten, a
      0&ndash;100 rating, a tier from Rookie to Master, whether you cleared the level, and the level
      that is currently beating you. It takes about an hour and needs nobody else in the building.</p>
      <p>Layouts are generated fresh for every test, so there is nothing to memorise, while the
      level&rsquo;s constraints &mdash; ball count, ball in hand, spacing, blockers &mdash; are fixed
      constants that are the same for every player on Android and iOS. New tables every time, the same
      difficulty every time.</p>

      <h2>A practical routine for a solo player</h2>
      <ol>
        <li><strong>Test at the level you think you can clear.</strong> Nothing is locked, so start
        where you think you belong rather than at the bottom.</li>
        <li><strong>Move up until a level beats you.</strong> Seven of ten clears a level; when you
        cannot make seven, you have found your edge.</li>
        <li><strong>Practise at the edge level,</strong> logging every attempt so the run-out rate is a
        fact rather than an impression.</li>
        <li><strong>Retest that level when the rate moves.</strong> Every two to four weeks suits most
        players &mdash; often enough to track real work, rarely enough that you are not measuring
        noise.</li>
        <li><strong>Compare ratings, not feelings.</strong> The rating delta on the result screen is
        the whole point.</li>
      </ol>

      <h2>What it costs you</h2>
      <p>An hour, a table you can book, and nothing else. The app is free to download, there is no
      account to create, it works entirely offline, and your history stays in the app&rsquo;s private
      storage on your own device. Runout Pro is optional and adds history: your rating plotted across
      every test, per-level progression and CSV export. Where you stand is free permanently.</p>

      <h2>If you do play league</h2>
      <p>Then keep your league rating &mdash; it is the right tool for handicapping matches, and this
      is not a replacement for it. Use a run-out test alongside it, because a match-result rating tells
      you the level you are at without telling you which part of your game is behind. See
      <a href="fargo-rate-alternative.html">the full comparison with Fargo Rate</a>.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="how-it-works.html">How the test works</a>
        <a class="btn btn--ghost" href="levels.html">See the six levels</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""

ABSOLUTE_TITLE = "Absolute vs relative pool ratings: why your city changes your number"
ABSOLUTE = f"""  <section class="page-head">
    <div class="container">
{breadcrumb("Absolute vs relative ratings")}
      <h1>Absolute vs relative pool ratings</h1>
      <p class="lead">Two players of identical ability, one in a strong city and one in a quiet one,
      can carry different relative ratings for years. That is not a flaw in the maths &mdash; it is
      what &ldquo;relative&rdquo; means. Here is the difference, and what each kind of rating is good
      for.</p>
{byline(UPDATED, UPDATED)}
    </div>
  </section>

  <section>
    <div class="container prose">
      <h2>What a relative rating is</h2>
      <p>A relative rating &mdash; Elo, Glicko, Fargo Rate and the rest of the family &mdash; has no
      notion of an absolute standard. It only knows results: you beat them, they beat someone else.
      From a large enough web of those results, the system finds the set of numbers that best explains
      the outcomes. Nobody ever measures a player directly; every rating is a position in a network of
      other ratings.</p>
      <p>That is an elegant design and it works remarkably well when the network is dense. It also
      carries two consequences that no amount of clever maths removes.</p>

      <h2>Consequence one: it needs a lot of games</h2>
      <p>A result is one bit of evidence, and one bit is very little. So the system needs volume before
      it can separate you from luck &mdash; which is why FargoRate uses a robustness measure and treats
      200 games as the minimum for calling a rating established, blending a starter rating into the
      number until you get there. Until you have paid that price in games, your rating is partly a
      guess about you.</p>

      <h2>Consequence two: it is anchored to your neighbours</h2>
      <p>Because every rating is defined against other ratings, a group of players only lines up
      correctly with the rest of the world if enough games connect them to it. Where that connection is
      thin &mdash; an isolated region, a new league, a scene whose players rarely travel to open events
      &mdash; the group can settle at a level that does not match the same numbers elsewhere. FargoRate
      describes precisely this case, two nearly isolated groups with one rated too high relative to the
      other, as a vexing problem, and notes that games against established opponents are worth more for
      exactly this reason.</p>
      <p>The practical version for a player: if your city is stacked with strong players, or barely
      connected to the wider rated population, your number is partly a statement about your
      surroundings. Two players of the same standard in different scenes need not read the same, and
      neither of them can do anything about it except play more games against outsiders.</p>

      <h2>What an absolute rating is</h2>
      <p>An absolute rating measures performance against a fixed standard rather than against people.
      Golf handicaps work this way against par. Athletics works this way against the clock. A stopwatch
      does not care who else is in the race, and 10.4 seconds in Manila is 10.4 seconds in Manchester.</p>
      <p>Pool has not traditionally had one, because pool lacks an obvious clock. Runout Rank supplies
      the equivalent: a set of defined table layouts and one question &mdash; can you run this out? Ten
      tables at a level, one attempt each, no retries and no skips. The number that comes out is
      computed entirely from your own results against the layouts.</p>
      <p>So there is no opponent pool to be strong or weak, nothing to drift against, and no minimum
      number of games before the measurement is valid. You have your rating at the end of the first
      session, and it means the same thing anywhere.</p>

      <h2>How a fixed standard avoids becoming a memory test</h2>
      <p>The obvious objection: a fixed set of layouts stops measuring skill as soon as you have played
      it a few times, because you are then recalling solutions rather than finding them.</p>
      <p>Runout Rank avoids that by fixing the <em>difficulty</em> rather than the tables. A level is a
      set of published constants &mdash; object ball count, ball in hand or not, minimum spacing,
      blockers &mdash; and layouts are generated fresh inside those rules every time. You never see the
      same table twice, and every table asks the same question. Ten of them in a row average out what
      luck remains.</p>

      <h2>What an absolute rating cannot do</h2>
      <p>It is not a handicap system, and it should not be used as one. A relative rating exists to
      predict a match between two specific people, and it is far better at that than any absolute
      measure &mdash; because match outcomes are what it is built from.</p>
      <p>An absolute rating also has its own variable to keep honest: the equipment. Pocket cut, table
      size and cloth speed all change how hard a run-out is, so a rating taken on a nine-foot table
      with tight pockets is a different measurement from one taken on a bar box. Fix your conditions,
      take the test on the table you compete on, and compare your own numbers over time.</p>

      <h2>Which one do you want?</h2>
      <div class="compare" style="margin:24px 0">
        <div class="card">
          <h3>Use a relative rating when</h3>
          <ul class="ticks">
            <li>You need a handicap for a match or a bracket</li>
            <li>Your league or tournament requires one</li>
            <li>You already play enough rated games to keep it robust</li>
          </ul>
        </div>
        <div class="card card--gold">
          <h3>Use an absolute rating when</h3>
          <ul class="ticks ticks--gold">
            <li>You want to know where you stand without playing a season first</li>
            <li>You practise alone, travel, or move between scenes</li>
            <li>You want to know <em>what to practise</em>, not just how you rank</li>
          </ul>
        </div>
      </div>
      <p>They answer different questions, and a serious player can reasonably carry both.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="fargo-rate-alternative.html">Compared with Fargo Rate</a>
        <a class="btn btn--ghost" href="how-it-works.html">How the rating is calculated</a>
      </div>
{FARGO_DISCLAIMER}
    </div>
  </section>

{CTA}
"""


FAQ_ITEMS = [
    ("Do I need a real pool table to use Runout Rank?",
     "Yes. Runout Rank is not a pool game &mdash; it is a companion to a real table. The app draws each "
     "layout top-down, you set it up on the cloth in front of you, play it, and record what happened."),
    ("Do I need an account or an internet connection?",
     "No, to both. There is nothing to sign up for and nothing to sign in to, and the app works fully "
     "offline. Your tests, attempts, favourites and statistics live only in the app's private storage "
     "on your own device."),
    ("How is the rating calculated?",
     "You play ten generated tables at one level, one attempt each. The score out of ten is converted "
     "into a 0&ndash;100 rating with a named tier, and seven out of ten clears the level. The result "
     "also shows how far your rating moved since your last test."),
    ("If the tests are random, how can two scores be compared?",
     "Because what is fixed is the level, not the tables. Each level defines the object ball count, "
     "whether you get ball in hand, the minimum spacing between balls and the number of blockers, and "
     "those constants are identical for every player on both platforms. Layouts are generated fresh "
     "inside those rules, and ten tables in a row average out the luck &mdash; so seven out of ten at "
     "Level 4 means the same thing whoever scored it."),
    ("Can I retry a table I misplayed?",
     "Not during a Rating Test &mdash; one attempt per table, no retries and no skips, which is what "
     "makes the score mean something. In free practice you can retry the same layout as often as you "
     "like."),
    ("What happens if I get interrupted mid-test?",
     "The test resumes at the exact table you stopped on. Deliberately quitting asks you to confirm "
     "first and explains that a part-finished run cannot be scored."),
    ("Do I have to start at Level 1?",
     "No. Nothing is locked. You can take a Rating Test at any of the six levels, and retake any level "
     "you have already tested."),
    ("What is my &ldquo;edge level&rdquo;?",
     "The level that is currently beating you &mdash; the highest one you cannot yet clear. It is the "
     "level worth practising at, and both the result screen and the Rank screen let you jump straight "
     "into it."),
    ("What does Runout Pro cost, and what does it add?",
     "Runout Pro is an optional monthly or annual subscription, priced by your store in your own "
     "currency. It adds history: your rating plotted over every test, per-level score progression, "
     "run-out rate over time, the full test log, and CSV export. Everything that tells you where you "
     "stand right now stays free."),
    ("Is my history safe when the app updates?",
     "Yes. Your existing tests, attempts and favourites are preserved across app updates. Because the "
     "data is local, uninstalling the app or clearing its data does remove it."),
    ("How is this different from Fargo Rate?",
     "Fargo Rate is a relative rating: it works out your number from results against other rated "
     "players, which is why FargoRate treats 200 games as the minimum robustness for an established "
     "rating, and why a weakly connected local scene can drift against the rest of the network. "
     "Runout Rank is absolute &mdash; it measures you against fixed generated layouts, so one "
     "ten-table session gives you a full rating and no opponent pool influences it. It is not a "
     "handicap system and does not replace a league rating for match handicapping."),
    ("How many games do I need before my Runout Rank rating means something?",
     "Ten tables &mdash; one test, about an hour. There is no qualifying period and no provisional "
     "phase, because the rating is computed from your run-outs against defined layouts rather than "
     "from a history of results against other players."),
    ("Does where I live affect my rating?",
     "No. Every level&rsquo;s constraints are the same constants everywhere, and no opponents enter "
     "the calculation. The one local variable is your "
     "equipment: pocket cut, table size and cloth speed change how hard a run-out is, so take the "
     "test on the table you actually play on and compare your own numbers over time."),
    ("Can I use Runout Rank and a league rating together?",
     "Yes, and that is the sensible thing to do if you play league. Keep the league rating for "
     "handicapping matches, and use the run-out test to find which level is beating you and to "
     "practise there &mdash; something a match-result rating cannot tell you."),
    ("Is Runout Rank the same on Android and iOS?",
     "Yes. The level definitions, the generator and the rating maths are shared code running on both "
     "platforms, so the phone you own has no effect on your rating."),
]

FAQ_BODY_ITEMS = "\n".join(
    f"""      <div class="faq-item">
        <h3>{q}</h3>
        <p>{a}</p>
      </div>"""
    for q, a in FAQ_ITEMS
)


def _plain(s):
    s = s.replace("&mdash;", "—").replace("&ldquo;", "“").replace("&rdquo;", "”")
    s = s.replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"<[^>]+>", "", s)


FAQ_SCHEMA_ITEMS = ",\n".join(
    '    {\n'
    '      "@type": "Question",\n'
    f'      "name": {json.dumps(_plain(q))},\n'
    f'      "acceptedAnswer": {{"@type": "Answer", "text": {json.dumps(_plain(a))}}}\n'
    '    }'
    for q, a in FAQ_ITEMS
)

FAQ_SCHEMA = f"""{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{FAQ_SCHEMA_ITEMS}
  ]
}}"""

FAQ = f"""  <section class="page-head">
    <div class="container">
{breadcrumb("FAQ")}
      <h1>Frequently asked questions</h1>
      <p class="lead">The test, the rating, the levels, the subscription and your data.</p>
    </div>
  </section>

  <section>
    <div class="container" style="max-width:52rem">
{FAQ_BODY_ITEMS}
      <p style="margin-top:28px">Still unsure how the number is produced?
      <a href="how-it-works.html">Read how the rating works &rarr;</a></p>
    </div>
  </section>

{CTA}
"""

NOT_FOUND = """  <section class="page-head">
    <div class="container">
      <h1>That table is not racked</h1>
      <p class="lead">The page you were looking for does not exist. Here is the way back.</p>
      <div class="btn-row" style="margin-bottom:40px">
        <a class="btn btn--primary" href="index.html">Back to the home page</a>
        <a class="btn btn--ghost" href="how-it-works.html">How the test works</a>
      </div>
    </div>
  </section>
"""


def privacy_body():
    """Render docs/PRIVACY_POLICY.md (kept in the app repo) into the site page."""
    src = os.path.join(HERE, "content", "privacy-policy.md")
    with open(src, encoding="utf-8") as fh:
        md = fh.read()
    return f"""  <section class="page-head">
    <div class="container">
{breadcrumb("Privacy policy")}
      <h1>Privacy policy</h1>
      <p class="lead">Your tests and statistics stay on your device. This page explains everything the
      app does collect, why, and what control you have over it.</p>
    </div>
  </section>

  <section>
    <div class="container prose">
{markdown_to_html(md)}
    </div>
  </section>
"""


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


PAGES = [
    dict(slug="index.html",
         title="Runout Rank — An Absolute Pool Skill Rating Test for Android and iOS",
         description="Get a real pool rating in one session, not in 200 league games. Runout Rank "
                     "measures you against ten generated table layouts rather than against local "
                     "opponents, so the 0–100 number means the same in every city. No league, no "
                     "account, works offline.",
         body=INDEX,
         schema=[APP_SCHEMA, SITE_SCHEMA],
         keywords="absolute pool rating, fargo rate alternative, pool skill test, billiards rating "
                  "app, pool rating without a league, run-out test, pool training app"),

    dict(slug="how-it-works.html",
         title="How the Runout Rank rating works — ten tables, one attempt each",
         description="Ten randomly generated tables at one level, one attempt each, scored into a "
                     "0–100 absolute pool rating and a tier. Fresh layouts every test, fixed level "
                     "constraints, so the number means the same thing in every city.",
         body=HOW,
         schema=[breadcrumb_schema("How it works", "how-it-works.html")]),

    dict(slug="levels.html",
         title="The six levels — Rookie to Master | Runout Rank",
         description="Rookie, Regular, League, Competitor, Advanced, Master. What changes at each "
                     "rung of the ladder — ball count, ball in hand, packing and blockers — and why "
                     "nothing is locked.",
         body=LEVELS,
         schema=[breadcrumb_schema("Levels", "levels.html")]),

    dict(slug="practice.html",
         title="Pool practice sessions and a training log that remembers | Runout Rank",
         description="Endless randomly generated practice layouts at the level you choose, one-tap "
                     "logging, retry and skip, favourites, and a complete training log of every "
                     "table you have run.",
         body=PRACTICE,
         schema=[breadcrumb_schema("Practice", "practice.html")]),

    dict(slug="fargo-rate-alternative.html",
         dated=True,
         title=FARGO_ALT_TITLE + " | Runout Rank",
         description="Fargo Rate needs 200 games before a rating is established, and a relative "
                     "rating is anchored to the players around you. Runout Rank is an absolute pool "
                     "rating from one ten-table session — compared side by side, fairly.",
         body=FARGO_ALT,
         schema=[article_schema(
             FARGO_ALT_TITLE,
             "Why a relative league rating takes 200 games to establish and shifts with your local "
             "player pool, what an absolute run-out rating does instead, and which of the two you want.",
             "fargo-rate-alternative.html", UPDATED, UPDATED),
             breadcrumb_schema("Fargo Rate alternative", "fargo-rate-alternative.html")],
         published=UPDATED,
         keywords="fargo rate alternative, fargo rating alternative, pool rating app, absolute pool "
                  "rating, fargo rate 200 games, established fargo rating, fargo rate accuracy"),

    dict(slug="pool-rating-without-a-league.html",
         dated=True,
         title=NO_LEAGUE_TITLE + " | Runout Rank",
         description="Every league rating asks for hundreds of matches against rated players before "
                     "the number is real. Here is how a casual or solo player gets an honest 0–100 "
                     "pool rating in one session on their own table.",
         body=NO_LEAGUE,
         schema=[article_schema(
             NO_LEAGUE_TITLE,
             "How a casual or solo player can get an honest pool rating in one session without "
             "joining a league or playing 200 rated games.",
             "pool-rating-without-a-league.html", UPDATED, UPDATED),
             breadcrumb_schema("A rating without a league", "pool-rating-without-a-league.html")],
         published=UPDATED,
         keywords="pool rating without a league, how to get a pool rating, casual pool player "
                  "rating, solo pool practice rating, get rated at pool, billiards skill rating"),

    dict(slug="absolute-vs-relative-pool-rating.html",
         dated=True,
         title=ABSOLUTE_TITLE + " | Runout Rank",
         description="Elo, Glicko and Fargo Rate are relative: every rating is a position in a "
                     "network of other ratings, so volume and local connectivity both matter. What "
                     "an absolute pool rating measures instead, and what each is good for.",
         body=ABSOLUTE,
         schema=[article_schema(
             ABSOLUTE_TITLE,
             "Why relative pool ratings depend on the players around you, what an absolute rating "
             "measures instead, and which one answers which question.",
             "absolute-vs-relative-pool-rating.html", UPDATED, UPDATED),
             breadcrumb_schema("Absolute vs relative ratings", "absolute-vs-relative-pool-rating.html")],
         published=UPDATED,
         keywords="absolute vs relative pool rating, relative rating system, elo pool rating, "
                  "regional fargo rating differences, pool rating explained"),

    dict(slug="runout-pro.html",
         title="Runout Pro — your full rating history and CSV export | Runout Rank",
         description="Where you stand is free, permanently. Runout Pro adds how you got there: "
                     "rating plotted over every test, per-level progression, the full test log and "
                     "CSV export.",
         body=PRO,
         schema=[breadcrumb_schema("Runout Pro", "runout-pro.html")]),

    dict(slug="pool-skill-level-test.html",
         dated=True,
         title=GUIDE_TITLE,
         description="What separates a pool skill test worth taking from a drill you happen to like: "
                     "whole run-outs, unpredictable layouts, defined difficulty, one attempt per "
                     "table, and what to do with the number.",
         body=GUIDE,
         schema=[article_schema(
             GUIDE_TITLE,
             "What separates a pool skill test worth taking from a drill you happen to like.",
             "pool-skill-level-test.html", FIRST_PUBLISHED, UPDATED),
             breadcrumb_schema("Pool skill level test", "pool-skill-level-test.html")],
         keywords="how to test pool skill level, pool skill test, billiards skill assessment, "
                  "run-out drill, pool rating system"),

    dict(slug="faq.html",
         title="Runout Rank FAQ — the test, the rating, the levels and your data",
         description="Do you need a real table? A league? How is the rating calculated, how does it "
                     "differ from Fargo Rate, and what does Runout Pro add? Answers to the common "
                     "questions.",
         body=FAQ,
         schema=[FAQ_SCHEMA, breadcrumb_schema("FAQ", "faq.html")]),
]


def main():
    written = []
    for spec in PAGES:
        slug = spec["slug"]
        with open(os.path.join(HERE, slug), "w", encoding="utf-8") as fh:
            fh.write(page(slug, spec["title"], spec["description"], spec["body"],
                          spec["schema"], keywords=spec.get("keywords"),
                          published=spec.get("published"), updated=spec.get("updated"),
                          dated=spec.get("dated", False)))
        written.append(slug)

    # Privacy policy is generated from Markdown so it can be kept in step with the app repo copy.
    with open(os.path.join(HERE, "privacy-policy.html"), "w", encoding="utf-8") as fh:
        fh.write(page(
            "privacy-policy.html",
            "Privacy policy | Runout Rank",
            "Runout Rank stores your tests, ratings and practice history on your device only. This "
            "policy explains the analytics the app does use, who data is shared with, and your rights.",
            privacy_body(),
            [breadcrumb_schema("Privacy policy", "privacy-policy.html")],
        ))
    written.append("privacy-policy.html")

    with open(os.path.join(HERE, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(page("404.html", "Page not found | Runout Rank",
                      "That page does not exist. Head back to the Runout Rank home page.",
                      NOT_FOUND, None, noindex=True))
    written.append("404.html")

    # sitemap.xml — 404 is deliberately excluded.
    urls = ["index.html", "how-it-works.html", "fargo-rate-alternative.html",
            "pool-rating-without-a-league.html", "absolute-vs-relative-pool-rating.html",
            "levels.html", "practice.html", "runout-pro.html",
            "pool-skill-level-test.html", "faq.html", "privacy-policy.html"]
    priority = {"index.html": "1.0", "how-it-works.html": "0.9",
                "fargo-rate-alternative.html": "0.9", "pool-rating-without-a-league.html": "0.9",
                "absolute-vs-relative-pool-rating.html": "0.8", "levels.html": "0.8",
                "practice.html": "0.8", "runout-pro.html": "0.7",
                "pool-skill-level-test.html": "0.7", "faq.html": "0.6", "privacy-policy.html": "0.3"}
    entries = "\n".join(
        f"""  <url>
    <loc>{SITE_URL}{'' if u == 'index.html' else u}</loc>
    <lastmod>{LASTMOD}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority[u]}</priority>
  </url>""" for u in urls)
    with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
""")
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

    print("wrote:\n  " + "\n  ".join(written))


if __name__ == "__main__":
    main()
