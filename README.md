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
| `runout-pro.html` | The free/Pro boundary |
| `pool-skill-level-test.html` | Long-form SEO guide: how to test your pool skill level |
| `faq.html` | FAQ (also emitted as `FAQPage` structured data) |
| `privacy-policy.html` | Generated from `content/privacy-policy.md` |
| `404.html` | Not-found page (`noindex`) |
| `sitemap.xml`, `robots.txt`, `site.webmanifest` | Generated |
| `assets/css/style.css` | The only stylesheet |
| `assets/img/` | Screenshots, icons, Open Graph image |
| `build.py` | Generates every page above |
| `serve.py` | Local preview server |

## Editing

All page copy lives in `build.py`. Edit it there, then regenerate:

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

## SEO

Every page carries a unique `<title>` and meta description, a canonical URL, Open Graph and Twitter
card tags, and JSON-LD. `index.html` declares `SoftwareApplication` and `WebSite`; the FAQ declares
`FAQPage`; the guide declares `Article`; sub-pages declare `BreadcrumbList`. `sitemap.xml` is
generated from the page list and referenced by `robots.txt`.

Images are sized (`width`/`height` set, so no layout shift), lazy-loaded below the fold, and the
hero image is marked `fetchpriority="high"`. There is no client-side JavaScript and no external
request of any kind — no fonts, no analytics, no CDN — so the pages render in one round trip.

## Before this goes live

1. **Set the domain.** `SITE_URL` at the top of `build.py` is currently
   `https://mylesieong.github.io/products/runout-rank/`, which matches the privacy-policy URL quoted
   in `docs/STORE_LISTINGS.md`. Change it if the site lands anywhere else, then rebuild — canonical
   tags, `og:url` and `sitemap.xml` all derive from it. Page links are relative, so the site works
   at a domain root or in a subdirectory either way.
2. **Fill in the privacy-policy placeholders.** `content/privacy-policy.md` still contains
   `[YOUR_LEGAL_ENTITY_NAME]`, `[YOUR_ADDRESS_OR_COUNTRY]`, `[YOUR_RETENTION_PERIOD]` and
   `[YOUR_SUPPORT_EMAIL]`, inherited from the app repo's copy. A published policy must not ship with
   those.
3. **Add the store links.** Both stores are rendered as "Coming soon" placeholders
   (`STORE_BLOCK` in `build.py`). Once the listings are live, turn them into `<a href>` elements.
4. **Verify ownership** in Google Search Console and Bing Webmaster Tools, and submit
   `sitemap.xml`.
