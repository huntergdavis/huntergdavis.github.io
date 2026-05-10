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
- [ ] **A.6** Map the WordPress slug long tail. From the CSV
      produced by A.2, every `/android-app-*`, `/android-game-*`,
      `/android-apps/<cat>/<slug>/`, `/popular-open-source-projects/*`,
      `/category/*`, and `/about/<slug>/` URL is slug-matched
      against the current `_posts/*.markdown` corpus. Auto-suggest
      a target Jekyll URL for each; human reviews; result merges
      into `_data/legacy_redirects.yml`. Aim to resolve **>90% of
      the 285-URL audit set** automatically. **L**
- [ ] **A.7** Emit redirect stubs for every entry in
      `_data/legacy_redirects.yml`. Two flavours, pick one:
      - **(a) Custom plugin** `_plugins/legacy_redirects.rb`:
        iterates the data file, emits a static stub at every
        `from`/`id` URL with `<meta http-equiv="refresh">` +
        `<link rel="canonical">`. Cleanest, requires CI build
        (Phase 8.3) since stock GitHub Pages disables custom
        `_plugins/`.
      - **(b) Frontmatter generator** `script/expand_redirects.py`:
        a one-shot script that reads `_data/legacy_redirects.yml`
        and adds a `redirect_from:` array to each Jekyll target
        post. Works on stock GH Pages today via
        `jekyll-redirect-from` (A.4). More frontmatter sprawl,
        but immediate. **M**
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
- [ ] **A.10** `script/check_redirects.py` — bootstrap with a
      curated list of canonical historical URLs (Hackaday-linked
      posts, the `/archives/NNN` IDs, the home, `/about.html`,
      `/feed.xml`, `/sitemap.xml`). Asserts 200 or refresh→200
      against a target host. Use `--host=http://localhost:4000`
      locally, `--host=https://hunterdavis.com` in CI. Extend to
      cover every entry in `_data/legacy_redirects.yml` once A.7
      is in place. **M**
- [ ] **A.11** Recover anything still unmapped from `archive.org`.
      `script/scrape_wayback_legacy_urls.py` walks
      `web.archive.org/web/*/hunterdavis.com/*`, extracts
      `(url, title, date)` tuples for any URL not already in
      `_data/legacy_redirects.yml`, best-matches each to a Jekyll
      post slug, output to CSV for human review. **L**
