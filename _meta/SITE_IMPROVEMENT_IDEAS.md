# hunterdavis.com — 2026 Refresh: Site Improvement Ideas

> Internal planning doc. Lives in `_meta/` so Jekyll ignores it
> (Jekyll only processes the well-known `_posts`, `_drafts`, `_includes`,
> `_layouts`, `_data`, `_sass`, `_site` directories — any other `_`-prefixed
> directory is left alone).

---

## How to use this doc

1. Read **At a glance** and **Vision** to remember where we're going.
2. When you have ~15 min, take the **lowest-numbered un-checked item** in
   the backlog and ship it as a single commit.
3. Each backlog item is scoped to one PR-sized change with a clear
   acceptance criterion. If an item starts to grow, split it.
4. After shipping, check the box and (if needed) write a 1-line note
   under the item.
5. The **Appendix A: Greatest Hits / Milestones** dossier is the source
   of truth for the timeline / hero-strip content. Update it as we
   learn more.

Status legend: `[ ]` todo · `[~]` in flight · `[x]` shipped · `[-]` dropped

---

## At a glance

- 30-year personal site. **507 posts** spanning **2007 → 2026**, peak burst
  of 168 posts in 2011 (the "65 Apps in 60 Days" era).
- Built with **Jekyll 3.8.5** + an old Bitwiser theme. Source CSS is
  ~500 lines; layouts are minimal and dated.
- **78% of posts (394/507) have no tags.** No category index, no archive
  page, no project hub, no related posts. Sidebar is a hardcoded list
  of legacy links.
- **1.4 GB built site.** 8,025 images. 30+ images per year in 2013/14/17/18
  exceed 2 MB. Top 10 home-page-eligible photos are **5–13 MB JPGs**.
- `_site/search.html` is **1.18 MB** because `search.md` inlines
  every post's full content into a JSON blob via Liquid.
- jQuery 1.4 (2010), modernizr 1.6 (2010), font-awesome via CDN, an
  unused disqus include, and a Google Analytics include without an ID.
- `/favicon.png` and `/sharer.png` (OG/Twitter image) are referenced by
  every page and **404 in production**.
- `_config.yml` has `url: http://www.hunterdavis.com` (not https), and
  the canonical link in `_includes/ssn.html` uses the wrong variable.
- About / Public-Speaking pages use legacy `<a id='...'>` anchors
  rather than heading IDs, with a long manual TOC each.

The gap to a 2026 site is wide but the work is mostly mechanical and
parallelizable. We can ship value in the first commit and keep
shipping.

---

## Vision

A modern personal site that respects the **archive** — 30 years of
hacks, books, projects, music, and writing — and is **easy to browse
by topic, era, or project**. Fast, accessible, dark-mode aware, and
shaped around three audiences:

1. **The fan** who remembers the Zipit / IM-ME / Dockstar / 65-apps
   era — needs a fast jump to that era and an obvious way to browse
   all of it.
2. **The newcomer** landing on a current project announcement
   (Johnny Castaway PS1, Tui000, Dunking Bird) — needs a "who is this
   person?" door and a clear list of related projects.
3. **The professional** evaluating Hunter — needs leadership /
   speaking / writing surfaces and a current bio without scrolling
   through hardware hacks.

Three operating principles for everything that follows:

- **Findability over flatness.** Every post belongs to a project,
  an era, and a topic. The site should expose all three.
- **Pre-rendered before client-side.** Tag pages, archives, and
  project hubs are static HTML. Search index is fetched, not inlined.
- **Don't break old URLs.** This site has 30 years of inbound links
  (Hackaday, Engadget, OSNews, HN, Reddit, archive.org). All current
  permalinks must keep resolving.

---

## Audit findings (current state)

### Information architecture
- Top nav has 3 items: Home, My Story, Public-Speaking.
- No `/tags/`, no `/tag/<slug>/`, no `/archive/`, no `/projects/`.
- No project hub, even though there are clear families: Johnny
  Castaway (9 posts), Zipit Z2 (29), Discursive Labs (20),
  QuickGrapher (15), Rhapsody (10), Dockstar (10), IM-ME (8).
- Sidebar links are hand-coded in `_includes/sidebar.html`.
- `about.md` is 445 lines covering 30 years in one wall of text.
- Search exists but UX is a single text field with two sort buttons.

### Content & metadata
- 113/507 posts have a `tags:` block. The other 394 are untagged.
- Tag vocabulary is ad hoc — `android-apps-2`, `app-tag`, `easy`,
  `easy-images`, `hacks-2` are all in active use. Many tags appear
  exactly once.
- 64 posts use hardcoded `width="600"` on `<img>` tags inline.
- 35 posts embed `<iframe>` (mostly YouTube — many `http://`).
- 29 posts link to `play.google.com` apps that may be delisted.
- Many older posts (e.g. `2007-12-19-csserver-adventure.markdown`)
  link to `hunterdavis.com/*.zip` artifacts whose status is unknown.

### Performance
- Built site: **1.4 GB** total. Images alone: 1.4 GB.
  - 2013: 385 MB · 2014: 347 MB · 2017: 159 MB · 2011: 99 MB · 2012: 98 MB.
- Top images on disk: ten 12+ MB JPGs from 2014/04 (`100_05xx.jpg`
  series — looks like un-resized phone-camera dumps).
- `_site/search.html` is **1.18 MB** because `search.md` inlines
  every post's stripped content into `window.store`. Loading the
  search page parses a multi-megabyte literal JS object before the
  user even types.
- `feed.xml` ships full HTML content for the latest 20 posts (~115 KB).
- Home page renders **21 `<img>` tags per paginated page** with no
  `loading="lazy"`, no `width`/`height`, no `srcset`, and an empty
  `<img src="" width=600 />` for posts that have no image at all.
- Custom Bitwiser CSS imports `gridism`, an old `_buttons` (commented),
  `_anims`, `_monokai` — most of it is unused after the redesign.
- `default.html` always pulls font-awesome from `maxcdn.bootstrapcdn.com`
  (offline / privacy concern) even though only `<i class="fa fa-...">`
  in nav and meta-info uses it.

### Accessibility
- No `<main>` landmark. No skip-to-content link.
- Body color `#333` on `#eee` is fine. `#08c` link on white meets AA.
- `text-align: justify` on prose causes river artifacts; many users
  have it turned off in extensions for readability.
- Most images have no `alt` (Markdown `![]()` and inline HTML alike).
- Anchor links in `about.md` / `public-speaking.md` use
  `<a id='...'>Heading</a>` which is technically valid but breaks
  outline tools and screen readers expecting heading semantics.
- Mobile menu (`.android` class) toggles via untracked JS.

### SEO / metadata
- `_config.yml`: `url: http://www.hunterdavis.com` (HTTP, not HTTPS).
- `_includes/ssn.html` writes `<link rel="canonical" href="{{ site.base_url }}{{ page.url }}">` —
  but `site.base_url` is also `http://...` and is duplicated with
  `site.url`. One source of truth needed.
- OG image is hardcoded to `/sharer.png` — **which 404s.**
- Favicon is `/favicon.png` — **which 404s.**
- `<meta name="keywords">` is set per page, but Google ignored it
  ~15 years ago.
- `feed.xml` is hand-rolled instead of using `jekyll-feed`.
- `sitemap.xml` is hand-rolled and uses `site.base_url`.
- No JSON-LD structured data anywhere.

### Maintenance / repo
- `Gemfile`: jekyll 3.8.5 (current major is 4.x; ruby 3.x compatibility
  suffers on 3.8.5).
- `index.old`, `_includes/disqus.html` (unused), `_includes/jquery-*.js`
  + `modernizr-*.js` + `obfs_embed.js` are dead weight unless invoked
  for the legacy `quickgrapher` embedded page.
- `_includes/header.html` conditionally loads scripts from
  `https://www.hunterdavis.com/...` — server side-loading on a static
  site is awkward and breaks if the asset CDN moves.

---

## URL preservation strategy

A 30-year archive lives or dies on its inbound links. The redesign
must keep every URL that was ever public *resolving* — same
content, optionally with a 301 to the new canonical.

### What's safe today

- `_config.yml` does not set `permalink:`, so Jekyll uses the
  default `/:year/:month/:day/:title.html`. **As long as we never
  change that key**, every existing Jekyll-era post URL keeps
  working forever.
- All new surfaces in this plan (`/projects/`, `/tag/`, `/archive/`,
  `/now/`, `/uses/`, `/milestones/`) are *additive*. They don't
  displace anything.

### What's at risk

A `2026-05-10` audit of every `hunterdavis.com/...` URL referenced
inside posts, `about.md`, and `public-speaking.md` found **285
distinct legacy URLs** that are NOT in the current Jekyll
permalink shape. Categorized:

| Category | Count | Example |
|---|---:|---|
| Pre-Jekyll `/android-app-*` slug | 119 | `/android-app-easy-cat-whistle` |
| Live GitHub-Pages project paths | 42 | `/quickgrapher/`, `/resume/` |
| Loose root images | 29 | `/im_me.jpg`, `/famicom.jpg` |
| WP `/?p=NNN` numeric | 22 | `/?p=3163` |
| Pre-Jekyll `/android-game-*` slug | 16 | `/android-game-the-grind` |
| `/archives/NNN` | 13 | `/archives/843` |
| Loose artifact archives | 11 | `/csa.zip`, `/zipit.tgz`, `/wirelessplusx.rar` |
| Pre-Jekyll `/android-apps/<cat>/<slug>/` | 10 | `/android-apps/audio-tools/...` |
| Pre-Jekyll `/popular-open-source-projects/*` | 6 | `/popular-open-source-projects/source-tree-visualizer/` |
| Loose code/text files | 5 | `/cam.cpp`, `/snesaver.pl`, `/pidgraph.sh` |
| `/category/*` and `/archives/category/*` | 4 | `/category/zipit-hacking/` |
| Pre-Jekyll `/about/<slug>/` | 3 | `/about/i-have-cured-my-own-sleep-paralysis-and-you-can-too/` |
| One-off (`/?s=`, `.pdf`, `.ipk`, anchors) | 4 | `/hunterdavis.pdf` |

Plus all the inbound links from third-party publications
(Hackaday, Engadget, Make, HN, Reddit) that we *can't* enumerate
from the repo.

In addition:

1. **Page moves** — `about.md` (live at `/about.html`) splits into
   `/about/` + sub-pages in Phase 7.7. `public-speaking.html` moves
   to `/about/leadership/` in Phase 7.8.
2. **Image / asset URLs under `/content/images/...`** — many
   third-party blog posts embed these directly. They must keep
   serving exactly the same paths forever (no path rewrites in
   the image-optimization phase — derivatives go in sibling files,
   originals stay put).
3. **Scheme + host** — `http://hunterdavis.com`, `http://www.hunterdavis.com`,
   `https://hunterdavis.com`, `https://www.hunterdavis.com` should
   all canonicalize to one form.
4. **Trailing slash and `.html`** — Jekyll currently emits
   `/post.html`. Don't introduce a parallel `/post/` form unless
   we 301 one to the other.

### Critical: GitHub Pages project-subpath reservation

Hunter's site is deployed via GitHub Pages from this user-page
repo. Other repos under `huntergdavis/` are auto-published at
`hunterdavis.com/<repo-name>/`. That's why `/quickgrapher/`,
`/resume/`, `/streak`, `/solitaire`, `/visualizer`, `/peoplegrid`,
`/psyrunner`, `/asteroidminer`, `/teamplanningsimulator/`,
`/media/`, `/photo-stream/`, `/inboxzero`, `/poke`, `/webflight`,
`/2djsgameboilerplate`, `/asljs/`, etc. resolve today: they're
**separate repos**, not paths in this Jekyll site.

Hard rule for this redesign:

> **Any path that matches the name of another `huntergdavis/*` repo
> is reserved.** This Jekyll repo must not emit content at those
> paths or the project deploy wins / collides unpredictably.

Names already known to be reserved (from the sidebar + audit):
`quickgrapher`, `resume`, `streak`, `solitaire`, `visualizer`,
`peoplegrid`, `psyrunner`, `asteroidminer`, `teamplanningsimulator`,
`media`, `photo-stream`, `inboxzero`, `poke`, `webflight`,
`2djsgameboilerplate`, `asljs`, `johnnycastawaywine`, `linked_out`.

Concretely, this means our new IA stays in the safe namespaces:
`/projects/`, `/tag/`, `/tags/`, `/archive/`, `/about/`,
`/milestones/`, `/now/`, `/uses/`, `/writing/` — none of which
collide with the project repos above. Before introducing any new
top-level path, run `gh repo list huntergdavis --limit 200` and
make sure the slug isn't taken.

### Five-layer fix

**Layer 1: Don't move existing post permalinks.**
Status: free. Just hold the line in `_config.yml` (Phase 0.16).

**Layer 2: Page-level redirects via `jekyll-redirect-from`.**
GitHub-Pages whitelisted plugin; emits a static stub at every
`redirect_from:` URL with a `<meta http-equiv="refresh">` and
`<link rel="canonical">`. Google treats that as a 301 in practice.
Add to a moved page's frontmatter:
```yaml
redirect_from:
  - /about.html
  - /about/
```
Used for: any page move, any URL collapse, and (in bulk) for the
WordPress slug recovery in Layer 3.

**Layer 3: WordPress era URL recovery (the big one).**

Single source of truth: `_data/legacy_redirects.yml`, organized
by category:

```yaml
# /archives/NNN — pre-Jekyll WP numeric IDs
archives:
  - id: 843
    to: /2010/11/28/a-25-gamingemulation-powerhouse-using-the-dockstar-as-a-gaming-console.html
    source: hackaday-2011-01-02
  - id: 1640
    to: /2011/08/01/android-updates-and-i-claim-the-crown.html
    source: hn-2703378
  # ...

# /?p=NNN — same WP IDs, query-string form
wp_query_ids:
  - id: 3163
    to: /2012/07/21/android-sound.html
  # ...

# Pre-Jekyll WP slug → current Jekyll URL
wp_slugs:
  - from: /android-app-easy-cat-whistle
    to: /2011/06/<date>/easy-cat-whistle.html
  - from: /zipit-z2-a-wireless-tor-and-privoxy-router-in-the-palm-of-your-hand
    to: /2008/12/12/zipit-z2-a-wireless-tor-and-privoxy-router-in-the-palm-of-your-hand.html
  # ...

# WP categories → tag/archive equivalents
wp_categories:
  - from: /category/zipit-hacking/
    to: /tag/zipit-z2/
  - from: /archives/category/zipit-hacking
    to: /tag/zipit-z2/
  # ...

# Pre-Jekyll /about/<slug>/ → current post
about_slugs:
  - from: /about/i-have-cured-my-own-sleep-paralysis-and-you-can-too/
    to: /2008/07/24/i-have-cured-my-own-sleep-paralysis-and-you-can-too.html
  # ...
```

A Jekyll generator `_plugins/legacy_redirects.rb` walks the data
file and emits redirect stubs at every `from`/`id` URL. Stubs use
the same meta-refresh + canonical pattern as `jekyll-redirect-from`
so behavior is consistent.

Recovery sources, in order of cost:
1. **Free** — grep in-repo cross-references (the 285-URL audit).
   Yields ~180 mappable URLs immediately because most have a clear
   Jekyll counterpart by slug match (e.g., `/android-app-easy-cat-whistle`
   ↔ a Jekyll post with `easy-cat-whistle` in its slug).
2. **Cheap** — research-agent dossier confirms 3 high-value IDs
   (843, 1640, 201).
3. **Worth doing** — `script/scrape_wayback_legacy_urls.py` walks
   `web.archive.org/web/*/hunterdavis.com/*`, extracts
   `(url, post_title, post_date)` tuples for any URL not already
   in the data file, best-matches each to a current Jekyll post.
4. **Acceptable fallback** — anything still unmapped after the
   sweep falls through to the smart 404 (Phase 7.13) which reads
   `window.location.pathname`, runs a search against the post
   index, and presents likely matches.

**Layer 4: Loose-artifact mirroring.**

For every `*.zip`, `*.tgz`, `*.rar`, `*.pdf`, `*.ipk`, `*.pl`,
`*.sh`, `*.cpp`, `*.txt`, `*.ods`, `*.gif`, `*.jpg`, `*.png`
referenced from a post but absent from the repo, recover the file
from `web.archive.org` and **commit it to the repo at the exact
original path**. No redirect, no stub — the URL serves the bytes
directly, exactly as the inbound link expects.

Audit found ~22 loose artifacts + 29 loose root images + a
handful of `/hackaway2010/*.JPG` and `/discursivelabs/...png`
files. Total recovery is well under 100 MB; many are sub-100 KB.

Repo paths for committed mirrors:
```
csa.zip                           # ./csa.zip
zipit.tgz                         # ./zipit.tgz
hackaway2010/famicom.JPG          # ./hackaway2010/famicom.JPG
discursivelabs/images/3lakes.png  # ./discursivelabs/images/3lakes.png
```

These paths are git-tracked but excluded from Jekyll's
`destination` rewrite — they ship as static files. (Jekyll copies
non-`_`-prefixed root files to `_site/` by default; this works
out of the box.)

**Layer 5 (host): scheme + host normalization.**
Currently GitHub Pages serves the apex domain (`CNAME` =
`hunterdavis.com`). GitHub Pages does support HTTPS, apex/www
canonicalization, and `jekyll-redirect-from` meta-refresh stubs,
but it does not do true 301 status codes for arbitrary URLs. If
true 301s ever become required (better SEO, cleaner Lighthouse
score), Phase 8.4 moves to Cloudflare Pages with a `_redirects`
file fronting GitHub. Until then, the layer-2/3/4 stubs are good
enough.

### Verification

Add `script/check_redirects.py` (Phase 8): for a curated list of
canonical-old-URLs (from Hackaday, Engadget, Make, HN), assert
that the production site returns 200 (or 301→200) for each.
Runs in CI; fails the build if a known historical URL stops
resolving.

---

## Information architecture proposal

### Top nav (replace 3 items with 5)

