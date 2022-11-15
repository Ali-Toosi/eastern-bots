.PHONY: local-up
local-up:
	@docker-compose -f local.yml up -d

.PHONY: local-down
local-down:
	@docker-compose -f local.yml down

.PHONY: local-restart
local-restart:
	@docker-compose -f local.yml restart django

.PHONY: local-rebuild
local-rebuild:
	@docker-compose -f local.yml stop django
	@docker-compose -f local.yml build django
	@docker-compose -f local.yml start django

.PHONY: local-manage
local-manage:
	@docker-compose -f local.yml run --rm django python manage.py $(cmd)

.PHONY: local-logs
local-logs:
	@docker-compose -f local.yml logs -f

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
