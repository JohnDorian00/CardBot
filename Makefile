# Docker Makefile
up:
	docker-compose down
	docker-compose --env-file .env.dev  up -d --build

prod:
	docker-compose --env-file .env.prod  up -d --build

down:
	docker-compose down