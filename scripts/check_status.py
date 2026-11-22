#!/usr/bin/env python3
"""Refresh last_commit, archived and license fields in data/entries.yaml from the GitHub API.

Runs weekly in CI. Needs a token in GITHUB_TOKEN (the default Actions token works).
Repos that 404 are reported and left unchanged so a maintainer can review them.

Usage:
    GITHUB_TOKEN=... python scripts/check_status.py
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "entries.yaml"
API = "https://api.github.com"


def gh(path: str, token: str | None) -> dict | None:
    req = urllib.request.Request(f"{API}{path}", headers={"Accept": "application/vnd.github+json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def last_commit_date(repo: str, branch: str, token: str | None) -> str | None:
    commit = gh(f"/repos/{repo}/commits/{branch}", token)
    if not commit:
        return None
    return commit["commit"]["committer"]["date"][:10]


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("warning: GITHUB_TOKEN not set; you will hit the 60 requests/hour limit", file=sys.stderr)

    yaml = YAML()  # round-trip mode keeps comments and ordering
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=4, offset=2)
    data = yaml.load(DATA.read_text(encoding="utf-8"))

    cache: dict[str, dict | None] = {}
    missing, changed = [], 0
    for e in data["entries"]:
        repo = e["repo"]
        if repo not in cache:
            meta = gh(f"/repos/{repo}", token)
            if meta is not None:
                meta["_last_commit"] = last_commit_date(repo, meta["default_branch"], token)
            cache[repo] = meta
        meta = cache[repo]
        if meta is None:
            missing.append(f"{e['name']} ({repo})")
            continue

        # GitHub follows renames; record the new name so links stay correct
        if meta["full_name"].lower() != repo.lower():
            print(f"renamed: {repo} -> {meta['full_name']}")
            e["repo"] = meta["full_name"]
            changed += 1

        new_date = meta["_last_commit"] or meta["pushed_at"][:10]
        if str(e.get("last_commit")) != new_date:
            e["last_commit"] = dt.date.fromisoformat(new_date)  # stays an unquoted YAML date
            changed += 1

        archived = bool(meta.get("archived"))
        if archived != bool(e.get("archived", False)):
            e["archived"] = archived
            changed += 1
            if archived:
                print(f"archived: {e['name']} ({repo})")

        spdx = (meta.get("license") or {}).get("spdx_id")
        if spdx and spdx != "NOASSERTION" and not str(e.get("license", "")).startswith(spdx):
            print(f"license differs for {e['name']}: yaml={e.get('license')!r} github={spdx!r} (not changed)")

    with DATA.open("w", encoding="utf-8") as fh:
        yaml.dump(data, fh)

    print(f"{changed} field(s) updated.")
    if missing:
        print("Not found (removed, private or renamed without redirect):\n  " + "\n  ".join(missing))
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
