all: install format test build changelog

documentation:
	uv run python -m jupyter_book clean docs
	uv run python -m jupyter_book build docs

format:
	uv run black . -l 79
	uv run linecheck . --fix

install:
	uv sync

test:
	uv run policyengine-core test -c policyengine_canada policyengine_canada/tests

build:
	uv build

changelog:
	uv run build-changelog changelog.yaml --output changelog.yaml --update-last-date --start-from 0.0.0 --append-file changelog_entry.yaml
	uv run build-changelog changelog.yaml --org PolicyEngine --repo policyengine-canada --output CHANGELOG.md --template .github/changelog_template.md
	uv run bump-version changelog.yaml pyproject.toml
	rm changelog_entry.yaml || true
	touch changelog_entry.yaml
