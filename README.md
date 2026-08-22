# Runout Rank — website

The static marketing site for [Runout Rank](https://github.com/) — a landing page plus a small set
of SEO pages. It is plain HTML and CSS: no framework, no JavaScript, no build step at deploy time.
Whatever is in this directory is what gets served.

The palette, type treatment and dark-only look are taken from the app itself
(`shared/src/commonMain/kotlin/com/municornio/app/tableinfinite/ui/theme/RunoutTheme.kt`), so the
site and the app read as the same product.

## Layout

| Path | What it is |
| --- | --- |
| `index.html` | Landing page |
| `how-it-works.html` | How the ten-table test and the rating work |
| `levels.html` | The six-level ladder and what changes at each rung |
| `practice.html` | Practice sessions and the training log |
| `fargo-rate-alternative.html` | Positioning page: the two pain points a relative league rating leaves open |
| `pool-rating-without-a-league.html` | Pain point one — a rating without 200 rated games |
| `absolute-vs-relative-pool-rating.html` | Pain point two — why a relative rating moves with your city |
| `runout-pro.html` | The free/Pro boundary |
| `pool-skill-level-test.html` | Long-form SEO guide: how to test your pool skill level |
| `faq.html` | FAQ (also emitted as `FAQPage` structured data) |
| `privacy-policy.html` | Generated from `content/privacy-policy.md` |
| `404.html` | Not-found page (`noindex`) |
| `zh/`, `vi/`, `pt/`, `ko/` | The same twelve pages in Simplified Chinese, Vietnamese, European Portuguese and Korean |
| `sitemap.xml`, `robots.txt`, `site.webmanifest` | Generated |
| `assets/css/style.css` | The only stylesheet |
| `assets/img/` | Screenshots, icons, Open Graph image |
| `build.py` | Layout, `<head>`, hreflang and sitemap. Contains no copy |
| `common.py` | Constants, the locale registry and copy helpers |
| `locales/` | All page copy, one module per language |
| `serve.py` | Local preview server |

## Editing

All page copy lives in `locales/<code>.py` — English in `locales/en.py`. `build.py` holds the layout
and no copy at all, so editing a page means editing its locale module, then regenerating:

```bash
python3 build.py
```

Preview locally at <http://127.0.0.1:4173>:

```bash
python3 serve.py
```

The generated `.html` files are committed deliberately — that is what makes this deployable to
GitHub Pages, Netlify, S3 or any static host with no pipeline.

### The privacy policy

`content/privacy-policy.md` is a copy of `docs/PRIVACY_POLICY.md` from the app repo, with the H1
removed (the page supplies its own). If the app's policy changes, copy it across and rebuild.

Each language has its own `content/privacy-policy.<code>.md` (for example `privacy-policy.ko.md`);
the build falls back to the English file if one is missing. Every translation opens with a note that
the English version prevails if the two disagree, so the translations stay a reading convenience
rather than a second legal text. **When the English policy changes, update the translations too.**

## Languages

The site ships in five languages: English at the root, and one subdirectory per translation.

| Code | Directory | Language |
| --- | --- | --- |
| `en` | *(root)* | English — the source language, and the `x-default` target |
| `zh-Hans` | `zh/` | Simplified Chinese |
| `vi` | `vi/` | Vietnamese |
| `pt-PT` | `pt/` | European Portuguese |
| `ko` | `ko/` | Korean |

Every page exists in every language, so the hreflang set is always complete and the footer language
switcher links to the *same* page in each language rather than dumping the reader on a home page.

Each `locales/<code>.py` exposes exactly three names — `LOCALE`, `UI` and `PAGES` (plus `NOT_FOUND`)
— and `build.py` renders a language from those alone. A translation is therefore a copy of
`locales/en.py` with the strings replaced: no template, layout or CSS changes are involved.

To add a language, add an entry to `LOCALES` in `common.py` and a matching module in `locales/`.
Nothing in `build.py` needs to change.

Some things are deliberately *not* translated: the level names (Rookie … Master) and the tier labels,
because they are what the app itself displays; `Runout Rank` and `Runout Pro`; and the app
screenshots, since the app is English-only.

## Positioning

The site markets Runout Rank as an **absolute** pool rating, against the two structural costs of the
relative league ratings players are otherwise pointed at (Fargo Rate and its family):

1. **A relative rating takes 200 games to establish.** FargoRate's own definition of *robustness*
   sets 200 games as the minimum for an established rating and blends in a starter rating below that
   — which for a casual player means a league, fees and most of a season before the number is theirs.
2. **A relative rating is anchored to the players around you.** Every rating is a position in a
   network of other ratings, so a thin or weakly connected local scene can sit high or low against
   the rest of the world. FargoRate describes the nearly-isolated-groups case as a vexing problem.

Runout Rank's answer: **a level's constraints are the yardstick** — object ball count, ball in hand
or not, minimum spacing, blockers — so no opponent enters the calculation, one session produces a
full rating, and the number travels.

Note what the yardstick is *not*. Layouts are generated fresh for every test and are **not** shared
between players; the app dropped seeded tests (see `RatingTestGenerator`'s comment on why), so the
site must never claim two players get the same ten tables, that a test number can be replayed, or
that anything is "pinned by golden vectors". What is fixed is the difficulty, not the tables.

Two rules for this copy. **Stay factual** — every claim about Fargo Rate above is traceable to
FargoRate's own published material, and the pages link to it. **Stay fair** — each comparison page
credits what a relative rating is better at (handicapping matches), states plainly that Runout Rank
is not a handicap system, admits its own variable (your table's pockets and cloth), and carries the
`FARGO_DISCLAIMER` non-affiliation notice. Do not let that slip in future edits; the audience knows
the subject and overreach costs more than it wins.

## Authorship and dates

`AUTHOR_NAME` in `common.py` and `author_title` in each locale's `UI` drive a visible byline under
the H1, plus
`<meta name="author">`, `article:published_time` / `article:modified_time`, and the `author` field of
each `Article` block.

**Only the long-form SEO pages are bylined and dated** — the four that carry `Article` schema
(`fargo-rate-alternative`, `pool-rating-without-a-league`, `absolute-vs-relative-pool-rating`,
`pool-skill-level-test`). They opt in with `dated=True` in their `PAGES` entry. The landing page and
the product pages deliberately carry neither: a byline on a landing page is noise, and the dates are
there to give the guides authorial provenance, not to date the product.

Dates come from two constants in `common.py`: `FIRST_PUBLISHED` (when the site went up) and
`UPDATED` (the date of
the current copy, and the sitemap `lastmod`). A page may override either with the `published` /
`updated` keys in its `PAGES` entry — the newer positioning pages set `published=UPDATED`. **Bump
`UPDATED` whenever you change page copy**, so the byline and the sitemap do not claim a page is
older than it is.

## SEO

Every page carries a unique `<title>` and meta description, a canonical URL, Open Graph and Twitter
card tags, authorship and date metadata, and JSON-LD. `index.html` declares `SoftwareApplication`
and `WebSite`; the FAQ declares `FAQPage`; the guide and the three positioning pages declare
`Article` with a `Person` author; sub-pages declare `BreadcrumbList`, and every block carries
`inLanguage`. `sitemap.xml` is generated from the page list and referenced by `robots.txt`.

Every page also carries the full `hreflang` set for all five languages plus `x-default` (pointing at
English), in both the `<head>` and as `xhtml:link` alternates on each `sitemap.xml` entry.

Images are sized (`width`/`height` set, so no layout shift), lazy-loaded below the fold, and the
hero image is marked `fetchpriority="high"`. There is no client-side JavaScript and no external
request of any kind — no fonts, no analytics, no CDN — so the pages render in one round trip.

## Before this goes live

1. **Set the domain.** `SITE_URL` at the top of `common.py` is currently
   `https://mylesieong.github.io/products/runout-rank/`, which matches the privacy-policy URL quoted
   in `docs/STORE_LISTINGS.md`. Change it if the site lands anywhere else, then rebuild — canonical
   tags, `og:url`, `hreflang` and `sitemap.xml` all derive from it. Page links are relative, so the site works
   at a domain root or in a subdirectory either way.
2. **Fill in the privacy-policy placeholders.** `content/privacy-policy.md` still contains
   `[YOUR_LEGAL_ENTITY_NAME]`, `[YOUR_ADDRESS_OR_COUNTRY]`, `[YOUR_RETENTION_PERIOD]` and
   `[YOUR_SUPPORT_EMAIL]`, inherited from the app repo's copy. A published policy must not ship with
   those. The four translated copies in `content/` carry the same placeholders.
3. **Add the App Store link.** Google Play is live and linked (`PLAY_URL` in `common.py`). The iOS
   build is still in review, so that half of `store_block()` is a `store-link--pending` label rather
   than a link — turn it into an `<a href>` once the listing is approved.
4. **Verify ownership** in Google Search Console and Bing Webmaster Tools, and submit
   `sitemap.xml`.
