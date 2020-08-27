VENV=.venv
BIN=$(VENV)/bin
PIP_OPTS = -Uqr


$(VENV):
	python3 -m venv $(VENV)

setup: $(VENV)
	$(BIN)/pip install $(PIP_OPTS) requirements.txt

test: setup
	-$(BIN)/flake8 --exclude="$(VENV)"
	$(BIN)/python -m unittest discover

clean:
	find . -name "$(VENV)" -prune -o -name "*.pyc" -print -exec rm {} \;
	find . -name "$(VENV)" -prune -o -type d -name __pycache__ -prune \
	-print -exec rm -rf {} \;