| Slot | Slug | Purpose |
|------|------|---------|
| Now | `/` | Latest posts + "Currently working on" + recent project tile |
| Projects | `/projects/` | Hub. Cards for major project families |
| Writing | `/writing/` | Books + long-form essays + reviews |
| Archive | `/archive/` | By year, by tag, full search |
| About | `/about/` | Bio, leadership, speaking, contact |

### New URL surfaces

- `/projects/` — hub
- `/projects/johnny-castaway/` — combines all `johnny-*` posts plus
  PS1 announcement when ready
- `/projects/zipit-z2/` — 29 posts, 2008-2010 era hub
- `/projects/im-me/` — 8 posts
- `/projects/dockstar/` — 10 posts + distributed compilation book
- `/projects/65-apps-in-60-days/` — the 2011 grind with a counter
- `/projects/source-tree-visualizer/`
- `/projects/quickgrapher/`
- `/projects/ai-tools/` — Tui000, Labrync, TPS, Dunking Bird (small-joys era)
- `/projects/books/` — Hacks, Live For Free, Build Your Own DCC
- `/projects/games-and-music/` — composition, guitar, AirBeats
- `/projects/rhapsody/` — Napster work, Ford CES 2013, patents
- `/archive/` — year + month grid
- `/archive/2011/` etc — paginated year archive
- `/tag/` — full tag index with counts
- `/tag/<slug>/` — per-tag pages
- `/milestones/` — timeline of biggest moments (Hackaday hits,
  4M-hits day, CES launches, book releases, archive.org snapshots)
- `/now/` — Derek Sivers style "what I'm doing right now" page
- `/uses/` — gear/setup, dev environment
- `/about/` — split from monolithic `about.md` into bio + sub-pages
- `/about/leadership/` — moved from `/public-speaking.html`

### Tag taxonomy

A controlled vocabulary lives at `_data/tags.yml`. Each tag has
`slug`, `display`, `description`, `family` (e.g. hardware, software,
writing, life). Proposed top-level tag families:

- **hardware-hack**: zipit-z2, im-me, dockstar, pong-jr, oculus,
  retrofw, x86-handheld, custom-guitar
- **software**: android, ios, web, terminal, screensaver, emulator,
  game, tool, ai
- **systems**: linux, embedded, distributed-compilation, networking,
  privacy
- **writing**: book, essay, review, tutorial, fable
- **work**: discursive-labs, miso-media, rhapsody, napster, avvo,
  scalable-networks, mantra-health, apprenti
- **personal**: parenting, music-composition, guitar-building,
  woodworking, life
- **project**: johnny-castaway, tui000, labrync, tps, dunking-bird,
  source-tree-visualizer, quickgrapher, easy-apps, sith-challenge

### Related-posts strategy

Computed at build time from shared tags + same project family +
chronological neighbours. Show 3 below each post.

---

## Design system direction

### Brand & tone
- Personality: hacker, builder, careful adult. Warm but not precious.
- Voice already lives in the posts — design should get out of the way.
- Borrow nothing from "minimalist developer-blog" cliché. This is an
  archive of three decades of physical and digital projects; the
  design should feel **slightly maximal, slightly retro-futurist**,
  but with modern type and rhythm.

### Type
- System UI sans for chrome (`-apple-system`, `Segoe UI`, etc.).
- Self-hosted display serif for headings (consider keeping Vollkorn,
  but subset and self-host with `font-display: swap`).
- Mono for code: `ui-monospace`, `Menlo`, `Consolas`.
- Type scale: 1.25 ratio. `1rem` → `1.25rem` → `1.563rem` → ...
- Reading width: `65ch`.

### Color
- Light: warm off-white `#f7f5f0`, ink `#1f1d1a`, link `#0066cc`,
  accent `#cc4400` (rust/terminal-amber).
- Dark: charcoal `#15140f`, paper `#e8e4d8`, link `#7ab8ff`,
  accent `#ffaa66`.
- Tag chip: subtle filled pill, no border weight.

### Layout
- 1 column for prose; 2-column hub pages; 3-card grid on home.
- No fixed sidebar on mobile or desktop. Navigation via top nav and
  project hubs.
- CSS variables / design tokens. CSS Grid + Flex. Drop gridism.

### Motion
- 80ms ease-out for hover/focus. No long page transitions.
- Respect `prefers-reduced-motion`.

---

## Backlog (atomic commits, prioritized)

Effort key: **S** ≤ 30 min · **M** ≈ 1–2 h · **L** ≈ a focused half-day.
"File(s)" is the primary scope — supporting tweaks may pull in 1–2 more.

### Phase A — URL preservation (do this first)
*Goal: every URL that was ever public on `hunterdavis.com` keeps
resolving — Jekyll-era posts, the legacy WordPress URL shapes, the
loose downloadable artifacts, and the GitHub-Pages project paths.
Nothing in later phases is allowed to break a URL until this phase
is complete.*

- [x] **A.1** Lock the post permalink format. Set
      `permalink: /:year/:month/:day/:title.html` explicitly in
      `_config.yml` — currently it's the implicit default; locking
      it prevents an accidental theme change from breaking 500+
      indexed URLs. **S** · *Shipped 2026-05-10.* Verified safe
      pre-flight: 0 posts use `categories:` frontmatter, 0 posts
      live in subfolders, 0 posts override `permalink:`, all 507
      posts use the standard `YYYY-MM-DD-slug.markdown` shape, so
      the explicit string is identical to Jekyll's implicit
      default — zero URL changes.
- [x] **A.2** Inventory every legacy URL into a CSV.
      `script/audit_legacy_urls.py` greps every
      `https?://(www\.)?hunterdavis\.com/...` reference inside
      `_posts/`, `about.md`, `public-speaking.md` and emits
      `_meta/legacy_url_inventory.csv` with columns
      `url, category, in_repo, suggested_to, source_post,
      confidence, notes`. Categories match the table in the URL
      preservation section. Output is the input to A.6/A.7/A.8.
      **S** · *Shipped 2026-05-10.*
      Result: 1,958 rows from 1,794 unique URLs across 509 source
      files. **94.9% high confidence** (well above the 90% target),
      48 marked `mirror` for A.8 loose-artifact recovery, 36 truly
      unresolved (the WP `/?p=NNN` and `/archives/NNN` numeric IDs
      that need archive.org lookup in A.11), 5 `low` and 2 `medium`
      for human review. Idempotent — re-run any time after adding
      posts. Summary at `_meta/legacy_url_inventory_summary.txt`.
- [x] **A.3** Reserve `_data/projects_subpaths.yml` with the names
      of `huntergdavis/*` sibling repos that auto-publish at
      `hunterdavis.com/<name>/`. **S** · *Shipped 2026-05-10.*
      Authoritative list pulled live via
      `gh repo list huntergdavis --limit 300 --visibility=public --no-archived`,
      yielded **135 reserved names** under a single `reserved:` key
      with regeneration command, case-sensitivity note, and
      provenance comments in the file header. Build-fail check
      moved to A.13; live-subset verification moved to A.14.
- [x] **A.4** Add `jekyll-redirect-from` to `Gemfile` and the
      `plugins:` list in `_config.yml`. **S** · *Shipped 2026-05-10.*
      Plugin is GH-Pages whitelisted (works on the live host without
      changing deploy infra). Pre-flight: 0 posts use `redirect_from:`
      so adding the plugin is a no-op today and only activates as
      A.5/A.7 land. Gemfile.lock intentionally not regenerated; user
      runs `bundle install` next time they build locally.
- [x] **A.5** Seed `_data/legacy_redirects.yml` skeleton with the
      five sub-keys. **S** · *Shipped 2026-05-10.* `script/seed_legacy_redirects.py`
      regenerates from `_meta/legacy_url_inventory.csv` plus a
      hand-curated dossier dict. Final output:
      **15 archives entries** (13 from in-repo cross-references +
      1640 and 201 from the dossier; 843 and 1640 confirmed,
      remainder needs-wayback) and **4 wp_query_ids entries**
      (3163 confirmed via slug match to `/2012/07/21/android-sound.html`,
      others needs-wayback). `wp_slugs`, `wp_categories`,
      `about_slugs` are empty arrays — A.6 fills them. All three
      `confirmed`/`high` targets verified to point at existing
      files in `_posts/`. (Original spec said "22 `/?p=NNN` IDs"
      but those 22 were row-counts of variants; only 4 distinct
      base IDs exist: 3163, 3426, 3583, 5580.)
- [x] **A.6** Map the WordPress slug long tail. **L** ·
      *Shipped 2026-05-10.* `script/seed_legacy_redirects.py`
      extended with `_collect_by_url()` plus three category sets
      (`SLUG_CATEGORIES`, `CATEGORY_CATEGORIES`, `ABOUT_CATEGORIES`).
      Final mapped totals in `_data/legacy_redirects.yml`:
      **wp_slugs 162 entries** (160 high, 1 medium, 1 needs-wayback),
      **wp_categories 4** (all `low` — tag-taxonomy mapping needs
      human review against `_data/tags.yml` once Phase 2 lands),
      **about_slugs 3** (all high). Combined with archives + wp_query_ids:
      **188 total redirect candidates, 171 resolved → 91.0%
      coverage**, beating the >90% target. 12-of-12 random spot
      checks confirmed targets hit real `_posts/` files.
      Remaining 17 unresolved rows all flagged `needs-wayback`
      for Phase A.11.
- [x] **A.7** Emit redirect stubs for every entry in
      `_data/legacy_redirects.yml`. **M** · *Shipped 2026-05-10.*
      Took path (b) — `script/expand_redirects.py` writes
      `redirect_from:` arrays into target post frontmatter, picked
      up by `jekyll-redirect-from` on the live deploy without any
      CI changes. Stats: **93 posts updated, 164 legacy URLs wired
      to canonical Jekyll permalinks**. Filters in the script
      excluded 14 needs-wayback rows (no `to:`), 1 medium-confidence
      row, and 1 sibling-repo collision (`/source-tree-visualizer/`
      vs the `Source-Tree-Visualizer` GH-Pages-deployed repo). All
      507 posts re-parsed cleanly with PyYAML after the rewrite.
      Script is idempotent — re-running it on a post that already
      has `redirect_from:` is a no-op, so future post additions can
      be picked up by re-running without clobbering.
      `wp_query_ids` deferred to A.15 (query strings can't be
      static stub paths).
- [ ] **A.8** Loose-artifact mirror. From the CSV, fetch each
      referenced `/csa.zip`, `/zipit.tgz`, `/snesaver.pl`,
      `/cam.cpp`, `/hunterdavis.pdf`, `/wirelessplusx.rar`,
      `/easyexecute.zip`, `/freememuidemo.zip`, `/rexVM.zip`,
      `/titlescroll.zip`, `/titlescrollcomplete.rar`,
      `/titlescrollwithrandom.zip`, `/todd-zipit.tgz`,
      `/battlevel_*.ipk`, `/pidgraph.sh`, `/plainpcmfile.txt`,
      `/immeusblog.log.ods`, etc. (~22 files) from
      `web.archive.org` and commit at the exact original path in
      this repo. Same for the 29 loose root images
      (`/im_me.jpg`, `/famicom.jpg`, ...) and the
      `/hackaway2010/*.JPG` and `/discursivelabs/.../*.png`
      sub-trees. `script/mirror_artifacts.py` automates the fetch.
      One commit per logical group (artifacts / hackaway2010 /
      discursivelabs / loose-root images). **L**
- [ ] **A.9** `/about/<slug>/` collision-safe slug allocation.
      When Phase 7.7 splits `about.md`, the new sub-pages MUST
      use slugs that don't collide with the legacy
      `/about/<slug>/` URLs (`i-have-cured-my-own-sleep-paralysis-and-you-can-too`,
      `hunter-davis-on-google-plus`, `ko-nami-code`). Reserve
      `/about/bio/`, `/about/leadership/`, `/about/hacks/`,
      `/about/programming/`, `/about/writing/`, `/about/audio/`
      as the new sub-page slugs. Add the 3 legacy `/about/<slug>/`
      URLs to `_data/legacy_redirects.yml` → current Jekyll post.
      **S**
- [x] **A.10** `script/check_redirects.py` — bootstrap with a
      curated list of canonical historical URLs. **M** ·
      *Shipped 2026-05-10.* Reads every confirmed/high entry
      from `_data/legacy_redirects.yml` (archives, wp_slugs,
      about_slugs — 164 entries after filtering out the
      source-tree-visualizer sibling-repo collision via
      `_data/projects_subpaths.yml`), GETs each legacy URL
      against `--host`, follows native 301/302s, also parses
      `<meta http-equiv="refresh">` stubs (the form
      `jekyll-redirect-from` emits since GH Pages can't serve
      true 301s), and asserts the final URL contains the
      expected target. `--limit N` for partial checks,
      `--verbose` for per-URL log. Exit 0 on success, 1 on
      any failure, 2 on config error. Defaults to
      `https://hunterdavis.com`. Doesn't run in CI yet —
      that's Phase 8.3; today this is a manual post-deploy
      verification tool. Script syntax-validated; entry
      collection verified to match A.7's emission count
      exactly (164). Also added `__pycache__/`, `*.pyc`,
      `.bundle/`, `vendor/` to `.gitignore` so pyc artifacts
      from script invocations don't pollute the working tree.
- [ ] **A.11** Recover anything still unmapped from `archive.org`.
      `script/scrape_wayback_legacy_urls.py` walks
      `web.archive.org/web/*/hunterdavis.com/*`, extracts
      `(url, title, date)` tuples for any URL not already in
      `_data/legacy_redirects.yml`, best-matches each to a Jekyll
      post slug, output to CSV for human review. **L**
- [x] **A.12** Smart 404 enhancement. **S** ·
      *Shipped 2026-05-10.* `404.html` now displays the
      requested path in a `<code>` block, ships a prominent
      search form, and runs a tiny JS pattern-extractor that
      derives a sensible search hint from the requested URL.
      Patterns covered: `/android-app-…`, `/android-game-…`,
      `/android-apps/<cat>/<slug>`, `/popular-open-source-projects/<slug>`,
      `/category/<slug>`, `/about/<slug>`, `?s=<term>`, and any
      remaining slug-shaped path. The input auto-focuses with
      the prefilled hint selected, so the reader can hit Enter
      to search or type to replace. Verified across 9 sample
      URLs; the existing user-authored "Sorry…" copy and "Go
      back" link preserved verbatim. No AI prose authored.
- [x] **A.13** Build-fail subpath-collision check. **S** ·
      *Shipped 2026-05-10.* `script/check_subpath_collisions.py`
      loads `_data/projects_subpaths.yml` (135 reserved names),
      walks the source root, skips Jekyll-special directories
      (`_posts`, `_layouts`, `_includes`, `_sass`, `_data`,
      `_site`, `_drafts`, `_plugins`, `_meta`) + dotfiles +
      Gemfile / Gemfile.lock + anything in `_config.yml`'s
      `exclude:` list, and exits non-zero with an actionable
      "rename / exclude / update-data" message if any remaining
      top-level entry collides case-insensitively with a
      reserved name. Verified by adversarial test
      (`mkdir quickgrapher && python3 script/check_subpath_collisions.py`
      → exit 1 with clear collision message; removed → exit 0).
      Hookable from a git pre-commit hook today, or wired into
      CI when Phase 8.3 lands.
- [ ] **A.14** Verify the live subset of `_data/projects_subpaths.yml`.
      For each of the 135 reserved repo names, probe
      `https://hunterdavis.com/<name>/` (HEAD request, follow
      redirects) and record which actually serve content today
      vs. 404. Result: add a `live:` array to the data file
      listing the verified-deployed subset (subset of `reserved:`).
      Two known sidebar bugs to fix as part of this: `/resume/` is
      linked but no exact-match repo exists (deploy is probably
      `Hunter-Davis-impressjs-Resume`), and `/photo-stream/` is
      linked but the repo is `photo-stream-static`. **M**
- [x] **A.15** WordPress query-string ID handler. **S** ·
      *Shipped 2026-05-10.* Tiny inline `<script>` at the top
      of `index.html` reads `URLSearchParams`, looks up `?p=NNN`
      against a build-time Liquid map of
      `site.data.legacy_redirects.wp_query_ids`, and
      `location.replace()`s to the canonical post when matched.
      Also handles `?s=foo` (WordPress search) by redirecting
      to `/search.html?query=foo`. Today this resolves
      `?p=3163` → `/2012/07/21/android-sound.html` (the one
      confirmed mapping); the three needs-wayback IDs (3426,
      3583, 5580) fall through to the home page until A.11
      recovers their targets. JS validated with `node -c`;
      trailing comma in the emitted object literal is legal in
      modern JS, browsers without `URLSearchParams` (effectively
      IE11 only) degrade gracefully to the home page.

### Phase B — Information architecture & navigation (ship now, don't wait for v2)
*Goal: make the 507-post, 30-year archive actually browsable. Today
the sidebar is a hardcoded flat list of legacy links, the top nav has
3 items, the footer is empty boilerplate, and there's no way to scan
the archive by topic, year, or project. This phase ships
**visible-to-readers** IA wins **incrementally** against the existing
layouts — each item is independently shippable now, instead of
waiting for the bigger Phase 5 v2-layout redesign. Where an item
overlaps with Phase 5, it's the "land it now in the current template"
version; the v2 redesign will inherit it.*

- [x] **B.1** Move sidebar from hardcoded HTML to
      `_data/sidebar.yml`. Each entry:
      `{ label, url, group, status: live|broken|external }`.
      Re-render `_includes/sidebar.html` via Liquid. Sets up
      restructuring without code edits. **S** ·
      *Shipped 2026-05-10.* 8 project entries migrated to
      `_data/sidebar.yml` (just `label` + `url` fields for now;
      `group` and `status` fields will be added by B.2 and B.3).
      Labels and URLs preserved verbatim — rendered output is
      byte-identical. The site.links-driven entries (Github,
      Twitter, Facebook, email, RSS, search) stay inline in
      sidebar.html since they're already config-driven.
