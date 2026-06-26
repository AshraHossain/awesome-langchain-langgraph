# Awesome LangChain & LangGraph [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Resources](https://img.shields.io/endpoint?url=https%3A%2F%2Fashrahossain.github.io%2Fawesome-langchain-langgraph%2Fapi%2Fshield.json)

> The go-to directory for people building AI agents on the LangChain ecosystem — curated tools, integrations, templates, learning, and real-world community projects, organized around the full agent lifecycle: **build → observe → evaluate → deploy**.

🔎 **[Browse it as a searchable web page →](https://ashrahossain.github.io/awesome-langchain-langgraph/)** *(auto-deploys via [`pages.yml`](.github/workflows/pages.yml) on push to `main`)*

---

## How the ecosystem fits together

If you're new here, four projects do most of the work, and they map cleanly onto the lifecycle of an agent:

| Project | What it is | Lifecycle stage |
|---|---|---|
| **LangChain** | The component framework — models, prompts, retrievers, tools, and the `create_agent` building block. | 🔨 Build |
| **LangGraph** | The orchestration runtime for stateful, long-running agents: durable execution, streaming, memory, and human-in-the-loop. | 🔨 Build · 🚀 Deploy |
| **Deep Agents** | The batteries-included harness *on top of* `create_agent` — planning, a virtual filesystem for context, subagents, and persistent memory. | 🔨 Build |
| **LangSmith** | Framework-agnostic platform to trace, evaluate, and monitor everything you build. | 🔭 Observe · 📊 Evaluate |
| **LangGraph Platform** | Managed deployment for LangGraph agents — scaling, persistence, cron, and the Assistants API. | 🚀 Deploy |

The mental model the LangChain team uses: **LangGraph is the runtime, `create_agent` is a minimal harness on top of it, and Deep Agents is a more opinionated harness on top of that.** You drop down a layer whenever you need more control. LangSmith wraps around all of them so you can see and grade what your agent actually did.

A typical journey through this list:

1. **🔨 Build** — start from a [template](#templates--starters), compose it with [integrations](#integrations), reach for [official prebuilt agents](#official-tools--prebuilt-agents) before writing your own.
2. **🔭 Observe** — turn on LangSmith tracing so every retrieval, reasoning step, tool call, and decision is recorded.
3. **📊 Evaluate** — build a dataset and run evaluators (`openevals`, `agentevals`) to score outputs *before* you trust them.
4. **🚀 Deploy** — ship on LangGraph Platform (or your own infra) with a UI like Agent Chat UI in front.

---

## The List

<!-- AUTOGEN:START -->

## Contents

- [Core Ecosystem](#core-ecosystem)
- [Official Tools & Prebuilt Agents](#official-tools--prebuilt-agents)
- [Integrations](#integrations)
- [Templates & Starters](#templates--starters)
- [Learning Resources](#learning-resources)
- [Community — RAG & Knowledge Assistants](#community--rag--knowledge-assistants)
- [Community — Research Agents](#community--research-agents)
- [Community — Web & Browser Automation](#community--web--browser-automation)
- [Community — Finance & Markets](#community--finance--markets)
- [Community — Productivity & Personal Assistants](#community--productivity--personal-assistants)
- [Community — Developer Tools & Coding Agents](#community--developer-tools--coding-agents)

### Core Ecosystem

The four pillars you build on. LangChain gives you the components, LangGraph runs the stateful agent, Deep Agents is the batteries-included harness, and LangSmith observes and evaluates the whole thing.

- [LangChain (Python)](https://github.com/langchain-ai/langchain) ⭐ 🔨 — The core framework: models, prompts, retrievers, tools, and the `create_agent` building block that everything else sits on.
- [LangChain.js](https://github.com/langchain-ai/langchainjs) ⭐ 🔨 — The TypeScript/JavaScript port of LangChain for building agents in Node and the browser.
- [LangGraph (Python)](https://github.com/langchain-ai/langgraph) ⭐ 🔨 🚀 — Low-level orchestration runtime for long-running, stateful agents. Durable execution, streaming, memory, and human-in-the-loop as first-class primitives.
- [LangGraph.js](https://github.com/langchain-ai/langgraphjs) ⭐ 🔨 🚀 — The TypeScript implementation of the LangGraph runtime.
- [Deep Agents](https://github.com/langchain-ai/deepagents) ⭐ 🔨 — The batteries-included agent harness on top of `create_agent`: built-in planning (write_todos), a virtual filesystem for context offloading, subagents with isolated context, and persistent memory. `pip install deepagents`.
- [LangSmith](https://docs.smith.langchain.com/) ⭐ 🔭 📊 — Unified platform to trace, evaluate, and monitor LLM apps. The observe + evaluate half of the lifecycle, framework-agnostic.
- [LangGraph Platform](https://www.langchain.com/langgraph-platform) ⭐ 🚀 — Managed deployment for LangGraph agents: horizontally scaling task queues, persistence, cron, and the Assistants API.
- [LangChain Docs](https://docs.langchain.com/) ⭐ 🔨 🔭 📊 🚀 — The unified documentation hub spanning LangChain, LangGraph, Deep Agents, and LangSmith.

### Official Tools & Prebuilt Agents

First-party packages and tooling from LangChain that you drop in instead of writing from scratch.

- [langgraph-supervisor](https://github.com/langchain-ai/langgraph-supervisor-py) ⭐ 🔨 — Prebuilt hierarchical multi-agent pattern: a central supervisor routes work to specialized agents.
- [langgraph-swarm](https://github.com/langchain-ai/langgraph-swarm-py) ⭐ 🔨 — Prebuilt swarm pattern where agents hand off control to each other and the system remembers who was last active.
- [LangMem](https://github.com/langchain-ai/langmem) ⭐ 🔨 — Long-term memory SDK: extract, store, and retrieve semantic, episodic, and procedural memories across threads.
- [LangGraph Studio](https://docs.langchain.com/langgraph-platform/langgraph-studio) ⭐ 🔨 🔭 — Visual IDE to run, debug, and time-travel through your LangGraph agent's state.
- [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) ⭐ 🔨 — Use any Model Context Protocol (MCP) server's tools inside LangChain and LangGraph agents.
- [Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui) ⭐ 🚀 — Next.js chat front-end that talks to any LangGraph deployment out of the box, including streaming and interrupts.
- [open-deep-research](https://github.com/langchain-ai/open_deep_research) ⭐ 🔨 — Open, configurable deep-research agent built on LangGraph — a reference implementation for multi-step research.
- [openevals](https://github.com/langchain-ai/openevals) ⭐ 📊 — Ready-made evaluators (LLM-as-judge, exact match, structured) for grading LLM outputs in CI and LangSmith.
- [agentevals](https://github.com/langchain-ai/agentevals) ⭐ 📊 — Evaluators specialized for agent trajectories — judge tool-call sequences and multi-step decisions, not just final answers.
- [LangGraph Bigtool](https://github.com/langchain-ai/langgraph-bigtool) ⭐ 🔨 — Prebuilt LangGraph agent that scales tool use by retrieving relevant tools from a large registry via semantic search.

### Integrations

The plug-in surface: model providers, vector stores, and tools that snap into LangChain via dedicated packages.

- [Integrations Directory](https://python.langchain.com/docs/integrations/providers/) ⭐ 🔨 — The canonical index of every provider, vector store, retriever, and tool integration.
- [langchain-anthropic](https://github.com/langchain-ai/langchain/tree/master/libs/partners/anthropic) ⭐ 🔨 — Claude model integration (chat, tool use, prompt caching).
- [langchain-openai](https://github.com/langchain-ai/langchain/tree/master/libs/partners/openai) ⭐ 🔨 — OpenAI and Azure OpenAI chat, embeddings, and tool-calling integration.
- [langchain-google-genai](https://github.com/langchain-ai/langchain-google) ⭐ 🔨 — Google Gemini and Vertex AI model integrations.
- [langchain-aws](https://github.com/langchain-ai/langchain-aws) ⭐ 🔨 — Amazon Bedrock models, Kendra retrieval, and other AWS integrations.
- [langchain-chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma/) ⭐ 🔨 — Chroma vector store integration for local and embedded RAG.
- [langchain-postgres (pgvector)](https://github.com/langchain-ai/langchain-postgres) ⭐ 🔨 — Postgres + pgvector vector store and chat-history store.
- [Tavily Search](https://github.com/tavily-ai/langchain-tavily) 🔨 — Search API built for agents; a common web-retrieval tool in LangGraph research agents.

### Templates & Starters

Clone-and-go starting points. Most are LangGraph templates wired for LangGraph Studio and Platform.

- [ReAct Agent Template](https://github.com/langchain-ai/react-agent) ⭐ 🔨 — The canonical tool-calling agent template — the fastest way to a working LangGraph agent.
- [Retrieval Agent Template](https://github.com/langchain-ai/retrieval-agent-template) ⭐ 🔨 — RAG agent scaffold with indexing and retrieval graphs ready to customize.
- [Memory Agent Template](https://github.com/langchain-ai/memory-agent) ⭐ 🔨 — Starter showing long-term memory with LangGraph's store and LangMem.
- [Data Enrichment Template](https://github.com/langchain-ai/data-enrichment) ⭐ 🔨 — Agent that researches and fills structured records — a template for extraction pipelines.
- [New LangGraph Project](https://github.com/langchain-ai/new-langgraph-project) ⭐ 🔨 🚀 — Minimal blank LangGraph project skeleton with config and CLI wiring.
- [Chat LangChain](https://github.com/langchain-ai/chat-langchain) ⭐ 🔨 🚀 — Full reference RAG chatbot over the LangChain docs — production patterns end to end.

### Learning Resources

Courses, tutorials, and channels to go from zero to shipping agents.

- [LangChain Academy](https://academy.langchain.com/) ⭐ 🔨 — Free first-party courses, including the well-regarded Introduction to LangGraph.
- [Deep Agents Overview (Docs)](https://docs.langchain.com/oss/python/deepagents/overview) ⭐ 🔨 — The official conceptual guide to what Deep Agents add over a bare agent.
- [AI Agents in LangGraph (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) 🔨 — Short course building agents from scratch and then in LangGraph.
- [LangChain Blog](https://blog.langchain.com/) ⭐ 🔨 🔭 📊 🚀 — Release notes, design rationale, and case studies straight from the team.
- [LangChain YouTube](https://www.youtube.com/@LangChain) ⭐ 🔨 — Walkthroughs, livestreams, and conference talks.
- [LangSmith Evaluation Docs](https://docs.smith.langchain.com/evaluation) ⭐ 📊 — How to build datasets, run evaluators, and gate releases on quality.

### Community — RAG & Knowledge Assistants

Real-world projects that retrieve over your data and answer questions.

- [Onyx (formerly Danswer)](https://github.com/onyx-dot-app/onyx) 🔨 🚀 — Open-source AI assistant that connects to your company's docs and apps for grounded answers.
- [Quivr](https://github.com/QuivrHQ/quivr) 🔨 — Opinionated RAG framework and 'second brain' for plugging LLMs into your files.
- [Verba](https://github.com/weaviate/Verba) 🔨 🚀 — Weaviate's open-source RAG application ('Golden RAGtriever') with a polished UI.

### Community — Research Agents

Agents that plan, search the web, and synthesize long-form reports.

- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) 🔨 — Autonomous agent that runs multi-source web research and produces cited reports; offers a LangGraph multi-agent variant.
- [GPT Newspaper](https://github.com/assafelovic/gpt-newspaper) 🔨 — LangGraph agent that curates and writes a personalized newspaper from live sources.
- [Local Deep Researcher](https://github.com/langchain-ai/local-deep-researcher) ⭐ 🔨 — Fully local web-research assistant on LangGraph that iteratively searches, summarizes, and fills knowledge gaps with any Ollama/LMStudio model.

### Community — Web & Browser Automation

Agents that drive browsers and act on the live web.

- [Browser Use](https://github.com/browser-use/browser-use) 🔨 — Library that lets LLM agents control a real browser; integrates with LangChain models.
- [LaVague](https://github.com/lavague-ai/LaVague) 🔨 — Open-source Large Action Model framework that turns natural-language objectives into executed browser actions; integrates with LangChain.

### Community — Finance & Markets

Agents applied to investing research and financial analysis.

- [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund) 🔨 — Educational multi-agent system (built with LangChain/LangGraph) that simulates investing analysts and a portfolio manager.
- [AI Financial Agent](https://github.com/virattt/ai-financial-agent) 🔨 — Proof-of-concept financial-analysis agent over market data and filings, built with LangChain and LangGraph.

### Community — Productivity & Personal Assistants

Agents that handle email, scheduling, and everyday workflows.

- [Executive AI Assistant](https://github.com/langchain-ai/executive-ai-assistant) ⭐ 🔨 🚀 — Reference LangGraph email assistant that triages inbox and drafts replies with human-in-the-loop.
- [Social Media Agent](https://github.com/langchain-ai/social-media-agent) ⭐ 🔨 🚀 — LangGraph agent that turns URLs into drafted social posts with human review.

### Community — Developer Tools & Coding Agents

Agents that read, write, and ship code.

- [Open SWE](https://github.com/langchain-ai/open-swe) ⭐ 🔨 🚀 — Open-source asynchronous coding agent built on LangGraph that plans and executes repo changes.

> **Legend:** ⭐ official LangChain project · 🔨 build · 🔭 observe · 📊 evaluate · 🚀 deploy

<!-- AUTOGEN:END -->

---

## Data API

The list is machine-readable, not just a web page. A static JSON API is
generated from the same `resources.json` and published alongside the site, so
you can build on top of it (dashboards, bots, your own filtered views):

| Endpoint | What you get |
|---|---|
| [`/api/resources.json`](https://ashrahossain.github.io/awesome-langchain-langgraph/api/resources.json) | Flat list of every resource, each tagged with its category and group. |
| [`/api/stats.json`](https://ashrahossain.github.io/awesome-langchain-langgraph/api/stats.json) | Counts by category, lifecycle stage, group, and official/community. |
| [`/api/lifecycle/{build,observe,evaluate,deploy}.json`](https://ashrahossain.github.io/awesome-langchain-langgraph/api/lifecycle/build.json) | Just the resources for one lifecycle stage. |
| [`/api/shield.json`](https://ashrahossain.github.io/awesome-langchain-langgraph/api/shield.json) | A [shields.io endpoint](https://shields.io/badges/endpoint-badge) powering the resource-count badge above. |

```bash
# e.g. list every deploy-stage tool, names only
curl -s https://ashrahossain.github.io/awesome-langchain-langgraph/api/lifecycle/deploy.json | jq '.[].name'
```

## Submitting a resource, the easy way

Open a **[Suggest a resource issue](../../issues/new?template=suggest-resource.yml)** and fill in the form. Once it's labeled `new-resource`, a bot parses it, validates it against the schema, and opens a PR for a maintainer to review — no fork or local setup required. (You can still open a PR by hand; see below.)

## Contributing

Found a great tool, template, or project that belongs here? **[Read CONTRIBUTING.md](CONTRIBUTING.md)** — it's a two-minute process:

1. Add your entry to [`data/resources.json`](data/resources.json) (one JSON object, not the README directly).
2. Run `python scripts/validate.py` and `python scripts/generate_readme.py`.
3. Open a PR. CI validates the schema, checks for duplicates, and verifies links.

The README's link sections are **generated** from `data/resources.json` — that's the single source of truth, and it's also what powers the web page. Don't hand-edit the list between the `AUTOGEN` markers; it'll be overwritten.

## Why this is built the way it is

This isn't just a markdown file — it's a tiny pipeline so the list stays correct as it grows:

- **One data file** (`data/resources.json`) feeds both the README and the web page, so they can never disagree.
- **A schema** (`data/schema.json`) plus `scripts/validate.py` reject malformed or duplicate entries on every PR.
- **`scripts/check_links.py`** runs on a schedule to catch links that rot over time.
- **`scripts/generate_readme.py --check`** fails CI if someone edits the data without regenerating.

See [Notes.md](Notes.md) *(local only)* for the full rationale, and [LICENSE](LICENSE) (CC0 — public domain) for usage.

## Running locally

```bash
pip install -r requirements.txt
python scripts/validate.py          # schema + structural checks
python scripts/generate_readme.py   # rebuild this README's list
python scripts/build_site.py        # stage data for the web page
python -m http.server -d site 8080  # browse at http://localhost:8080
```

Or with Docker:

```bash
docker compose up --build           # serves the searchable page at http://localhost:8080
```
