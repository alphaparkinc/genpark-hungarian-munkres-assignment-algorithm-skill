# genpark-hungarian-munkres-assignment-algorithm-skill

[![GitHub stars](https://img.shields.io/github/stars/alphaparkinc/genpark-hungarian-munkres-assignment-algorithm-skill?style=social)](https://github.com/alphaparkinc/genpark-hungarian-munkres-assignment-algorithm-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Kuhn-Munkres (Hungarian) Bipartite Matching Algorithm for Optimal 1-to-1 Task-Agent Assignment

Part of the **GenPark Autonomous Operations Research & Combinatorial Optimization Swarm**.

## Architecture Overview

```mermaid
graph TD
    A[Agent-Task Cost/Benefit Matrix] --> B[Square Matrix Normalization]
    B --> C[Initialize Dual Potentials u and v]
    C --> D[Find Tight Alternating Tree]
    D --> E{Augmenting Path Exists?}
    E -->|No| F[Adjust Dual Labels via Minimal Delta Slack]
    F --> D
    E -->|Yes| G[Augment Matching along Alternating Path]
    G --> H{All Agents Assigned?}
    H -->|No| D
    H -->|Yes| I[Optimal 1-to-1 Assignment & Dual Cert]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies (no NumPy, SciPy, or PuLP needed). Runs anywhere.
- **Production-Grade Design**: Type annotations, exhaustive edge cases, robust numerical stability.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/alphaparkinc/genpark-hungarian-munkres-assignment-algorithm-skill.git
cd genpark-hungarian-munkres-assignment-algorithm-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
