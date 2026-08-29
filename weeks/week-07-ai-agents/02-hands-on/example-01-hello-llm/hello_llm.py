#!/usr/bin/env python3
"""Example 01: Hello LLM — first API call with OpenAI or Ollama."""

import os
import sys

PROVIDER = os.getenv("AI_PROVIDER", "ollama")


def chat_openai(message: str) -> str:
    from openai import OpenAI

    client = OpenAI()
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful DevOps tutor."},
            {"role": "user", "content": message},
        ],
    )
    return r.choices[0].message.content or ""


def chat_ollama(message: str) -> str:
    import httpx

    base = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    r = httpx.post(
        f"{base}/api/chat",
        json={
            "model": os.getenv("OLLAMA_MODEL", "llama3.2"),
            "messages": [{"role": "user", "content": message}],
            "stream": False,
        },
        timeout=120.0,
    )
    r.raise_for_status()
    return r.json()["message"]["content"]


def main():
    message = sys.argv[1] if len(sys.argv) > 1 else "Explain Docker in one paragraph."
    print(f"Provider: {PROVIDER}\n")

    if PROVIDER == "openai":
        print(chat_openai(message))
    elif PROVIDER == "ollama":
        print(chat_ollama(message))
    else:
        print(f"Set AI_PROVIDER=openai or ollama (got {PROVIDER})")
        sys.exit(1)


if __name__ == "__main__":
    main()
