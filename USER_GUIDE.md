# Awesome LangChain & LangGraph — User Guide

> The go-to directory for building AI agents on the LangChain ecosystem.  
> **Live at:** http://localhost:8080 (when running via Docker)  
> **Public:** https://ashrahossain.github.io/awesome-langchain-langgraph/

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Browsing the Directory](#browsing-the-directory)
3. [Searching & Filtering](#searching--filtering)
4. [Understanding the Lifecycle](#understanding-the-lifecycle)
5. [Using the Data API](#using-the-data-api)
6. [Contributing a Resource](#contributing-a-resource)
7. [Glossary](#glossary)

---

## Getting Started

### Option 1: Docker (Recommended)
```bash
cd awesome-langchain-langgraph
docker compose up -d
```
Then open **http://localhost:8080** in your browser.

### Option 2: Local Development
```bash
python -m http.server -d site 8080
```
Open **http://localhost:8080**.

### Option 3: GitHub Pages
Visit **https://ashrahossain.github.io/awesome-langchain-langgraph/** (live, no setup needed).

---

## Browsing the Directory

### The Homepage

When you open the site, you'll see:

```
┌─────────────────────────────────────────────────────────────┐
│  Awesome LangChain & LangGraph  [Resources: 51]            │
│                                                              │
│  The directory for building AI agents — across the full    │
│  lifecycle: build → observe → evaluate → deploy.           │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Search tools, integrations, projects...  (press /)  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  [🔨 build]  [🔭 observe]  [📊 evaluate]  [🚀 deploy]      │
│                                                              │
│  [All]  [Ecosystem]  [Community]                            │
│                                                              │
│  51 resources shown                                         │
└─────────────────────────────────────────────────────────────┘
```

**Key elements:**
- **Search box** — type to find resources by name or description
- **Lifecycle badges** — filter by agent lifecycle stage
- **Group tabs** — All / Ecosystem (official) / Community (user-built)
- **Resource counter** — shows how many match your filters

### Scrolling Through Resources

Resources are organized by **11 sections**:

1. **Core Ecosystem** — LangChain, LangGraph, Deep Agents, LangSmith (the "four pillars")
2. **Official Tools & Prebuilt Agents** — langgraph-supervisor, langgraph-swarm, LangMem, etc.
3. **Integrations** — Model providers, vector stores, and tools
4. **Templates & Starters** — Clone-and-go project scaffolds
5. **Learning Resources** — Courses, tutorials, documentation
6. **Community — RAG & Knowledge Assistants** — Real-world RAG projects
7. **Community — Research Agents** — Multi-step research automation
8. **Community — Web & Browser Automation** — Browser-driving agents
9. **Community — Finance & Markets** — Financial analysis tools
10. **Community — Productivity & Personal Assistants** — Email, scheduling, workflows
11. **Community — Developer Tools & Coding Agents** — Code generation, refactoring

Each **resource card** shows:
```
┌────────────────────────────────────┐
│ LangGraph (Python)              ⭐ │ ← Official badge (LangChain-built)
│                                    │
│ Low-level orchestration runtime    │ ← Description
│ for long-running, stateful agents. │
│ Durable execution, streaming,      │
│ memory, and human-in-the-loop as   │
│ first-class primitives.            │
│                                    │
│ ⭐ official  🔨 build  🚀 deploy   │ ← Badges: official status + lifecycle
└────────────────────────────────────┘
```

---

## Searching & Filtering

### Live Search (Press `/`)

Press `/` anywhere on the page to jump to the search box. Type to find resources:

| Query | Result |
|-------|--------|
| `langgraph` | All LangGraph projects (core, supervisor, swarm, etc.) |
| `rag` | RAG-focused resources (retrieval agents, knowledge systems) |
| `openai` | OpenAI integrations |
| `research` | Research agents and deep-research templates |
| `evaluation` | LangSmith, openevals, agentevals |

**Search is live** — results update as you type.

### Lifecycle Filters

Click any badge to toggle filtering by stage:

| Badge | Meaning | Use Cases |
|-------|---------|-----------|
| **🔨 build** | Compose agents, chains, graphs | Writing agent code |
| **🔭 observe** | Trace, monitor, debug | LangSmith, Studio |
| **📊 evaluate** | Score outputs, build datasets | openevals, agentevals, metrics |
| **🚀 deploy** | Ship to production | LangGraph Platform, Docker, Assistants API |

Example: Click `🚀 deploy` to see only tools you can use to ship agents to production.

### Group Filters

**All** — Everything (default)
**Ecosystem** — Official LangChain-owned projects (marked ⭐)
**Community** — User-built, open-source projects

---

## Understanding the Lifecycle

The directory is organized around **four stages of building AI agents:**

### 🔨 Build
**"Compose chains, agents, and graphs that do the work."**

Resources: LangChain, LangGraph, Deep Agents, templates, integrations.

→ Start here: pick a template, add a model, wire in tools.

### 🔭 Observe
**"Trace every retrieval, reasoning step, tool call, and decision."**

Resources: LangSmith (tracing + monitoring), LangGraph Studio (IDE + debugger).

→ Turn this on first — you can't optimize what you can't see.

### 📊 Evaluate
**"Score outputs against datasets and rubrics before you trust them."**

Resources: LangSmith (evaluation), openevals (ready-made graders), agentevals (agent-specific scoring).

→ Build a dataset, run an evaluator, gate your release on the score.

### 🚀 Deploy
**"Ship durable, stateful agents to production with scaling and human-in-the-loop."**

Resources: LangGraph Platform (managed), Agent Chat UI (frontend), Docker, LangGraph Assistants API.

→ Choose a deployment model, set up observability, test the flow end to end.

---

## Using the Data API

The directory is also **machine-readable**. Every resource lives in a JSON file that powers both the web page and a static API.

### API Endpoints

#### `/api/resources.json` — Full List
```bash
curl http://localhost:8080/api/resources.json | jq '.[0]'
```

Returns:
```json
{
  "name": "LangChain (Python)",
  "url": "https://github.com/langchain-ai/langchain",
  "description": "The core framework: models, prompts, retrievers, tools...",
  "official": true,
  "lifecycle": ["build"],
  "category_id": "core-ecosystem",
  "category_title": "Core Ecosystem",
  "group": "ecosystem"
}
```

#### `/api/stats.json` — Aggregate Statistics
```bash
curl http://localhost:8080/api/stats.json | jq '.'
```

Returns:
```json
{
  "version": "1.0.0",
  "updated": "2026-06-26",
  "total": 51,
  "categories": 11,
  "official": 40,
  "by_group": {
    "ecosystem": 26,
    "community": 25
  },
  "by_lifecycle": {
    "build": 45,
    "observe": 4,
    "evaluate": 6,
    "deploy": 13
  },
  "by_category": {
    "Core Ecosystem": 8,
    "Official Tools & Prebuilt Agents": 9,
    ...
  }
}
```

#### `/api/lifecycle/{stage}.json` — Stage-Specific Resources
```bash
# All deploy-stage tools
curl http://localhost:8080/api/lifecycle/deploy.json | jq '.[].name'
```

Stages: `build`, `observe`, `evaluate`, `deploy`

#### `/api/shield.json` — Live Resource Count (Badge Endpoint)
```bash
curl http://localhost:8080/api/shield.json | jq '.'
```

Returns:
```json
{
  "schemaVersion": 1,
  "label": "resources",
  "message": "51",
  "color": "#1c8c5a"
}
```

Used in shields.io badges and README badges.

### Example: Build a Custom Dashboard
```bash
# Get all RAG resources (by description search)
curl http://localhost:8080/api/resources.json | \
  jq '.[] | select(.description | contains("RAG")) | {name, url}'

# Count official vs community
curl http://localhost:8080/api/stats.json | \
  jq '{official: .official, community: (.total - .official)}'

# Find all projects that do both observe AND deploy
curl http://localhost:8080/api/resources.json | \
  jq '.[] | select(.lifecycle | contains(["observe", "deploy"])) | .name'
```

---

## Contributing a Resource

### Path 1: The Easy Way (No Fork Needed)

1. **Open a "Suggest a resource" issue:**
   - Click **"Issues"** on GitHub
   - Click **"New issue"**
   - Select **"Suggest a resource"** template
   - Fill in the form

2. **The bot takes it from there:**
   - Fills in your submission data
   - Opens a PR automatically
   - A maintainer reviews & merges
   - Your resource goes live on the next deploy

### Path 2: Direct PR

1. **Clone the repo and edit `data/resources.json`:**
   ```json
   {
     "name": "Your Project",
     "url": "https://github.com/you/your-project",
     "description": "One sentence (10–280 chars) describing what it does and why it's useful.",
     "official": false,
     "lifecycle": ["build"]
   }
   ```

2. **Validate locally:**
   ```bash
   python scripts/validate.py          # checks schema + duplicates
   python scripts/generate_readme.py   # regenerates the README's list
   ```

3. **Open a PR** — CI runs all checks automatically.

### What Makes a Good Submission

✅ **Include:**
- A working link (we check it weekly)
- One concise sentence describing what it does
- The lifecycle stage(s) it covers
- Your name/org if you're the author

❌ **Avoid:**
- Dead links (we'll remove them)
- Marketing copy (be factual)
- Duplicate projects already on the list
- Repos with no README or activity in 2+ years

---

## Glossary

### Agent
A system that can perceive its environment, reason about goals, and take actions via tools to achieve them. Built with LangChain/LangGraph.

### LangChain
The component framework: models, prompts, retrievers, tools, and the `create_agent` building block.

### LangGraph
The stateful orchestration runtime: manages long-running agent execution, memory, streaming, and human-in-the-loop.

### Deep Agents
A batteries-included harness on top of LangGraph: adds planning (write_todos), virtual filesystem, subagents, and persistent memory.

### LangSmith
Unified platform for tracing (observe), evaluating (score), and monitoring (in prod) LLM applications.

### LangGraph Platform
Managed deployment for LangGraph agents: scales, persists state, runs crons, exposes an Assistants API.

### RAG (Retrieval-Augmented Generation)
Agents that retrieve context (from docs, databases, APIs) before generating responses — grounds LLM answers in your data.

### Tool
A function an agent can call (web search, calculator, API, database query, etc.). Defined with a name, description, and input schema.

### Lifecycle Stage
- **Build** — Write the agent
- **Observe** — See what it's doing (tracing)
- **Evaluate** — Score whether it's good enough (evals)
- **Deploy** — Ship it to users (production runtime)

### Official
Badge `⭐` indicates the project is maintained by LangChain (langchain-ai GitHub org). Community resources are community-maintained.

---

## Troubleshooting

### "The site won't load"
- Docker running? `docker compose ps` should show `site-1   Up`
- Port 8080 in use? Try `docker compose up -d -p 8081:80` and visit http://localhost:8081

### "Search isn't working"
- Try pressing `/` first, then typing
- Searches are case-insensitive and match partial strings in name + description

### "A link is broken"
- We run a link checker weekly in CI
- Report it as an issue: **"Link broken in [resource name]"**
- We'll update or remove it within a few days

### "I want to add my project"
- Follow **[Contributing a Resource](#contributing-a-resource)** above
- Questions? Open an issue — we're friendly

---

## Advanced: Running Locally

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Validate & Generate
```bash
make validate     # check data/resources.json against schema
make generate     # regenerate README.md from data
make site         # stage resources.json and API artifacts for the web
```

### View the Site
```bash
make serve        # http://localhost:8080
```

### Run Tests
```bash
make test         # 61 tests covering data integrity, generation, API
```

### Check Links
```bash
make links        # verifies all 51+ URLs are reachable (slow, ~2-3 min)
```

---

## Questions?

- **About a resource?** Check its GitHub or documentation link.
- **How do I contribute?** See [Contributing a Resource](#contributing-a-resource) above.
- **Found a bug?** Open a [GitHub issue](../../issues/new).
- **Want to help improve the directory?** Pull requests welcome — see `CONTRIBUTING.md`.

**Happy building!** 🚀
