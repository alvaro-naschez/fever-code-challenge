run:
	docker compose up --remove-orphans --build --scale postgresql-test=0
down:
	docker compose down
