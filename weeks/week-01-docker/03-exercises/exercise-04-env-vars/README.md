# Exercise 04 — Environment Variables

Build a small API that reads:
- `APP_ENV` (e.g. development, production)
- `API_KEY` (secret — runtime only)

Requirements:
1. Create `.env.example` with placeholder values
2. Use `env_file: .env` in compose
3. `/config` endpoint returns `{"app_env": "...", "api_key_set": true}` — never the actual key
4. `.env` in `.gitignore`

Verify secret not in image:
```bash
docker history your-image | grep -i api_key  # should return nothing
```
