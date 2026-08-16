# Error handling

Invalid values raise `RutTransformError`, an `AppCommandError` subclass. The
exception stores the original user input in `value` and chains the underlying
rut-validator exception as its cause.

```python
import discord

from discord_rut_transformer import RutTransformError


@tree.error
async def on_app_command_error(
    interaction: discord.Interaction,
    error: discord.app_commands.AppCommandError,
) -> None:
    if isinstance(error, RutTransformError):
        await interaction.response.send_message(str(error), ephemeral=True)
        return

    raise error
```

Malformed or empty values report a format error. Structurally valid values with
an incorrect check digit report a check-digit error. Do not log unmasked RUTs in
production unless your privacy policy explicitly permits it.
