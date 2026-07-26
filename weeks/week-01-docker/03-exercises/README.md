# Week 1 Practice Exercises

**Rules:**
1. Try each exercise **without** looking at solutions
2. Time yourself — 20–30 min per exercise
3. If stuck >15 min, read the hint
4. After solving, compare with solution and understand differences
5. Commit your work: `git commit -m "week-01: exercise 01 complete"`

Solutions are in [`solutions/`](solutions/) — resist peeking!

---

## Exercise 1: Fix the Broken Dockerfile

**Difficulty:** Easy  
**Time:** 20 min

**Location:** [`exercise-01-broken-dockerfile/`](exercise-01-broken-dockerfile/)

The Dockerfile builds but the container exits immediately or curl fails.

**Your task:**
1. Identify all issues (there are 4+)
2. Fix the Dockerfile and/or app
3. Successfully run: `curl http://localhost:5000/health`

**Hint:** Check what address the app binds to, user permissions, and CMD format.

---

## Exercise 2: Optimize Image Size

**Difficulty:** Medium  
**Time:** 30 min

**Location:** [`exercise-02-optimize-image/`](exercise-02-optimize-image/)

A bloated Python Dockerfile is provided (~450MB).

**Your task:**
1. Reduce image size by at least 50% without changing app behavior
2. Document what you changed and size before/after in `NOTES.md`
3. Keep non-root user and health check

**Hints:** Base image choice, layer combining, .dockerignore, unnecessary packages.

---

## Exercise 3: Add Health Checks and Restart Policy

**Difficulty:** Medium  
**Time:** 25 min

**Location:** [`exercise-03-healthchecks/`](exercise-03-healthchecks/)

A compose stack starts but API reports unhealthy under load.

**Your task:**
1. Add proper HEALTHCHECK to Dockerfile
2. Configure compose with `restart: unless-stopped`
3. Add db healthcheck with `depends_on: condition: service_healthy`
4. Verify with `docker compose ps` — all services healthy

---

## Exercise 4: Environment Variables and Secrets

**Difficulty:** Easy  
**Time:** 20 min

**Location:** [`exercise-04-env-vars/`](exercise-04-env-vars/)

**Your task:**
1. Create `.env.example` (safe to commit) and use `.env` (gitignored)
2. Wire DATABASE_URL and API_KEY through compose without hardcoding in Dockerfile
3. App should read env vars and expose `/config` showing env names (not secret values!)

**Security rule:** API_KEY must never appear in `docker history` or image layers.

---

## Exercise 5: Compose Networking Debug

**Difficulty:** Medium  
**Time:** 30 min

**Location:** [`exercise-05-networking/`](exercise-05-networking/)

Two services can't communicate. Error: `Connection refused to localhost:5432`.

**Your task:**
1. Fix connection strings to use Docker DNS
2. Remove unnecessary port exposures on internal services
3. Document in `FIX.md` why `localhost` failed

---

## Exercise 6: Volume Persistence

**Difficulty:** Medium  
**Time:** 25 min

**Location:** [`exercise-06-volumes/`](exercise-06-volumes/)

**Your task:**
1. Configure named volume for SQLite/Postgres data
2. Write data, run `docker compose down`, then `docker compose up -d`
3. Prove data survived in README with command output
4. Run `docker compose down -v` and prove data is gone

---

## Self-Assessment

After all exercises, you should confidently:

- [ ] Debug a failing container in under 10 minutes
- [ ] Write a production Dockerfile from scratch
- [ ] Compose a 3-tier stack with healthchecks
- [ ] Explain every line of your Dockerfile in an interview

---

## Next

👉 **[Capstone Project: TaskFlow Platform](../04-capstone-project/README.md)**

When stuck, ask me — explain what you tried and the error message.
