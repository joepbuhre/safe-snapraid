ROOT_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

dev:
	docker run --rm -v $(ROOT_DIR):/app safesnapraid:dev-lc

build:
	docker build . -t safesnapraid:dev-lc

test:
	docker run --rm safesnapraid:dev-lc --test