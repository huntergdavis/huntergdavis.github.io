#!/usr/bin/env python3
"""Audit which `_data/projects_subpaths.yml` entries actually serve
content at hunterdavis.com/<name>/.

The list is the set of every sibling repo under github.com/huntergdavis/
that *could* publish to /<name>/ via GitHub Pages. Not every repo
actually has Pages enabled, so we HEAD-check each path and classify:
  - LIVE      : 200 from the project subdomain
  - REDIRECT  : 301/302 — common when Pages serves the apex via a
                redirect; record the target
  - DEAD      : 404 — repo exists but Pages is off (or 404 page)
  - ERROR     : timeout / DNS / TLS / etc.

Writes a markdown report at _meta/projects_subpaths_audit.md.

Usage:
    python3 script/audit_subpaths.py [--workers N]
"""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("PyYAML required.")

REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "_data" / "projects_subpaths.yml"
OUT = REPO / "_meta" / "projects_subpaths_audit.md"
BASE = "https://hunterdavis.com"
TIMEOUT = 8


def head(url: str) -> tuple[int | None, str | None, str | None]:
    """Return (status, location_header, error_kind)."""
    req = urllib.request.Request(url, method="HEAD")
    req.add_header("User-Agent", "huntergdavis-audit/1.0")
    try:
        opener = urllib.request.build_opener(
            urllib.request.HTTPRedirectHandler  # follow redirects, capture final
        )
        # We want to *see* redirects, not follow blindly. Custom handler:
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, *a, **kw):  # type: ignore
                return None

        opener = urllib.request.build_opener(NoRedirect)
        with opener.open(req, timeout=TIMEOUT) as r:
            return (r.status, r.headers.get("Location"), None)
    except urllib.error.HTTPError as e:
        return (e.code, e.headers.get("Location") if e.headers else None, None)
    except Exception as e:
        return (None, None, f"{type(e).__name__}: {e}")


def classify(status: int | None, location: str | None) -> str:
    if status is None:
        return "ERROR"
    if 200 <= status < 300:
        return "LIVE"
    if 300 <= status < 400:
        return "REDIRECT"
    if status == 404:
        return "DEAD"
    return f"OTHER-{status}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()

    data = yaml.safe_load(DATA.read_text(encoding="utf-8")) or {}
    names = data.get("reserved_subpaths") or data.get("subpaths") or []
    # Be flexible: top-level key might just be the list, or a dict.
    if isinstance(data, list):
        names = data
    if not names:
        # Try alternate parsing: file is a list literal under no key
        # or a top-level YAML list — try the raw text.
        raw = DATA.read_text(encoding="utf-8")
        names = []
        for line in raw.splitlines():
            line = line.strip()
            if line.startswith("- "):
                names.append(line[2:].strip())
    names = [n for n in names if n and not n.startswith("#")]
    print(f"Auditing {len(names)} subpaths against {BASE}/", file=sys.stderr)

    results: dict[str, tuple[int | None, str | None, str | None]] = {}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(head, f"{BASE}/{n}/"): n for n in names}
        for fut in as_completed(futs):
            n = futs[fut]
            results[n] = fut.result()

    buckets: dict[str, list[tuple[str, int | None, str | None]]] = {}
    for n in sorted(names, key=str.lower):
        status, location, err = results[n]
        cat = classify(status, location)
        buckets.setdefault(cat, []).append((n, status, location or err))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines: list[str] = [
        "# `projects_subpaths.yml` live-subset audit",
        "",
        f"_Generated: {now} via `script/audit_subpaths.py`._",
        "",
        f"Total reserved subpaths: **{len(names)}**.",
        "",
        "## Summary",
        "",
        "| Category | Count |",
        "|---|---|",
    ]
    order = ["LIVE", "REDIRECT", "DEAD", "ERROR"]
    seen = set()
    for cat in order:
        n = len(buckets.get(cat, []))
        lines.append(f"| {cat} | {n} |")
        seen.add(cat)
    for cat in sorted(buckets):
        if cat in seen:
            continue
        lines.append(f"| {cat} | {len(buckets[cat])} |")
    lines.append("")

    for cat in order + sorted(b for b in buckets if b not in seen):
        items = buckets.get(cat) or []
        if not items:
            continue
        lines.append(f"## {cat} ({len(items)})")
        lines.append("")
        for name, status, extra in items:
            bits = [f"`{name}`"]
            if status is not None:
                bits.append(f"`{status}`")
            if extra:
                bits.append(str(extra))
            lines.append("- " + " · ".join(bits))
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(REPO)}")
    for cat in order:
        print(f"  {cat}: {len(buckets.get(cat, []))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
