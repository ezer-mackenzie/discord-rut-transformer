# Contributing

Thank you for improving discord-rut-transformer.

## Development setup

Fork and clone the repository, then install Poetry 2 and the locked dependencies:

```bash
poetry install
```

## Quality checks

Run the same checks as CI before opening a pull request:

```bash
poetry run ruff format --check .
poetry run ruff check .
poetry run mypy
poetry run pytest
poetry run mkdocs build --strict
poetry build
```

Tests must maintain 100% line coverage. Add tests for every behavior change and
update the documentation when the public API changes.

## Pull requests

- Keep each pull request focused on one change.
- Explain the motivation and user-visible behavior.
- Add an entry under `Unreleased` in `CHANGELOG.md` for user-facing changes.
- Use clear, imperative commit messages.
- Confirm that CI is green and resolve review feedback.

By participating, you agree to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Releases

Maintainers update the version in `pyproject.toml`, finalize the changelog,
commit the release, create an annotated `vX.Y.Z` tag, and publish the artifacts.
Breaking changes require a new major version. Publishing a GitHub Release starts
the PyPI Trusted Publishing workflow; it does not use a long-lived API token.
