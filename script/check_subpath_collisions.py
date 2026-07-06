#!/usr/bin/env python3
"""
Fail fast if any top-level file or directory in this Jekyll source
tree would collide with a sibling-repo path that GitHub Pages
publishes under the same hostname.

Background:
  hunterdavis.com is served by the GitHub Pages user-site repo
  (huntergdavis/huntergdavis.github.io). Any other public repo under
  huntergdavis/ that has Pages enabled is auto-published at
  hunterdavis.com/<repo-name>/. If this Jekyll site ever emitted a
  top-level path with the same name, the project deploy and the
  user-page deploy would collide unpredictably.

  _data/projects_subpaths.yml is the canonical list of reserved
  names (135 repos as of last refresh). This script reads that list
  and the source tree, and reports any case-insensitive collision.

Exit codes:
  0  no collisions; safe to commit / build
  1  one or more collisions found; build should fail

Intended use:
  - manual: `python3 script/check_subpath_collisions.py`
  - git pre-commit hook: add a one-liner that runs this and
    aborts the commit on non-zero
  - CI: invoke before `bundle exec jekyll build`
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.stderr.write("PyYAML required (pip install pyyaml).\n")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
SUBPATHS_YML = REPO_ROOT / "_data" / "projects_subpaths.yml"
CONFIG_YML = REPO_ROOT / "_config.yml"

# Jekyll's own special directories. Their names are reserved by
# the build system and never published as top-level paths.
JEKYLL_DIRS = {
    "_config.yml",
    "_data",
    "_drafts",
    "_includes",
    "_layouts",
    "_plugins",
    "_posts",
    "_sass",
    "_site",
    "_meta",  # local convention: planning doc + audit data
}


def load_reserved_names() -> set[str]:
    if not SUBPATHS_YML.exists():
        sys.stderr.write(f"missing {SUBPATHS_YML.relative_to(REPO_ROOT)}\n")
        sys.exit(2)
    data = yaml.safe_load(SUBPATHS_YML.read_text(encoding="utf-8")) or {}
    return {str(name).lower() for name in data.get("reserved", []) if name}


def load_excluded() -> set[str]:
    """Names listed in _config.yml's `exclude:` array."""
    if not CONFIG_YML.exists():
        return set()
    data = yaml.safe_load(CONFIG_YML.read_text(encoding="utf-8")) or {}
    excluded = data.get("exclude", []) or []
    if isinstance(excluded, str):
        excluded = [excluded]
    return {str(name).lower().rstrip("/") for name in excluded}


def top_level_entries() -> list[str]:
    """Names of every file and directory at the repo root that
    Jekyll would otherwise publish as a top-level path."""
    out = []
    for p in REPO_ROOT.iterdir():
        name = p.name
        # Skip Jekyll-special dirs (handled by the build) and dotfiles
        if name in JEKYLL_DIRS or name.startswith("."):
            continue
        # Skip Gemfile / Gemfile.lock / *.lock — never published
        if name in {"Gemfile", "Gemfile.lock"}:
            continue
        out.append(name)
    return out


def main() -> int:
    reserved = load_reserved_names()
    excluded = load_excluded()
    collisions = []

    for entry in sorted(top_level_entries()):
        if entry.lower() in excluded:
            continue
        if entry.lower() in reserved:
            collisions.append(entry)

    if collisions:
        print("Subpath collisions detected:", file=sys.stderr)
        for c in collisions:
            print(f"  /{c}  collides with sibling-repo subpath of the same name", file=sys.stderr)
        print("", file=sys.stderr)
        print("Fix one of:", file=sys.stderr)
        print("  - rename the file/directory in this repo", file=sys.stderr)
        print("  - add it to _config.yml's `exclude:` list", file=sys.stderr)
        print("  - rename the sibling repo (and update _data/projects_subpaths.yml)", file=sys.stderr)
        return 1

    print(f"OK: no collisions. {len(reserved)} reserved names, {len(top_level_entries())} top-level entries checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
