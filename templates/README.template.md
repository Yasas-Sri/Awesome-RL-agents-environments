# Awesome Agent RL Environments [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated, checked list of **environments for training and evaluating LLM agents with reinforcement learning**, covering coding, web, computer use, tool use, games and more.

Most "awesome agent" lists give you a name and a link. This one tells you what you actually need before you pick an environment:

- **Train or eval?** Many popular "environments" are really benchmarks. Training on them contaminates your results.
- **Runs on:** can you try it on a laptop, or does it need Docker, VMs or a GPU cluster?
- **Reward:** checked by code (verifiable) or by an LLM judge?
- **Status:** updated weekly from GitHub, so you can see what's still maintained.

{{ENV_COUNT}} environments so far. Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Contents

- [Which environment should I use?](#which-environment-should-i-use)
- [Environments](#environments)
{{TOC_ENVIRONMENTS}}
- [Plugging environments into training](#plugging-environments-into-training)
{{TOC_PLUGGING}}
- [Learn](#learn)
- [Related lists](#related-lists)
- [Legend](#legend)

## Which environment should I use?

| I want to… | Train on | Evaluate on | Trainer to try |
|---|---|---|---|
| Learn agent RL on a laptop or free Colab | [TextArena](https://github.com/TextArena/TextArena), [Reasoning Gym](https://github.com/open-thought/reasoning-gym) | the same envs at harder settings | [Unsloth](https://github.com/unslothai/unsloth), [TRL](https://github.com/huggingface/trl) |
| Train a software-engineering agent | [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym), [R2E-Gym](https://github.com/R2E-Gym/R2E-Gym) | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | [SkyRL](https://github.com/skyrl-project/SkyRL) |
| Make tasks from my own repo | [SWE-smith](https://github.com/SWE-bench/SWE-smith) | held-out tasks from the same repo | [SkyRL](https://github.com/skyrl-project/SkyRL) |
| Build a tool-calling / API agent | [AppWorld](https://github.com/StonyBrookNLP/appworld) | [τ²-bench](https://github.com/sierra-research/tau2-bench), [BFCL](https://github.com/ShishirPatil/gorilla) | [verl](https://github.com/verl-project/verl), [ART](https://github.com/OpenPipe/ART) |
| Test agents on real MCP servers | — | [MCPMark](https://github.com/eval-sys/mcpmark), [MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe) | — |
| Build a web agent | [BrowserGym](https://github.com/ServiceNow/BrowserGym) (MiniWoB), [WebShop](https://github.com/princeton-nlp/WebShop) | [WebArena](https://github.com/web-arena-x/webarena) | [verl](https://github.com/verl-project/verl) |
| Build a mobile agent | [AndroidWorld](https://github.com/google-research/android_world) | [AndroidWorld](https://github.com/google-research/android_world) (held-out params) | — |
| Try self-play or social skills | [TextArena](https://github.com/TextArena/TextArena) + [SPIRAL](https://github.com/spiral-rl/spiral), [Sotopia](https://github.com/sotopia-lab/sotopia) | [Sotopia](https://github.com/sotopia-lab/sotopia) | — |
| Publish my own environment | [OpenEnv](https://github.com/openenv/OpenEnv) or [verifiers](https://github.com/PrimeIntellect-ai/verifiers) | — | — |

## Environments

{{ENVIRONMENTS}}

## Plugging environments into training

An **environment** gives the agent tasks and rewards. A **trainer** updates the model's weights from those rewards. **Environment frameworks** are the standard formats that let any environment plug into any trainer. Only a short selection is listed here. See [Related lists](#related-lists) for fuller catalogs.

{{PLUGGING}}

## Learn

- [Environment Scaling for Interactive Agentic Experience Collection: A Survey](https://arxiv.org/abs/2511.09586) — a map of how agent environments are built, scaled and used for RL.
- [OpenEnv environment catalog](https://huggingface.co/docs/openenv/environments) — browse ready-to-run environments on Hugging Face.
- [Prime Intellect Environments Hub](https://app.primeintellect.ai/dashboard/environments) — community environments built with verifiers.

## Related lists

- [AgentsMeetRL](https://github.com/thinkwee/AgentsMeetRL) — table of open-source repos for training LLM agents with RL (trainer-focused).
- [Awesome Environment Scaling](https://github.com/lukahhcm/Awesome_Environment_Scaling) — paper list that goes with the survey above.
- [Awesome AI Sandboxes](https://github.com/tizkovatereza/awesome-ai-sandboxes) — cloud sandboxes for running agent rollouts.
- [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) — the standard API for classic (non-LLM) RL environments.

## Legend

| Column | Values |
|---|---|
| Use | 🏋️ Train: has training tasks or generates them · 📏 Eval: benchmark, don't train on it · 🏋️ + 📏: separate train and test splits |
| Runs on | 💻 Laptop: CPU is fine · 🐳 Docker: containers per task · 🖥️ VM / emulator · ☁️ GPU / cloud: needs serious compute or cloud sandboxes |
| Reward | ✅ Verifiable: checked by code (tests, state) · ⚖️ LLM judge · Mixed |
| Status | 🟢 Active: commit in the last 6 months · 🟡 Quiet: 6–12 months · 🔴 Stale: over 12 months · ⚫ Archived |

"Runs on" means running the *environment*. Training a model on it usually needs a GPU no matter what.

---

<sub>Last generated {{UPDATED}} from [`data/entries.yaml`](data/entries.yaml). Edit the YAML, not this file.</sub>
