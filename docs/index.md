# discord-rut-transformer

`discord-rut-transformer` converts a Discord application-command string into a
validated, immutable Chilean RUT value.

```python
from discord import Interaction, app_commands
from discord_rut_transformer import RutOption


@app_commands.command()
async def lookup(interaction: Interaction, rut: RutOption) -> None:
    await interaction.response.send_message(rut.formatted)
```

## Why use it?

- Validation happens before the command callback runs.
- Callbacks receive a typed `rut_validator.Rut`, not an unchecked string.
- Format and check-digit failures become one Discord-friendly exception.
- The package includes type information for mypy and other type checkers.

[Get started](getting-started.md){ .md-button .md-button--primary }
[View the API](api.md){ .md-button }

## Compatibility

The stable `1.x` series supports Python 3.12 through 3.14, discord.py 2.7, and
rut-validator 1.x.
