#!/usr/bin/env python3
"""
Seed _data/legacy_redirects.yml from the audit CSV plus a small
hand-curated dossier of third-party-confirmed mappings.

Phase A.5 scope: WordPress numeric IDs only. The slug, category, and
about-slug categories are emitted as empty arrays here; Phase A.6
will extend this script to populate them from the audit CSV's
high-confidence rows.

Inputs:
    _meta/legacy_url_inventory.csv     -- output of audit_legacy_urls.py

Output:
    _data/legacy_redirects.yml          -- consumed by Phase A.7

Usage:
    python3 script/seed_legacy_redirects.py

Safe to re-run: regenerates the file from inputs every time.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INPUT_CSV = REPO_ROOT / "_meta" / "legacy_url_inventory.csv"
OUTPUT_YML = REPO_ROOT / "_data" / "legacy_redirects.yml"

# ---------------------------------------------------------------------------
# Hand-curated mappings sourced from the research dossier
# (_meta/SITE_IMPROVEMENT_IDEAS.md, Appendix A). These take precedence
# over the audit CSV's machine-generated suggestions whenever both
# cover the same legacy URL.
DOSSIER_CONFIRMED = {
    # /archives/<id>
    "archives": {
        843: {
            "to": "/2010/11/28/a-25-gamingemulation-powerhouse-using-the-dockstar-as-a-gaming-console.html",
            "source": "dossier-hackaday-2011-01-02",
            "confidence": "confirmed",
        },
        1640: {
            "to": "/2011/06/27/so-thats-30-am-i-a-software-jedi-now-maybe-a-software-sith-lord.html",
            "source": "dossier-hn-2703378",
            "confidence": "confirmed",
        },
        201: {
            # 2009-09-25 "With Zipit, Who Needs A Netbook?" Hackaday article
            # links here; no current Jekyll post is an obvious target match.
            # Tracked for archive.org recovery in A.11.
            "to": "",
            "source": "dossier-hackaday-2009-09-25",
            "confidence": "needs-wayback",
        },
    },
    # /?p=<id>
    "wp_query_ids": {
        # (none yet — 3163 is filled in by the audit's slug match below)
    },
}

# CSV category buckets that fold into each YAML key
SLUG_CATEGORIES = frozenset({
    "wp_slug_android_app",
    "wp_slug_android_game",
    "wp_slug_android_apps_nested",
    "wp_slug_popular_oss",
    "wp_slug_post",
    "wp_slug_personal_finance",
    "wp_slug_books",
})
CATEGORY_CATEGORIES = frozenset({"wp_category", "wp_archives_category"})
ABOUT_CATEGORIES = frozenset({"wp_slug_about"})


def load_csv_rows(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            rows.append(r)
    return rows


def collect_archives(rows):
    """Collect /archives/<id> IDs, dedup, apply dossier overrides."""
    seen = {}
    for r in rows:
        if r["category"] != "archives_id":
            continue
        m = re.match(r"^/archives/(\d+)", r["url"])
        if not m:
            continue
        nid = int(m.group(1))
        if nid in seen:
            continue
        seen[nid] = {
            "to": r["suggested_to"] or "",
            "source": "in-repo-cross-reference",
            "confidence": "needs-wayback" if not r["suggested_to"] else r["confidence"],
        }
    # Apply dossier overrides
    for nid, override in DOSSIER_CONFIRMED.get("archives", {}).items():
        seen[nid] = override
    return [{"id": nid, **seen[nid]} for nid in sorted(seen)]


def _collect_by_url(rows, allowed_categories):
    """Generic collector: dedup by URL, take any row's suggested_to and
    confidence (they're identical across rows for the same URL)."""
    seen = {}
    for r in rows:
        if r["category"] not in allowed_categories:
            continue
        url = r["url"]
        if url in seen:
            continue
        seen[url] = {
            "to": r["suggested_to"] or "",
            "source": "audit-slug-match" if r["suggested_to"] else "in-repo-cross-reference",
            "confidence": r["confidence"] if r["suggested_to"] else "needs-wayback",
        }
    return [{"from": u, **seen[u]} for u in sorted(seen)]


def collect_wp_slugs(rows):
    return _collect_by_url(rows, SLUG_CATEGORIES)


def collect_wp_categories(rows):
    return _collect_by_url(rows, CATEGORY_CATEGORIES)


def collect_about_slugs(rows):
    return _collect_by_url(rows, ABOUT_CATEGORIES)


def collect_wp_query_ids(rows):
    """Collect /?p=<id> bases. For each ID, prefer the highest-confidence
    variant (e.g., /?p=3163/android-sound/#a6 carries a slug we matched)."""
    by_id = defaultdict(list)
    for r in rows:
        if r["category"] != "wp_query_id":
            continue
        m = re.search(r"/\?p=(\d+)", r["url"])
        if not m:
            continue
        by_id[int(m.group(1))].append(r)

    rank = {"high": 4, "medium": 3, "low": 2, "mirror": 1, "none": 0}

    out = {}
    for nid, variants in by_id.items():
        best = max(variants, key=lambda r: rank.get(r["confidence"], 0))
        if best["suggested_to"]:
            out[nid] = {
                "to": best["suggested_to"],
                "source": "audit-slug-match",
                "confidence": best["confidence"],
            }
        else:
            out[nid] = {
                "to": "",
                "source": "in-repo-cross-reference",
                "confidence": "needs-wayback",
            }
    # Apply dossier overrides if any
    for nid, override in DOSSIER_CONFIRMED.get("wp_query_ids", {}).items():
        out[nid] = override
    return [{"id": nid, **out[nid]} for nid in sorted(out)]


# ---------------------------------------------------------------------------
# YAML emission — write by hand to keep the output stable, comment-rich,
# and indistinguishable from a hand-curated file. (Avoiding pyyaml's
# default formatting since this file gets diffed and human-reviewed.)


HEADER = """\
# Single source of truth for legacy-URL → current-Jekyll-URL redirects.
# Consumed by Phase A.7 (jekyll-redirect-from frontmatter generator).
#
# Schema (all sub-keys are arrays of objects):
#   archives:       old /archives/<id>       → new
#   wp_query_ids:   old /?p=<id>             → new
#   wp_slugs:       old /<wp-slug>/          → new   (populated by A.6)
#   wp_categories:  old /category/<slug>/    → new   (populated by A.6)
#   about_slugs:    old /about/<slug>/       → new   (populated by A.6)
#
# Each entry has:
#   id (or from), to, source, confidence
#
# Confidence levels:
#   confirmed       third-party source verified the mapping (Hackaday,
#                   Engadget, the research dossier, etc.)
#   high            audit's slug match between legacy URL and Jekyll post
#                   is exact
#   medium / low    partial / token-overlap slug match
#   needs-wayback   target unknown; recovery via web.archive.org is
#                   tracked in Phase A.11
#
# To regenerate this file:
#   python3 script/seed_legacy_redirects.py
#
# Last regenerated: 2026-05-10
"""


def emit_yaml(archives_entries, wp_query_entries, wp_slug_entries,
              wp_cat_entries, about_slug_entries) -> str:
    lines = [HEADER, ""]

    def emit_section(name, entries, key="id"):
        if not entries:
            lines.append(f"{name}: []")
            lines.append("")
            return
        lines.append(f"{name}:")
        for e in entries:
            lines.append(f"  - {key}: {e[key]}")
            to = e["to"]
            # Quote empty strings explicitly so YAML doesn't turn them into null
            if to == "":
                lines.append(f"    to: \"\"")
            else:
                lines.append(f"    to: {to}")
            lines.append(f"    source: {e['source']}")
            lines.append(f"    confidence: {e['confidence']}")
        lines.append("")

    emit_section("archives", archives_entries, key="id")
    emit_section("wp_query_ids", wp_query_entries, key="id")
    emit_section("wp_slugs", wp_slug_entries, key="from")
    emit_section("wp_categories", wp_cat_entries, key="from")
    emit_section("about_slugs", about_slug_entries, key="from")

    return "\n".join(lines)


def _summarize(label, entries):
    by_conf = {}
    for e in entries:
        by_conf[e["confidence"]] = by_conf.get(e["confidence"], 0) + 1
    parts = ", ".join(f"{c}={n}" for c, n in sorted(by_conf.items()))
    print(f"  {label:14s} {len(entries):4d}  ({parts})")


def main() -> int:
    if not INPUT_CSV.exists():
        print(f"missing input: {INPUT_CSV}", file=sys.stderr)
        return 2

    rows = load_csv_rows(INPUT_CSV)
    archives = collect_archives(rows)
    wp_ids = collect_wp_query_ids(rows)
    wp_slugs = collect_wp_slugs(rows)
    wp_cats = collect_wp_categories(rows)
    about_slugs = collect_about_slugs(rows)

    yaml_text = emit_yaml(archives, wp_ids, wp_slugs, wp_cats, about_slugs)

    OUTPUT_YML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_YML.write_text(yaml_text, encoding="utf-8")

    print(f"wrote {OUTPUT_YML.relative_to(REPO_ROOT)}")
    _summarize("archives", archives)
    _summarize("wp_query_ids", wp_ids)
    _summarize("wp_slugs", wp_slugs)
    _summarize("wp_categories", wp_cats)
    _summarize("about_slugs", about_slugs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