- [ ] **A.12** Smart 404 enhancement. When the requested path
      starts with `/archives/`, `/category/`, `/android-app-`,
      `/android-game-`, `/?p=`, or `/about/`, the page extracts
      the slug from `window.location.pathname`, runs a prefilled
      lunr search over the post index, and presents likely
      matches. Catches anything the explicit redirects miss
      (especially URLs only linked from third-party sites we
      can't enumerate). **S**
- [ ] **A.13** Build-fail subpath-collision check. Add
      `script/check_subpath_collisions.py` (callable from a git
      pre-commit hook AND from Phase 8.3 CI). It loads
      `_data/projects_subpaths.yml`, lists every top-level file
      and directory in the source tree (excluding `_`-prefixed
      Jekyll dirs and the entries already in `_config.yml`'s
      `exclude:`), and exits non-zero if any path collides
      case-insensitively with a `reserved:` name. **S**
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

### Phase 0 — Hygiene & broken-asset fixes
*Goal: stop shipping bugs. Each item is independently shippable.
URL preservation work moved to Phase A above.*

- [ ] **0.1** Add `favicon.png` (and `favicon.svg`, 32×32 PNG fallback) at
      repo root. **S** · *Why:* every page references it and 404s today.
- [ ] **0.2** Add `sharer.png` (default 1200×630 OG image) at repo root.
      **S** · *Why:* every shared link 404s its preview image.
- [ ] **0.3** Switch `_config.yml` `url` and `base_url` to
      `https://www.hunterdavis.com`. Update `robots.txt` / `sitemap.xml`
      / `feed.xml` to use `site.url` consistently. **S**
- [ ] **0.4** Collapse `site.url` and `site.base_url` to a single key
      and fix all references in `_includes/ssn.html`, `feed.xml`,
      `sitemap.xml`, `robots.txt`. **S**
- [ ] **0.5** Fix empty `<img src="" width=600 />` on the home list:
      only render the image element when `post.image` is non-empty.
      Edit `index.html`. **S**
- [ ] **0.6** Add `loading="lazy"` and `decoding="async"` to home and
      post-list image renders. **S**
- [ ] **0.7** Remove the `{{ post.featured_img }}` line entirely from
      `index.html` (the recent dunking-bird fix proved it's redundant).
      **S**
- [ ] **0.8** Delete `_includes/disqus.html` — unused, references a
      `site.disqus` value that's commented out. **S**
- [ ] **0.9** Delete `_includes/jquery-1.4.4.min.js`,
      `jquery-ui-1.8.9.custom.min.js`, `modernizr-1.6.min.js`,
      `obfs_embed.js`, `deck.js`, `simulator.js` from `_includes/` if
      not actually consumed by the live site (verify each is only
      referenced by legacy embed pages on hunterdavis.com paths).
      **S** · *Acceptance:* `grep -r` shows no live references.
- [ ] **0.10** Drop the maxcdn font-awesome `<link>` from
      `_layouts/default.html`; replace the 4–5 used icons with inline
      SVG in `_includes/icons/*.svg`. **M** · *Why:* removes a CDN
      dependency and ~30 KB.
- [ ] **0.11** Drop the dead Twitter/Facebook share buttons from
      `_layouts/post.html` (Twitter share UX is broken on X anyway).
      Replace with a single "Copy link" button. **S**
- [ ] **0.12** Delete `index.old` (it's a Jekyll comment-only stub). **S**
- [ ] **0.13** Replace `_includes/analytics.html` with a privacy-respecting
      analytics snippet (Plausible / GoatCounter / self-hosted) only if
      `site.analytics_url` is set. Otherwise remove the include
      altogether. **S**
- [ ] **0.14** Add `<main>` landmark and a visually-hidden
      "Skip to content" link in `_layouts/default.html`. **S**
- [ ] **0.15** Set explicit `width` and `height` on home-list images
      (use a default ratio like 1200×630 if unknown) to eliminate CLS.
      **S**

### Phase 1 — Performance quick wins
*Goal: kill the obvious perf cliffs without touching design yet.*

- [ ] **1.1** Replace `search.md` inline JSON dump with a
      `search.json` data file built by Liquid, fetched async by
      `js/search.js`. **M** · *Acceptance:* `_site/search.html`
      drops below 50 KB; first paint of search is sub-200 ms on 4G.
- [ ] **1.2** Trim the search corpus: index `title`, `date`, `tags`,
      `excerpt` only — not full content. Keep full-content search as a
      progressive enhancement loaded after the first keystroke. **M**
- [ ] **1.3** Self-host the Vollkorn font subset (latin only,
      400/700 + italics) with `font-display: swap`. **M** · *Why:*
      drops Google Fonts dependency + speeds first paint.
- [ ] **1.4** Trim `feed.xml` to title + excerpt + link; add
      `feed-full.xml` for full-content readers. **S**
- [ ] **1.5** Remove unused SCSS partials (`_buttons.scss` already
      commented; audit `_anims.scss`, `_monokai.scss`, parts of
      `_markdown.scss`). **S**
- [ ] **1.6** Replace the `headroom.min.js` shrinking-header on
      scroll with CSS `position: sticky` (no JS required). **S**
- [ ] **1.7** Add `<link rel="preload">` for the hero image and
      self-hosted font on the home and post pages. **S**
- [ ] **1.8** Inline critical above-the-fold CSS in `<head>` and
      defer the rest with `media="print" onload`. **M**
- [ ] **1.9** Add a build-time HTML minifier (jekyll-compress-html
      layout include or `jekyll-minifier`). **S**

### Phase 2 — Information architecture scaffolding
*Goal: surfaces exist (even if empty), so subsequent commits can
populate.*

- [ ] **2.1** Create `_data/tags.yml` with the controlled vocabulary
      defined under "Tag taxonomy" above. **M**
- [ ] **2.2** Add a `_plugins/tag_pages.rb` generator (or use
      `jekyll-archives`) to emit `/tag/<slug>/index.html` per tag,
      with paginated post lists. **M** · *Note:* GitHub Pages disallows
      custom plugins on the default builder — confirm whether deploy
      uses GH Actions / Netlify / custom CI before assuming plugins
      are OK.
- [ ] **2.3** Build `/tag/index.html` — alphabetical list of tags
      with post counts and family grouping. **S**
- [ ] **2.4** Build `/archive/index.html` — year list + month grid +
      recent-25 strip. **M**
- [ ] **2.5** Build per-year `/archive/<year>/` archives. **M**
      (auto-generated; no manual content).
- [ ] **2.6** Build `/projects/index.html` — hub of cards, one per
      project family. Initial cards reference inline content; project
      pages are stubbed. **M**
- [ ] **2.7** Add `_data/projects.yml` listing each project with
      `slug, name, family, tags, hero_image, dates, blurb,
      external_links`. **M**
- [ ] **2.8** Add `_layouts/project.html` for project landing pages —
      renders project metadata, "Posts" list filtered by tag/slug, and
      external links. **S**

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
- [ ] **5.9** Remove `text-align: justify` site-wide. **S**
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
- [ ] **7.1** Add JSON-LD `Article` schema to post layout and
      `Person` schema on home. **S**
- [ ] **7.2** Compute reading-time at build (kramdown word count /
      225 wpm) and surface in post header + home cards. **S**
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
- [ ] **7.10** Convert `<a id='...'>foo</a>` anchors throughout
      `about.md` and `public-speaking.md` to real heading IDs. **S**
      (becomes mostly moot after 7.7/7.8.)
- [ ] **7.11** Sweep posts for `http://hunterdavis.com/...` self-links
      and rewrite to relative URLs. **M**
- [ ] **7.12** Sweep posts for `<iframe ... src="http://...">` and
      upgrade YouTube embeds to `https://www.youtube-nocookie.com/`
      (privacy-friendly + works in modern browsers). **S**
- [ ] **7.13** Add 404 page upgrade with site-map and search.
      (Smart-routing extensions for legacy paths handled in A.12.) **S**

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
