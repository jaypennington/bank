VENV = env
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

test: $(VENV)/bin/activate
	$(PYTEST) test/*

clean:
	rm -rf .pytest_cache/
	rm -rf __pycache__
	rm -rf $(VENV)