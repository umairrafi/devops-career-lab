# Exercise 06 — Volume Persistence

Complete the compose file to persist Postgres data across restarts.

Prove persistence:
1. POST a note via API
2. `docker compose down` (no -v)
3. `docker compose up -d`
4. GET notes — data still there

Then prove deletion with `docker compose down -v`.

Scaffold provided — implement volumes and API CRUD for `notes` table.
