# Awesome LangChain & LangGraph — Visual User Guide

> **Live demo running at:** http://localhost:8080 (Docker) or https://ashrahossain.github.io/awesome-langchain-langgraph/ (public)

---

## The Full Site Layout

When you open the site, you'll see this structure:

```
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║   Awesome LangChain & LangGraph  📊 Resources: 51                          ║
║   ────────────────────────────────────────────────────────────             ║
║                                                                             ║
║   The directory for building AI agents — across the full lifecycle:        ║
║   build → observe → evaluate → deploy.                                    ║
║                                                                             ║
║   ┌─────────────────────────────────────────────────────────────────────┐  ║
║   │ 🔍 Search tools, integrations, projects...  (press /)              │  ║
║   └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                             ║
║   ┌─────────────────────────────────────────────────────────────────────┐  ║
║   │ [🔨 build]  [🔭 observe]  [📊 evaluate]  [🚀 deploy]              │  ║
║   └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                             ║
║   ┌─────────────────────────────────────────────────────────────────────┐  ║
║   │ [All]  [Ecosystem]  [Community]                                    │  ║
║   └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                             ║
║   📊 51 resources shown                                                    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

---

## Step 1: Understanding the Header

### Search Box
```
┌─────────────────────────────────────────────────────────────┐
│ 🔍 Search tools, integrations, projects...  (press /)      │
└─────────────────────────────────────────────────────────────┘
```

**What to do:**
1. **Click in the search box** (or press `/` anywhere on the page)
2. **Type keywords:**
   - `langgraph` → finds all LangGraph projects
   - `rag` → finds RAG resources
   - `research` → finds research agents
   - `openai` → finds OpenAI integrations
   - `docker` → finds containerized tools

**Result:** The page filters in real-time as you type. Only matching resources stay visible.

---

## Step 2: Using the Lifecycle Filters

### The Four Stages
```
┌─────────────────────────────────────────────────────────────┐
│  🔨 build     🔭 observe     📊 evaluate     🚀 deploy     │
└─────────────────────────────────────────────────────────────┘
```

**Click any badge to filter by that stage:**

| Badge | Meaning | What you'll find |
|-------|---------|-----------------|
| **🔨 build** | Building agents | LangChain, LangGraph, templates, integrations, tools |
| **🔭 observe** | Tracing & debugging | LangSmith, LangGraph Studio, monitoring tools |
| **📊 evaluate** | Scoring outputs | openevals, agentevals, LangSmith evaluation |
| **🚀 deploy** | Shipping to prod | LangGraph Platform, Docker, Assistants API, UIs |

**Example workflow:**
1. Start with **🔨 build** to see what frameworks exist
2. Click **🔭 observe** to add tracing/debugging tools to your selection
3. Click **📊 evaluate** to add scoring tools
4. Click **🚀 deploy** to add production deployment options
5. **Click any badge again to deselect it**

**Current selection:** Shows at the top (e.g., "51 resources shown" → "4 resources shown" after filtering).

---

## Step 3: Choosing Your Group

### All / Ecosystem / Community
```
┌─────────────────────────────────────────────────────────────┐
│  [All]  [Ecosystem]  [Community]                           │
└─────────────────────────────────────────────────────────────┘
```

**What's the difference?**

| Group | Shows | Example |
|-------|-------|---------|
| **All** | Everything (51 total) | All projects, official & community |
| **Ecosystem** | Official LangChain projects only (40 total) | LangChain, LangGraph, Deep Agents, LangSmith, openevals |
| **Community** | User-built, open-source projects (25 total) | OnYX, Quivr, GPT Researcher, Browser Use |

**Use this to:**
- **"Show me ONLY official tools"** → Click [Ecosystem]
- **"Show me community projects"** → Click [Community]
- **"Show me everything"** → Click [All]

---

## Step 4: What a Resource Card Looks Like

When you see resources on the page, each one looks like this:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  LangGraph (Python)                                  ⭐    │
│  ─────────────────────────────────────────────────────     │
│                                                             │
│  Low-level orchestration runtime for long-running,         │
│  stateful agents. Durable execution, streaming, memory,    │
│  and human-in-the-loop as first-class primitives.          │
│                                                             │
│  ⭐ official  🔨 build  🚀 deploy                           │
│                                                             │
│  [Click name to open on GitHub]                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Breaking it down:**

| Part | Meaning |
|------|---------|
| **LangGraph (Python)** | Project name (clickable link) |
| **⭐** | Official LangChain project (only shown for official tools) |
| **Description** | One sentence explaining what it does |
| **⭐ official** | Badges showing official status |
| **🔨 build** | Lifecycle stages (what phase it covers) |
| **🚀 deploy** | (can have multiple badges) |

---

## Step 5: Scrolling Through Categories

The site shows resources **organized by 11 sections:**

### Section 1: Core Ecosystem (The Four Pillars)
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Core Ecosystem
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The four pillars you build on. LangChain gives you the components,
LangGraph runs the stateful agent, Deep Agents is the batteries-included
harness, and LangSmith observes and evaluates the whole thing.

  ┌──────────────────────────┐
  │ LangChain (Python)    ⭐ │
  │ 🔨 build              │
  │ [description...]      │
  └──────────────────────────┘

  ┌──────────────────────────┐
  │ LangGraph (Python)    ⭐ │
  │ 🔨 build  🚀 deploy   │
  │ [description...]      │
  └──────────────────────────┘

  ┌──────────────────────────┐
  │ Deep Agents           ⭐ │
  │ 🔨 build              │
  │ [description...]      │
  └──────────────────────────┘

  ┌──────────────────────────┐
  │ LangSmith             ⭐ │
  │ 🔭 observe  📊 eval   │
  │ [description...]      │
  └──────────────────────────┘
```