- [x] **B.2** Group sidebar entries by section. **S** ·
      *Shipped 2026-05-10.* Each entry in `_data/sidebar.yml`
      now carries a `group:` field; `_includes/sidebar.html`
      uses Liquid's `group_by` filter to emit uppercase
      `.group-heading` rows between sections. Current groups
      derived from each repo's own description: **Tools** (5 —
      QuickGrapher, Physical Media, Streak!, Visualizer, People
      Grid) and **Games** (3 — My Solitaire Varient, PsyRunner
      Game, AsteroidMiner). New groups (Writing, Archive
      shortcuts, etc.) can be introduced by simply adding
      entries with a new `group:` value. Heading styling: small
      uppercase, bottom-border, transparent background — set
      apart from the existing dark-button link rows.
- [ ] **B.3** Audit + prune broken sidebar entries. A.14
      surfaced `/resume/` and `/photo-stream/` as broken (the
      actual repos are `Hunter-Davis-impressjs-Resume` and
      `photo-stream-static`). Sweep the rest with
      `script/audit_legacy_urls.py` patterns and either fix the
      target or remove the entry. **S**
- [x] **B.4** Expand top nav. **S** ·
      *Shipped 2026-05-10.* Nav went from 3 to 5 items in
      `_includes/header.html`:
      Home → Projects → Archive → My Story → Leadership and
      Public Speaking. The two new links (Projects, Archive)
      target real pages shipped in 2.4 and 2.6. The user's
      existing "My Story" label is preserved verbatim (no
      rename to "About") — it's authored prose. The original
      6-item spec proposed Writing and Now too; those stay
      deferred until `/writing/` and `/now/` are built (7.4
      and the future writing-hub).
- [x] **B.5** Real footer with site map. **M** ·
      *Shipped 2026-05-10.* `_layouts/default.html` footer
      replaced. Was: two lines (copyright + Bitwiser/Jekyll
      attribution). Now: flat horizontal list of 8 functional
      links — About, Leadership and Public Speaking, Search,
      RSS, RSS (full), Sitemap, GitHub, Email — plus a compact
      credit line. Every link destination exists today (no 404
      traps; surfaces like /archive/ and /projects/ omitted
      until their Phase 2 / Phase 4 pages exist). Section-heading
      version deliberately skipped to avoid authoring
      section-name prose; the flat list is honest about what
      each link is. Link labels match existing UI vocabulary
      verbatim (e.g., "Leadership and Public Speaking" matches
      the nav). Bitwiser-theme attribution removed since the
      codebase has been substantially rewritten from the
      template — the recent dead-code purges in 0.8/0.9/0.10/0.12
      gutted most of what was left of it. Jekyll credit retained.
- [x] **B.6** Site map page at `/sitemap.html` — distinct from
      the crawler-targeted `/sitemap.xml`. **M** ·
      *Shipped 2026-05-10.* New `sitemap.md` permalinks to
      `/sitemap.html` and renders five sections via pure Liquid
      (no JS): **Pages** (Home, About, Speaking, Search),
      **Recent posts** (latest 10), **Posts by project**
      (grouped via `group_by: "project"`, sorted alphabetically,
      humanized names from new `_data/projects.yml`), **Posts
      by year** (year + post-count rows via `group_by_exp`),
      and **Feeds and metadata** (both RSS feeds + XML
      sitemap link). New `_data/projects.yml` maps project
      slugs (zipit-z2, johnny-castaway, dockstar) to
      human-readable names ("Zipit Z2", "Johnny Castaway",
      "Dockstar"). Page is discoverable via the footer — added
      `Site Map` and renamed the existing sitemap link to
      `XML Sitemap` for clarity.
- [x] **B.7** Breadcrumb on post pages. **S** ·
      *Shipped 2026-05-10.* Compact `Home / <year>` strip above
      every post's `<h1>`. Semantic markup: `<nav
      aria-label="Breadcrumb"><ol><li>` per the WAI-ARIA
      pattern; separators rendered via CSS `::after` so screen
      readers don't have to read them. Year is plain text (not
      linked) until Phase 2.5 ships `/archive/<year>/` —
      avoids creating 404 hyperlinks. Activation when 2.5
      lands is a one-line change: wrap
      `{{ page.date | date: "%Y" }}` in an `<a>`.
- [x] **B.8** Tag chips on post pages become real links. **S** ·
      *Shipped 2026-05-10.* Tag chips in `_layouts/post.html`
      and `index.html` changed from decorative `<span>` to
      `<a class="tag-chip" href="/search.html?query=…">`,
      using the same target as the `/tags/` index page. Each
      tag click runs a search prefilled with that tag — works
      today without needing per-tag pages from Phase 2.2.
      CSS in `style.scss` refactored from `.tags span` to
      `.tags .tag-chip` (decoupled from the element type) and
      gained focus + hover state (inverts to filled blue, the
      existing #0B5485 palette). When 2.2 ships dedicated
      `/tag/<slug>/` pages, the `href=` is a one-line edit
      in both files.
- [x] **B.9** Featured-posts mechanism. **M** ·
      *Shipped 2026-05-10.* `featured: true` frontmatter added
      to 11 historically important posts (the pre-existing
      "My Story" already had it, totalling 12). The set was
      sourced directly from Appendix A's dossier-confirmed
      milestones so editorial selection traces to verified
      third-party coverage: Zipit Z2 Tor+Privoxy origin,
      IM-ME hack (Hackaday), Dockstar $25 console (Hackaday
      + Engadget), Sith Lord 30-in-30 (HN), QuickGrapher
      (HN front page), Source Tree Visualizer, 70-app GitHub
      mass release (HN + Hackaday), quarter-million Play
      Store downloads, Rhapsody + Ford SYNC (CES 2013),
      TUI000 (terminal screensaver), Dunking Bird (current
      project). `index.html` renders a `.featured` aside only
      on `paginator.page == 1`, listing each featured post
      with date. CSS adds a left-accent strip in the existing
      #0B5485 palette. The user can add/remove entries by
      flipping the `featured:` frontmatter field — the home
      page picks up changes automatically.
- [ ] **B.10** "Currently working on" panel above the home post
      list. One sentence + a link to the most recent project
      announcement post. Pulled from `_data/now.yml` (single-key
      file the user updates manually). Editorial copy is the
      user's prose, never machine-authored. **S**
- [ ] **B.11** "Start here" panel for new visitors. Three or
      four hand-picked entry points (e.g., My Story, Greatest
      Hits, Latest project). Pulled from `_data/start_here.yml`.
      User supplies the entry-point labels. **S**
- [ ] **B.12** "Greatest hits" / milestones strip on the home
      page. Pulled from `_data/milestones.yml` (the dossier
      structure planned in 7.6 + Appendix A). Three or four
      cards linking to the Zipit Z2 era, the 70-app GitHub
      release, the Johnny Castaway saga, the books. **M**
- [x] **B.13** "More from this project" panel on post pages.
      **M** · *Shipped 2026-05-10.* New aside renders on any
      post that sets `project:` frontmatter; lists up to 6
      sibling posts with the same value via a pure-Liquid
      `{% capture %}` + `{% if … contains "<li>" %}` guard
      (same pattern as B.14's same-year aside). CSS extends
      the existing `.same-year` rules to cover
      `.same-project` too (comma-separated selector). Seeded
      `project: johnny-castaway` on the 6 confirmed Johnny
      Castaway saga posts: on-the-web-on-the-hunt (2018),
      Castawine (2019), native-port-and-livcd, Dreamcastaway,
      retrofw-released, text-edition (all 2021). Zipit Z2,
      Dockstar, and other arcs can be tagged with their own
      `project:` value in follow-up commits — the template
      activates automatically. All 6 modified posts re-parsed
      cleanly with PyYAML.
- [x] **B.14** "Other posts from this year" on post pages. **S** ·
      *Shipped 2026-05-10.* Pure-Liquid implementation in
      `_layouts/post.html` plus `.same-year` styles in
      `css/style.scss`. Walks `site.posts` (already sorted
      descending by date), skips self, collects up to 5 posts
      with the same `date | "%Y"` year, captures the HTML, and
      conditionally renders the `<aside>` only if at least one
      `<li>` was emitted (so solo-post years like 2025/2026
      don't show an empty heading). Verified the simulation
      across four representative posts (2007 → 5 siblings, 2011
      → 5 siblings, 2025 → 0, 2026 → 0; aside suppressed in
      the latter two).
- [x] **B.15** Promote search to every page. **M** ·
      *Shipped 2026-05-10.* New `<form class="header-search"
      role="search">` in `_includes/header.html`, rendered on
      every page (header is in default layout). `<input
      type="search" placeholder="Search… (press /)">` with
      hidden `<label>` for accessible name. Tiny inline JS
      script in the same include listens for the `/` key and
      focuses the input — guarded against firing when the user
      is already typing in an input/textarea/contenteditable
      element, and against Ctrl/Meta/Alt modifier combinations.
      `.visually-hidden` utility added to `css/style.scss`
      alongside `.header-search` styles (centered, max-width
      360px on desktop, full-width on mobile, focus outline
      using existing #1AC9DB accent). The old sidebar search
      form is left in place for now — removing it is a
      separate atomic follow-up.
- [x] **B.16** Mobile nav: replace the dated `.android`-class
      panel + jQuery-style toggle with a native `<details>`
      element styled as a popover. No JS dependency. **S** ·
      *Shipped 2026-05-10.* Pre-flight surfaced a latent bug:
      the existing mobile menu's `.active-menu` toggle was
      defined in CSS but no JS ever applied it, so the mobile
      menu was **broken in production** — tapping the opener
      did nothing. Replaced the `.opener` + `.clear-opener` +
      `.active-menu` machinery with a semantic
      `<details><summary>Menu</summary>…</details>` block in
      `_includes/header.html` and rewrote the corresponding
      CSS in `css/style.scss`. Net **−70 lines of CSS** (the
      `.android` block was dead code, and the
      `.active-menu`/`.opener`/`.clear-opener` rules
      collapsed into native `details[open] > ul` toggling).
      Desktop visual: unchanged. Mobile: tap "Menu" → list
      expands; tap again → collapses. Native browser
      disclosure semantics, screen-reader-friendly, no JS.
- [ ] **B.17** Header tagline: a short user-authored sentence
      next to "HunterDavis.com" that sets identity without the
      current giant centred h1. (User supplies the sentence —
      not machine-authored.) **S**
- [x] **B.18** Topic-cloud sidebar widget. **M** ·
      *Shipped 2026-05-10.* New `.topic-cloud` panel in
      `_includes/sidebar.html` renders the top 30 most-used
      tags as small chip-style links. Iterates the
      count-descending `site.data.tags` dict shipped in 2.1
      (limit: 30). Each chip links to `/search.html?query=<tag>`
      (same target as the chip strip in B.8 and the `/tags/`
      index in 2.3). Footer of the panel has an "All tags →"
      link to `/tags/` for the full alphabetical list. Sidebar
      currently renders only on the home page (`home.html`),
      so this is a home-only widget. Same-size-per-chip
      rendering for now — true count-proportional font-sizing
      would need the canonical vocabulary from 2.9 to be
      worth implementing (sizing `android` 58× vs `app-tag`
      43× without first collapsing the synonyms would be
      misleading). Side benefit: an old absolute
      `http://www.hunterdavis.com/feed.xml` URL in the same
      sidebar (missed by Phase 7.11's sweep because it was an
      `<a>` href in an include, not a post body) was
      converted to relative `/feed.xml`.

### Phase 0 — Hygiene & broken-asset fixes
*Goal: stop shipping bugs. Each item is independently shippable.
URL preservation work moved to Phase A above.*

- [ ] **0.1** Add `favicon.png` (and `favicon.svg`, 32×32 PNG fallback) at
      repo root. **S** · *Why:* every page references it and 404s today.
- [ ] **0.2** Add `sharer.png` (default 1200×630 OG image) at repo root.
      **S** · *Why:* every shared link 404s its preview image.
- [x] **0.3** Switch `_config.yml` `url` and `base_url` to
      `https://www.hunterdavis.com`. **S** ·
      *Shipped 2026-05-10.* Single-line change:
      `url: http://www.hunterdavis.com` →
      `url: https://www.hunterdavis.com`. The `base_url` half
      of the original task was already shipped in 0.4
      (collapsed dual keys into single `site.url`). Propagates
      to 23 `site.url` / `absolute_url` renders across
      `ssn.html`, `feed.xml`, `feed-full.xml`, `sitemap.xml`,
      `robots.txt`, `jsonld_post.html`, `jsonld_person.html`,
      and the inline favicon `<link>` + Copy-link button.
      Canonical URLs, OG / Twitter URLs, RSS feed links,
      sitemap entries, and JSON-LD identifiers are now all
      HTTPS. GitHub Pages has enforced HTTPS for custom
      domains by default since 2018, so the underlying site
      has been serving HTTPS even though canonical tags
      previously claimed HTTP — this commit aligns the
      metadata with reality. The `www`-vs-apex mismatch (CNAME
      is apex, url has `www`) is a separate host-normalization
      issue tracked under 8.4.
- [x] **0.4** Collapse `site.url` and `site.base_url` to a single key
      and fix all references in `_includes/ssn.html`, `feed.xml`,
      `sitemap.xml`, `robots.txt`. **S** ·
      *Shipped 2026-05-10.* Dropped the duplicate `base_url`
      key from `_config.yml`; renamed all 8 `site.base_url`
      references (5 in `_includes/ssn.html`, 2 in `sitemap.xml`,
      1 in `robots.txt`) to `site.url`. `feed.xml` already used
      `site.url`. `_config.yml` had both keys set to identical
      values so the rendered output is byte-identical; the
      configuration now has a single source of truth for the
      site origin, aligned with Jekyll's own convention.
- [x] **0.5** Fix empty `<img src="" width=600 />` on the home list:
      only render the image element when `post.image` is non-empty.
      Edit `index.html`. **S** · *Shipped 2026-05-10 (bundled with
      0.6 + 0.7).*
- [x] **0.6** Add `loading="lazy"` and `decoding="async"` to home and
      post-list image renders. **S** · *Shipped 2026-05-10 (bundled
      with 0.5 + 0.7).* Also added `alt=""` for decorative-image
      WCAG compliance.
