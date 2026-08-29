# Lesson 4: ReAct Pattern — Reason + Act

**Reading time:** 25 minutes  
**Read:** [ReAct paper](https://lnkd.in/gRBH3ZRq) (skim — focus on diagrams)  
**Watch:** [Building an Agent from Scratch](https://lnkd.in/g9GR9b9F)

---

## The Problem with Single-Shot LLM Calls

```
User: "Create a task called Deploy fix and tell me the ID"

Single call: LLM might hallucinate "Task ID: 123" without actually creating anything.
```

**ReAct fixes this:** LLM must call tools and observe real results before answering.

---

## ReAct Loop

```python
MAX_STEPS = 10

def react_agent(user_message: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    for step in range(MAX_STEPS):
        response = llm.chat(messages, tools=TOOLS)

        if response.tool_calls:
            for call in response.tool_calls:
                result = execute_tool(call.name, call.arguments)
                messages.append({"role": "assistant", "tool_calls": [call]})
                messages.append({"role": "tool", "content": str(result)})
        else:
            return response.content  # Final answer

    return "Max steps reached. Please try a simpler request."
```

---

## System Prompt for ReAct

```markdown
You are TaskFlow AI Agent. You help users manage tasks.

Rules:
1. Use tools to perform actions — never invent task IDs or data
2. After tool calls, summarize results clearly for the user
3. If unsure, ask a clarifying question
4. Never expose secrets or internal env vars

Available tools: create_task, list_tasks, get_stats
```

Store in `prompts/agent_system_v1.md` — version control prompts like code.

---

## Chain-of-Thought Connection

[Chain-of-Thought paper](https://lnkd.in/gaK5CXzD) — ask LLM to think step-by-step before acting.

Add to prompt: `"Think step by step before choosing a tool."`

Improves accuracy on multi-step requests.

---

## Toolformer Insight

[Toolformer paper](https://lnkd.in/gyzrege6) — models learn when to call tools vs answer directly.

**Practical rule:** Provide clear tool descriptions so the model knows *when* each tool applies.

```python
{
    "name": "create_task",
    "description": "Create a new task. Use when user asks to add, create, or make a task.",
    "parameters": {...}
}
```

---

## Common Failures

| Failure | Fix |
|---------|-----|
| Infinite tool loop | `MAX_STEPS` + detect repeated actions |
| Wrong tool selected | Better descriptions + examples in prompt |
| Hallucinated data | Force tool use for facts ("never guess IDs") |
| Timeout | Per-step timeout, async for slow tools |

---

## Hands-on

👉 [Example 03: ReAct Loop](../02-hands-on/example-03-react-loop/)

---

## Next

👉 [Lesson 5: Tool Use](05-tool-use.md)