**Other sections include:**
- Official Tools & Prebuilt Agents (supervisor, swarm, LangMem)
- Integrations (by model provider: OpenAI, Anthropic, Google, AWS)
- Templates & Starters (blank project scaffolds)
- Learning Resources (courses, docs, tutorials)
- Community by Use Case (RAG, research, web automation, finance, productivity, dev tools)

---

## Step 6: Finding What You Need — Real Examples

### "I want to build an agent that researches topics"

1. **Start with the lifecycle:** Click **🔨 build**
2. **Look in these sections:**
   - **Core Ecosystem** → LangChain + LangGraph (the foundation)
   - **Templates** → Retrieval Agent Template or Data Enrichment
   - **Community — Research Agents** → GPT Researcher, Local Deep Researcher
3. **Add tracing:** Click **🔭 observe** to also see LangSmith + Studio
4. **Ready to ship?** Click **🚀 deploy** to see LangGraph Platform + Docker

### "I need to evaluate my agent's output"

1. **Click:** **📊 evaluate**
2. **You'll see:**
   - LangSmith (evaluation platform)
   - openevals (ready-made scorers)
   - agentevals (agent-specific scoring)
3. **Pick one** → Click the link → Read the docs

### "I want to deploy to production"

1. **Click:** **🚀 deploy**
2. **You'll see:**
   - LangGraph Platform (managed, easiest)
   - Agent Chat UI (frontend for your agent)
   - Docker (if you want to self-host)
   - Assistants API
3. **Choose one** → Follow its docs

---

## Step 7: Using the Machine-Readable API

The site's **data is also available as JSON**, so you can build tools on top of it.

### Check Live Stats
```bash
curl http://localhost:8080/api/stats.json | jq '.'
```

**Returns:**
```json
{
  "total": 51,
  "official": 40,
  "by_lifecycle": {
    "build": 45,
    "observe": 4,
    "evaluate": 6,
    "deploy": 13
  }
}
```

### Get All Deploy-Stage Tools
```bash
curl http://localhost:8080/api/lifecycle/deploy.json | jq '.[].name'
```

**Returns:**
```
LangGraph Platform
Agent Chat UI
LangGraph.js
open-swe
...
```

### Get the Full List (for your own dashboard)
```bash
curl http://localhost:8080/api/resources.json | jq '.[] | {name, url, lifecycle}'
```

---

## Step 8: Contributing Your Own Resource

### Option A: The Bot Way (Easiest)

1. **Click "Issues" → "New issue"**
2. **Select "Suggest a resource" template**
3. **Fill in the form:**
   ```
   Name: Your Project Name
   URL: https://github.com/you/your-project
   Description: One sentence about what it does
   Category: Official Tools & Prebuilt Agents (or pick one)
   Lifecycle: ☑ build  ☐ observe  ☐ evaluate  ☐ deploy
   Official?: ☐ Yes  ☑ No
   ```
4. **Click "Submit"**
5. **Wait ~30 seconds** → A bot opens a PR with your entry
6. **A maintainer reviews** → Merges within 24 hours
7. **Done!** Your resource goes live on the next deploy

### Option B: Direct PR

1. **Clone the repo:**
   ```bash
   git clone https://github.com/AshraHossain/awesome-langchain-langgraph.git
   cd awesome-langchain-langgraph
   ```

