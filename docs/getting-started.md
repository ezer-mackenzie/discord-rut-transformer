# Getting started

## Requirements

- Python 3.12 or newer
- A discord.py application using application commands

## Installation

Install the stable release from PyPI:

```bash
python -m pip install discord-rut-transformer
```

## First command

Annotate a slash-command parameter with `RutOption`:

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
        await interaction.response.send_message(
            f"Validated RUT: {rut.formatted}",
            ephemeral=True,
        )
```

The callback runs only after the argument passes format and modulo-eleven
validation. Its `rut` argument is a `rut_validator.Rut` instance.

## Register the command

Add the group to your command tree and sync it using your application's normal
startup flow. discord.py command registration is unchanged by this package.
