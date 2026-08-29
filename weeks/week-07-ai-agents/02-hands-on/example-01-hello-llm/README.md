# Example 01: Hello LLM

**Time:** 15 minutes

## Setup

```bash
cd weeks/week-07-ai-agents/02-hands-on/example-01-hello-llm

# Option A: Local free (Ollama)
ollama pull llama3.2
export AI_PROVIDER=ollama
python hello_llm.py "What is an AI agent?"

# Option B: OpenAI
pip install openai httpx
export AI_PROVIDER=openai
export OPENAI_API_KEY=sk-...
python hello_llm.py "What is an AI agent?"
```

## What you learned

- LLM API request/response shape
- System vs user messages
- Provider abstraction pattern (used in capstone)

## Next

Example 02: Function calling
