# Week 10: Agent Evals & LLMOps

**Prerequisites:** Week 9 complete  
**Resources:** Evaluating AI Agents, LLMOps, Reflexion paper — see [RESOURCE-MAP](../../tracks/ai-agents/RESOURCE-MAP.md) Phase 7

## You Build

- Eval dataset: 20+ test cases for TaskFlow agent
- GitHub Action: run evals on PR
- Token/cost logging
- Prompt versioning (git tags)
- Self-correction loop (Reflexion-inspired)

## Capstone

**Agent CI Pipeline** — bad prompt changes fail PR checks before merge.

Connects to Week 3 GitHub Actions skills.

## Production Readiness Checklist

- [ ] Eval pass rate > 90% on golden set
- [ ] P95 latency logged
- [ ] Cost per request tracked
- [ ] Fallback provider configured
- [ ] No secrets in traces/logs

👉 Full course content added when you start Week 10.
