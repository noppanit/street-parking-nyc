IP := $(shell docker-machine ip default)
export DATABASE_URL := postgres://postgres@$(IP)/postgres
test:
	py.test tests -s

server:
	python server.py

psql:
	psql -h "$(IP)" -U postgres
