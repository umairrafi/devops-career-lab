# Lesson 1: What is an AI Agent?

**Reading time:** 20 minutes  
**Watch first:** [Agentic AI Overview (Stanford)](https://lnkd.in/gk4GKdxa)

---

## Chatbot vs Agent

| | Chatbot | AI Agent |
|---|---------|----------|
| **Output** | Text only | Text + **actions** |
| **Tools** | None | APIs, DB, files, shell, MCP |
| **Loop** | Single turn or conversation | Observe → Think → Act → repeat |
| **Example** | "Explain Docker" | "Create a task and confirm it exists" |

**Interview line:** "A chatbot generates responses. An agent uses an LLM as a reasoning engine and executes tools to accomplish goals in the environment."

---

## The Agent Loop

```
┌─────────────────────────────────────────┐
│  User: "Create a high-priority task       │
│         to review Terraform plan"         │
└──────────────────┬──────────────────────┘
                   ▼
┌─────────────────────────────────────────┐
│  LLM (Reasoning)                        │
│  "I need to call create_task with       │
│   priority=high"                        │
└──────────────────┬──────────────────────┘
                   ▼
┌─────────────────────────────────────────┐
│  Tool: create_task(title, priority)     │
│  → { "id": 42, "status": "created" }    │
└──────────────────┬──────────────────────┘
                   ▼
┌─────────────────────────────────────────┐
│  LLM (Respond)                          │
│  "Created task #42: Review Terraform"   │
└─────────────────────────────────────────┘
```

---

## Core Components

1. **LLM** — reasoning and language (GPT-4, Claude, Llama via Ollama)
2. **System prompt** — role, rules, tool descriptions
3. **Tools** — functions the agent can call (your Python/API code)
4. **Memory** — conversation history (+ RAG in Week 8)
5. **Orchestrator** — loop that runs until done or max steps

---

## Why Backend Engineers Win at Agents

You already build:
- REST APIs → **tools**
- Lambda handlers → **tool executors**
- Secrets Manager → **secure credentials for agents**
- Event loops (SQS) → **agent observe/act cycles**
- Flask/FastAPI → **agent HTTP interface**

Agents are **orchestration** on top of skills you have.

---

## ReAct (Preview — Lesson 4)

**Re**asoning + **Act**ion — from the [ReAct paper](https://lnkd.in/gRBH3ZRq):

```
Thought: User wants a new task. I should use create_task.
Action: create_task(title="Review Terraform", priority="high")
Observation: {"id": 42, "title": "Review Terraform"}
Thought: Task created. I can respond to user.
Answer: Created task #42.
```

You'll implement this in the capstone.

---

## Safety Basics

- **Max iterations** — prevent infinite loops (e.g. 10 steps max)
- **Tool allowlist** — agent only calls defined tools
- **Human-in-the-loop** — confirm before delete/deploy
- **No secrets in prompts** — use env/IAM like your Secrets Manager work

---

## Check Your Understanding

1. What's the difference between an agent and a chatbot?
2. Name 3 components every agent needs.
3. Why should agents have a max iteration limit?

<details>
<summary>Answers</summary>

1. Agents take actions via tools; chatbots only output text.
2. LLM, tools, orchestrator loop (also: prompts, memory).
3. Prevents runaway loops, runaway cost, and infinite API calls.

</details>

---

## Next

👉 [Lesson 2: LLM APIs](02-llm-apis.md)  
🎬 Watch: [LLM Introduction](https://lnkd.in/gN8sv7Q5)
