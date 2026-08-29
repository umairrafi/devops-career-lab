# Week 7 Capstone: TaskFlow AI Agent v1

**Goal:** Production-style agent integrated into TaskFlow FastAPI app.

---

## Architecture

```
POST /api/ai/agent
        │
        ▼
┌───────────────┐
│ Agent Router  │  (FastAPI)
└───────┬───────┘
        ▼
┌───────────────┐
│ ReAct Loop    │  max 10 steps
└───────┬───────┘
        ▼
┌───────────────┐     ┌─────────────────┐
│ LLM Client    │────▶│ OpenAI/Claude/  │
└───────────────┘     │ Ollama          │
        │             └─────────────────┘
        ▼
┌───────────────┐
│ Tools         │
│ · create_task │
│ · list_tasks  │
│ · get_stats   │
└───────┬───────┘
        ▼
   TaskFlow DB / Redis (existing)
```

---

## Requirements

### API Endpoints

```bash
# Simple chat (no tools)
curl -X POST http://localhost/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is TaskFlow?"}'

# Agent with tools
curl -X POST http://localhost/api/ai/agent \
  -H "Content-Type: application/json" \
  -d '{"message": "Create a high priority task: Complete Week 7 capstone"}'
```

### Tools (minimum 3)

| Tool | Maps to |
|------|---------|
| `create_task` | POST /api/tasks |
| `list_tasks` | GET /api/tasks |
| `get_stats` | GET /api/stats |

Implement by calling existing Python functions — not HTTP to yourself.

### Code structure

```
api/app/ai/
├── __init__.py
├── llm_client.py
├── react_loop.py
├── tools.py
└── router.py
prompts/
├── agent_system_v1.md
└── chat_system_v1.md
```

---

## Acceptance Criteria

- [ ] Agent creates real task in Postgres (verify via GET /api/tasks)
- [ ] Max iteration guard prevents infinite loops
- [ ] Provider swappable via `AI_PROVIDER` env
- [ ] No API keys in Git
- [ ] README with curl examples and demo screenshot
- [ ] LinkedIn post: "Built my first production AI agent"

---

## Stretch Goals

- [ ] Streaming responses (SSE)
- [ ] Conversation session ID (memory across turns)
- [ ] LangSmith or simple JSON logging of agent traces

---

## Interview Pitch

> "I built a ReAct agent on TaskFlow using Python and FastAPI. It uses function calling to create and list tasks against a real Postgres backend, with provider abstraction for OpenAI and Ollama, max-step guards, and version-controlled prompts in Git."

---

## After Capstone

Week 8 adds **RAG** (ask questions about Docker docs) and **MCP** (standardized tools).

See: [Week 8 README](../../week-08-rag-mcp/README.md)
