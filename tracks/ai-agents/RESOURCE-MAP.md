# 50 Resources — Phased Learning Map

Every resource is assigned to a **phase**, **week**, and **action** (watch / read / build / reference).

**Legend:**  
🎬 Watch · 📖 Read · 🛠 Build · 📌 Reference (bookmark, use when needed)

---

## Phase 1: LLM Foundations (Week 7, Days 1–2)

*Goal: Understand how LLMs work before building agents.*

| # | Resource | Type | Action | When |
|---|----------|------|--------|------|
| 1 | [LLM Introduction](https://lnkd.in/gN8sv7Q5) | Video | 🎬 Watch | Day 1 morning |
| 2 | [LLMs from Scratch](https://lnkd.in/gJt-SQj2) | Video | 🎬 Watch | Day 1 afternoon |
| 3 | AI for the Rest of Us — [Book](https://lnkd.in/gTQyc_fi) | Book | 📖 Read ch 1–3 | Day 2 |
| 4 | Understanding Deep Learning — [Book](https://lnkd.in/g4xgvu_q) | Book | 📌 Reference | When ML concepts unclear |
| 5 | Building an LLM from Scratch — [Book](https://lnkd.in/g2YGbnWS) | Book | 📌 Reference | Optional deep dive |
| 6 | The LLM Engineering Handbook — [Book](https://lnkd.in/gWUT2EXe) | Book | 📖 Read ch on inference | Day 2 |
| 7 | AI Engineering — [Book](https://lnkd.in/gpfQSMCQ) | Book | 📖 Read ch on production | Week 10 |
| 8 | [Prompt Engineering Guide](https://lnkd.in/gJjGbxQr) | Repo | 🛠 Use daily | Week 7+ |
| 9 | [Improving LLM Accuracy](https://lnkd.in/gsE-4FvY) | Course | 🎬 Watch | Week 7 Day 2 |

**Build after Phase 1:** TaskFlow `/api/ai/chat` — simple LLM call with system prompt (no tools yet).

---

## Phase 2: Agent Patterns (Week 7, Days 3–7)

*Goal: Understand agent loops, ReAct, and effective agent design.*

| # | Resource | Type | Action | When |
|---|----------|------|--------|------|
| 10 | [Agentic AI Overview (Stanford)](https://lnkd.in/gk4GKdxa) | Video | 🎬 Watch | Day 3 |
| 11 | [Building and Evaluating Agents](https://lnkd.in/ghBiVjdF) | Video | 🎬 Watch | Day 3 |
| 12 | [Building Effective Agents](https://lnkd.in/g_m78sid) | Video | 🎬 Watch | Day 4 |
| 13 | [Building an Agent from Scratch](https://lnkd.in/g9GR9b9F) | Video | 🛠 Follow along | Day 4–5 |
| 14 | [Philo Agents](https://lnkd.in/gnxRq9n9) | Video | 🎬 Watch | Day 5 |
| 15 | [Google's Agent Whitepaper](https://lnkd.in/gFvCfbSN) | Guide | 📖 Read | Day 3 |
| 16 | [Google's Agent Companion](https://lnkd.in/gfmCrgAH) | Guide | 📖 Read | Day 4 |
| 17 | [Building Effective Agents by Anthropic](https://lnkd.in/gRWKANS4) | Guide | 📖 Read + apply | Day 4 |
| 18 | [OpenAI's Practical Guide to Building Agents](https://lnkd.in/guRfXsFK) | Guide | 📖 Read | Day 5 |
| 19 | [GenAI Agents repo](https://lnkd.in/gvfAc-9H) | Repo | 🛠 Clone & study | Day 5 |
| 20 | [Microsoft AI Agents for Beginners](https://lnkd.in/gK8MiVfv) | Repo | 🛠 Work through | Week 7–8 |
| 21 | [AI Agent Papers collection](https://lnkd.in/gfKQ82Fs) | Repo | 📌 Reference | Ongoing |

### Papers (implement concepts, don't just read)

| Paper | Link | Implement in |
|-------|------|--------------|
| ReAct | [lnkd.in/gRBH3ZRq](https://lnkd.in/gRBH3ZRq) | Week 7 capstone — reason + act loop |
| Chain-of-Thought | [lnkd.in/gaK5CXzD](https://lnkd.in/gaK5CXzD) | System prompts |
| Toolformer | [lnkd.in/gyzrege6](https://lnkd.in/gyzrege6) | Tool selection logic |
| Reflexion | [lnkd.in/gGFMgjUj](https://lnkd.in/gGFMgjUj) | Week 10 evals — self-correction |
| Tree of Thoughts | [lnkd.in/gRJdv_iU](https://lnkd.in/gRJdv_iU) | 📌 Reference |
| Generative Agents | [lnkd.in/gsDCUsWm](https://lnkd.in/gsDCUsWm) | 📌 Reference |
| RAG Survey | [lnkd.in/gGUqkkyR](https://lnkd.in/gGUqkkyR) | Week 8 |

**Build after Phase 2:** TaskFlow ReAct agent — create task, list tasks, get stats via tool calls.

---

## Phase 3: RAG & Vector Memory (Week 8)

*Goal: Ground agents in your docs and data.*

| # | Resource | Type | Action | When |
|---|----------|------|--------|------|
| 22 | [HuggingFace Agent Course](https://lnkd.in/gmTftTXV) | Course | 🛠 Modules 1–3 | Week 8 |
| 23 | [Building and Evaluating RAG apps](https://lnkd.in/g2qC9-mh) | Course | 🛠 Complete | Week 8 Day 1–3 |
| 24 | [Building Vector Databases with Pinecone](https://lnkd.in/gCS4sd7Y) | Course | 🎬 Watch | Week 8 Day 2 |
| 25 | [Vector Databases from Embeddings to Apps](https://lnkd.in/gm9HR6_2) | Course | 🛠 Build | Week 8 Day 3–4 |
| 26 | [Agent Memory](https://lnkd.in/gNFpC542) | Course | 🎬 Watch | Week 8 Day 5 |

**Build after Phase 3:** Index TaskFlow docs + Docker lessons → `/api/ai/ask` RAG endpoint.

---

## Phase 4: Tools & MCP (Week 8–9)

*Goal: Connect agents to GitHub, DB, Terraform, browser.*

| # | Resource | Type | Action | When |
|---|----------|------|--------|------|
| 27 | [Building Agents with MCP](https://lnkd.in/gAzBzr3W) | Video | 🛠 Follow along | Week 8 Day 6 |
| 28 | [MCP with Anthropic](https://lnkd.in/geffcwdq) | Course | 🛠 Complete | Week 9 Day 1–2 |
| 29 | [Building Browser Agents](https://lnkd.in/gsMmCifQ) | Course | 🎬 Watch | Week 9 optional |
| 30 | [Computer Use with Anthropic](https://lnkd.in/gMUWg7Fa) | Course | 📌 Reference | FDE roles |

**Build after Phase 4:** MCP server exposing: `list_tasks`, `query_github_pr`, `terraform_plan_summary`.

---

## Phase 5: Multi-Agent & Automation (Week 9)

*Goal: Orchestrate specialized agents for DevOps workflows.*

| # | Resource | Type | Action | When |
|---|----------|------|--------|------|
| 31 | [Multi-Agent Use](https://lnkd.in/gU9DY9kj) | Course | 🛠 Build | Week 9 Day 3 |
| 32 | [Multi Agent Systems](https://lnkd.in/gUayts9s) | Course | 🎬 Watch | Week 9 Day 4 |
| 33 | [Agent Design Patterns](https://lnkd.in/gzKvx5A4) | Course | 📖 Apply patterns | Week 9 |
| 34 | [Claude Code Best Agentic Coding practices](https://lnkd.in/gs99zyCf) | Guide | 🛠 Daily use | Every coding session |

**Build after Phase 5:** DevOps Agent Team — Planner + Executor + Reviewer for CI/Terraform tasks.

---

## Phase 6: Evals & LLMOps (Week 10)

*Goal: Production-grade agents with tests, monitoring, CI.*

| # | Resource | Type | Action | When |
|---|----------|------|--------|------|
| 35 | [Evaluating AI Agents](https://lnkd.in/gHJtwF5s) | Course | 🛠 Build eval suite | Week 10 Day 1–2 |
| 36 | [LLMOps](https://lnkd.in/g7bHU37w) | Course | 🛠 Apply to TaskFlow | Week 10 Day 3–4 |

**Build after Phase 6:** GitHub Action that runs agent evals on every PR + prompt version tracking.

---

## Phase 7: Agentic Coding (Daily Habit)

*Use Cursor + Claude Code patterns every day you code.*

| Resource | Link | Habit |
|----------|------|-------|
| Claude Code Best Practices | [lnkd.in/gs99zyCf](https://lnkd.in/gs99zyCf) | Rules, skills, plan-before-code |
| Your Cursor skill | `career-brand` + create `agentic-coding` skill | Project conventions |

**Automate:**
- PR descriptions from diffs
- Terraform plan summaries
- Test generation for FastAPI routes
- README updates from code changes

---

## Phase 8: Stay Current (Weekly, 30 min)

| Newsletter | Link | Focus |
|------------|------|-------|
| Gradient Ascent | [lnkd.in/gZbZAeQW](https://lnkd.in/gZbZAeQW) | ML/AI trends |
| DecodingML (Paul) | [lnkd.in/gpZPgk7J](https://lnkd.in/gpZPgk7J) | Production ML |
| Deep (Learning) Focus (Cameron) | [lnkd.in/gTUNcUVE](https://lnkd.in/gTUNcUVE) | Deep learning |
| NeoSage (Shivani) | [blog.neosage.io](https://blog.neosage.io/) | AI engineering |
| Jam with AI | [lnkd.in/gQXJzuV8](https://lnkd.in/gQXJzuV8) | Practical AI |
| Data Hustle (Sai) | [lnkd.in/gZpdTTYD](https://lnkd.in/gZpdTTYD) | Data/AI career |

**Habit:** Sunday 30 min — read one issue, note one idea, optionally write LinkedIn comment/post.

---

## Quick Reference: Week-by-Week Checklist

### Week 7
- [ ] Videos 1–8 (LLM + Agents intro)
- [ ] Guides: Anthropic + OpenAI agent guides
- [ ] Read ReAct paper + implement loop
- [ ] Capstone: TaskFlow chat agent with tools

### Week 8
- [ ] HF Agent course (start)
- [ ] RAG courses + vector DB
- [ ] MCP video + Anthropic MCP course
- [ ] Capstone: RAG + MCP server

### Week 9
- [ ] Multi-agent courses
- [ ] Agent design patterns
- [ ] Agentic coding daily with Cursor
- [ ] Capstone: DevOps multi-agent

### Week 10
- [ ] Evaluating agents course
- [ ] LLMOps course
- [ ] Reflexion paper → self-correction in agent
- [ ] Capstone: Eval pipeline in GitHub Actions

---

## Don't Do This

❌ Try to consume all 50 before building anything  
❌ Read papers without implementing a minimal version  
❌ Skip Weeks 1–3 (agents need deployment target)  
❌ Build agents without evals (Week 10 exists for a reason)

✅ One resource → one commit  
✅ TaskFlow grows every week  
✅ Portfolio + LinkedIn post after each capstone
