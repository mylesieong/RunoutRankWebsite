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
TAGLINE = "Pool skill rating test and training app for Android and iOS"
LASTMOD = "2026-08-20"

HERE = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Home"),
    ("how-it-works.html", "How it works"),
    ("levels.html", "Levels"),
    ("practice.html", "Practice"),
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

STORE_BLOCK = """<div class="store-links">
        <div class="store-link" aria-label="Coming soon to the App Store"><span>Coming soon</span><span>App Store</span></div>
        <div class="store-link" aria-label="Coming soon to Google Play"><span>Coming soon</span><span>Google Play</span></div>
      </div>"""


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
          <p style="margin-top:12px;max-width:24rem">A ten-table run-out test on your own pool table,
          a 0&ndash;100 rating, and the level that beats you. No account, no server, no internet needed.</p>
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
          <h4>More</h4>
          <ul>
            <li><a href="pool-skill-level-test.html">Pool skill level test guide</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="privacy-policy.html">Privacy policy</a></li>
            <li><a href="sitemap.xml">Sitemap</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; {date.today().year} Runout Rank. Built for players, not for arcade pool.</span>
        <span>Android &amp; iOS &middot; Dark mode only, like the app</span>
      </div>
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


def page(slug, title, description, body, extra_schema=None, noindex=False, keywords=None):
    canonical = SITE_URL + ("" if slug == "index.html" else slug)
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    schema = ""
    if extra_schema:
        for block in extra_schema:
            schema += f'  <script type="application/ld+json">\n{block}\n  </script>\n'
    kw = f'  <meta name="keywords" content="{html.escape(keywords)}">\n' if keywords else ""
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
{schema}</head>
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
  "description": "Runout Rank is a billiards skill-rating app. Take a ten-table run-out test on a real pool table, get a 0-100 rating and a tier from Rookie to Master, then practise at the level that beats you. All data stays on your device.",
  "featureList": [
    "Ten-table Rating Test with a 0-100 rating and a named tier",
    "Six challenge levels from Rookie to Master",
    "Seeded tests that are identical for every player on Android and iOS",
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
        <p class="eyebrow">Billiards skill rating &middot; Android &amp; iOS</p>
        <h1>How good are you at pool, <span class="accent">really</span>?</h1>
        <p class="lead">You have put in the hours. Runout Rank turns them into a number.
        Take a ten-table run-out test on your own table, get a 0&ndash;100 rating and a tier from
        Rookie to Master, then train at the level that is actually beating you.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="how-it-works.html">See how the test works</a>
          <a class="btn btn--ghost" href="levels.html">Browse the six levels</a>
        </div>
        <p class="hero-note">No account &middot; No sign-in &middot; Works offline &middot; Data stays on your device</p>
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
        <div><span class="stat">10</span><p class="dim">tables per test, one attempt each &mdash; no retries, no skips</p></div>
        <div><span class="stat">0&ndash;100</span><p class="dim">rating with a named tier, the moment the test ends</p></div>
        <div><span class="stat">6</span><p class="dim">levels from Rookie to Master, none of them locked</p></div>
        <div><span class="stat">0</span><p class="dim">accounts, servers and network calls required</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">The difference</p>
        <h2>Random layouts. <span class="accent">Identical for everyone.</span></h2>
        <p class="lead">Most skill tests use the same fixed layouts, so sooner or later you are
        practising the answers rather than the skill. Runout Rank generates every table randomly
        &mdash; but from a seed. Level&nbsp;3 Test&nbsp;#12 is the same ten tables for every player,
        on Android and on iOS.</p>
      </div>
      <div class="grid grid--3">
        <div class="card">
          <h3>Unpredictable to you</h3>
          <p>You cannot memorise a layout you have never seen. Every test you start is generated,
          not pulled from a fixed set of drills.</p>
        </div>
        <div class="card">
          <h3>Comparable to anyone</h3>
          <p>Share a test number and a friend gets the identical ten tables. Two scores from the same
          level and test number mean the same thing.</p>
        </div>
        <div class="card">
          <h3>Proven across platforms</h3>
          <p>The generator is pinned by golden-vector tests on both platforms, so an Android score and
          an iOS score are the same measurement.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">How it works</p>
        <h2>Three steps, one sitting</h2>
      </div>
      <div class="grid grid--3 steps">
        <div class="card step">
          <h3>Rack what the app draws</h3>
          <p>Each table is drawn top-down with the cue ball, the object balls and any blockers, so you
          can set the exact layout up on the table in front of you.</p>
        </div>
        <div class="card step">
          <h3>Play it once</h3>
          <p>Run out or miss, then record it with one tap. One attempt per table &mdash; that is what
          makes the score at the end mean something.</p>
        </div>
        <div class="card step">
          <h3>Get a rating and a plan</h3>
          <p>Score out of ten, a 0&ndash;100 rating, your tier, whether you cleared the level, and the
          level that is beating you. Practise there in one tap.</p>
        </div>
      </div>
      <p style="margin-top:28px"><a href="how-it-works.html">Read the full explanation of the rating &rarr;</a></p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-test.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="A Rating Test in progress showing table 6 of 10, the generated layout, and the run-out and miss buttons."></div>
        </div>
        <div>
          <p class="eyebrow">The Rating Test</p>
          <h3>Ten tables. One attempt each.</h3>
          <p>You always know where you stand mid-test: which table you are on, which ones you ran out,
          which ones you missed. Get interrupted and the test resumes at the exact table you stopped on,
          so a phone call or a closing venue does not cost you the sitting.</p>
          <ul class="ticks">
            <li>One tap to record a run-out or a miss</li>
            <li>No retries and no skips &mdash; the score is honest by construction</li>
            <li>Quitting takes a confirmation, so you never discard a run by accident</li>
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
          <p>Seven out of ten clears a level. The result screen gives you the score, the 0&ndash;100
          rating, your tier and how far the rating moved since your last test &mdash; then names your
          edge level in plain language and sends you straight there to practise.</p>
          <ul class="ticks">
            <li>Rating delta so improvement is visible immediately</li>
            <li>Share the result as a card or as text naming the level and test number</li>
            <li>Whoever you send it to can take the identical test</li>
          </ul>
        </div>
      </div>

      <div class="feature">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-levels.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="The levels screen showing the six-level ladder with the current edge level highlighted in gold."></div>
        </div>
        <div>
          <p class="eyebrow">The ladder</p>
          <h3>Six levels. Nothing locked.</h3>
          <p>Rookie, Regular, League, Competitor, Advanced, Master. Each level tells you exactly what
          makes it harder &mdash; ball count, whether you get ball in hand, how tightly the balls are
          packed, and blockers. Test at any level you like; a strong player never has to grind up from
          the bottom.</p>
          <p><a href="levels.html">Compare all six levels &rarr;</a></p>
        </div>
      </div>

      <div class="feature feature--flip">
        <div class="feature-media">
          <div class="phone"><img src="assets/img/screen-practice.png" width="1080" height="2400" loading="lazy" decoding="async"
            alt="A practice session showing a generated four-ball layout and the success and failed buttons."></div>
        </div>
        <div>
          <p class="eyebrow">Practice</p>
          <h3>Set it up on your own table.</h3>
          <p>An endless stream of randomly generated layouts at whatever level you choose. Log a
          success or a failure with one tap, retry the same layout until you own it, skip one you do
          not fancy, or come straight back to the last table you generated.</p>
          <p><a href="practice.html">More on practice and the training log &rarr;</a></p>
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
          <p>Where you stand is free, permanently: rating, tier, cleared level, edge level, lifetime
          attempts, run-out rate, best streak and the per-level breakdown. Runout Pro adds the history
          &mdash; every test plotted over time, the full test log, and CSV export.</p>
          <p><a href="runout-pro.html">What Runout Pro adds &rarr;</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="container">
      <div class="grid grid--2">
        <div class="card">
          <p class="eyebrow">Privacy</p>
          <h3>Your record never leaves your phone</h3>
          <p>Tests, attempts, favourites and statistics are stored only in the app's private storage
          on your own device. There is no account to create and nothing to sign in to, and your
          history survives app updates.</p>
          <p><a href="privacy-policy.html">Read the privacy policy &rarr;</a></p>
        </div>
        <div class="card">
          <p class="eyebrow">Same app, either platform</p>
          <h3>Android and iOS, identical scoring</h3>
          <p>The test generator and the rating maths are shared code, verified against the same golden
          vectors on both platforms. The phone you happen to own has no effect on your rating.</p>
          <p><a href="pool-skill-level-test.html">Why a repeatable test beats a guess &rarr;</a></p>
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

      <h2>Why the tests are random <em>and</em> comparable</h2>
      <p>Every test is generated rather than picked from a fixed set, so there are no answers to
      memorise in advance. But the generator is seeded by the level and the test number, which means
      <strong>Level&nbsp;3 Test&nbsp;#12 is the identical ten tables for every player</strong>, on
      Android and on iOS alike.</p>
      <p>That is what lets you share a score. Send a friend the level and test number, they take the
      same ten tables, and the two results are directly comparable &mdash; with no account, no server
      and no leaderboard in between.</p>

      <h2>What the rating is not</h2>
      <p>It is a measurement of your run-out ability on generated layouts, taken under a no-retry rule.
      It is not a handicap system, not a governing-body rating, and it does not talk to any league
      database. It is an honest number you can take yourself, on your own table, whenever you want a
      fresh one.</p>

      <div class="btn-row" style="margin-top:36px">
        <a class="btn btn--primary" href="levels.html">See the six levels</a>
        <a class="btn btn--ghost" href="faq.html">Read the FAQ</a>
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

      <h2>3. It has to be repeatable in the same form for everyone</h2>
      <p>Here is the tension: randomness makes a test honest, and it also makes two scores
      incomparable. If your ten tables were harder than mine, our scores mean different things.</p>
      <p>The fix is <strong>seeding</strong>. The layouts are generated by an algorithm from a fixed
      starting number, so they are unpredictable to the player but perfectly reproducible for the
      program. In Runout Rank, the seed is the level plus the test number: Level&nbsp;3 Test&nbsp;#12
      is the same ten tables for every player, on Android and iOS alike. You cannot practise the
      answers, and you can still compare your score to anyone else's &mdash; without an account, a
      server, or a leaderboard.</p>

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

      <div class="note">Runout Rank does all of this on the table you already play on: it generates
      the layouts, scores the run-outs, keeps the history on your device, and names the level to train
      at next. <a href="how-it-works.html">See exactly how the test works &rarr;</a></div>
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
     "The layouts are generated from a seed made of the level and the test number. That makes them "
     "unpredictable to a player but perfectly reproducible for the app: Level 3 Test #12 is the "
     "identical ten tables for everyone, on Android and iOS."),
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
    ("Is Runout Rank the same on Android and iOS?",
     "Yes. The test generator and the rating maths are shared code, pinned by the same golden-vector "
     "tests on both platforms, so the phone you own has no effect on your rating."),
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
    ("index.html",
     "Runout Rank — Pool Skill Rating Test & Training App for Android and iOS",
     "How good are you at pool, really? Take a ten-table run-out test on your own table, get a 0–100 "
     "rating and a tier from Rookie to Master, then practise at the level that beats you. No account, "
     "works offline.",
     INDEX, [APP_SCHEMA, SITE_SCHEMA],
     "pool skill test, billiards rating app, run-out test, pool training app, pool skill level, "
     "billiards practice app, pool rating 0-100"),
    ("how-it-works.html",
     "How the Runout Rank rating works — ten tables, one attempt each",
     "Ten randomly generated tables at one level, one attempt each, scored into a 0–100 pool rating "
     "and a tier. Seeded so the same test number is the identical ten tables for every player.",
     HOW, [breadcrumb_schema("How it works", "how-it-works.html")], None),
    ("levels.html",
     "The six levels — Rookie to Master | Runout Rank",
     "Rookie, Regular, League, Competitor, Advanced, Master. What changes at each rung of the ladder — "
     "ball count, ball in hand, packing and blockers — and why nothing is locked.",
     LEVELS, [breadcrumb_schema("Levels", "levels.html")], None),
    ("practice.html",
     "Pool practice sessions and a training log that remembers | Runout Rank",
     "Endless randomly generated practice layouts at the level you choose, one-tap logging, retry and "
     "skip, favourites, and a complete training log of every table you have run.",
     PRACTICE, [breadcrumb_schema("Practice", "practice.html")], None),
    ("runout-pro.html",
     "Runout Pro — your full rating history and CSV export | Runout Rank",
     "Where you stand is free, permanently. Runout Pro adds how you got there: rating plotted over "
     "every test, per-level progression, the full test log and CSV export.",
     PRO, [breadcrumb_schema("Runout Pro", "runout-pro.html")], None),
    ("pool-skill-level-test.html",
     GUIDE_TITLE,
     "What separates a pool skill test worth taking from a drill you happen to like: whole run-outs, "
     "unpredictable layouts, seeded repeatability, one attempt per table, and what to do with the number.",
     GUIDE,
     [f"""{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{GUIDE_TITLE}",
  "description": "What separates a pool skill test worth taking from a drill you happen to like.",
  "image": "{SITE_URL}assets/img/og-image.png",
  "author": {{"@type": "Organization", "name": "Runout Rank"}},
  "publisher": {{"@type": "Organization", "name": "Runout Rank"}},
  "datePublished": "{LASTMOD}",
  "dateModified": "{LASTMOD}",
  "mainEntityOfPage": "{SITE_URL}pool-skill-level-test.html"
}}""", breadcrumb_schema("Pool skill level test", "pool-skill-level-test.html")],
     "how to test pool skill level, pool skill test, billiards skill assessment, run-out drill, "
     "pool rating system"),
    ("faq.html",
     "Runout Rank FAQ — the test, the rating, the levels and your data",
     "Do you need a real table? An account? How is the rating calculated, how can random tests be "
     "comparable, and what does Runout Pro add? Answers to the common questions.",
     FAQ, [FAQ_SCHEMA, breadcrumb_schema("FAQ", "faq.html")], None),
]


def main():
    written = []
    for slug, title, description, body, schema, keywords in PAGES:
        with open(os.path.join(HERE, slug), "w", encoding="utf-8") as fh:
            fh.write(page(slug, title, description, body, schema, keywords=keywords))
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
    urls = ["index.html", "how-it-works.html", "levels.html", "practice.html", "runout-pro.html",
            "pool-skill-level-test.html", "faq.html", "privacy-policy.html"]
    priority = {"index.html": "1.0", "how-it-works.html": "0.9", "levels.html": "0.8",
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
  "description": "Pool skill rating test and training app for Android and iOS.",
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
