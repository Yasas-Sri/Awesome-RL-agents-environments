# Awesome Agent RL Environments [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated, checked list of **environments for training and evaluating LLM agents with reinforcement learning**, covering coding, web, computer use, tool use, games and more.

Most "awesome agent" lists give you a name and a link. This one tells you what you actually need before you pick an environment:

- **Train or eval?** Many popular "environments" are really benchmarks. Training on them contaminates your results.
- **Runs on:** can you try it on a laptop, or does it need Docker, VMs or a GPU cluster?
- **Reward:** checked by code (verifiable) or by an LLM judge?
- **Status:** updated weekly from GitHub, so you can see what's still maintained.

32 environments so far. Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Contents

- [Which environment should I use?](#which-environment-should-i-use)
- [Environments](#environments)
  - [Coding & software engineering](#coding--software-engineering)
  - [Web & browser](#web--browser)
  - [Computer use (desktop & mobile)](#computer-use-desktop--mobile)
  - [Tool use & MCP](#tool-use--mcp)
  - [Verifiable reasoning](#verifiable-reasoning)
  - [Games & text worlds](#games--text-worlds)
  - [Social & multi-agent](#social--multi-agent)
  - [Multi-domain suites](#multi-domain-suites)
- [Plugging environments into training](#plugging-environments-into-training)
  - [Environment frameworks](#environment-frameworks)
  - [Trainers](#trainers)
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

### Coding & software engineering

| Name | What it is · *use when* | Use | Runs on | Multi-turn | Reward | License | Status |
|---|---|---|---|:---:|---|---|---|
| [Harbor](https://github.com/harbor-framework/harbor)<br>![stars](https://img.shields.io/github/stars/harbor-framework/harbor?style=flat-square&label=%E2%98%85) | Framework for running agents on container tasks at scale; the official harness for Terminal-Bench 2.0 and can generate RL rollouts.<br>*You want terminal-style tasks run in parallel on cloud sandboxes.* | 🏋️ + 📏 | 🐳 Docker | ✓ | ✅ Verifiable | Apache-2.0 | 🟢 Active |
| [MLE-bench](https://github.com/openai/mle-bench)<br>![stars](https://img.shields.io/github/stars/openai/mle-bench?style=flat-square&label=%E2%98%85) | 75 Kaggle competitions for testing end-to-end ML engineering agents.<br>*You're evaluating agents that train models, not just write code.* | 📏 Eval | ☁️ GPU / cloud | ✓ | ✅ Verifiable | MIT | 🟡 Quiet |
| [R2E-Gym](https://github.com/R2E-Gym/R2E-Gym)<br>![stars](https://img.shields.io/github/stars/R2E-Gym/R2E-Gym?style=flat-square&label=%E2%98%85) | 8.1K procedurally curated SWE problems across 13 repos, with unit-test rewards built in.<br>*You need more SWE training tasks than SWE-Gym provides.* | 🏋️ Train | 🐳 Docker | ✓ | ✅ Verifiable | Apache-2.0 | 🔴 Stale |
| [SWE-bench](https://github.com/SWE-bench/SWE-bench)<br>![stars](https://img.shields.io/github/stars/SWE-bench/SWE-bench?style=flat-square&label=%E2%98%85) | The standard benchmark of real GitHub issues resolved by passing the repo's tests.<br>*You need the number everyone else reports. Never train on it.* | 📏 Eval | 🐳 Docker | ✓ | ✅ Verifiable | MIT | 🟢 Active |
| [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym)<br>![stars](https://img.shields.io/github/stars/SWE-Gym/SWE-Gym?style=flat-square&label=%E2%98%85) | 2.4K real GitHub tasks from 11 Python repos, each with an executable environment and tests.<br>*You want to RL-train a SWE agent on real issues, not synthetic ones.* | 🏋️ Train | 🐳 Docker | ✓ | ✅ Verifiable | Apache-2.0 | 🟢 Active |
| [SWE-smith](https://github.com/SWE-bench/SWE-smith)<br>![stars](https://img.shields.io/github/stars/SWE-bench/SWE-smith?style=flat-square&label=%E2%98%85) | Toolkit that turns any Python repo into an unlimited supply of bug-fixing tasks with execution environments.<br>*You want training tasks from your own codebase or a repo nobody has covered yet.* | 🏋️ Train | 🐳 Docker | ✓ | ✅ Verifiable | MIT | 🟡 Quiet |
| [Terminal-Bench](https://github.com/harbor-framework/terminal-bench-1)<br>![stars](https://img.shields.io/github/stars/harbor-framework/terminal-bench-1?style=flat-square&label=%E2%98%85) | Benchmark of hard command-line tasks in sandboxed terminals (v1; v2 runs through Harbor).<br>*You want to measure an agent's real shell skills.* | 📏 Eval | 🐳 Docker | ✓ | ✅ Verifiable | Apache-2.0 | 🟢 Active |

### Web & browser

| Name | What it is · *use when* | Use | Runs on | Multi-turn | Reward | License | Status |
|---|---|---|---|:---:|---|---|---|
| [BrowserGym](https://github.com/ServiceNow/BrowserGym)<br>![stars](https://img.shields.io/github/stars/ServiceNow/BrowserGym?style=flat-square&label=%E2%98%85) | Gym interface that wraps MiniWoB, WorkArena, WebArena and others behind one browser API.<br>*You want one interface for many web environments; MiniWoB tasks run on a laptop.* | 🏋️ + 📏 | 🐳 Docker | ✓ | ✅ Verifiable | Apache-2.0 | 🟢 Active |
| [VisualWebArena](https://github.com/web-arena-x/visualwebarena)<br>![stars](https://img.shields.io/github/stars/web-arena-x/visualwebarena?style=flat-square&label=%E2%98%85) | WebArena extension where tasks need visual understanding of the page.<br>*You're evaluating multimodal web agents.* | 📏 Eval | 🐳 Docker | ✓ | ✅ Verifiable | MIT | 🔴 Stale |
| [WebArena](https://github.com/web-arena-x/webarena)<br>![stars](https://img.shields.io/github/stars/web-arena-x/webarena?style=flat-square&label=%E2%98%85) | Self-hosted realistic websites (shopping, forums, GitLab, CMS) with functional task checks.<br>*You need the standard realistic web-agent benchmark.* | 📏 Eval | 🐳 Docker | ✓ | ✅ Verifiable | Apache-2.0 | 🟡 Quiet |
| [WebShop](https://github.com/princeton-nlp/WebShop)<br>![stars](https://img.shields.io/github/stars/princeton-nlp/WebShop?style=flat-square&label=%E2%98%85) | Simulated e-commerce site with 1.18M products and 12,087 crowd-sourced shopping instructions.<br>*You want a cheap, classic web-navigation environment with a training set.* | 🏋️ + 📏 | 💻 Laptop | ✓ | ✅ Verifiable | MIT | 🔴 Stale |

### Computer use (desktop & mobile)

| Name | What it is · *use when* | Use | Runs on | Multi-turn | Reward | License | Status |
|---|---|---|---|:---:|---|---|---|
| [AndroidWorld](https://github.com/google-research/android_world)<br>![stars](https://img.shields.io/github/stars/google-research/android_world?style=flat-square&label=%E2%98%85) | 116 parameterized tasks across 20 Android apps, instantiated dynamically on an emulator.<br>*You're training or testing mobile agents; parameterized tasks give you many variants.* | 🏋️ + 📏 | 🖥️ VM / emulator | ✓ | ✅ Verifiable | Apache-2.0 | 🟢 Active |
| [OSWorld](https://github.com/xlang-ai/OSWorld)<br>![stars](https://img.shields.io/github/stars/xlang-ai/OSWorld?style=flat-square&label=%E2%98%85) | Real desktop OS tasks running in virtual machines, checked by execution-based scripts.<br>*You're building full computer-use agents.* | 📏 Eval | 🖥️ VM / emulator | ✓ | ✅ Verifiable | Apache-2.0 | 🟢 Active |
| [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena)<br>![stars](https://img.shields.io/github/stars/microsoft/WindowsAgentArena?style=flat-square&label=%E2%98%85) | Windows-OS tasks across real apps, run in a VM.<br>*Your agent needs to work on Windows specifically.* | 📏 Eval | 🖥️ VM / emulator | ✓ | ✅ Verifiable | MIT | 🟢 Active |

### Tool use & MCP

| Name | What it is · *use when* | Use | Runs on | Multi-turn | Reward | License | Status |
|---|---|---|---|:---:|---|---|---|
| [AppWorld](https://github.com/StonyBrookNLP/appworld)<br>![stars](https://img.shields.io/github/stars/StonyBrookNLP/appworld?style=flat-square&label=%E2%98%85) | Simulated world of 9 everyday apps and 457 APIs, with train/dev splits and parallel worlds for RL rollouts.<br>*You want rich, stateful API tasks that run fully offline.* | 🏋️ + 📏 | 💻 Laptop | ✓ | ✅ Verifiable | Apache-2.0 | 🟢 Active |
| [BFCL](https://github.com/ShishirPatil/gorilla)<br>![stars](https://img.shields.io/github/stars/ShishirPatil/gorilla?style=flat-square&label=%E2%98%85) | Berkeley Function Calling Leaderboard — function-calling accuracy including multi-turn categories.<br>*You want a quick check on raw function-calling ability.* | 📏 Eval | 💻 Laptop | ✓ | ✅ Verifiable | Apache-2.0 | 🟡 Quiet |
| [MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)<br>![stars](https://img.shields.io/github/stars/SalesforceAIResearch/MCP-Universe?style=flat-square&label=%E2%98%85) | Long-horizon tasks against real MCP servers; can also run MCPMark tasks.<br>*You're evaluating agents on actual MCP servers, not mocks.* | 📏 Eval | ☁️ GPU / cloud | ✓ | ✅ Verifiable | Apache-2.0 | 🟢 Active |
| [MCPMark](https://github.com/eval-sys/mcpmark)<br>![stars](https://img.shields.io/github/stars/eval-sys/mcpmark?style=flat-square&label=%E2%98%85) | Verified tasks on real MCP tools (Notion, GitHub, filesystem, Postgres, Playwright) in isolated sandboxes.<br>*You want reproducible MCP evals with strict verifiers, including easy tasks for small models.* | 📏 Eval | 🐳 Docker | ✓ | ✅ Verifiable | Apache-2.0 | 🟢 Active |
| [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox)<br>![stars](https://img.shields.io/github/stars/apple-aiml-research/ToolSandbox?style=flat-square&label=%E2%98%85) | Stateful, conversational tool-use benchmark with a simulated user.<br>*You want to test how tools change state over a conversation.* | 📏 Eval | 💻 Laptop | ✓ | ✅ Verifiable | Apple (custom) | 🟢 Active |
| [τ-bench](https://github.com/sierra-research/tau-bench)<br>![stars](https://img.shields.io/github/stars/sierra-research/tau-bench?style=flat-square&label=%E2%98%85) | The original tool-agent-user benchmark (retail and airline); succeeded by τ²-bench.<br>*You need comparability with older papers.* | 📏 Eval | 💻 Laptop | ✓ | ✅ Verifiable | MIT | 🟡 Quiet |
| [τ²-bench](https://github.com/sierra-research/tau2-bench)<br>![stars](https://img.shields.io/github/stars/sierra-research/tau2-bench?style=flat-square&label=%E2%98%85) | Customer-service domains where an agent and a simulated user both act on shared state; adds multilingual and voice tracks.<br>*You care about multi-turn tool use with a human in the loop.* | 📏 Eval | 💻 Laptop | ✓ | ✅ Verifiable | MIT | 🟢 Active |

### Verifiable reasoning

| Name | What it is · *use when* | Use | Runs on | Multi-turn | Reward | License | Status |
|---|---|---|---|:---:|---|---|---|
| [Reasoning Gym](https://github.com/open-thought/reasoning-gym)<br>![stars](https://img.shields.io/github/stars/open-thought/reasoning-gym?style=flat-square&label=%E2%98%85) | 100+ procedural generators of verifiable reasoning tasks (algebra, logic, graphs, games) with adjustable difficulty.<br>*You want unlimited RLVR data with a curriculum; works directly with verifiers.* | 🏋️ Train | 💻 Laptop | — | ✅ Verifiable | Apache-2.0 | 🟢 Active |

### Games & text worlds

| Name | What it is · *use when* | Use | Runs on | Multi-turn | Reward | License | Status |
|---|---|---|---|:---:|---|---|---|
| [ALFWorld](https://github.com/alfworld/alfworld)<br>![stars](https://img.shields.io/github/stars/alfworld/alfworld?style=flat-square&label=%E2%98%85) | Text household tasks aligned with the embodied ALFRED dataset.<br>*You want a classic agent env that most RL-for-agents papers report.* | 🏋️ + 📏 | 💻 Laptop | ✓ | ✅ Verifiable | MIT | 🟡 Quiet |
| [BALROG](https://github.com/balrog-ai/BALROG)<br>![stars](https://img.shields.io/github/stars/balrog-ai/BALROG?style=flat-square&label=%E2%98%85) | Benchmark of long-horizon game environments for LLM and VLM agents, with a public leaderboard.<br>*You want to test long-horizon planning cheaply.* | 📏 Eval | 💻 Laptop | ✓ | ✅ Verifiable | MIT | 🟡 Quiet |
| [NLE](https://github.com/NetHack-LE/nle)<br>![stars](https://img.shields.io/github/stars/NetHack-LE/nle?style=flat-square&label=%E2%98%85) | The NetHack Learning Environment — a very hard, procedurally generated roguelike.<br>*You want an environment no current agent comes close to solving.* | 🏋️ + 📏 | 💻 Laptop | ✓ | ✅ Verifiable | NetHack GPL | 🟢 Active |
| [ScienceWorld](https://github.com/allenai/ScienceWorld)<br>![stars](https://img.shields.io/github/stars/allenai/ScienceWorld?style=flat-square&label=%E2%98%85) | Text simulator of grade-school science experiments.<br>*You want multi-step procedural tasks with partial credit.* | 🏋️ + 📏 | 💻 Laptop | ✓ | ✅ Verifiable | Apache-2.0 | 🟢 Active |
| [TextArena](https://github.com/TextArena/TextArena)<br>![stars](https://img.shields.io/github/stars/TextArena/TextArena?style=flat-square&label=%E2%98%85) | 100+ single-, two- and multi-player text games behind a Gym-style interface.<br>*You want cheap multi-turn environments or self-play.* | 🏋️ + 📏 | 💻 Laptop | ✓ | ✅ Verifiable | MIT | 🟢 Active |
| [TextWorld](https://github.com/microsoft/TextWorld)<br>![stars](https://img.shields.io/github/stars/microsoft/TextWorld?style=flat-square&label=%E2%98%85) | Generator and sandbox for text adventure games, built for RL agents.<br>*You want to generate your own text-game curriculum.* | 🏋️ Train | 💻 Laptop | ✓ | ✅ Verifiable | MIT | 🟢 Active |

### Social & multi-agent

| Name | What it is · *use when* | Use | Runs on | Multi-turn | Reward | License | Status |
|---|---|---|---|:---:|---|---|---|
| [Sotopia](https://github.com/sotopia-lab/sotopia)<br>![stars](https://img.shields.io/github/stars/sotopia-lab/sotopia?style=flat-square&label=%E2%98%85) | Open-ended social scenarios where agents interact and are scored on social goals.<br>*You're training or testing social and negotiation skills.* | 🏋️ + 📏 | 💻 Laptop | ✓ | ⚖️ LLM judge | MIT | 🟡 Quiet |
| [SPIRAL](https://github.com/spiral-rl/spiral)<br>![stars](https://img.shields.io/github/stars/spiral-rl/spiral?style=flat-square&label=%E2%98%85) | Recipe for multi-agent, multi-turn self-play RL on zero-sum games built on TextArena.<br>*You want a working self-play setup instead of building one.* | 🏋️ Train | ☁️ GPU / cloud | ✓ | ✅ Verifiable | MIT | 🟡 Quiet |

### Multi-domain suites

| Name | What it is · *use when* | Use | Runs on | Multi-turn | Reward | License | Status |
|---|---|---|---|:---:|---|---|---|
| [AgentBench](https://github.com/THUDM/AgentBench)<br>![stars](https://img.shields.io/github/stars/THUDM/AgentBench?style=flat-square&label=%E2%98%85) | Eight environments including OS, database, knowledge graph and card game tasks.<br>*You want a broad agent eval across very different domains.* | 📏 Eval | 🐳 Docker | ✓ | ✅ Verifiable | Apache-2.0 | 🟡 Quiet |
| [AgentGym](https://github.com/WooooDyy/AgentGym)<br>![stars](https://img.shields.io/github/stars/WooooDyy/AgentGym?style=flat-square&label=%E2%98%85) | Many agent environments (web, embodied, games and more) served behind one HTTP interface.<br>*You want to train across many domains with one client.* | 🏋️ + 📏 | 🐳 Docker | ✓ | ✅ Verifiable | MIT | 🟢 Active |

## Plugging environments into training

An **environment** gives the agent tasks and rewards. A **trainer** updates the model's weights from those rewards. **Environment frameworks** are the standard formats that let any environment plug into any trainer. Only a short selection is listed here. See [Related lists](#related-lists) for fuller catalogs.

### Environment frameworks

| Name | What it is · *use when* | License | Status |
|---|---|---|---|
| [AgentGym-RL](https://github.com/WooooDyy/AgentGym-RL)<br>![stars](https://img.shields.io/github/stars/WooooDyy/AgentGym-RL?style=flat-square&label=%E2%98%85) | Multi-turn RL framework on top of AgentGym's environments.<br>*You want to train on AgentGym environments end to end.* | MIT | 🟡 Quiet |
| [GEM](https://github.com/axon-rl/gem)<br>![stars](https://img.shields.io/github/stars/axon-rl/gem?style=flat-square&label=%E2%98%85) | A Gym for agentic LLMs: a standard interface plus a bundle of ready-made environments, including MCP tasks.<br>*You want a Gym-like API that feels familiar from classic RL.* | Apache-2.0 | 🟡 Quiet |
| [OpenEnv](https://github.com/openenv/OpenEnv)<br>![stars](https://img.shields.io/github/stars/openenv/OpenEnv?style=flat-square&label=%E2%98%85) | Gymnasium-style spec where each environment is a Docker image; catalog of 40+ environments on Hugging Face.<br>*You're publishing an environment and want others to use it easily.* | BSD-3-Clause | 🟢 Active |
| [SkyRL-Gym](https://github.com/skyrl-project/SkyRL)<br>![stars](https://img.shields.io/github/stars/skyrl-project/SkyRL?style=flat-square&label=%E2%98%85) | Gymnasium-API library of math, coding, search and SQL tool-use environments, shipped inside SkyRL.<br>*You're already training with SkyRL.* | Apache-2.0 | 🟢 Active |
| [verifiers](https://github.com/PrimeIntellect-ai/verifiers)<br>![stars](https://img.shields.io/github/stars/PrimeIntellect-ai/verifiers?style=flat-square&label=%E2%98%85) | Library for writing environments for training and evaluating LLMs, tied to the Environments Hub and prime-rl.<br>*You want to write a small environment in Python and share it.* | MIT | 🟢 Active |

### Trainers

| Name | What it is · *use when* | License | Status |
|---|---|---|---|
| [ART](https://github.com/OpenPipe/ART)<br>![stars](https://img.shields.io/github/stars/OpenPipe/ART?style=flat-square&label=%E2%98%85) | Agent Reinforcement Trainer for multi-step agents, with Colab notebooks.<br>*You want to RL-train an existing agent loop with little glue code.* | Apache-2.0 | 🟢 Active |
| [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)<br>![stars](https://img.shields.io/github/stars/OpenRLHF/OpenRLHF?style=flat-square&label=%E2%98%85) | Ray-based RLHF and RL framework.<br>*You already run Ray clusters.* | Apache-2.0 | 🟢 Active |
| [rLLM](https://github.com/rllm-org/rllm)<br>![stars](https://img.shields.io/github/stars/rllm-org/rllm?style=flat-square&label=%E2%98%85) | Framework for post-training language agents with RL.<br>*You want agent-first abstractions on top of a scalable backend.* | Apache-2.0 | 🟢 Active |
| [SkyRL](https://github.com/skyrl-project/SkyRL)<br>![stars](https://img.shields.io/github/stars/skyrl-project/SkyRL?style=flat-square&label=%E2%98%85) | Modular full-stack RL library for long-horizon agents; used in SWE-Gym and SWE-smith recipes.<br>*You're training SWE agents.* | Apache-2.0 | 🟢 Active |
| [slime](https://github.com/THUDM/slime)<br>![stars](https://img.shields.io/github/stars/THUDM/slime?style=flat-square&label=%E2%98%85) | Large-scale RL framework used to train the GLM model family.<br>*You're doing frontier-scale RL.* | Apache-2.0 | 🟢 Active |
| [TRL](https://github.com/huggingface/trl)<br>![stars](https://img.shields.io/github/stars/huggingface/trl?style=flat-square&label=%E2%98%85) | Hugging Face post-training library with GRPOTrainer and an async variant.<br>*You want the most documented path to GRPO.* | Apache-2.0 | 🟢 Active |
| [Unsloth](https://github.com/unslothai/unsloth)<br>![stars](https://img.shields.io/github/stars/unslothai/unsloth?style=flat-square&label=%E2%98%85) | Memory-efficient fine-tuning, including GRPO, aimed at single consumer GPUs and Colab.<br>*You're on free or limited compute.* | Apache-2.0 (core) | 🟢 Active |
| [verl](https://github.com/verl-project/verl)<br>![stars](https://img.shields.io/github/stars/verl-project/verl?style=flat-square&label=%E2%98%85) | Widely used scalable RL post-training framework with multi-turn agent support.<br>*You're scaling past a single GPU.* | Apache-2.0 | 🟢 Active |

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

<sub>Last generated 2026-11-22 from [`data/entries.yaml`](data/entries.yaml). Edit the YAML, not this file.</sub>
