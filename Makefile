LINT:=black --check --verbose --target-version py310 *.py
TYPES:=mypy .
TEST:=py.test --doctest-modules
DOCKER_TAG:=advent-of-code
DOCKER_RUN:=docker run --rm -t $(DOCKER_TAG)
VENV_PATH:=venv

test: docker-build
	$(DOCKER_RUN) $(TEST)

lint: docker-build
	$(DOCKER_RUN) $(LINT)

types: docker-build
	$(DOCKER_RUN) $(TYPES)


docker-build:
	docker build -t $(DOCKER_TAG) .

clean:
	rm -rf $(VENV_PATH)

venv:
	python3 -m venv $(VENV_PATH) && \
		source venv/bin/activate && \
		pip install -r requirements.txt -r test_requirements.txt

# Test & Lint whenever a file changes (Docker)
watch-test-and-lint:
	while true; \
		do fswatch -1 .; \
		clear; \
		make test lint types; \
		sleep 0.3; \
	done

# Test & Lint whenever a file changes using a virtual environemnt.
# Faster, but not assured to be
watch-test-and-lint-venv: venv
	while true; \
		do \
			fswatch -1 -e '\..*' .; \
			clear; \
			source venv/bin/activate && \
			$(TEST) && \
			$(LINT) && \
			$(TYPES) && \
		sleep 0.3; \
	done
