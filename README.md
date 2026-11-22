# Awesome RL Agent Environments [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of environments, gyms and benchmarks for training and evaluating reinforcement learning agents — from classic control and games to LLM agents that browse, code and use computers.

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

## Contents

- [LLM & Agentic RL Environments](#llm--agentic-rl-environments)
  - [Environment Frameworks & Hubs](#environment-frameworks--hubs)
  - [Web & Browser](#web--browser)
  - [Computer & Mobile Use](#computer--mobile-use)
  - [Software Engineering & Coding](#software-engineering--coding)
  - [Tool Use & Reasoning](#tool-use--reasoning)
  - [Text Games](#text-games)
- [Classic RL Environments](#classic-rl-environments)
  - [Standard APIs & Suites](#standard-apis--suites)
  - [Games](#games)
  - [Open-Ended & Procedural](#open-ended--procedural)
  - [JAX / GPU-Accelerated](#jax--gpu-accelerated)
  - [Multi-Agent](#multi-agent)
  - [Robotics & Physics](#robotics--physics)
  - [Embodied & 3D](#embodied--3d)
  - [Autonomous Driving](#autonomous-driving)
  - [Offline RL Datasets](#offline-rl-datasets)
  - [Safety & Multi-Objective](#safety--multi-objective)
  - [Real-World Domains](#real-world-domains)
- [Training Frameworks](#training-frameworks)
  - [LLM Agent RL](#llm-agent-rl)
  - [Classic RL](#classic-rl)
- [Related Lists](#related-lists)

---

## LLM & Agentic RL Environments

### Environment Frameworks & Hubs

- [OpenEnv](https://github.com/openenv/OpenEnv) - Gym-style spec and hub for isolated, containerized agentic RL environments.
- [verifiers](https://github.com/PrimeIntellect-ai/verifiers) - Library for building RL environments and verifiable rewards for LLMs.
- [Prime Intellect Environments Hub](https://app.primeintellect.ai/dashboard/environments) - Community hub of open RL environments built on `verifiers`.
- [Atropos](https://github.com/NousResearch/atropos) - Nous Research's framework for collecting and scoring LLM rollouts across many environments (archived).
- [GEM](https://github.com/axon-rl/gem) - General Experience Maker: Gym-like environment suite for agentic LLMs.
- [AgentGym](https://github.com/WooooDyy/AgentGym) - Unified interface over many agent environments for training and evaluating LLM agents.
- [RAGEN](https://github.com/mll-lab-nu/RAGEN) - Multi-turn RL for LLM agents with a modular set of environments.

### Web & Browser

- [WebArena](https://github.com/web-arena-x/webarena) - Realistic self-hosted websites for autonomous web agents.
- [VisualWebArena](https://github.com/web-arena-x/visualwebarena) - Multimodal extension of WebArena with visually grounded tasks.
- [BrowserGym](https://github.com/ServiceNow/BrowserGym) - Gym environment for web agents, unifying many web benchmarks.
- [WorkArena](https://github.com/ServiceNow/WorkArena) - Enterprise knowledge-work tasks on the ServiceNow platform.
- [MiniWoB++](https://github.com/Farama-Foundation/MiniWoB-plusplus) - 100+ small web interaction tasks.
- [WebShop](https://github.com/princeton-nlp/WebShop) - Simulated e-commerce site with natural language shopping instructions.

### Computer & Mobile Use

- [OSWorld](https://github.com/xlang-ai/OSWorld) - Real desktop OS tasks across Ubuntu, Windows and macOS.
- [AndroidWorld](https://github.com/google-research/android_world) - Dynamic Android environment with reward signals for 100+ tasks.
- [AndroidEnv](https://github.com/google-deepmind/android_env) - RL platform for controlling an Android emulator.

### Software Engineering & Coding

- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Resolve real GitHub issues in Python repositories.
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) - Training environment of real-world software engineering tasks.
- [R2E-Gym](https://github.com/R2E-Gym/R2E-Gym) - Procedurally curated executable environments for SWE agents.
- [SWE-smith](https://github.com/SWE-bench/SWE-smith) - Generate SWE training tasks at scale for any repository.
- [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) - Hard tasks for agents operating in a terminal.
- [InterCode](https://github.com/princeton-nlp/intercode) - Interactive coding with execution feedback (Bash, SQL, Python).

### Tool Use & Reasoning

- [τ-bench](https://github.com/sierra-research/tau-bench) - Tool-agent-user interaction in customer service domains.
- [τ²-bench](https://github.com/sierra-research/tau2-bench) - Dual-control successor to τ-bench.
- [AppWorld](https://github.com/StonyBrookNLP/appworld) - Simulated world of apps and APIs for coding agents.
- [AgentBench](https://github.com/THUDM/AgentBench) - Multi-environment benchmark for LLMs as agents.
- [Reasoning Gym](https://github.com/open-thought/reasoning-gym) - Procedurally generated reasoning tasks with verifiable rewards.

### Text Games

- [TextArena](https://github.com/TextArena/TextArena) - Collection of single- and multi-player text-based games for LLMs.
- [BALROG](https://github.com/balrog-ai/BALROG) - Benchmark of agentic LLM/VLM reasoning on games.
- [TextWorld](https://github.com/microsoft/TextWorld) - Generate and play text-based adventure games.
- [Jericho](https://github.com/microsoft/jericho) - Learning environment for classic interactive fiction games.
- [ALFWorld](https://github.com/alfworld/alfworld) - Text-based household tasks aligned with embodied ALFRED.
- [ScienceWorld](https://github.com/allenai/ScienceWorld) - Text-based environment for elementary science experiments.

## Classic RL Environments

### Standard APIs & Suites

- [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) - The standard single-agent RL API (maintained fork of OpenAI Gym).
- [DeepMind Control Suite](https://github.com/google-deepmind/dm_control) - Continuous control tasks built on MuJoCo.
- [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents) - Turn Unity games and simulations into RL environments.
- [EnvPool](https://github.com/sail-sg/envpool) - Highly parallel C++ execution engine for Gym/DM environments.

### Games

- [Arcade Learning Environment](https://github.com/Farama-Foundation/Arcade-Learning-Environment) - Atari 2600 games for RL.
- [Stable-Retro](https://github.com/Farama-Foundation/Stable-Retro) - Retro console games as RL environments.
- [ViZDoom](https://github.com/Farama-Foundation/ViZDoom) - Doom-based visual RL platform.
- [OpenSpiel](https://github.com/google-deepmind/open_spiel) - Huge collection of games and algorithms for RL and game theory.
- [NetHack Learning Environment](https://github.com/NetHack-LE/nle) - The roguelike NetHack as an RL environment.
- [MiniHack](https://github.com/NetHack-LE/minihack) - Sandbox for designing custom tasks on top of NLE.

### Open-Ended & Procedural

- [Procgen](https://github.com/openai/procgen) - 16 procedurally generated games for measuring generalization.
- [MiniGrid](https://github.com/Farama-Foundation/Minigrid) - Simple, fast gridworlds including BabyAI.
- [Crafter](https://github.com/danijar/crafter) - 2D Minecraft-like benchmark for general agent abilities.
- [MineRL](https://github.com/minerllabs/minerl) - Minecraft environments and human demonstration datasets.
- [MineDojo](https://github.com/MineDojo/MineDojo) - Open-ended Minecraft framework with thousands of tasks.

### JAX / GPU-Accelerated

- [Brax](https://github.com/google/brax) - Massively parallel rigid-body physics in JAX.
- [MuJoCo Playground](https://github.com/google-deepmind/mujoco_playground) - GPU-accelerated MuJoCo environments for robot learning.
- [Gymnax](https://github.com/RobertTLange/gymnax) - Classic Gym environments rewritten in JAX.
- [Jumanji](https://github.com/instadeepai/jumanji) - JAX combinatorial and industry-inspired environments.
- [Craftax](https://github.com/MichaelTMatthews/Craftax) - JAX rewrite and extension of Crafter and NetHack-style mechanics.
- [XLand-MiniGrid](https://github.com/dunnolab/xland-minigrid) - JAX meta-RL gridworlds with millions of unique tasks.
- [Kinetix](https://github.com/FLAIROx/Kinetix) - Open-ended 2D physics tasks in JAX.
- [Pgx](https://github.com/sotetsuk/pgx) - Vectorized board game environments (Go, chess, shogi...) in JAX.

### Multi-Agent

- [PettingZoo](https://github.com/Farama-Foundation/PettingZoo) - The standard multi-agent RL API and environments.
- [Melting Pot](https://github.com/google-deepmind/meltingpot) - Social generalization in multi-agent scenarios.
- [JaxMARL](https://github.com/bold-lab-ai/JaxMARL) - JAX multi-agent environments and baselines.
- [SMACv2](https://github.com/oxwhirl/smacv2) - StarCraft II micromanagement challenge.
- [Google Research Football](https://github.com/google-research/football) - Football (soccer) simulation for RL (archived).
- [Overcooked-AI](https://github.com/HumanCompatibleAI/overcooked_ai) - Cooperative cooking benchmark for human-AI coordination.

### Robotics & Physics

- [MuJoCo](https://github.com/google-deepmind/mujoco) - Fast, accurate physics engine for robotics and control.
- [Isaac Lab](https://github.com/isaac-sim/IsaacLab) - GPU-accelerated robot learning on NVIDIA Isaac Sim.
- [ManiSkill](https://github.com/mani-skill/ManiSkill) - GPU-parallelized robot manipulation simulation.
- [Meta-World](https://github.com/Farama-Foundation/Metaworld) - 50 manipulation tasks for multi-task and meta-RL.
- [robosuite](https://github.com/ARISE-Initiative/robosuite) - Modular robot manipulation simulation framework.
- [LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO) - Lifelong robot learning benchmark.
- [Genesis](https://github.com/Genesis-Embodied-AI/genesis-world) - Generative, GPU-fast physics platform for robotics.

### Embodied & 3D

- [Habitat-Lab](https://github.com/facebookresearch/habitat-lab) - Embodied AI in photorealistic 3D homes.
- [DeepMind Lab](https://github.com/google-deepmind/lab) - First-person 3D navigation and puzzle tasks.

### Autonomous Driving

- [CARLA](https://github.com/carla-simulator/carla) - Open-source urban driving simulator.
- [MetaDrive](https://github.com/metadriverse/metadrive) - Lightweight driving simulator for generalizable RL.
- [HighwayEnv](https://github.com/Farama-Foundation/HighwayEnv) - Minimal environments for highway decision making.

### Offline RL Datasets

- [Minari](https://github.com/Farama-Foundation/Minari) - Standard format and hosting for offline RL datasets (successor to D4RL).
- [D4RL](https://github.com/Farama-Foundation/D4RL) - Classic offline RL benchmark datasets.

### Safety & Multi-Objective

- [Safety-Gymnasium](https://github.com/PKU-Alignment/safety-gymnasium) - Constrained and safe RL benchmarks.
- [MO-Gymnasium](https://github.com/Farama-Foundation/MO-Gymnasium) - Multi-objective RL environments.

### Real-World Domains

- [FinRL](https://github.com/AI4Finance-Foundation/FinRL) - Financial trading environments.
- [Grid2Op](https://github.com/Grid2op/grid2op) - Power grid operation.

## Training Frameworks

### LLM Agent RL

- [verl](https://github.com/verl-project/verl) - Flexible, efficient RL training library for LLMs.
- [TRL](https://github.com/huggingface/trl) - Hugging Face library for post-training LLMs (PPO, GRPO, DPO...).
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) - Scalable Ray-based RLHF framework.
- [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) - Asynchronous decentralized RL training at scale.
- [SkyRL](https://github.com/skyrl-project/SkyRL) - Modular full-stack RL library for long-horizon agents.
- [rLLM](https://github.com/agentica-project/rllm) - RL for language agents.
- [ART](https://github.com/OpenPipe/ART) - Agent Reinforcement Trainer for multi-step agents.
- [slime](https://github.com/THUDM/slime) - LLM post-training framework for RL scaling.
- [AReaL](https://github.com/areal-project/AReaL) - Fully asynchronous RL system for reasoning and agents.

### Classic RL

- [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3) - Reliable PyTorch implementations of RL algorithms.
- [CleanRL](https://github.com/vwxyzjn/cleanrl) - Single-file, research-friendly RL implementations.
- [RLlib](https://github.com/ray-project/ray/tree/master/rllib) - Scalable industry-grade RL on Ray.
- [TorchRL](https://github.com/pytorch/rl) - PyTorch-native RL library.
- [Tianshou](https://github.com/thu-ml/tianshou) - Modular PyTorch RL library.
- [PureJaxRL](https://github.com/luchris429/purejaxrl) - End-to-end JAX RL on the GPU.
- [Sample Factory](https://github.com/alex-petrenko/sample-factory) - High-throughput asynchronous RL.

## Related Lists

- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - AI autonomous agents.
- [awesome-rl](https://github.com/aikorea/awesome-rl) - Reinforcement learning resources.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
