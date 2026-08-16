# discord-rut-transformer

[![CI](https://github.com/ezer-mackenzie/discord-rut-transformer/actions/workflows/ci.yml/badge.svg)](https://github.com/ezer-mackenzie/discord-rut-transformer/actions/workflows/ci.yml)
[![Codecov](https://codecov.io/gh/ezer-mackenzie/discord-rut-transformer/graph/badge.svg)](https://codecov.io/gh/ezer-mackenzie/discord-rut-transformer)
[![Documentation](https://readthedocs.org/projects/discord-rut-transformer/badge/?version=stable)](https://discord-rut-transformer.readthedocs.io/en/stable/)
[![Python](https://img.shields.io/pypi/pyversions/discord-rut-transformer.svg)](https://pypi.org/project/discord-rut-transformer/)
[![PyPI](https://img.shields.io/pypi/v/discord-rut-transformer.svg)](https://pypi.org/project/discord-rut-transformer/)

A small, typed [discord.py](https://discordpy.readthedocs.io/) app-command
transformer that validates Chilean RUT values before your command callback runs.
It is built on [rut-validator](https://pypi.org/project/rut-validator/).

## Installation

```bash
python -m pip install discord-rut-transformer
```

Python 3.12 through 3.14 are supported.

## Quick start

```python
import discord
from discord import app_commands

from discord_rut_transformer import RutOption


class TaxCommands(app_commands.Group):
    @app_commands.command(description="Look up a Chilean RUT")
    async def lookup(
        self,
        interaction: discord.Interaction,
        rut: RutOption,
    ) -> None:
        await interaction.response.send_message(rut.formatted, ephemeral=True)
```

The user enters a string such as `12.345.678-5`; the callback receives a
validated `rut_validator.Rut` object with `formatted`, `hyphenated`,
`normalized`, `body`, and `check_digit` properties. Invalid input raises
`RutTransformError` through discord.py's application-command error flow.

## Documentation

The complete guide, error-handling examples, API reference, and compatibility
policy are available on [Read the Docs](https://discord-rut-transformer.readthedocs.io/).

## Development

```bash
poetry install
poetry run pytest
poetry run ruff format --check .
poetry run ruff check .
poetry run mypy
poetry run mkdocs build --strict
poetry build
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the complete workflow.

## Stability

The `1.x` series is production/stable and follows Semantic Versioning. Public
imports documented in the API reference remain backward compatible throughout
the major version. See [CHANGELOG.md](CHANGELOG.md) for release notes.

## License

Distributed under the MIT License. See [LICENSE.md](LICENSE.md).
