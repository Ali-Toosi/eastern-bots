.PHONY: migrations
migrations:
	@docker-compose -f local.yml run --rm django python manage.py makemigrations

.PHONY: up
up:
	@docker-compose -f local.yml up -d

.PHONY: down
down:
	@docker-compose -f local.yml down

.PHONY: restart
restart:
	@docker-compose -f local.yml restart django

.PHONY: rebuild
rebuild:
	@docker-compose -f local.yml stop django
	@docker-compose -f local.yml up --build -d django

.PHONY: manage
manage:
	@docker-compose -f local.yml run --rm django python manage.py $(cmd)

.PHONY: logs
logs:
	@docker-compose -f local.yml logs -f --tail 100 django

.PHONY: prod-up
prod-up:
	@docker-compose -f production.yml up -d

.PHONY: prod-down
prod-down:
	@docker-compose -f production.yml down

.PHONY: prod-restart
prod-restart:
	@docker-compose -f production.yml down && docker-compose -f production.yml up -d

.PHONY: prod-manage
prod-manage:
	@docker-compose -f production.yml run --rm django python manage.py $(cmd)

.PHONY: prod-logs
prod-logs:
	@docker-compose -f production.yml logs -f
