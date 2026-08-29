# Lesson 2: LLM APIs — OpenAI, Anthropic, Ollama

**Reading time:** 25 minutes  
**Watch:** [LLMs from Scratch](https://lnkd.in/gJt-SQj2) (conceptual overview)

---

## Three Providers for This Course

| Provider | Best for | Env var |
|----------|----------|---------|
| **OpenAI** | Function calling, wide docs | `OPENAI_API_KEY` |
| **Anthropic** | Long context, safety, MCP | `ANTHROPIC_API_KEY` |
| **Ollama** | Free local dev, offline | `OLLAMA_BASE_URL` |

Use one abstraction in code — swap via `AI_PROVIDER` env.

---

## OpenAI Chat Completions (Python)

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are TaskFlow assistant."},
        {"role": "user", "content": "List my open tasks"},
    ],
)
print(response.choices[0].message.content)
```

---

## Anthropic Messages API

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system="You are TaskFlow assistant.",
    messages=[{"role": "user", "content": "List my open tasks"}],
)
print(message.content[0].text)
```

---

## Ollama (Local — Free)

```bash
ollama pull llama3.2
ollama serve   # default :11434
```

```python
import httpx

response = httpx.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "llama3.2",
        "messages": [{"role": "user", "content": "Hello"}],
        "stream": False,
    },
)
print(response.json()["message"]["content"])
```

**Tip:** Use Ollama for Week 7 dev; use cloud APIs for evals and demos.

---

## Unified Client Pattern

```python
# agent/llm_client.py — pattern for capstone
import os

PROVIDER = os.getenv("AI_PROVIDER", "openai")

def chat(messages: list[dict], tools: list | None = None) -> str:
    if PROVIDER == "openai":
        return _openai_chat(messages, tools)
    if PROVIDER == "anthropic":
        return _anthropic_chat(messages, tools)
    if PROVIDER == "ollama":
        return _ollama_chat(messages)
    raise ValueError(f"Unknown provider: {PROVIDER}")
```

This matches how you'd swap Lambda runtimes — same interface, different backend.

---

## Messages Format

All providers use similar structure:

```python
messages = [
    {"role": "system", "content": "..."},   # Instructions
    {"role": "user", "content": "..."},     # Human
    {"role": "assistant", "content": "..."}, # Model
    {"role": "tool", "content": "...", "tool_call_id": "..."},  # Tool result
]
```

Keep conversation history in a list — that's **short-term memory**.

---

## Cost & Production Tips

- Use **gpt-4o-mini** or **claude-haiku** for dev
- Log `input_tokens` / `output_tokens` per request
- Set `max_tokens` limit
- Cache system prompts where provider supports it
- Never commit API keys — use `.env` + Secrets Manager in prod

---

## Hands-on

👉 [Example 01: Hello LLM](../02-hands-on/example-01-hello-llm/)

---

## Next

👉 [Lesson 3: Prompt Engineering](03-prompt-engineering.md)
