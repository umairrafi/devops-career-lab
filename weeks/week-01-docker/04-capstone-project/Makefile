.PHONY: up down logs ps test health clean

up:
	docker compose up -d --build

down:
	docker compose down

down-v:
	docker compose down -v

logs:
	docker compose logs -f

ps:
	docker compose ps

health:
	curl -s http://localhost/health | python3 -m json.tool

test:
	curl -s http://localhost/api/projects | python3 -m json.tool
	curl -s http://localhost/api/tasks | python3 -m json.tool
	curl -s http://localhost/api/stats | python3 -m json.tool

clean:
	docker compose down -v --rmi local