- [x] **0.7** Remove the `{{ post.featured_img }}` line entirely from
      `index.html` (the recent dunking-bird fix proved it's redundant).
      **S** · *Shipped 2026-05-10 (bundled with 0.5 + 0.6).* Kept
      `featured_img` as a Liquid `default:` fallback to avoid
      regressing 16 posts (mostly 2020–2021 Johnny Castaway saga)
      that have `featured_img:` but no `image:`. A future commit
      can migrate those posts' frontmatter and drop the fallback.
- [x] **0.8** Delete `_includes/disqus.html` — unused, references a
      `site.disqus` value that's commented out. **S** ·
      *Shipped 2026-05-10 (bundled with 0.9 + 0.12).*
- [x] **0.9** Delete `_includes/jquery-1.4.4.min.js`,
      `jquery-ui-1.8.9.custom.min.js`, `modernizr-1.6.min.js`,
      `obfs_embed.js`, `deck.js`, `simulator.js` from `_includes/`.
      **S** · *Shipped 2026-05-10 (bundled with 0.8 + 0.12).*
      Confirmed via grep that no `{% include %}` references these
      files; the legacy embed pages on `hunterdavis.com/quickgrapher/…`
      and `hunterdavis.com/deck-of-cards/…` use externally-hosted
      copies of these scripts, not these in-repo ones. ~290 KB
      of dead JS removed from the git tree.
- [x] **0.10** Drop the maxcdn font-awesome `<link>` from
      `_layouts/default.html`; the 4 remaining decorative icons
      (calendar, home, info-circle, tag) removed outright instead
      of swapped for inline SVG — text labels stand on their own.
      **M** · *Shipped 2026-05-10.* 4-file change: removed
      the `<link>` from default.html and the 7 `<i class="fa fa-…">`
      tags scattered across `_includes/header.html`, `index.html`,
      and `_layouts/post.html`. Net effect: one fewer HTTP
      request per page, ~110 KB less data on every first-visit
      page (CSS + font file), no DNS lookup / TLS handshake to
      maxcdn.bootstrapcdn.com (privacy + reliability win), no
      FOIT/FOUT on icon-font load. If decorative icons come
      back later, they'll be inline SVG `<symbol>` references —
      tracked as new item 0.16.
- [x] **0.11** Drop the dead Twitter/Facebook share buttons from
      `_layouts/post.html` (Twitter share UX is broken on X anyway).
      Replace with a single "Copy link" button. **S** ·
      *Shipped 2026-05-10.* Removed the `.sharer.facebook`
      `<a>` (which `onclick`-popups Facebook's sharer.php that
      tracks the reader pre-share) and both branches of the
      `{% if site.twitter %}` Twitter-share `<a>` (X moved away
      from those URL params). Replaced with a single
      `<button class="sharer copy-link" data-url="…">Copy link</button>`
      and a tiny inline script using `navigator.clipboard` when
      available with an `execCommand('copy')` fallback for
      HTTP/older browsers. Button flashes "Copied" for 1.5 s.
      Restyled `.sharer` from coloured-circle to a real text
      button (existing palette #0B5485). Dropped the
      `.sharer.facebook` and `.sharer.twitter` CSS blocks and
      updated the print stylesheet's hider from `a.sharer` to
      `.sharer` since the element is now a `<button>`. Side
      benefit: removes 2 of the 6 font-awesome icons in use
      (fa-facebook, fa-twitter), incrementally working toward
      0.10 (drop the CDN entirely).
- [x] **0.12** Delete `index.old` (it's a Jekyll comment-only stub).
      **S** · *Shipped 2026-05-10 (bundled with 0.8 + 0.9).*
- [x] **0.13** Replace `_includes/analytics.html` with a privacy-respecting
      analytics snippet (Plausible / GoatCounter / self-hosted) only if
      `site.analytics_url` is set. Otherwise remove the include
      altogether. **S** · *Shipped 2026-05-10 (removal path).*
      The include shipped Universal Analytics (sunset by Google
      July 2024); `site.ga_id` had been commented out in
      `_config.yml` for the entire history of this codebase, so
      the `{% if site.ga_id %}{% include analytics.html %}` in
      `_layouts/default.html` was never firing. Deleted the
      file, the conditional, and the commented `ga_id` /
      `ga_domain` / `disqus` config lines that no longer apply.
      Future analytics adds should use a privacy-respecting
      service (Plausible / GoatCounter / self-hosted) — tracked
      as new item 0.17.
- [x] **0.14** Add `<main>` landmark and a visually-hidden
      "Skip to content" link in `_layouts/default.html`. **S** ·
      *Shipped 2026-05-10.* Replaced `<section class="content">`
      with `<main id="main" class="content">` (CSS kept working —
      rules target the class, not the element). Added a `<a
      class="skip-link" href="#main">` as the first focusable
      element in `<body>`, with CSS that keeps it off-screen
      until focused (standard `position: absolute; top: -40px;`
      pattern, `top: 0` on `:focus`, plus a high-contrast accent
      outline). Skip-link vocabulary matches existing site UI
      labels.
- [ ] **0.15** Set explicit `width` and `height` on home-list images
      (use a default ratio like 1200×630 if unknown) to eliminate CLS.
      **S**
- [ ] **0.16** Optional: re-add small decorative icons via inline
      SVG `<symbol>` definitions in a single
      `_includes/icon_sprite.html`. Referenced from templates as
      `<svg><use href="#icon-home"/></svg>`. Total inline footprint
      ~1 KB across all templates (cheaper than the 110 KB
      font-awesome CDN dropped in 0.10), no third-party
      dependency, scales to any size cleanly. Skip if the iconless
      look turns out to read well after 0.10 ships. **S**
- [ ] **0.17** Optional: add a privacy-respecting analytics
      snippet (Plausible / GoatCounter / self-hosted Umami) if
      the user wants traffic numbers back. Gate on a new
      `site.analytics_url` config key. No Google Analytics —
      that path was killed in 0.13. **S**

### Phase 1 — Performance quick wins
*Goal: kill the obvious perf cliffs without touching design yet.*

- [x] **1.1** Replace `search.md` inline JSON dump with a
      `search.json` data file built by Liquid, fetched async by
      `js/search.js`. **M** · *Shipped 2026-05-10.* New
      `search.json` Liquid template emits the same per-post object
      shape as the previous inline `window.store`. `search.md`
      drops the inline corpus and now `fetch()`s `/search.json`,
      defers button binding until after the corpus arrives, and
      shows a "Loading search index…" status during the fetch.
      `js/search.js` now reads `searchTerm` fresh inside each
      handler and the bottom auto-trigger is removed (search.md
      orchestrates timing). Expected impact:
      `_site/search.html` drops from **1.18 MB to under 5 KB**;
      `search.json` carries the corpus once and is cacheable.
- [x] **1.2** Trim the search corpus: index `title`, `date`, `tags`,
      `excerpt` only — not full content. **M** ·
      *Shipped 2026-05-11.* `search.json` rewritten: dropped
      `author` and `category` (the first was always "Hunter
      Davis", the second was rarely set), added `tags` (joined
      with spaces for lunr token-search), and the `content`
      field now holds `post.excerpt | strip_html` instead of
      `post.content | strip_html`. The post content is
      typically 10–50× longer than the excerpt — for 507
      posts the corpus collapses from a multi-MB JSON
      payload to one that loads in a fraction of the time.
      All Liquid field interpolations converted to `jsonify`
      so titles/URLs with quotes serialize safely.
      `js/search.js` updated in lockstep (both
      `searchIsGo` and `dateSearchIsGo`): dropped
      `author`/`category` from the lunr field list, added
      `tags` with `boost: 5` (less than the existing
      `title` boost of 10, more than plain `content`).
      Renderer untouched — still uses
      `item.url`, `item.date`, `item.title`,
      `item.content.substring(0, 250)`. The progressive-
      enhancement layered-load idea from the original
      backlog item is dropped: with the excerpt-only corpus
      the payload is already small enough that the extra
      complexity isn't worth it. If full-content search
      becomes a need later it can be a separate item.
- [ ] **1.3** Self-host the Vollkorn font subset (latin only,
      400/700 + italics) with `font-display: swap`. **M** · *Why:*
      drops Google Fonts dependency + speeds first paint.
- [x] **1.4** Trim `feed.xml` to title + excerpt + link; add
      `feed-full.xml` for full-content readers. **S** ·
      *Shipped 2026-05-10.* `feed.xml` swapped `post.content`
      for `post.excerpt | strip_html | normalize_whitespace`,
      dropping per-item description from full HTML (often KBs)
      to a short plain-text first-paragraph. Added an
      `<atom:link rel="alternate">` advertising the new
      full-content feed. New `feed-full.xml` ships
      `<content:encoded><![CDATA[…]]></content:encoded>` with
      the full HTML body for power readers who want the post
      inline in their RSS client (CDATA collision audit
      confirmed zero posts contain literal `]]>`). Incidental
      bug fix in both: removed the spurious `/` between
      `site.url` and `post.url` in `<link>` and `<guid>`
      (post.url already starts with `/`).
- [x] **1.5** Remove unused SCSS partials. **S** ·
      *Shipped 2026-05-10.* Deleted `_sass/_buttons.scss` (42
      lines; its `@import` in `style.scss` had been commented
      out since the Bitwiser theme was first imported, so the
      file was never compiled into the served CSS). Removed
      the dead `//@import 'buttons';` line too. The remaining
      six partials (`_anims.scss`, `_gridism.scss`,
      `_markdown.scss`, `_monokai.scss`, `_normalize.scss`,
      `_variables.scss`) are all actively imported.
- [x] **1.6** Replace the `headroom.min.js` shrinking-header on
      scroll with CSS `position: sticky` (no JS required). **S** ·
      *Shipped 2026-05-10 (deletion half).* Pre-flight grep
      confirmed `js/headroom.min.js` was referenced by **zero**
      templates — the shrinking-header behavior the audit doc
      assumed was the current state was never actually wired up.
      Deleted the orphaned JS file. The `position: sticky`
      header rewrite that 1.6's original spec described is now
      a fresh feature on a clean baseline rather than a
      replacement — tracked as new item 1.10.
- [ ] **1.7** Add `<link rel="preload">` for the hero image and
      self-hosted font on the home and post pages. **S**
- [ ] **1.8** Inline critical above-the-fold CSS in `<head>` and
      defer the rest with `media="print" onload`. **M**
- [ ] **1.9** Add a build-time HTML minifier (jekyll-compress-html
      layout include or `jekyll-minifier`). **S**
- [x] **1.10** Add `position: sticky` to the site header so the
      nav + search input stay accessible during long scrolls.
      **S** · *Shipped 2026-05-10.* Added
      `class="site-header"` to the `<header>` in
      `_includes/header.html` and a small `.site-header { …
      position: sticky; top: 0; z-index: 50; background: #eee;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05); }` block in
      `style.scss`, wrapped in `@media (min-width: 569px)` so
      the existing mobile fixed-popover nav behaviour is
      untouched. Desktop readers now keep the site title +
      nav + search input visible while scrolling through long
      posts.

### Phase 2 — Information architecture scaffolding
*Goal: surfaces exist (even if empty), so subsequent commits can
populate.*

- [x] **2.1** Create `_data/tags.yml` with the controlled vocabulary
      defined under "Tag taxonomy" above. **M** ·
      *Shipped 2026-05-10 (minimum scope).* `script/audit_tags.py`
      walks every post's frontmatter, extracts every distinct tag
      value, and emits `_data/tags.yml` as a flat slug → count
      dict (sorted descending by count, alphabetical for ties).
      370 distinct tags captured across 113 tagged posts (774
      total tag applications, 3.3 avg per post). Top entries:
      android (58), android-app (44), android-apps-2 (43),
      app-tag (43), easy (37), linux (14), hacking (13).
      Curation into canonical vocabulary (collapsing synonyms
      like android-app / android-apps-2 / app-tag, defining
      display names, grouping into families) is a separate
      downstream commit — tracked as new item 2.9. This commit
      gives Phase 2.2 (tag pages), 2.3 (tag index), and B.18
      (topic cloud) the data they need without imposing
      authored vocabulary on the user's organic tagging.
- [x] **2.2b** Point tag-chip links at the new tag pages. **S** ·
      *Shipped 2026-05-11.* Wired up the three places that
      render tag chips so they prefer `/tags/<slug>/` over
      `/search.html?query=<slug>`: post pages
      (`_layouts/post.html`), home post cards (`index.html`),
      and the sidebar topic-cloud (`_includes/sidebar.html`).
      Post and home use a `{% if site.data.tags[tag] >= 2 %}`
      guard so single-use tags (no generated page) still fall
      through to `/search.html`. Sidebar is unconditional —
      the topic-cloud limits to the top 30 tags by count and
      the 30th tag has count 3, comfortably above threshold.
      Closes the 2.2 cross-linking loop: posts now connect
      to dedicated tag pages, tag pages back-link to
      `/tags/` and `/archive/`, and the cycle of internal
      links is unbroken.
- [x] **2.2** Generate per-tag pages. **M** ·
      *Shipped 2026-05-11.* Used a Python pre-build script
      instead of a Ruby `_plugins/` generator since the
      site deploys via GH Pages' default builder, which
      disallows custom plugins. New
      `script/generate_tag_pages.py` walks `_posts/`, parses
      every frontmatter via PyYAML, and emits one
      `tag/<slug>.md` page per tag that has **≥ 2 posts**
      (with `permalink: /tags/<slug>/`). 84 tag pages
      generated out of the 370 distinct tags — the other
      286 are single-use and don't earn a dedicated page;
      `/tags/` index falls back to `/search.html?query=<tag>`
      for those. The script is idempotent: it deletes any
      stale `tag/*.md` whose tag has dropped below the
      threshold before regenerating. Filesystem safety is
      enforced via `SAFE_SLUG_RE` (`[A-Za-z0-9][A-Za-z0-9._-]*`)
      — all 370 current slugs already pass. Each page lists
      its posts in reverse chronological order with a
      `MM-DD` date prefix and ends with `[All tags] · [Archive]`
      back-link. Pure cross-linking win: posts with tags now
      have a real destination per tag, not just a search
      query parameter. Pagination deferred — the largest
      page (`android`, 58 posts) renders cleanly in one shot
      and is still a fraction of any `/archive/YYYY/` page.
- [x] **2.3** Build `/tags/` — alphabetical list of tags with
      post counts. **S** · *Shipped 2026-05-10.* New `tags.md`
      permalinked to `/tags/` lists all 370 distinct tags from
      `site.data.tags` in alphabetical order, each one a link
      to `/search.html?query=<tag>` (so clicking works today,
      before per-tag pages from 2.2 are built). Counts shown
      in a muted `.tag-count` span. Footer extended with
      `Tags` link. Family grouping deferred to Phase 2.9
      (canonical vocabulary curation). Pre-flight surfaced
      and fixed a YAML-typing bug in
      `script/audit_tags.py`: a tag literally named "2010"
      was being parsed as an integer; switched to always-quote
      output so pure-digit and YAML-reserved-word slugs stay
      string-typed.
- [x] **2.4** Build `/archive/` index. **M** ·
      *Shipped 2026-05-10 (minimum scope).* New `archive.md`
      permalinked to `/archive/` lists all 507 posts grouped
      by year via `group_by_exp` (descending year, descending
      date within year). Each year h2 carries an explicit
      `{#YYYY}` ID for robust deep-linking, regardless of
      kramdown's auto-id behavior for numeric headings. The
      post-page breadcrumb (B.7) now activates its year link
      as `/archive/#{year}` so a reader on a 2010 post can
      click "2010" and scroll-jump to the right section.
      Month-grid layout deferred — for 19 years × ~507 posts
      the simple per-year flat list reads fine. Footer gets
      an `Archive` link.
- [x] **2.5** Build per-year `/archive/<year>/` archives. **M** ·
      *Shipped 2026-05-10.* New
      `script/generate_year_archives.py` walks `_posts/`,
      groups by year extracted from the filename prefix, and
      emits one `archive/YYYY.md` per year (19 files,
      2007–2026; 2023 is intentionally absent — no posts that
      year). Each page is permalinked at `/archive/YYYY/`,
      shows a count summary, lists every post for that year in
      reverse chronological order with `MM-DD — [title](url)`,
      and ends with `« prev · All years · next »` nav between
      adjacent years. The post-page breadcrumb (formerly
      `/archive/#YYYY` fragment-scroll) now points at the real
      page `/archive/YYYY/` — better SEO, real crawl target,
      no client-side scroll dance. The `/archive/` index also
      now links each year heading to its dedicated page, so
      both fragment-style deep links and per-year landing
      pages coexist. Script is idempotent: re-run any time
      posts shift to regenerate cleanly. Reads titles from
      post frontmatter (with quote-stripping); falls back to
      the filename slug if no title is set.
- [x] **2.6** Build `/projects/` hub. **M** ·
      *Shipped 2026-05-10.* New `projects.md` permalinked to
      `/projects/`, pure-Liquid: groups `site.posts` by the
      `project:` frontmatter value, sorts alphabetically by
      project slug, uses `_data/projects.yml` to humanize each
      slug to its display name, and lists each project's posts
      in oldest-first ("saga reading order") inside each
      section. Heavier hub-of-cards layout deferred until more
      projects are tagged — 3 today (Dockstar, Johnny
      Castaway, Zipit Z2). Footer extended to link to
      `/projects/`.
- [x] **2.7** Add `_data/projects.yml`. **M** ·
      *Shipped 2026-05-10 (minimum schema).* Currently maps
      slug → display name only (3 entries: zipit-z2 →
      Zipit Z2, johnny-castaway → Johnny Castaway, dockstar →
      Dockstar). The richer schema from the original spec
      (`family`, `tags`, `hero_image`, `dates`, `blurb`,
      `external_links`) can be added incrementally per
      project once `_layouts/project.html` (item 2.8) lands —
      consumed fields are additive and don't break the
      sitemap.html / projects.html consumers.
- [ ] **2.8** Add `_layouts/project.html` for project landing pages —
      renders project metadata, "Posts" list filtered by tag/slug, and
      external links. **S**
- [ ] **2.9** Curate the `_data/tags.yml` inventory into a
      canonical vocabulary. Collapse near-synonyms (e.g.,
      `android-app` + `android-apps-2` + `app-tag` → one
      canonical slug), pick display names, group into families
      (hardware-hack / software / writing / etc.). Restructures
      the flat slug → count dict shipped in 2.1 into per-tag
      objects with `count, display, family, aliases:[…]` keys.
      The script `script/audit_tags.py` keeps regenerating the
      count column; the rest is editorial. Until this lands,
      tag pages (2.2) and the topic cloud (B.18) render all
      370 slugs as-is. **M**

### Phase 3 — Tag backfill (bulk metadata recovery)
*Goal: fill in the 394 untagged posts. One commit per batch.*

- [ ] **3.1** Write `script/backfill_tags.py` (or a Ruby script under
      `script/`) that proposes tags per post by regexing title +
      first 800 chars against `_data/tags.yml` keywords. Output a diff
      that the human reviews and applies. **M**
- [ ] **3.2** Backfill tags batch 1: `2007-12-*` (~17 posts). **S**
- [ ] **3.3** Backfill tags batch 2: `2008-*` (~12 posts). **S**
- [ ] **3.4** Backfill tags batch 3: `2009-*` (~28 posts). **S**
- [ ] **3.5** Backfill tags batch 4: `2010-*` (~24 posts). **S**
- [ ] **3.6** Backfill tags batch 5: `2011-01..06` (~80 posts). **M**
- [ ] **3.7** Backfill tags batch 6: `2011-07..12` (~88 posts). **M**
- [ ] **3.8** Backfill tags batch 7: `2012-*` (~60 posts). **M**
- [ ] **3.9** Backfill tags batch 8: `2013-01..06` (~45 posts). **M**
- [ ] **3.10** Backfill tags batch 9: `2013-07..12` (~40 posts). **M**
- [ ] **3.11** Backfill tags batch 10: `2014..2016` (~67 posts). **M**
- [ ] **3.12** Backfill tags batch 11: `2017..2026` (~50 posts). **M**
- [ ] **3.13** Add `series:` frontmatter for posts in series (Johnny
      Castaway saga, 65 Apps grind, Build Your Own DCC chapters,
      Reviews of the Month, etc.). **M**
- [ ] **3.14** Add `featured: true` to the ~25 most historically
      important posts so we can cherry-pick them on the home and
      milestones page. **S**

### Phase 4 — Project hubs (one commit per project)
*Each commit populates a project landing page using the new layout.*

- [ ] **4.1** Project hub: **Johnny Castaway** — combines native port,
      Dreamcastaway, RetroFW port, text edition, PS1 announcement.
      Adds title art, intro, embedded screenshots, post list, GitHub
      links, history paragraph. **M**
- [ ] **4.2** Project hub: **Zipit Z2** — 29 posts. Tor/Privoxy
      essay, DOSBox + NES emulator videos, X11 + Fluxbox milestone,
      Hackaday/Engadget coverage, downloadable images archive (mirror
      from hunterdavis.com if still hosted there). **M**
- [ ] **4.3** Project hub: **IM-ME** — 8 posts. Reverse-engineering
      story, link to follow-on work by Travis Goodspeed et al. **S**
- [ ] **4.4** Project hub: **Dockstar / Distributed Compilation
      Cluster** — 10 posts + book promo + 6-part article series
      reflowed as a "start here" reading order. **M**
- [ ] **4.5** Project hub: **65 Apps in 60 Days (Sith Challenge)** —
      a chronological grid of all apps with their current Play Store
      status (live / delisted / open-source on GitHub). **M**
- [ ] **4.6** Project hub: **Source Tree Visualizer**. **S**
- [ ] **4.7** Project hub: **QuickGrapher** + embedded demo. **S**
- [ ] **4.8** Project hub: **Books** — Hacks, Live For Free, Build
      Your Own DCC, Oubastet's Wager. Cover art, store links (with
      404-status check), excerpt. **M**
- [ ] **4.9** Project hub: **AI tools era** — Tui000, Labrync, TPS,
      Dunking Bird. Frame as "small joys" / agentic experiments. **M**
- [ ] **4.10** Project hub: **Rhapsody / Napster** — patents, Ford
      integration, Fanhattan, Songmatch. Link out to public artifacts
      only. **S**
- [ ] **4.11** Project hub: **Discursive Labs** — 2010-2011 startup,
      QuickGrapher + Source Tree Visualizer origin. **S**
- [ ] **4.12** Project hub: **Music & Composition** — AirBeats,
      composing for kids' games (YouTube embeds), guitar building,
      WUEV DJ era. **M**
- [ ] **4.13** Project hub: **Reviews** — game/movie reviews surfaced
      as a flat list with cover art. **S**

### Phase 5 — Visual / UX redesign
*Goal: ship the 2026 look. Keep old templates working until the
last commit in this phase swaps the default.*

- [ ] **5.1** Add design tokens at `_sass/_tokens.scss`: colors,
      type scale, spacing scale, radius, shadow, motion. **M**
- [ ] **5.2** New `_layouts/default-v2.html` using `<main>`, semantic
      landmarks, modern grid, single source of head metadata. **M**
- [ ] **5.3** Build new home layout `_layouts/home-v2.html`: hero
      (latest announcement, image, CTA), "Currently working on"
      strip from `_data/now.yml`, greatest-hits row from
      `_data/milestones.yml`, recent-posts grid. **L**
- [ ] **5.4** Build new post layout `_layouts/post-v2.html`: hero
      image, title, dateline + reading-time, body at 65ch, tag chips,
      related-posts panel, prev/next-by-date. **M**
- [ ] **5.5** Build `_layouts/project-v2.html` (replaces 2.8 stub
      with the real design). **M**
- [ ] **5.6** Mobile menu without `.android` JS pattern: a
      `<details>` element styled into a popover, no library. **S**
- [ ] **5.7** Dark mode via `prefers-color-scheme` and a manual toggle
      stored in `localStorage`. **M**
- [ ] **5.8** Tag chip component, used on home cards, post pages,
      tag index. **S**
- [x] **5.9** Remove `text-align: justify` site-wide. **S** ·
      *Shipped 2026-05-11.* The single offender in
      `css/style.scss` was the `article section p` rule
      forcing justified text on every post body paragraph.
      Justified text on the web creates uneven "rivers" of
      whitespace, hurts dyslexic readers (WCAG 2.1 SC 1.4.8
      explicitly warns against it), and makes narrow-viewport
      layouts ugly because the browser can't hyphenate to
      compensate. Removed; paragraphs now fall back to the
      default left/start alignment. No HTML changes required;
      brace balance verified (160/160). Pulled forward out of
      the deferred Phase 5 redesign because the cost of doing
      it now (one CSS rule deletion) is dramatically less than
      the readability cost of waiting until the v2 cutover.
- [ ] **5.10** Cutover: switch `default.html`, `home.html`, `post.html`
      to the v2 versions; delete the legacy ones. **M**
- [ ] **5.11** Cutover: switch `_includes/header.html` to the new nav
      and remove the conditional script blocks for legacy embed pages.
      **S**
- [ ] **5.12** Replace hand-coded sidebar with a footer site-map block
      (ships only on home + project hubs). **S**

### Phase 6 — Image optimization (the big win)
*Goal: cut image weight by 5–10× without losing originals.*

- [ ] **6.1** Add `script/optimize_images.py` that, for each image
      under `content/images/`, emits `name.webp` (q=80) and
      `name@1200.webp` / `@800.webp` / `@400.webp` derivatives into a
      sibling directory. Originals stay untouched. **M**
- [ ] **6.2** Add a Liquid helper / include `_includes/picture.html`
      that emits a `<picture>` with `srcset` for the WebP derivatives
      and a fallback `<img>`. **S**
- [ ] **6.3** Add a `featured_image_optim:` frontmatter convention
      for new posts. **S**
- [ ] **6.4** Optimize 2014/04/`100_05*` (the ten 12+ MB phone-camera
      JPGs) and any post that references them. **M**
- [ ] **6.5** Optimize batch: 2013 (`385 MB → target <80 MB`). **L**
- [ ] **6.6** Optimize batch: 2014 (`347 MB → target <70 MB`). **L**
- [ ] **6.7** Optimize batch: 2017 (`159 MB → target <40 MB`). **M**
- [ ] **6.8** Optimize batch: 2011 (`99 MB`). **M**
- [ ] **6.9** Optimize batch: 2012 (`98 MB`). **M**
- [ ] **6.10** Optimize batch: 2018 (`75 MB`). **M**
- [ ] **6.11** Optimize remaining years: 2008, 2009, 2010, 2015, 2016,
      2019, 2020, 2021, 2022, 2024, 2025, 2026. **M** total.
- [ ] **6.12** Add `script/check_image_budget.py` to fail CI if any
      committed image exceeds 500 KB without an explicit override
      flag in a sibling `.image-meta.yml`. **S**

### Phase 7 — Content polish & findability
- [x] **7.1** Add JSON-LD `Article` schema to post layout. **S** ·
      *Shipped 2026-05-10.* New `_includes/jsonld_post.html` rendered
      from `_layouts/post.html` for every post page; emits a
      `BlogPosting` with `headline`, `datePublished`, canonical
      `url`, `mainEntityOfPage`, `author` (Person/Hunter Davis),
      and conditional `image` and `keywords` based on frontmatter.
      Validated structure against four representative post shapes
      (Dockstar tags-only, TUI000 image-only, Dunking Bird both,
      csserver minimal) — all parse as valid JSON. Person schema
      on the home page split out to new item 7.14.
- [x] **7.2** Compute reading-time at build (kramdown word count /
      225 wpm) and surface in post header + home cards. **S** ·
      *Shipped 2026-05-10 (post header only).* Pure Liquid:
      `content | strip_html | number_of_words | divided_by: 225 |
      plus: 1` produces an integer `~N min read` next to the post
      date, with a tooltip explaining the 225 wpm assumption.
      Verified sane across 5 representative posts (csserver = 1 min,
      Dockstar = 11 min, etc.). Home-card reading-time tracked
      separately as 7.15.
- [ ] **7.3** Compute related-posts at build using
      `_plugins/related_posts.rb` (shared tags + same family +
      chronological neighbours). **M**
- [ ] **7.4** Build `/now/` page from `_data/now.yml`. **S**
- [ ] **7.5** Build `/uses/` page from `_data/uses.yml`. **S**
- [ ] **7.6** Build `/milestones/` timeline page from
      `_data/milestones.yml` (see Appendix A). **M**
- [ ] **7.7** Split `about.md` into `/about/` (bio overview) +
      `/about/hacks/`, `/about/programming/`, `/about/writing/`,
      `/about/audio/`, `/about/leadership/`. Each existing anchor
      becomes a real heading on a real page; the new `/about/` index
      adds `redirect_from: ["/about.html"]` so the old URL keeps
      resolving. **L**
- [ ] **7.8** Migrate `public-speaking.md` content into
      `/about/leadership/` with
      `redirect_from: ["/public-speaking.html"]`. **S**
- [ ] **7.9** New search UX: instant results below the input, filter
      chips for year + tag, keyboard shortcut `/` to focus. **M**
- [x] **7.10** Convert `<a id='...'>foo</a>` anchors throughout
      `about.md` and `public-speaking.md` to real heading IDs.
      **S** · *Shipped 2026-05-10 (about.md half).* 37 inline
      `<a id='X'>Title</a>` anchors converted to proper
      kramdown headings (`## Title {#X}` for top-level
      sections, `### Title {#X}` for sub-sections; hierarchy
      determined from the TOC's bullet indentation). Sections
      are now visually distinct headings instead of inline
      anchor text. Pre-flight surfaced a duplicate
      `id="miso"` bug (Miso Media appears under both Start-Ups
      and Audio sections with the same anchor) — fixed by
      renaming the second occurrence to `miso-audio` and
      updating its TOC link to match. Cross-check confirms 37
      TOC refs ↔ 37 heading IDs, 0 missing, 0 orphans.
      `public-speaking.md` half tracked as new item 7.16.
- [x] **7.11** Sweep posts for `http://hunterdavis.com/...` self-links
      and rewrite to relative URLs. **M** ·
      *Shipped 2026-05-10.* **2,404 same-origin URLs**
      converted to relative paths across **321 files**
      (`_posts/`, `about.md`, `public-speaking.md`). Two-pass
      Python regex: first pass converted `https?://(www\.)?hunterdavis\.com/X`
      → `/X` across 2,399 URLs; second pass with a stricter
      character class (excluding `(`, `)`, `[`, `]`) cleaned
      up 5 markdown-link `[label](url)` edge cases where both
      label and url were absolute. The 16 bare-domain prose
      mentions (`http://www.hunterdavis.com.` etc.) were
      preserved as authored text. Wins:
      (a) every internal link saves a DNS+TLS handshake,
      (b) every link survives future host changes (apex/www
      flip in 8.4, any future domain move),
      (c) the codebase becomes portable — `_site/` can be
      served from any origin without rewriting bodies.
- [x] **7.12** Sweep posts for `<iframe ... src="http://...">` and
      upgrade YouTube embeds to `https://www.youtube-nocookie.com/`
      (privacy-friendly + works in modern browsers). **S** ·
      *Shipped 2026-05-10.* Single regex pass via sed:
      `https?://(www\.)?youtube\.com/embed/` →
      `https://www.youtube-nocookie.com/embed/`. **48 URLs
      migrated across 28 post/page files** (the 4 `/watch?v=`
      hyperlinks were intentionally left untouched — those are
      links to YouTube, not embeds, and don't have the embed
      tracking-cookie problem until the user clicks them).
      youtube-nocookie.com is Google's "privacy-enhanced mode"
      that doesn't set tracking cookies until playback starts.
- [x] **7.23** Add CollectionPage + ItemList JSON-LD to
      `/projects/`. **S** · *Shipped 2026-05-11.* Inlined a
      Liquid-templated `<script type="application/ld+json">`
      block at the top of `projects.md` that declares the
      page as a `CollectionPage` whose `mainEntity` is an
      `ItemList` over all 31 posts with a `project:` tag.
      Each `ListItem` jsonifies its `position`, `url`, and
      `name`, so titles containing quotes/backslashes
      serialize safely. `forloop.last` suppresses the
      trailing comma. Mirrors the per-year-archive treatment
      from 7.21 (CollectionPage + ItemList) but inline-Liquid
      instead of Python-baked, since `projects.md` is a
      Liquid template rather than a generator output. Schema
      footprint: posts have BlogPosting + BreadcrumbList;
      home has Person + WebSite; year archives and now
      `/projects/` have CollectionPage + ItemList. `/tags/`
      is the next list page that could get the same
      treatment, tracked under a separate item.
- [x] **7.22** Fix broken `<img src="">` on post hero. **S** ·
      *Shipped 2026-05-11.* `_layouts/post.html` previously
      emitted `<img src="{{ page.image }}" >` unconditionally,
      which rendered as `<img src="">` on every post without a
      hero image — invalid HTML that Chrome misinterprets as a
      reference to the document URL, plus no `alt` attribute
      (WCAG 1.1.1 violation). Replaced with a guarded block:
      resolves through `page.image | default: page.featured_img`
      (same pattern as `index.html`'s home cards, picking up
      legacy `featured_img` posts too), emits the `<img>` only
      when a real source exists, adds `alt=""` (decorative —
      the H1 title is right above), `decoding="async"`, and a
      new `.post-hero` class. New CSS rule (`display: block;
      max-width: 100%; height: auto; margin: 1em auto`) keeps
      wide images contained within the post column and
      centered. Brace balance 166/166. Older posts with
      `featured_img` (e.g., `2024-04-01-privacy-and-ai-update`,
      `2024-08-25-media`, `2024-08-25-search`) now correctly
      render their hero too — previously they fell through
      silently because the layout only checked `page.image`.
- [x] **7.21** Add CollectionPage + ItemList JSON-LD to per-year
      archive pages. **S** · *Shipped 2026-05-11.* Updated
      `script/generate_year_archives.py` to emit a
      `<script type="application/ld+json">` block at the top
      of every `archive/YYYY.md` page declaring the page as a
      `CollectionPage` whose `mainEntity` is an `ItemList`,
      one `ListItem` per post (position, name, url, descending
      order via `ItemListOrderDescending`). Regenerated all
      19 pages (2007–2026 minus 2023); validated all 19 emit
      well-formed JSON via a round-trip parse. Titles are
      JSON-encoded via `json.dumps` so post titles containing
      quotes/backslashes serialize safely. Posts ship
      BlogPosting + BreadcrumbList; home ships Person +
      WebSite; year archives now ship CollectionPage +
      ItemList. The `/projects/` hub and `/tags/` index are
      the remaining list pages that could get the same
      treatment — tracked separately when their generators
      land.
- [x] **7.13** Add 404 page upgrade with site-map and search.
      **S** · *Shipped 2026-05-11.* The 404 page already had a
      search box and JS-driven path-derivation (auto-fills the
      query from common legacy URL patterns like
      `/android-app-*/`, `/category/*`, `?s=` etc.). Added a
      `<nav class="not-found-nav">` with five quick-escape
      links — Home, Archive, Projects, Tags, Site map —
      mirroring the footer link set. Removed the misleading
      "Go back" anchor (it actually went to `/`, not the
      previous page). New CSS uses flex + wrap so the link row
      gracefully degrades on narrow viewports. Smart-routing
      for *resolvable* legacy paths is still handled
      server-side in A.12; this page is the fallback when
      nothing matches. Palette-consistent with the rest of the
      site (#0B5485 / #149797).
- [x] **7.16** Convert `<a id='X'>` anchors in
      `public-speaking.md` to real kramdown heading IDs (same
      pattern as 7.10's about.md conversion). **S** ·
      *Shipped 2026-05-10.* 5 inline anchors converted: 3 h2
      (apprenticeship, military, leadership) and 2 h3
      (fourblock, operationcode). The two existing `#` h1
      lines the user authored as page dividers ("Public
      Speaking" and "Leadership") were left untouched. TOC
      anchor refs now 5/5 resolve to real headings, 0 missing,
      0 orphans. The remaining `<h1>` duplication of the page
      title within the body is intentional — the user wrote it
      that way and removing it would be editing prose.
- [x] **7.14** Add JSON-LD `Person` schema to the home page. **S** ·
      *Shipped 2026-05-10.* New `_includes/jsonld_person.html`
      referenced from `_layouts/home.html`. Fields: `@type: Person`,
      `name: Hunter Davis`, `url` (site root via `absolute_url`),
      and `sameAs` array with three dossier-confirmed identities
      (GitHub via `site.links.github`, LinkedIn, Hacker News).
      Validated as valid JSON. Pairs with 7.1's BlogPosting so
      search engines can resolve `BlogPosting.author.name` to a
      single Person entity with verified profile links.
- [x] **7.20** Complete article-level Open Graph metadata on
      posts. **S** · *Shipped 2026-05-11.* `_includes/ssn.html`
      previously emitted `og:url` only on the home branch
      (when `page.excerpt` was empty), which is the opposite
      of what's needed — share scrapers want `og:url` on
      every page to identify the canonical share target.
      Added: `og:url` on the article branch (resolved through
      `absolute_url`, matching the canonical), plus
      `article:published_time` (ISO 8601 via
      `date_to_xmlschema`), `article:author`, and one
      `article:tag` per `page.tags` entry. The two
      date/author tags are guarded by `{% if page.date %}` so
      they only fire on real posts, not the static markdown
      pages (about, archive, projects, etc.) that also enter
      the article branch by virtue of having an excerpt.
      Facebook, LinkedIn, Discord, Slack, Mastodon and any
      OGP-compliant scraper can now show the publication date
      and tag list in the rich-card preview, not just the
      title/image. Completes the OG metadata story started
      with 7.18 (per-post share-card image).
- [x] **7.19** Add JSON-LD `WebSite` + `SearchAction` to home.
      **S** · *Shipped 2026-05-11.* New
      `_includes/jsonld_website.html` referenced from
      `_layouts/home.html` (alongside the existing Person
      include from 7.14). Declares the site name, description,
      canonical root URL, language, and a
      `potentialAction.SearchAction` whose `urlTemplate`
      points at `/search.html?query={search_term_string}` —
      the exact URL pattern the on-site search form
      (`_includes/header.html`, `search.md`) already uses.
      `{search_term_string}` survives `absolute_url`
      unmolested (Jekyll's `absolute_url` doesn't URL-encode
      paths) and `jsonify` doesn't need to escape `{`/`}` in
      JSON strings, so the placeholder reaches Google
      verbatim per its SearchAction spec. Unlocks the
      sitelinks search box in Google SERPs when the site is
      eligible: searching "hunterdavis.com" can now show an
      inline search box that submits directly to
      `/search.html`. Posts ship BlogPosting + BreadcrumbList;
      home ships Person + WebSite — the per-page schema
      footprint is now complete for current page types.
- [x] **7.18** Per-post share-card image. **S** ·
      *Shipped 2026-05-11.* Updated `_includes/ssn.html` so
      `og:image` and `twitter:image` resolve to the post's own
      `page.image` (or `page.featured_img`) when present,
      falling back to the site-wide `/sharer.png`. Path
      resolution uses Liquid's `default` chain plus
      `absolute_url`, so relative paths
      (`/content/images/2026/foo.png`) and absolute paths
      (GitHub raw URLs) both serialize correctly. Twitter
      card type now also flips from `summary` to
      `summary_large_image` for any post with a hero image —
      Twitter's spec wants `summary_large_image` for cards
      with images ≥ 300×157px, and every post hero on this
      site exceeds that. Pure-additive change: posts without
      an explicit hero image behave identically to before.
      The pre-existing missing-`sharer.png` issue (item 0.2)
      is unchanged — that fallback path is the same one used
      previously and still 404s until the OG image asset
      lands. The win: posts like the recent
      `announcing-dunking-bird` and `announcing-tps` posts
      now share with their actual hero image instead of a
      broken generic.
- [x] **7.17** Add JSON-LD `BreadcrumbList` schema to post
      pages. **S** · *Shipped 2026-05-10.* New
      `_includes/jsonld_breadcrumb_post.html` referenced from
      `_layouts/post.html`. Emits a three-step trail
      (Home → YYYY → post title), each with absolute URLs via
      `absolute_url` and JSON-safe strings via `jsonify`. The
      year step links to the real per-year archive page
      shipped in Phase 2.5 (`/archive/YYYY/`), not a fragment
      anchor — Google's BreadcrumbList spec wants real URLs
      per step, so this only works *because* 2.5 landed first.
      Visible breadcrumb in `_layouts/post.html` already uses
      WAI-ARIA `<nav aria-label="Breadcrumb">` markup (B.7);
      the JSON-LD mirrors that exact structure so eligible
      results in Google SERP can render the crumb trail
      directly under the title. Pairs with 7.1 (BlogPosting)
      and 7.14 (Person) to give every post a complete schema
      footprint with no prose involved.
- [x] **7.15** Surface reading-time on home post-list cards too.
      **S** · *Shipped 2026-05-10.* Two-line addition to
      `index.html` reusing the existing `.reading-time` CSS
      from Phase 7.2. Each home card now shows
      `{{ post.date | date: "%B %-d, %Y" }} · ~N min read`.
      Verified the formula across the latest 10 posts: spread
      from 1 to 6 minutes, matches the post-page indicator
      exactly. Build cost is ~510 Liquid invocations of
      `content | strip_html | number_of_words` across the 51
      paginated home pages — measured negligible.

### Phase 8 — Modernize tooling & infrastructure
- [ ] **8.1** Bump Jekyll to 4.x, update Gemfile + `Gemfile.lock`,
      validate with `bundle exec jekyll build`. **M**
- [ ] **8.2** Add `jekyll-feed`, `jekyll-sitemap`, `jekyll-seo-tag`
      plugins (replacing hand-rolled equivalents). **M**
- [ ] **8.3** GitHub Actions: build on push, preview deploy on PR,
      run `htmlproofer` and Lighthouse-CI budgets, deploy to GH Pages
      / Netlify on merge to `main`. **L**
- [ ] **8.4** Add `_redirects` (Netlify / Cloudflare Pages) for
      true 301s on canonical host (`hunterdavis.com` →
      `https://www.hunterdavis.com`), HTTP→HTTPS, optional trailing
      slash policy, and a fallback `/archives/:id  /archives/:id/  301`
      so any tail-end recovery can be done at the edge instead of
      requiring a rebuild. Add `_headers` for HSTS + a sensible
      CSP. **S** · *Why:* `jekyll-redirect-from` ships meta-refresh
      stubs (treated as 301 by Google but not a true 301 status).
      Edge redirects give true 301s and centralize host/scheme
      logic.
- [ ] **8.5** Add a service worker that pre-caches the home, the
      latest 5 posts, and core CSS — offline reading. **M**
- [ ] **8.6** Stretch: spike Eleventy or Astro migration on a branch.
      Keep Jekyll as canonical until image pipeline + IA features
      reach parity. **L**

### Phase 9 — Stretch / aspirational
- [ ] **9.1** Add `giscus` (GitHub-discussions backed) comments on
      selected posts where conversation is wanted. **S**
- [ ] **9.2** Add a "newsletter" sign-up via Buttondown or similar,
      sending a monthly digest. **M**
- [ ] **9.3** Add an offline-friendly RSS reader recommendation
      footer. **S**
- [ ] **9.4** Add a `/feed.json` JSON Feed alongside RSS. **S**
- [ ] **9.5** Add IndieWeb h-card / h-entry microformats. **S**
- [ ] **9.6** Add a "save game" feature: a static page that mirrors
      classic downloadable artifacts (csserver-adventure, snesaver,
      etc.) — possibly hosted via GitHub Releases. **M**

---

## Appendix A — Greatest hits / milestones (research dossier)

> Source for `_data/milestones.yml` and `/milestones/` (Phase 7.6).
> Compiled `2026-05-10` from primary-source verification across
> hunterdavis.com, Hackaday tag pages, Engadget, Make, evolver.fm,
> TechCrunch, the Hacker News Algolia API, Springer, and Napster's
> blog. Items marked `[unverified]` are repeated from Hunter's bio
> but lacked third-party confirmation in this pass.

### Confirmed milestones (with URLs for the timeline page)

#### 1999 — *csserver adventure*
Text-based CS-department roleplaying game written freshman year at
U. Evansville. Surfaced in archive form as
`_posts/2007-12-19-csserver-adventure.markdown`. Earliest dated
artifact on the site.

#### 2007 — MS Computer Science, Indiana University
Focus on scientific computing + AI. Co-author of *Common Instrument
Middleware Architecture* in *Grid Enabled Remote Instrumentation*
(Springer 2008, ISBN 978-0-387-09662-9, DOI
[10.1007/978-0-387-09663-6_26](https://link.springer.com/chapter/10.1007/978-0-387-09663-6_26)).

#### 2009-08-10 — DOSBox on the Zipit Z2
Ported DOSBox to the $40 Zipit Z2 wireless messenger; ran old DOS
games at 315 MHz on a QVGA Linux device.
Hackaday: <https://hackaday.com/2009/08/10/dosbox-on-zipit/>

#### 2009-09-03 — NES on the Zipit Z2
FCE Ultra NES emulator + Fluxbox + Java framework, no reflash.
Hackaday: <https://hackaday.com/2009/09/03/nes-on-zipit/>

#### 2009-09-25 — "With Zipit, Who Needs A Netbook?"
Linux 2.6.29 on the Z2 with mouse, audio, WiFi, microSD root —
flagship Z2 hack that turned a $38 IM toy into a pocket Linux
computer.
- Hackaday: <https://hackaday.com/2009/09/25/with-zipit-who-needs-a-netbook/>
- Engadget (2009-09-28): <https://www.engadget.com/2009-09-28-38-zipit-wireless-messenger-receives-linux-injection-becomes.html>
- Make (2009-09-28): <https://makezine.com/article/craft/linux-on-zipit/>

#### 2009-11-30 — IM-ME "Pink Wireless Terminal of Wonder"
Reverse-engineered the $14 Girl Tech IM-ME via USB sniffing;
discovered plaintext-hex protocol with no security. Seeded later
spectrum-analysis work in the wider community.
- Hackaday: <https://hackaday.com/2009/11/30/pink-wireless-terminal-of-wonder/>
- Hackaday tag (canonical): <https://hackaday.com/tag/hunter-davis/>

#### 2010-11-28 — $25 Dockstar emulation console
Seagate FreeAgent Dockstar + DisplayLink USB→VGA + USB sound +
Fluxbox = sub-$25 emulation box (Contra, Monkey Island, Quake 3).
- Self: <https://hunterdavis.com/2010/11/28/a-25-gamingemulation-powerhouse-using-the-dockstar-as-a-gaming-console.html>
- Engadget (2010-11-29): <https://www.engadget.com/2010-11-29-dockstar-freeagent-hacked-into-inexpensive-emulation-masterpiece.html>
- Hackaday (2011-01-02): <https://hackaday.com/2011/01/02/classic-game-emulation-on-the-dockstar/>
- HN: <https://news.ycombinator.com/item?id=1947852>

#### 2010-2011 — Discursive Labs (with Mark Christensen)
Bootstrapped startup that incubated Source Tree Visualizer and
QuickGrapher.

#### 2011 summer — Sith Challenge: 65 Android apps in 60 days
Doubled Jeff Hoogland's "Jedi" 30-in-30. Most popular: *Easy Cat
Whistle*. Reportedly grew to 250 K+ active users.
- HN announce (2011-06-27): <https://news.ycombinator.com/item?id=2703378>
- Results post: <http://www.hunterdavis.com/2011/08/01/android-updates-and-i-claim-the-crown>

#### 2011-09-11 — AirBeats AR drum kit, TechCrunch Disrupt SF
Augmented-reality iPad drum kit, front-facing camera, built in
under 15 hours.
- TechCrunch video: <https://techcrunch.com/video/air-beats-ar-drum-kit/>
- Evolver.fm coverage: <http://evolver.fm/2011/09/11/air-beats-augmented-reality-drumset-for-ipad>

#### 2012-01-23 — QuickGrapher open-sourced
HTML5 equation solver / grapher. HN front-page post (47 pts).
- Self: <http://www.hunterdavis.com/2012/01/23/quickgrapher/>
- HN: <https://news.ycombinator.com/item?id=3499000>

#### 2012-01-23 — Source Tree Visualizer open-sourced
Visualizes git/svn repos as actual growing trees (BSD).
- GitHub: <https://github.com/huntergdavis/Source-Tree-Visualizer>
- HN: <https://news.ycombinator.com/item?id=3499006>
- Tutorial (2012-12-24): <http://www.hunterdavis.com/2012/12/24/spruce-up-your-github-readme-with-a-current-source-tree-visualization>

#### 2012-03-14 — Web Strobe Tuner (Miso Media → HTML5/WebGL)
Ported Miso Media's proprietary FFT/pitch detection to JS/WebGL.
- Self: <http://www.hunterdavis.com/2012/03/14/webgl-html5-audio-web-strobe-tuner>
- HN: <https://news.ycombinator.com/item?id=3705978>

#### 2012-04-11 — The 70-app GitHub mass release
Wrote a script to auto-create repos from local project folders;
pushed ~70 apps in a day (Hackaday says 70+, his bio says 80).
Bio claims a ~4 M-hits/day peak after this. `[unverified — primary
source is the bio itself]`
- Self: <http://www.hunterdavis.com/2012/04/11/i-released-70-open-source-projects-today/>
- HN: <https://news.ycombinator.com/item?id=3830109>
- Hackaday (2012-04-12): <https://hackaday.com/2012/04/12/open-sourcing-everything-theres-an-app-for-that/>

#### 2012-12-30 — Quarter-million Play Store downloads
End-of-year metrics post.
- HN: <https://news.ycombinator.com/item?id=4986697>

#### 2013-01-07 — Rhapsody / Ford SYNC AppLink launch (CES)
Lead Android dev on Rhapsody's first full automotive integration.
- Napster blog: <https://blog.napster.com/2013/01/07/rhapsody-hits-the-road-with-ford-sync-applink/>
- SlashGear: <https://www.slashgear.com/rhapsody-comes-to-ford-and-lincoln-vehicles-through-sync-applink-07263651/>
- Ford developer program: <https://venturebeat.com/mobile/ford-mobile-app-developer-program/>

#### 2013-05-30 — Fanhattan / Fan TV set-top box unveiled
Per his bio, sole programmer on Fan TV (Yves Behar industrial
design, Android-based). Product ultimately failed.
- Engadget: <https://www.engadget.com/2013/05/30/fanhattan-fan-tv-stb/>
- Fast Company: <https://www.fastcompany.com/3010928/fanhattan-unveils-new-set-top-box-fan-tv>
- TIME/Techland: <https://techland.time.com/2013/05/30/with-fan-tv-fanhattan-thinks-it-has-the-home-entertainment-god-box/>

#### 2017-2019 — Apprenti speaking circuit
TECNA Toronto (2017-07), Seattle Code Fellows (2017-10), Utah DoL
Summit (2018-06), VentureBeat profile (2018-08), DoL SME
recognition (2018-09), Reuters World of Work (2018-12, 2019-01).
- VentureBeat: <https://venturebeat.com/entrepreneur/seattles-apprenti-seeks-to-take-its-tech-apprenticeship-program-nationwide>

#### 2020-12-20 — Atari Mini Pong Jr. hack
Open ADB debug interface on the $130 Mini Pong Jr.; revealed Mali
400, ARM sun8i, 512 MB RAM under the hood.
- Self: <https://hunterdavis.com/2020/12/20/hacking-atari-pong-jr-mini.html>

#### 2021 — Johnny Castaway revival saga
- Native port + Live CD (2021-03-10): <https://hunterdavis.com/2021/03/10/johnny_castaway_native_port_and_livcd.html>
- Dreamcastaway (Dreamcast, 640×480 @ 60 fps, 2021-03-21): <https://hunterdavis.com/2021/03/21/johnny_dreamcastaway_released.html>
- RetroFW port (LDK / RG-300 / RS97 .ipk, 2021-07-25): <https://hunterdavis.com/2021/07/25/johnny-castaway-for-retrofw-released.html>
- Text edition (2021-12-11): <https://hunterdavis.com/2021/12/11/johnny-castaway-text-edition.html>
- GitHub: <https://github.com/huntergdavis/johnnycastaway>

#### 2021-08-01 — RetroFW USB multiplayer networking
Bridged static USB-debug networks across RetroFW handhelds via a
$5–10 Pi Zero — netplay Duke Nukem, SNES link-cable emulation.
- Self: <https://hunterdavis.com/2021/08/01/retrofw-usb-multiplayer-networking.html>

#### 2021-12-09 — $15 HDMI-In on Oculus Go
USB OTG + ~$15 HDMI capture dongle → live HDMI-to-Go up to 1080p.
- Self: <https://hunterdavis.com/2021/12/09/hdmi-in-on-oculus-go.html>

#### 2024-11-07 — Tui000 ("three-thousand")
Terminal life-decision screensaver: ~240 weekend choices, lives
saved as JSON in a graveyard folder.
- Self: <https://hunterdavis.com/2024/11/07/announcing-tui000.html>
- GitHub: <https://github.com/huntergdavis/tui000>

#### 2024-11-16 — Labrync
ncurses maze screensaver / pathfinder. Auto-solve, breadcrumbs,
fog of war.
- Self: <https://hunterdavis.com/2024/11/16/announcing-labrync.html>
- GitHub: <https://github.com/huntergdavis/labrync>

#### 2024-12-29 — TPS (Team Planning Simulator)
Office Space riff. Hiring/throughput/cost planner by quarter and
2-week sprints, JSON save/load.
- Self: <https://hunterdavis.com/2024/12/29/announcing-tps.html>

#### 2025-10-05 — 2025 project spree recap
PicoCalc, InboxZero, Streak, Visualizer (Winamp/MilkDrop in
browser), Solitaire, People Grid, Poke (bar game), Web Flight,
PsyRunner, Asteroid Miner, 2D JS Game Boilerplate.
- Self: <https://hunterdavis.com/2025/10/05/a-bunch-of-one-off-projects-for-2025.html>

#### 2026-03-21 — Dunking Bird (current project)
Sits outside an AI agent's UI and repeatedly fires a configurable
prompt; window-capture tested on KDE/Wayland. Built to keep
long-running PS1 dev agents going.
- Self: <https://hunterdavis.com/2026/03/21/announcing-dunking-bird.html>
- GitHub: <https://github.com/huntergdavis/dunkingbird>

#### 2026 — Johnny Castaway PS1 (in flight)
Referenced by the Dunking Bird post; this redesign is timed to its
launch. No dedicated announcement yet.

### Books

- **Hacks** — 40+ chapter compilation of his Zipit/Linux/IM-ME
  tutorials. Listed across Amazon Kindle, B&N, Sony, Kobo, Apple,
  Smashwords. Kobo: <https://www.kobo.com/us/en/ebook/hacks>
- **Live For Free: The Chronicles of a Nerd Saving for a Startup**
  — distributed 2008-2010, originally via liveforfree.net.
- **Build Your Own Distributed Compilation Cluster — A Practical
  Walkthrough** — 60+ pages, ARM↔x86_64 distcc cluster how-to.
- **Oubastet's Wager** — open-sourced fable.
- Books index post: <https://hunterdavis.com/2012/04/25/books.html>

### Career timeline (independently verified where possible)

- Indiana University BS / MS → Senior Software Engineer II at
  **Scalable Network Technologies** (~2007).
- **Discursive Labs** co-founder/CEO (2010–2011, with Mark
  Christensen).
- **Miso Media** Android lead (2011–2012, GV / 500 Startups-funded).
- **Rhapsody / Napster** Android (2012–2016): Ford SYNC, Fanhattan,
  SongMatch.
- **Avvo** Director of Engineering (2016–2019): <https://stories.avvo.com/inside-avvo/life-at-avvo/meet-hunter-davis>
- **RealSelf** Director of Engineering (2019–2022).
- **Mantra Health** VP of Engineering (2022–present): <https://theorg.com/org/mantra-health/org-chart/hunter-davis>
- LinkedIn: <https://www.linkedin.com/in/hunterdavis/>
- His own write-up on first day as a team leader: <https://medium.com/avvo/your-first-day-as-a-team-leader-b38a7dedf19b>

### Notable coverage (publication backlinks)

**Hackaday** — full tag page <https://hackaday.com/tag/hunter-davis/>
- 2009-08-10 DOSBox on Zipit
- 2009-09-03 NES on Zipit
- 2009-09-25 With Zipit, who needs a netbook?
- 2009-11-30 Pink Wireless-terminal of Wonder (IM-ME)
- 2011-01-02 Classic Game Emulation on the Dockstar
- 2012-04-12 Open Sourcing Everything… There's An App For That
- 2012-08-12 Hackaday Links (license-plate tablet rack)
- 2013-06-30 Hackaday Links (Retrode + Ouya note)

**Engadget**
- 2009-09-28 $38 Zipit becomes a netbook
- 2010-11-29 Dockstar FreeAgent emulation masterpiece
- 2013-05-30 Fanhattan Fan TV set-top

**Make Magazine**
- 2009-09-28 Linux on Zipit

**TechCrunch / Evolver.fm** — AirBeats (2011-09-11)

**Hacker News** (his account `huntergdavis`,
[user page](https://news.ycombinator.com/user?id=huntergdavis))
- 2010-11-28 Dockstar (18 pts)
- 2011-06-27 Sith Challenge announce
- 2012-01-23 QuickGrapher (47 pts)
- 2012-01-23 Source Tree Visualizer
- 2012-03-14 Web Strobe Tuner (9 pts)
- 2012-04-11 70-app GitHub release
- 2012-12-30 Quarter-million downloads recap

### Archive.org notes

The Wayback Machine availability API was unreachable from this
agent's environment, so a manual browse is needed for the
timeline. Key things to look for at
<https://web.archive.org/web/*/hunterdavis.com>:

- **Earliest snapshot** — bio implies late-1990s launch but the
  earliest dated post on the current archive is 2007-12-19. A
  pre-2007 snapshot would be the strongest evidence of the
  30-year claim.
- **2009 era** — Hackaday inbound links from 2009-08 onward; a
  snapshot from this era is essentially guaranteed.
- **2012-04 traffic spike** — most interesting era for a
  "Greatest Hits" page hero image.
- **Bitwiser-theme adoption** — current Jekyll era.

URL patterns confirm two distinct CMS eras worth visualizing:
- **Pre-Jekyll** — `hunterdavis.com/archives/NNN` (numeric IDs;
  examples: `/archives/843` for Dockstar Nov 2010, `/archives/1640`
  for Sith Challenge Jun 2011, `/archives/201` for Linux on Zipit
  2009). Implies WordPress / MovableType.
- **Jekyll** — `hunterdavis.com/YYYY/MM/DD/post-name.html` from at
  least 2012-01 onward. (`content/images/README.md` mentions a Ghost
  era as well — possibly between WordPress and Jekyll.)

### Items the agent could not independently confirm

These are repeated from Hunter's bio but lacked third-party
verification in the research pass; flag them as `[unverified]` in
any public-facing milestone copy until a source is added.

1. **30-year site lifetime** / 1990s launch — no Wayback snapshot
   accessible during research.
2. **4 M hits/day peak (April 2012)** — bio claim only.
3. **Tor / Privoxy on Zipit Z2** — narrative implies a working
   port but no Hackaday article confirms it (DOSBox/NES/Linux are
   all confirmed; Tor/Privoxy specifically is not).
4. **IM-ME → Travis Goodspeed → police-radio jamming** — Hunter's
   reverse-engineering work is documented; the chain to Goodspeed's
   later spectrum analysis is implied but I couldn't pull a single
   bridging article URL.
5. **Two audio patents at Rhapsody/Napster** — bio claim only;
   USPTO/Justia inventor lookup couldn't be completed in this
   environment.
6. **Apprenti board membership** — speaking + DoL SME work
   confirmed; no third-party listing of Hunter as a *board* member
   was found.
7. **Lifehacker / OSNews / Slashdot coverage** — bio mentions
   "hundreds of blogs and forums"; only Hackaday / Engadget / Make
   surfaced in this pass.
8. **Springer co-author list** — chapter URL confirmed but full
   author list is behind an SSO redirect.
9. **AirBeats team members** — TechCrunch video has no team listing;
   Evolver.fm article was unreachable.

### Open questions for Hunter (for the human, not the agent)

**Resolved 2026-05-10:**

- ~~Legacy artifacts mirror strategy~~ → **decided:** recover from
  `archive.org` and commit at original paths (Phase 7.18).
- ~~WordPress URL recovery scope~~ → **decided:** map every URL we
  can prove (Phase 7.16/7.17), smart-404 catches the rest.
- ~~`/about/` collision~~ → **decided:** keep the new `/about/`
  hub; sub-pages use non-colliding slugs; redirect the 3 legacy
  `/about/<slug>/` URLs (Phase 7.19).
- ~~Hosting~~ → **decided:** GitHub Pages from this user-page repo;
  sibling project repos auto-publish at `hunterdavis.com/<repo>/`.
  This means custom `_plugins/` won't run on stock GH Pages — a
  CI-built deploy (Phase 8.3) is required if we want `_plugins/`
  rather than per-post `redirect_from:` frontmatter.

**Still open:**

- Sith Challenge apps on `play.google.com` — which are still live,
  which are open-sourced on GitHub, which are formally retired? A
  one-time audit would let project hub 4.5 show real status chips.
- Comments back (giscus on selected posts) or stay read-only?
- Newsletter — yes, no, maybe later?
- Display serif — keep Vollkorn, or pick something else?
- Confirm the four `[unverified]` claims (4 M hits/day, Tor on Z2,
  two audio patents, Apprenti board seat) before they go on
  `/milestones/`, or hedge the copy ("the bio says…").

---

## Out of scope (for now)

- Migration off Jekyll to Eleventy/Astro/Next — tracked as 8.6
  stretch, not on the critical path.
- Rebuilding embedded interactive demos (QuickGrapher, deck-of-cards
  simulator) — they live on `hunterdavis.com/...` paths and should
  be left alone until the IA refresh completes.
- A full content rewrite. We're improving findability of the existing
  archive, not rewriting it.

---

## Living changelog

- `2026-05-11` — **Phase 2.2b shipped**: tag chips on post pages,
  home post cards, and the sidebar topic-cloud now link to the
  new `/tags/<slug>/` pages instead of `/search.html?query=`.
  Post/home use a conditional guard on `_data/tags.yml`
  counts so single-use tags fall back to search; sidebar
  top-30 is unconditional (all eligible).
- `2026-05-11` — **Phase 2.2 shipped**: per-tag pages. New
  `script/generate_tag_pages.py` emits 84 pages at
  `/tags/<slug>/` for every tag with ≥ 2 posts (286 single-use
  tags still fall through to `/search.html`). `/tags/` index
  updated to link to the new pages conditionally on the count
  in `_data/tags.yml`. Big cross-linking win.
- `2026-05-11` — **Phase 1.2 shipped**: trimmed the search corpus.
  `search.json` now indexes title, tags, excerpt, url, date — no
  more `author`/`category` noise, no more full-`post.content`
  bloat. `js/search.js` updated in lockstep (both lunr index
  bodies), `tags` field added with `boost: 5`. Corpus shrinks ~10×
  for typical posts.
- `2026-05-11` — **Phase 7.23 shipped**: CollectionPage + ItemList
  JSON-LD on `/projects/`. Inline Liquid block at top of
  `projects.md` lists all 31 `project:`-tagged posts as
  structured ListItems with jsonify-safe titles and URLs.
- `2026-05-11` — **Phase 7.22 shipped**: fixed broken hero `<img>`
  in `_layouts/post.html`. Previously every post emitted
  `<img src="">` with no alt. Now guarded by `if hero != blank`,
  resolves `page.image | default: page.featured_img`, adds
  `alt=""`, `decoding="async"`, `.post-hero` class. New CSS
  rule contains the hero within the column. Legacy
  `featured_img` posts now render their hero correctly too.
- `2026-05-11` — **Phase 7.21 shipped**: CollectionPage + ItemList
  JSON-LD on per-year archive pages. `generate_year_archives.py`
  bakes a JSON-LD block into each of the 19 `archive/YYYY.md`
  files, listing every post for that year as a structured
  `ListItem`. Round-trip-validated as JSON across all 19 pages.
- `2026-05-11` — **Phase 7.13 shipped**: 404 page upgrade.
  Added a quick-escape `<nav>` with five links (Home, Archive,
  Projects, Tags, Site map) mirroring the footer. Replaces the
  misleading "Go back" anchor. Smart-search auto-fill from
  legacy URL patterns (Android apps, /category/, ?s= etc.)
  was already in place. CSS uses flex-wrap so the link row
  collapses cleanly on narrow viewports.
- `2026-05-11` — **Phase 7.20 shipped**: completed article-level
  Open Graph metadata on posts. `_includes/ssn.html` now emits
  `og:url`, `article:published_time`, `article:author`, and one
  `article:tag` per tag on every post — Facebook/LinkedIn/Slack
  rich cards now include the publication date and tag list.
- `2026-05-11` — **Phase 7.19 shipped**: WebSite + SearchAction
  JSON-LD on home page. New `_includes/jsonld_website.html`
  declares the site and a SearchAction whose `urlTemplate`
  points at the existing `/search.html?query={search_term_string}`
  endpoint, making the site eligible for Google's sitelinks
  search box. Per-page schema set is now complete: posts have
  BlogPosting + BreadcrumbList, home has Person + WebSite.
- `2026-05-11` — **Phase 5.9 shipped (pulled forward)**: removed
  `text-align: justify` from article body paragraphs. WCAG-aligned
  accessibility fix; eliminates "river" whitespace in long-form
  posts. One rule deleted from `css/style.scss`, brace balance
  160/160.
- `2026-05-11` — **Phase 7.18 shipped**: per-post share-card
  image. `_includes/ssn.html` now resolves `og:image` and
  `twitter:image` to the post's own hero (`page.image` or
  `page.featured_img`) via Liquid `default` chain + `absolute_url`,
  falling back to `/sharer.png`. Twitter card type auto-upgrades
  to `summary_large_image` when a hero is present. Recent
  announcement posts (Dunking Bird, TPS, Labrync, Tui000) now
  share with their real hero image.
- `2026-05-10` — **Phase 7.17 shipped**: BreadcrumbList JSON-LD
  on every post page. New `_includes/jsonld_breadcrumb_post.html`
  emits a three-step `Home → YYYY → title` trail mirroring the
  visible B.7 breadcrumb. The year step points at the real
  per-year archive URL from Phase 2.5; the title step
  references the canonical post URL. Validated JSON-safe via
  `jsonify`. Burns down "schema support" project line: posts
  now ship BlogPosting + BreadcrumbList; home ships Person.
- `2026-05-10` — **Phase 2.5 shipped**: per-year archive pages.
  `script/generate_year_archives.py` emits 19 pages at
  `/archive/2007/`–`/archive/2026/` (2023 has no posts so it's
  skipped), each with reverse-chronological listing + adjacent-year
  nav. Post breadcrumbs now point at real pages instead of fragment
  anchors. Archive index also cross-links each year heading.
- `2026-05-10` — initial draft created. Audit of 507 posts, 1.4 GB
  built site, 1.18 MB search page, ~78% untagged corpus.
- `2026-05-10` — Appendix A populated with verified milestones,
  publication backlinks, archive.org URL-pattern analysis, and a
  flagged list of `[unverified]` bio claims. Source URLs in place
  for `_data/milestones.yml`.
- `2026-05-10` — URL preservation strategy expanded after audit
  found 285 distinct legacy URLs (not just `/archives/NNN`). Added
  GitHub Pages project-subpath reservation rule, five-layer fix
  (was three), and Phase 0/7 backlog items 0.19, 0.20, 7.14–7.21
  for full WordPress era recovery + loose-artifact mirroring.
- `2026-05-10` — Backlog reorganized: URL preservation pulled to
  the top as **Phase A** (12 items), the Phase 0 hygiene track
  drops behind it. **Phase A.2 shipped**: `script/audit_legacy_urls.py`
  + `_meta/legacy_url_inventory.csv` (1,794 unique URLs, 94.9%
  high confidence, 48 to mirror, 36 needing archive.org lookup).
- `2026-05-10` — **Phase A.1 shipped**: explicit
  `permalink: /:year/:month/:day/:title.html` in `_config.yml`.
  Pre-flight checks confirmed zero output diff vs. Jekyll's implicit
  default for this corpus. Foundation for all later URL preservation
  work locked in.
- `2026-05-10` — **Phase A.3 shipped**: `_data/projects_subpaths.yml`
  with all 135 public, non-archived `huntergdavis/*` repo names
  reserved. Source of truth for the future build-fail collision
  check (A.13) and the live-subset verification (A.14). Two sidebar
  bugs (`/resume/`, `/photo-stream/`) surfaced and recorded.
- `2026-05-10` — **Phase A.4 shipped**: `jekyll-redirect-from`
  added to the `:jekyll_plugins` group in `Gemfile` and the
  `plugins:` array in `_config.yml`. No-op today (no post uses
  `redirect_from:` yet) but unblocks every later URL-recovery
  item (A.5, A.7, A.9, the `/about/` split, etc.).
- `2026-05-10` — **Phase A.5 shipped**: `_data/legacy_redirects.yml`
  generated by `script/seed_legacy_redirects.py`. Five sub-keys
  in place (`archives`, `wp_query_ids`, `wp_slugs`,
  `wp_categories`, `about_slugs`). 15 + 4 numeric-ID entries
  populated, 3 with confirmed/high-confidence targets verified
  against `_posts/`, the rest flagged `needs-wayback` for A.11.
  The slug categories stay empty arrays in this commit; A.6
  extends the script to fold in the audit's high-confidence
  slug matches.
- `2026-05-10` — **Phase A.6 shipped**: WP slug long-tail folded
  in. `_data/legacy_redirects.yml` now holds **188 redirect
  candidates with 171 resolved (91.0%)** — beats the >90% target
  the doc specified. wp_slugs 162 (98.7% high confidence),
  wp_categories 4 (low; need manual taxonomy review later),
  about_slugs 3 (all high). Spot-check confirmed sample targets
  point at real posts.
- `2026-05-10` — **Phase A.7 shipped**: `script/expand_redirects.py`
  wrote `redirect_from:` frontmatter onto **93 posts covering 164
  legacy URLs**. Once GH Pages rebuilds, every Hackaday / Engadget /
  HN inbound link from the WordPress era starts resolving again
  via `jekyll-redirect-from` static stubs. Filtered out: 14
  needs-wayback (no target), 1 medium-confidence, 1 sibling-repo
  collision (`/source-tree-visualizer/`). All 507 posts still
  parse cleanly post-rewrite. `wp_query_ids` (`?p=NNN`) deferred
  to new item A.15 since they're query strings, not paths.
- `2026-05-10` — **Phase 7.1 shipped**: BlogPosting JSON-LD on
  every post page via new `_includes/jsonld_post.html` referenced
  from `_layouts/post.html`. Schema fields: headline,
  datePublished, url, mainEntityOfPage, author (Hunter Davis),
  conditional image + keywords. Output validated as valid JSON
  across four representative post shapes. Burns down the
  "schema support" project line. Person schema on home tracked
  separately as 7.14.
- `2026-05-10` — **Phase 7.14 shipped**: Person JSON-LD on home
  page via new `_includes/jsonld_person.html` referenced from
  `_layouts/home.html`. `sameAs` array contains three
  dossier-confirmed identity URLs (GitHub, LinkedIn, HN).
  Together with 7.1, the search-engine entity graph is now
  complete: every post is a BlogPosting authored by the home
  page's Person, and that Person resolves to three verified
  profile pages.
- `2026-05-10` — **Cross-linking, opening salvo**: prev/next
  chronological nav added to `_layouts/post.html` plus a
  `.post-nav` block in `css/style.scss`. Uses Jekyll built-ins
  `page.previous` / `page.next` so no precomputation needed.
  Every one of the 507 posts now links to its date-adjacent
  neighbours. Precursor to Phase 5.4's full post-v2 redesign;
  tag-overlap "related posts" still tracked under 7.3.
- `2026-05-10` — **Phase 0.5 + 0.6 + 0.7 shipped** (bundled):
  home image rendering modernized. Replaced two `<img>` lines
  (one always broken from `featured_img`, one always rendered
  even with empty `src`) with a single guarded `<img>` that
  uses `post.image | default: post.featured_img`, adds
  `loading="lazy" decoding="async" alt=""`, and quotes the
  `width="600"` attribute. Net effect: **338 broken-icon
  renders eliminated** across the archive while preserving the
  169 posts that have a hero image (153 via `image:`, 16 via
  `featured_img:` fallback). Zero regression.
- `2026-05-10` — **Phase 0.14 shipped**: `<main>` landmark and
  skip-to-content link in `_layouts/default.html`. Keyboard
  users now have a one-tab path past the header navigation
  straight to the content; screen readers can identify the
  primary landmark on every page. CSS uses the standard
  off-screen-until-focused pattern.
- `2026-05-10` — **Phase 1.1 shipped**: search corpus split out
  to a fetched `/search.json` so `_site/search.html` is a thin
  shell instead of a 1.18 MB inline-data page. Search button
  binding deferred to after the fetch resolves; status message
  for slow loads / failure. `js/search.js` refactored to read
  the URL query fresh inside each handler. The single biggest
  performance cliff on the site is gone.
- `2026-05-10` — **Phase 7.2 shipped (post header only)**:
  reading-time indicator next to every post date, computed via
  pure Liquid (`content | strip_html | number_of_words |
  divided_by: 225 | plus: 1`). Also adds a small `.reading-time`
  CSS rule. Home-card reading-time deferred to new item 7.15.
- `2026-05-10` — **Phase B added** (18 items). Real
  information-architecture / navigation track: sidebar
  restructure, top-nav expansion, real footer, site map,
  breadcrumbs, tag-chip links, featured posts, "currently
  working on" + "start here" + "greatest hits" home panels,
  "more from this project" + "other posts from this year"
  cross-linking, header search + keyboard shortcut, mobile-nav
  rewrite, header tagline, topic-cloud widget. The whole phase
  ships against the existing layouts incrementally — does not
  wait for the bigger Phase 5 v2 redesign. Editorial copy
  (now, start here, header tagline) is user-supplied, never
  machine-authored.
- `2026-05-10` — **Phase B.1 shipped**: sidebar project list
  migrated from hardcoded HTML in `_includes/sidebar.html` to
  `_data/sidebar.yml`. 8 project entries (QuickGrapher, Physical
  Media, Streak!, Visualizer, My Solitaire Varient, People
  Grid, PsyRunner Game, AsteroidMiner) preserved verbatim;
  rendered output byte-identical. Unblocks B.2 (grouping) and
  B.3 (prune broken) without touching template code.
- `2026-05-10` — **Phase B.2 shipped**: sidebar entries grouped
  into **Tools** (5) and **Games** (3) by a new `group:` field
  per entry plus a Liquid `group_by` in the template plus a
  `.group-heading` CSS rule. The 8 project links are now
  visually scannable as two distinct categories instead of one
  flat list. New groups can be added with no template changes —
  just new YAML entries.
- `2026-05-10` — **Phase B.14 shipped**: "More from {year}"
  aside on post pages. Pure-Liquid sibling-finder via a capture
  + `contains "<li>"` guard so solo-post years don't render an
  empty section. Discovery boost across the 30-year archive
  without any frontmatter changes or precomputation.
- `2026-05-10` — **Phase B.16 shipped**: mobile nav rewritten
  with native `<details>/<summary>`, fixing a latent
  production bug (the `.active-menu` toggle was defined in CSS
  but no JS ever applied it). Net −70 lines of dead CSS
  (`.android`, `.opener`, `.clear-opener`, `.active-menu`
  rules removed). Desktop visual unchanged; mobile menu now
  actually opens.
- `2026-05-10` — **Phase B.15 shipped**: search input promoted
  to the header, rendered on every page (was sidebar-only,
  home-only). Tiny inline JS adds a `/` keyboard shortcut to
  focus the input, guarded against firing while typing in an
  input/textarea/contenteditable. `role="search"` and
  hidden-label a11y. The deep archive now has a one-keystroke
  search affordance from any post page.
- `2026-05-10` — **Phase 0.11 shipped**: dead Facebook /
  Twitter share `<a>` blocks removed from post pages and
  replaced with a single `<button class="copy-link">` that
  uses `navigator.clipboard` when available, falls back to
  `execCommand('copy')` for HTTP / older browsers, and flashes
  "Copied" for 1.5 s. Drops 2 of the 6 font-awesome icons in
  use (incremental progress toward 0.10) and replaces a
  privacy-leaky (Facebook tracks pre-share) + broken-on-X
  share UX with a modern social-agnostic copy affordance.
- `2026-05-10` — **Phase 0.10 shipped**: font-awesome CDN
  dropped. The 4 remaining decorative icons (calendar, home,
  info-circle, tag) removed instead of swapped for inline SVG
  — labels stand on their own. Saves ~110 KB and one DNS+TLS
  handshake on every page; removes a third-party CDN
  dependency (privacy + reliability win). Future inline-SVG
  alternative tracked as new item 0.16.
- `2026-05-10` — **Phase A.15 shipped**: WordPress
  query-string redirect handler. Inline `<script>` at the top
  of `index.html` reads `?p=NNN` and `?s=foo` via
  `URLSearchParams` and bounces to the canonical Jekyll URL
  (or `/search.html` for searches). Build-time Liquid map
  pulls from `site.data.legacy_redirects.wp_query_ids`, so
  any future A.11 archive.org recovery automatically extends
  the handler with no JS change. Final hole in URL
  preservation closed for the WP-era inbound links our audit
  could see.
- `2026-05-10` — **Phase 7.12 shipped**: every YouTube embed
  on the site now uses `youtube-nocookie.com` over HTTPS.
  Single regex pass swapped 48 URLs across 28 post/page files
  (the 4 `/watch?v=` hyperlinks were intentionally left as-is
  — they're links to YouTube, not embeds). Embedded videos no
  longer set tracking cookies on readers' browsers until they
  actually press play.
- `2026-05-10` — **Phase 0.4 shipped**: dual `site.url` /
  `site.base_url` config keys collapsed into a single
  `site.url`. 8 `site.base_url` references in `ssn.html`,
  `sitemap.xml`, and `robots.txt` renamed; the duplicate
  config line dropped from `_config.yml`. Byte-identical
  output (both keys held the same value), but now there's a
  single source of truth for the site origin — important
  before the HTTPS switch in 0.3.
- `2026-05-10` — **Phase 0.8 + 0.9 + 0.12 shipped** (bundled):
  dead-code purge from `_includes/` and root. Deleted
  `_includes/disqus.html`, `_includes/jquery-1.4.4.min.js`,
  `_includes/jquery-ui-1.8.9.custom.min.js`,
  `_includes/modernizr-1.6.min.js`, `_includes/obfs_embed.js`,
  `_includes/deck.js`, `_includes/simulator.js`, and
  `index.old`. ~290 KB removed from git tree. `_includes/`
  went from 13 files to 6, every remaining file actively
  referenced by a `{% include %}` statement. Zero behaviour
  change — none of these were ever loaded by Liquid.
- `2026-05-10` — **Phase B.7 shipped**: breadcrumb strip
  above every post's `<h1>`. `Home / <year>` rendered as a
  WAI-ARIA `<nav aria-label="Breadcrumb"><ol><li>`. Home
  links to `/`; year is plain text until Phase 2.5 ships
  `/archive/<year>/`. Adds an immediate contextual cue at
  the top of every post without creating broken links.
- `2026-05-10` — **Phase A.13 shipped**:
  `script/check_subpath_collisions.py`. Reads
  `_data/projects_subpaths.yml` (135 reserved names) and the
  source root, exits non-zero if any non-Jekyll-special,
  non-excluded top-level entry collides case-insensitively
  with a sibling-repo subpath. Adversarial test confirms:
  `mkdir quickgrapher` → exit 1 with remediation message;
  removed → exit 0. Defensive infrastructure that prevents
  future commits from silently clobbering a sibling-repo
  deploy.
- `2026-05-10` — **Phase A.12 shipped**: smart 404 page. The
  existing "Sorry…" copy is preserved, joined by a path
  display and a prefilled search form. Tiny JS pattern-matcher
  derives a search hint from `/android-app-…`,
  `/android-apps/<cat>/<slug>`, `/popular-open-source-projects/<slug>`,
  `/category/<slug>`, `/about/<slug>`, `?s=…`, and slug-shaped
  paths. Reader lands on an unknown URL → sees what they
  asked for, an auto-focused search input prefilled with a
  best-guess term, and a Go-back affordance. Catches anything
  the explicit redirects miss.
- `2026-05-10` — **Phase 1.4 shipped**: feed slimmed +
  full-content feed added. `feed.xml` now ships
  `post.excerpt | strip_html | normalize_whitespace` per
  item (was full `post.content`), trimming RSS payload from
  ~115 KB to a small fraction. New `feed-full.xml` keeps the
  full HTML body in a `<content:encoded><![CDATA[…]]>` block
  for power readers; both feeds cross-reference each other
  via `<atom:link rel="alternate">`. Incidental fix: removed
  the spurious `/` in `<link>{{ site.url }}/{{ post.url }}`
  that produced double-slash URLs.
- `2026-05-10` — **Phase 1.5 + 1.6 (deletion half) shipped**:
  dead-code purge from `_sass/` and `js/`. Deleted
  `_sass/_buttons.scss` (42 lines; the `@import 'buttons'`
  line in style.scss had been commented out for the entire
  history of this codebase) and `js/headroom.min.js`
  (orphaned, referenced by nothing). The `position: sticky`
  header rewrite originally described by 1.6 is a fresh
  feature now, not a replacement — tracked as new 1.10.
- `2026-05-10` — **Phase 1.10 shipped**: sticky header on
  desktop. `_includes/header.html` gains `class="site-header"`,
  `style.scss` gains a small `@media (min-width: 569px)`
  block that pins the header to the top with a subtle drop
  shadow. Mobile keeps its existing fixed-popover nav.
  Search input and site title now stay one keystroke / one
  click away no matter how far you scroll.
- `2026-05-10` — **Phase 0.13 shipped**: dead Google
  Analytics include purged. `_includes/analytics.html` used
  the Universal Analytics `ga()` snippet (sunset by Google
  July 2024), and `site.ga_id` had been commented out in
  `_config.yml` for the entire history of this codebase, so
  the conditional include never fired. Deleted the file, the
  conditional in `_layouts/default.html`, and the stale
  commented `ga_id` / `ga_domain` / `disqus` lines in
  `_config.yml`. ~20 lines of dead code removed total.
  Future analytics adds via the privacy-respecting path
  tracked as new item 0.17.
- `2026-05-10` — **Phase 7.15 shipped**: reading-time on
  every home-list card. Same `content | strip_html |
  number_of_words | divided_by: 225 | plus: 1` Liquid chain
  as 7.2, reusing the `.reading-time` CSS class. Readers
  scanning the home page now see "~N min read" next to each
  post date, matching the post-page indicator. Spread on the
  latest 10 posts: 1–6 minutes.
- `2026-05-10` — **Phase B.5 shipped**: real footer with site
  map. The two-line copyright + Bitwiser-theme attribution
  was replaced by a flat horizontal list of 8 functional
  links (About, Leadership and Public Speaking, Search, RSS,
  RSS full, Sitemap, GitHub, Email) plus a compact Jekyll
  credit. Every link goes somewhere that resolves today.
  Footer renders on every page via the default layout. The
  Bitwiser-theme credit was dropped since the codebase has
  been substantially rewritten from the original (most of the
  Bitwiser scaffolding has been deleted in recent commits).
- `2026-05-10` — **Phase 0.3 shipped**: `site.url` flipped
  from `http://www.hunterdavis.com` to
  `https://www.hunterdavis.com`. One-line config change
  propagates to 23 downstream renders (canonical tags,
  OG/Twitter URLs, RSS feed links, sitemap entries, JSON-LD
  identifiers, favicon `<link>`, Copy-link button). GitHub
  Pages has enforced HTTPS for custom domains since 2018 so
  the underlying site has been HTTPS-reachable all along —
  this commit finally makes the canonical metadata agree.
- `2026-05-10` — **Phase B.13 shipped**: "More in this
  project" aside on post pages. Renders on any post that
  sets a `project:` frontmatter value, listing up to 6
  sibling posts. Seeded with `project: johnny-castaway` on
  the 6 confirmed saga posts (on-the-web-on-the-hunt,
  Castawine, native-port, Dreamcastaway, retrofw, text
  edition). A reader landing on the Dreamcast port now sees
  five other Johnny Castaway commits one click away. Zipit,
  Dockstar, etc. arcs can be retro-tagged in follow-ups.
- `2026-05-10` — **B.13 extension**: tagged the Zipit Z2
  saga with `project: zipit-z2`. **19 posts** spanning
  2008-12 → 2015-05, covering the full Z2 arc: Tor + Privoxy
  router, DOSBox port, kernel updates, ScummVM, NES emulator,
  Fluxbox WM, Aliosa27 / RootNexus / Mozzwald userlands,
  HULU streaming, cross-compiler setup, Hulu, pen-testing
  distribution, Cloud Print, "Spirit of the Zipit Lives On".
  The aside template from this morning's B.13 commit
  activates automatically — every Zipit post now lists 5
  others in the era. Tangential mentions (Dockstar gaming
  console, Hacks ebook, Hackaway-prize threads, My Story,
  the modern site-search announce) deliberately not tagged.
- `2026-05-10` — **Phase 7.10 shipped (about.md half)**:
  37 inline `<a id='X'>Title</a>` anchors in `about.md`
  converted to kramdown headings (`## Title {#X}` for
  top-level, `### Title {#X}` for sub-sections; hierarchy
  taken from the TOC bullets). Sections are now real
  headings instead of inline anchor text — readers get
  visible h2/h3 separators between life chapters. Surfaced
  and fixed a pre-existing duplicate-anchor bug ("Miso
  Media" appears under both Start-Ups and Audio with the
  same `#miso` id) by renaming the second to `#miso-audio`
  and updating its TOC link. Public-speaking.md half tracked
  as 7.16.
- `2026-05-10` — **Phase 7.16 shipped**: same conversion
  applied to `public-speaking.md` — 5 inline anchors → 5
  kramdown headings (3 h2: apprenticeship, military,
  leadership; 2 h3: fourblock, operationcode). TOC anchor
  refs now 5/5 resolve. The two pre-existing `# h1` lines
  the user authored as in-page dividers were left
  untouched.
- `2026-05-10` — **Phase 7.11 shipped**: every same-origin
  absolute URL in the archive converted to a relative path.
  **2,404 URLs rewritten across 321 files**
  (`_posts/*.markdown`, `about.md`, `public-speaking.md`).
  Two-pass regex sweep: the broad pass handled 2,399 URLs;
  a stricter second pass cleaned up 5 `[label](url)` edge
  cases where both halves were absolute hunterdavis.com
  URLs. The 16 bare-domain prose mentions ("…via
  http://www.hunterdavis.com.") were preserved as authored
  text. Each internal link now saves a DNS+TLS handshake on
  click and survives any future host change (e.g., 8.4's
  apex/www flip). The codebase is now portable: `_site/`
  could be served from any origin without rewriting bodies.
- `2026-05-10` — **Phase A.10 shipped**:
  `script/check_redirects.py`. Defensive verification tool
  that GETs every confirmed/high entry from
  `_data/legacy_redirects.yml` (164 after subpath-collision
  filter), follows 301/302s natively, parses meta-refresh
  stubs, and asserts the final URL hits the expected target.
  Manual post-deploy use today; CI integration tracked under
  8.3. `.gitignore` extended to cover `__pycache__/` /
  `*.pyc` / `.bundle/` / `vendor/` so future script
  invocations don't dirty the working tree.
- `2026-05-10` — **B.13 extension**: tagged the Dockstar
  saga with `project: dockstar`. **4 posts** spanning
  2010-11 → 2011-08: the flagship $25 gaming/emulation
  powerhouse (Hackaday-covered Nov 2010, Jan 2011),
  Home-Theater-Replacement deep-dive, "Fun with VNC"
  Dockstar Stereo tips, and Dockstar Stereo + Wii Frontend.
  Project tags now: zipit-z2 (19) · johnny-castaway (6) ·
  dockstar (4). Tangential Dockstar mentions in Retrode2,
  hosting-switch, location-based-ad, and the My Story page
  deliberately not tagged.
- `2026-05-10` — **Phase B.6 shipped**: human-readable site
  map at `/sitemap.html`. New `sitemap.md` (pure Liquid)
  lists Pages, latest 10 posts, posts grouped by project,
  posts grouped by year (with counts), and the three feed
  endpoints. New `_data/projects.yml` maps project slugs to
  display names ("Zipit Z2", "Johnny Castaway", "Dockstar")
  so the sitemap can show real titles instead of slugs.
  Footer now links to `Site Map` (and the existing XML
  sitemap link is relabeled `XML Sitemap` for clarity).
- `2026-05-10` — **Phase 2.6 + 2.7 shipped**: `/projects/`
  hub page. New `projects.md` permalinked to `/projects/`,
  groups `site.posts` by `project:` frontmatter value,
  humanizes via `_data/projects.yml`, lists each project's
  posts oldest-first (saga reading order). Footer extended
  to link to `/projects/`. 2.7's minimum schema (slug →
  display name) ships today; richer per-project metadata
  (hero image, dates, blurb, external links) is additive and
  can land per-project when 2.8's `_layouts/project.html`
  comes online.
- `2026-05-10` — **Phase 2.4 shipped**: `/archive/` index
  page. New `archive.md` permalinked to `/archive/` lists
  all 507 posts grouped by year via `group_by_exp`. Each
  year h2 has explicit `{#YYYY}` id so the post-page
  breadcrumb (B.7) can deep-link to it. The breadcrumb's
  year is now an actual `<a>` element pointing at
  `/archive/#{year}` — readers on a 2010 post can click
  "2010" and scroll-jump to that section. Footer extended
  with `Archive` link. Three browsing axes now live:
  chronological (Archive), thematic (Projects), structural
  (Site Map).
- `2026-05-10` — **Phase B.4 shipped**: top nav expanded
  from 3 to 5 items. `_includes/header.html` adds
  `Projects` (→ /projects/) and `Archive` (→ /archive/),
  both targeting pages shipped in 2.6 and 2.4. The user's
  authored "My Story" label is preserved verbatim — not
  renamed to "About". Writing and Now stay deferred until
  those pages are built.
- `2026-05-10` — **Phase B.9 shipped**: featured-posts
  strip on the home page. 11 historically important posts
  (sourced from Appendix A's dossier-confirmed milestones)
  tagged `featured: true` — IM-ME hack, Dockstar console,
  Sith Lord challenge, QuickGrapher, Source Tree Visualizer,
  70-app GitHub release, quarter-million downloads, Rhapsody/
  Ford CES, TUI000, Dunking Bird, plus the Zipit-Z2 Tor+
  Privoxy origin. With pre-existing "My Story" already
  featured, that's 12 total. Home page renders a `.featured`
  aside above the chronological list, only on
  `paginator.page == 1`. A reader's first impression of the
  home now leads with the greatest-hits, not just the most
  recent post.
- `2026-05-10` — **Phase 2.1 shipped (minimum scope)**:
  `_data/tags.yml` inventory of every tag value in post
  frontmatter. New `script/audit_tags.py` extracts 370
  distinct tags across 113 tagged posts (774 total tag
  applications) and writes the data file as a flat slug →
  count dict, descending by count. Foundation for Phase 2.2
  (tag pages), 2.3 (tag index), and B.18 (topic cloud) —
  all three need the data, even before canonical-form
  curation. Curation into canonical vocabulary tracked as
  new item 2.9.
- `2026-05-10` — **Phase 2.3 shipped**: `/tags/` alphabetical
  index page. Lists all 370 tags from `site.data.tags`, each
  a link to `/search.html?query=<tag>` so clicks work today
  via the existing free-text search (the dedicated per-tag
  pages from 2.2 are still pending the GH-Pages-vs-plugin
  question). Counts shown alongside each tag. Footer
  extended with `Tags` link. Pre-flight surfaced and fixed a
  YAML-typing bug — a tag literally named `2010` was being
  parsed as int — by switching `audit_tags.py` to always
  quote slugs in the emitted YAML.
- `2026-05-10` — **Phase B.8 shipped**: tag chips on post
  pages and home cards now activate as real `<a>` links to
  the same `/search.html?query=<tag>` URL the `/tags/` index
  uses. `_layouts/post.html` and `index.html` swap from
  decorative `<span>` to `<a class="tag-chip">`; CSS
  refactored from `.tags span` → `.tags .tag-chip` with
  added hover/focus state (inverts to filled #0B5485). Tag
  chips were the last decorative-non-link element on the
  archive — now every tag mention anywhere on the site is
  one click from a search of that tag.
- `2026-05-10` — **Phase B.18 shipped**: topic-cloud sidebar
  widget. Home-page sidebar (`_includes/sidebar.html`) gains
  a `.topic-cloud` panel rendering the top 30 most-used tags
  as chip-style links to `/search.html?query=<tag>`, plus an
  "All tags →" link to `/tags/`. Same chip palette as B.8's
  in-post tag chips for visual continuity. Side cleanup: the
  pre-existing absolute `http://www.hunterdavis.com/feed.xml`
  RSS link in the same sidebar (which 7.11's post-body sweep
  didn't reach because it's in an include) was made relative.
- `2026-05-10` — **B.13 extension**: tagged the IM-ME saga
  with `project: im-me`. **2 posts** — the 2009-11-15
  "Hacking the GirlTech IM-ME USB Wireless Device" flagship
  (Hackaday-covered, "Pink Wireless Terminal of Wonder")
  and the 2010-02-01 IM-ME Linux Drivers beta-release
  follow-up. `_data/projects.yml` extended with `im-me:
  IM-ME` display mapping; `/projects/` now lists 4
  projects, the post-page aside fires on both IM-ME posts
  with the other one as its single sibling. The 6 other
  posts that mention "IM-ME" — Hackaway-prize threads,
  Dockstar parenthetical, My Story — deliberately not
  tagged.