2. **Edit `data/resources.json`** and add your resource:
   ```json
   {
     "name": "Your Project",
     "url": "https://github.com/you/repo",
     "description": "One sentence describing what it does.",
     "official": false,
     "lifecycle": ["build"]
   }
   ```

3. **Test locally:**
   ```bash
   python scripts/validate.py          # ✅ passes
   python scripts/generate_readme.py   # ✅ generates
   ```

4. **Open a PR** on GitHub
5. **CI runs automatically** → All checks pass
6. **Maintainer merges** → Goes live

---

## Step 9: Common Tasks at a Glance

| Goal | Steps |
|------|-------|
| **Find all official tools** | Click [Ecosystem] |
| **Find community projects** | Click [Community] |
| **See only RAG tools** | Type `rag` in search |
| **See what's in the 'build' phase** | Click 🔨 build |
| **Get all deploy tools as JSON** | `curl .../api/lifecycle/deploy.json` |
| **Check how many resources exist** | `curl .../api/stats.json \| jq .total` |
| **Add my project** | Issue form (Option A) or PR (Option B) |
| **Run locally** | `docker compose up -d` or `make serve` |

---

## Step 10: Tips & Tricks

### Keyboard Shortcut: Search Anywhere
**Press `/` on any page** → Jump to search box instantly

### Live Filtering
- **Search + Lifecycle filters stack**
  - Type `langgraph` AND click **🔨 build** → See only build-stage LangGraph projects
  - Type `langsmith` AND click **📊 evaluate** → See only LangSmith evaluation features

### Multiple Lifecycle Selection
- Click **🔨 build** and **🔭 observe** together → Show tools that do BOTH
- Useful for: "What can I use to build AND trace my agent?"

### Direct Link to Filtered Results
- Not yet (the site doesn't generate URLs for filter state)
- Workaround: Use the API endpoint for your filter instead

---

## Step 11: The Lifecycle Journey (Visual)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  MY AGENT JOURNEY                                                  │
│  ─────────────────                                                 │
│                                                                     │
│  WEEK 1: 🔨 BUILD                                                  │
│  ├─ Pick: LangChain (models + tools)                               │
│  ├─ Choose: LangGraph (orchestration)                              │
│  ├─ Use: Retrieval Agent Template                                  │
│  └─ Wire: OpenAI integration                                       │
│                                                                     │
│  WEEK 2: 🔭 OBSERVE                                                │
│  ├─ Enable: LangSmith tracing                                      │
│  ├─ Open: LangGraph Studio (IDE)                                   │
│  └─ Watch: Every tool call, reasoning step                         │
│                                                                     │
│  WEEK 3: 📊 EVALUATE                                               │
│  ├─ Build: Test dataset (100 examples)                             │
│  ├─ Run: openevals (LLM-as-judge)                                  │
│  └─ Gate: Only ship if score > 0.8                                 │
│                                                                     │
│  WEEK 4: 🚀 DEPLOY                                                 │
│  ├─ Choose: LangGraph Platform (or Docker)                         │
│  ├─ Add: Agent Chat UI (frontend)                                  │
│  └─ Launch: Production agent taking live requests                  │
│                                                                     │
│  ONGOING: 🔭 MONITOR                                               │
│  └─ LangSmith: Watch prod metrics, user feedback                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Troubleshooting

### "The search box is empty"
**→ It's searching, but maybe no results match. Try:**
- Simpler keywords: `langchain` instead of `langchain official tools`
- Partial matches: `openai` (not `OpenAI API Integration`)
- Category names: `rag`, `research`, `finance`

### "I want to filter by multiple lifecycle stages"
**→ Click them in order (🔨 then 🔭 then 📊 then 🚀)**
- You'll see only resources tagged with ALL selected stages

### "The link to a resource is broken"
**→ Report it as an issue:**
- Title: "Link broken: [resource name]"
- We check links weekly and fix/remove broken ones

### "How do I know if a tool is still maintained?"
**→ Look at:**
- GitHub "Last updated" badge
- Number of recent commits
- Open issues
- We remove projects inactive >2 years

---

## Next Steps

**Pick your journey:**

1. **I want to LEARN** → Go to [Learning Resources](#section-5-learning-resources) → Click a course
2. **I want to BUILD** → Go to [Core Ecosystem](#section-1-core-ecosystem) + [Templates](#section-4-templates--starters) → Follow the tutorial
3. **I want to DEPLOY** → Filter by 🚀 deploy → Pick a platform → Read the docs
4. **I want to CONTRIBUTE** → Follow [Step 8: Contributing](#step-8-contributing-your-own-resource)

---

**You're all set!** Start with a search or click a lifecycle badge. Happy building! 🚀
