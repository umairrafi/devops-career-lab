# Week 7: AI Agents — Foundations & First Agent

**Duration:** 7 days (20–25 hours)  
**Prerequisites:** Week 1 Docker (TaskFlow running), Python/FastAPI comfort  
**Outcome:** Working ReAct-style agent on TaskFlow with tool use

**Resource track:** [AI Agents Track](../../tracks/ai-agents/README.md) — Phase 1 & 2

---

## What You'll Build

```
TaskFlow API
    └── /api/ai/chat          ← LLM conversation
    └── /api/ai/agent         ← Agent with tools (create/list tasks)
    └── agent/
        ├── llm_client.py     ← OpenAI/Anthropic/Ollama wrapper
        ├── tools.py          ← TaskFlow tool definitions
        ├── react_loop.py     ← ReAct: Reason → Act → Observe
        └── prompts/          ← Version-controlled system prompts
```

---

## Weekly Schedule

| Day | Resources (from 50-list) | Build |
|-----|--------------------------|-------|
| **1** | LLM Intro video, LLMs from Scratch | LLM client + `/api/ai/chat` |
| **2** | LLM Engineering Handbook, Improving LLM Accuracy | Prompts, error handling |
| **3** | Stanford Agentic AI, Google Agent Whitepaper | Agent architecture design |
| **4** | Anthropic Effective Agents, Building Agent from Scratch | ReAct loop |
| **5** | OpenAI Agent Guide, GenAI Agents repo | Tool definitions |
| **6** | ReAct paper + Microsoft Agents repo | Wire tools to TaskFlow API |
| **7** | — | Capstone polish + README + demo |

Full resource links: [RESOURCE-MAP.md](../../tracks/ai-agents/RESOURCE-MAP.md)

---

## Lessons

| # | Lesson | File |
|---|--------|------|
| 1 | What is an AI agent (vs chatbot) | [01-what-is-an-agent.md](01-lessons/01-what-is-an-agent.md) |
| 2 | LLM APIs — OpenAI, Anthropic, Ollama | [02-llm-apis.md](01-lessons/02-llm-apis.md) |
| 3 | Prompt engineering for agents | [03-prompt-engineering.md](01-lessons/03-prompt-engineering.md) |
| 4 | ReAct pattern — Reason + Act | [04-react-pattern.md](01-lessons/04-react-pattern.md) |
| 5 | Tool use and function calling | [05-tool-use.md](01-lessons/05-tool-use.md) |
| 6 | Agent design (Anthropic/OpenAI guides) | [06-agent-design.md](01-lessons/06-agent-design.md) |

---

## Hands-on Examples

| # | Example | Folder |
|---|---------|--------|
| 1 | Hello LLM — first API call | [example-01-hello-llm](02-hands-on/example-01-hello-llm/) |
| 2 | Function calling | [example-02-function-calling](02-hands-on/example-02-function-calling/) |
| 3 | Mini ReAct loop | [example-03-react-loop](02-hands-on/example-03-react-loop/) |

---

## Exercises

[03-exercises/README.md](03-exercises/README.md)

1. Fix a broken agent loop (infinite loop)
2. Add a new tool (`delete_task`)
3. Improve system prompt for edge cases
4. Handle API rate limits gracefully

---

## Capstone

[04-capstone-project/README.md](04-capstone-project/README.md) — **TaskFlow AI Agent v1**

Requirements:
- [ ] `/api/ai/chat` — basic chat
- [ ] `/api/ai/agent` — agent with ≥3 tools
- [ ] ReAct loop with max iterations guard
- [ ] Prompts in `prompts/` folder (version controlled)
- [ ] Works with OpenAI OR Ollama (config via env)
- [ ] README with architecture diagram

---

## Environment Setup

```bash
# Add to TaskFlow .env
OPENAI_API_KEY=sk-...          # or
ANTHROPIC_API_KEY=sk-ant-...   # or local:
OLLAMA_BASE_URL=http://localhost:11434
AI_PROVIDER=openai             # openai | anthropic | ollama

# Python deps (add to api/requirements.txt)
# openai>=1.30.0
# anthropic>=0.25.0
# httpx>=0.27.0
```

---

## Key Concepts for Interviews

1. **Agent vs chatbot:** Agent chooses actions via tools; chatbot only generates text.
2. **ReAct:** Thought → Action → Observation loop until task complete.
3. **Tool design:** Clear names, typed parameters, idempotent when possible.
4. **Guardrails:** Max iterations, timeout, human approval for destructive actions.

---

## Progress Checklist

```
Lessons
[ ] 01 - What is an agent
[ ] 02 - LLM APIs
[ ] 03 - Prompt engineering
[ ] 04 - ReAct pattern
[ ] 05 - Tool use
[ ] 06 - Agent design

Hands-on
[ ] Example 01 - Hello LLM
[ ] Example 02 - Function calling
[ ] Example 03 - ReAct loop

Exercises
[ ] All 4 exercises

Capstone
[ ] TaskFlow AI Agent v1 running
[ ] Demo video or curl examples in README
[ ] Pushed to GitHub
```

---

## Next Week

**Week 8:** RAG + Vector DB + MCP — [../week-08-rag-mcp/README.md](../week-08-rag-mcp/README.md)

---

## Start

👉 [Lesson 1: What is an AI Agent](01-lessons/01-what-is-an-agent.md)
