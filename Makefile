all: install format test build changelog

documentation:
	jupyter-book clean docs
	jupyter-book build docs

format:
	black . -l 79
	linecheck . --fix

install:
	pip install -e .[dev]

test:
	policyengine-core test -c policyengine_canada policyengine_canada/tests

build:
	python -m build

changelog:
	python .github/bump_version.py
	towncrier build --yes --version $$(python -c "import re; print(re.search(r'version = \"(.+?)\"', open('pyproject.toml').read()).group(1))")