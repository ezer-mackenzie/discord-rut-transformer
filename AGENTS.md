# Repository guidelines

This repository contains a small, typed Python library that integrates
`rut-validator` with discord.py application commands. Keep changes focused and
preserve the public API unless the project is preparing a major release.

## Project layout

- `src/discord_rut_transformer/` contains the distributed package.
- `tests/` contains the pytest suite.
- `docs/` contains the MkDocs documentation source.
- `pyproject.toml` and `poetry.lock` define the Python environments.
- `.github/workflows/` contains CI and Trusted Publishing automation.

## Public API

The following package-root imports are stable in the `1.x` series:

```python
from discord_rut_transformer import (
    RutOption,
    RutTransformer,
    RutTransformError,
)
```

`RutTransformer.transform` must return a validated `rut_validator.Rut` object,
not a string. Keep `RutOption` in `types.py` and exceptions in `errors.py`.

## Development workflow

Use Poetry for dependency management and command execution:

```bash
poetry install
poetry run ruff format --check .
poetry run ruff check .
poetry run mypy
poetry run pytest
poetry run mkdocs build --strict
poetry check
poetry build
```

All checks must pass before committing. Tests must retain 100% line coverage.
Add or update tests whenever behavior changes, and update the English
documentation for public API or workflow changes.

## Style and compatibility

- Support Python 3.12 through 3.14.
- Use strict type annotations for source and test code.
- Follow Ruff formatting and lint rules from `pyproject.toml`.
- Keep user-facing Discord errors concise and avoid exposing real RUT values in
  logs, fixtures, or documentation.
- Do not add runtime dependencies when a standard-library solution is adequate.

## Releases

The project follows Semantic Versioning. Patch releases contain compatible
fixes and documentation changes; breaking API changes require a new major
version. Update `pyproject.toml`, package-version tests, and `CHANGELOG.md`
together. Never move or overwrite a published tag.

PyPI publication is performed only by `.github/workflows/publish.yml` through
the protected `pypi` environment and Trusted Publishing. Do not add API tokens
or publish locally. Read the Docs installs the locked `docs` dependency group
through Poetry as configured in `.readthedocs.yaml`.
