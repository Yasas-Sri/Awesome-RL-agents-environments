# Contributing

Thanks for helping! This list stays useful by being **selective** and **accurate**, so please read this first.

## What belongs here

An entry must be one of:

1. **An environment:** something that gives an LLM agent tasks, takes its actions and returns a reward. It must be **multi-turn or interactive**, *or* a procedural generator of verifiable tasks built for RL (like Reasoning Gym).
2. **An environment framework or trainer** (the "Plugging in" sections). These are kept short on purpose. Only add one that's widely used or that integrates with environments listed here.

And it must:

- be open source, with a license file;
- have a README that shows how to run it;
- define a reward or success check (tests, state checks or a documented judge);
- have a commit in the **last 12 months**, for new additions. Older entries stay listed but are marked 🔴 Stale automatically.

**Not accepted:** single-turn Q&A datasets, classic non-LLM RL environments (Atari, MuJoCo; use [Gymnasium](https://github.com/Farama-Foundation/Gymnasium)), closed-source products, papers without code, and your own project unless it clearly meets the bar above. Self-submissions are fine, just say so in the PR.

## How to add an entry

1. Edit **`data/entries.yaml` only.** `README.md` is generated, so don't edit it by hand.
2. Add your entry under the right section:

```yaml
  - name: MyEnv
    repo: owner/repo
    section: tools            # coding | web | computer | tools | reasoning | games | social | suites | frameworks | trainers
    desc: One sentence in your own words, what it is.
    use_when: One short "use this when…" line.
    interface: gym            # gym | http | mcp | harness | library
    reward: verifiable        # verifiable | judge | mixed
    multi_turn: true
    runs_on: laptop           # laptop | docker | vm | cloud
    use: both                 # train | eval | both
    license: MIT
    last_commit: 2026-11-01   # any recent date; CI corrects it weekly
```

3. Regenerate and check:

```bash
pip install ruamel.yaml
python scripts/build_readme.py
```

4. Open a PR. CI fails if the YAML is invalid or the README wasn't regenerated.

## How to choose the tricky fields

- **`use`**
  - `train`: it ships training tasks or generates them.
  - `eval`: it's a benchmark. Pick this if the authors present it as a benchmark and there's no separate training split, even if people *do* train on it.
  - `both`: it has documented separate train and test splits, or procedural generation with held-out seeds.
- **`runs_on`** is what you need to run the *environment* (not to train a model):
  - `laptop`: plain Python, CPU is fine
  - `docker`: one or more containers
  - `vm`: full virtual machines or a mobile emulator
  - `cloud`: needs a GPU or cloud sandboxes in practice
- **`reward`**: `verifiable` if code decides success, `judge` if an LLM scores it, `mixed` for both.

If you're unsure, say so in the PR and a maintainer will help.

## Corrections

Found a wrong field, a dead project or a broken link? Open an issue or a PR against `data/entries.yaml`. Corrections are the most valuable contributions here.
