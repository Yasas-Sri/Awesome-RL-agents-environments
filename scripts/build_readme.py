#!/usr/bin/env python3
"""Generate README.md from data/entries.yaml and templates/README.template.md.

Usage:
    python scripts/build_readme.py           # write README.md
    python scripts/build_readme.py --check   # exit 1 if README.md is out of date
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "entries.yaml"
TEMPLATE = ROOT / "templates" / "README.template.md"
README = ROOT / "README.md"

ENV_SECTIONS = ["coding", "web", "computer", "tools", "reasoning", "games", "social", "suites"]
PLUG_SECTIONS = ["frameworks", "trainers"]

ALLOWED = {
    "interface": {"gym", "http", "mcp", "harness", "library"},
    "reward": {"verifiable", "judge", "mixed"},
    "runs_on": {"laptop", "docker", "vm", "cloud"},
    "use": {"train", "eval", "both"},
}
REQUIRED = ["name", "repo", "section", "desc", "use_when", "license", "last_commit"]
ENV_REQUIRED = ["interface", "reward", "multi_turn", "runs_on", "use"]

USE_LABEL = {"train": "🏋️ Train", "eval": "📏 Eval", "both": "🏋️ + 📏"}
RUNS_LABEL = {"laptop": "💻 Laptop", "docker": "🐳 Docker", "vm": "🖥️ VM / emulator", "cloud": "☁️ GPU / cloud"}
REWARD_LABEL = {"verifiable": "✅ Verifiable", "judge": "⚖️ LLM judge", "mixed": "Mixed"}


def status(entry: dict, today: dt.date) -> str:
    if entry.get("archived"):
        return "⚫ Archived"
    last = entry["last_commit"]
    if isinstance(last, str):
        last = dt.date.fromisoformat(last)
    age = (today - last).days
    if age <= 180:
        return "🟢 Active"
    if age <= 365:
        return "🟡 Quiet"
    return "🔴 Stale"


def validate(data: dict) -> list[str]:
    errors = []
    sections = data["sections"]
    seen = set()
    for i, e in enumerate(data["entries"]):
        label = e.get("name", f"entry #{i}")
        for f in REQUIRED:
            if f not in e:
                errors.append(f"{label}: missing '{f}'")
        if e.get("section") not in sections:
            errors.append(f"{label}: unknown section '{e.get('section')}'")
        key = (e.get("repo"), e.get("section"))
        if key in seen:
            errors.append(f"{label}: duplicate repo in the same section")
        seen.add(key)
        if e.get("section") in ENV_SECTIONS:
            for f in ENV_REQUIRED:
                if f not in e:
                    errors.append(f"{label}: missing '{f}'")
            for f, allowed in ALLOWED.items():
                if f in e and e[f] not in allowed:
                    errors.append(f"{label}: '{f}' must be one of {sorted(allowed)}")
    return errors


def name_cell(e: dict) -> str:
    repo = e["repo"]
    stars = f"![stars](https://img.shields.io/github/stars/{repo}?style=flat-square&label=%E2%98%85)"
    return f"[{e['name']}](https://github.com/{repo})<br>{stars}"


def env_table(entries: list[dict], today: dt.date) -> str:
    rows = [
        "| Name | What it is · *use when* | Use | Runs on | Multi-turn | Reward | License | Status |",
        "|---|---|---|---|:---:|---|---|---|",
    ]
    for e in sorted(entries, key=lambda x: x["name"].lower()):
        rows.append(
            f"| {name_cell(e)} | {e['desc']}<br>*{e['use_when']}* | {USE_LABEL[e['use']]} "
            f"| {RUNS_LABEL[e['runs_on']]} | {'✓' if e['multi_turn'] else '—'} "
            f"| {REWARD_LABEL[e['reward']]} | {e['license']} | {status(e, today)} |"
        )
    return "\n".join(rows)


def plug_table(entries: list[dict], today: dt.date) -> str:
    rows = [
        "| Name | What it is · *use when* | License | Status |",
        "|---|---|---|---|",
    ]
    for e in sorted(entries, key=lambda x: x["name"].lower()):
        rows.append(
            f"| {name_cell(e)} | {e['desc']}<br>*{e['use_when']}* | {e['license']} | {status(e, today)} |"
        )
    return "\n".join(rows)


def anchor(title: str) -> str:
    keep = "".join(c for c in title.lower() if c.isalnum() or c in " -")
    return keep.strip().replace(" ", "-")


def render(data: dict, today: dt.date) -> str:
    sections = data["sections"]
    by_section: dict[str, list[dict]] = {}
    for e in data["entries"]:
        by_section.setdefault(e["section"], []).append(e)

    env_parts, toc_env = [], []
    for key in ENV_SECTIONS:
        if key not in by_section:
            continue
        title = sections[key]
        toc_env.append(f"  - [{title}](#{anchor(title)})")
        env_parts.append(f"### {title}\n\n{env_table(by_section[key], today)}")

    plug_parts, toc_plug = [], []
    for key in PLUG_SECTIONS:
        if key not in by_section:
            continue
        title = sections[key]
        toc_plug.append(f"  - [{title}](#{anchor(title)})")
        plug_parts.append(f"### {title}\n\n{plug_table(by_section[key], today)}")

    n_env = sum(len(by_section.get(k, [])) for k in ENV_SECTIONS)
    template = TEMPLATE.read_text(encoding="utf-8")
    return (
        template.replace("{{TOC_ENVIRONMENTS}}", "\n".join(toc_env))
        .replace("{{TOC_PLUGGING}}", "\n".join(toc_plug))
        .replace("{{ENVIRONMENTS}}", "\n\n".join(env_parts))
        .replace("{{PLUGGING}}", "\n\n".join(plug_parts))
        .replace("{{ENV_COUNT}}", str(n_env))
        .replace("{{UPDATED}}", today.isoformat())
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if README.md is stale")
    parser.add_argument("--today", help="override today's date (YYYY-MM-DD), for reproducible builds")
    args = parser.parse_args()

    data = YAML(typ="safe").load(DATA.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        print("entries.yaml has problems:\n  " + "\n  ".join(errors), file=sys.stderr)
        return 1

    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    current = README.read_text(encoding="utf-8") if README.exists() else ""
    if args.check and not args.today:
        # Rebuild as of the date the README was generated, so status badges
        # ageing by a few days never fails an unrelated PR.
        m = re.search(r"Last generated (\d{4}-\d{2}-\d{2})", current)
        if m:
            today = dt.date.fromisoformat(m.group(1))
    out = render(data, today)

    if args.check:
        # ignore the date line so the check doesn't fail just because a day passed
        strip = lambda s: "\n".join(l for l in s.splitlines() if not l.startswith("<sub>Last generated"))
        if strip(current) != strip(out):
            print("README.md is out of date. Run: python scripts/build_readme.py", file=sys.stderr)
            return 1
        print("README.md is up to date.")
        return 0

    README.write_text(out, encoding="utf-8")
    print(f"Wrote {README.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
