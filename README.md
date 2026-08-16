# discord-rut-transformer

Transformador de comandos de aplicación de Discord para validar RUT chilenos.
Usa [`rut-validator`](https://pypi.org/project/rut-validator/) y entrega un objeto
`Rut` validado directamente al callback del comando.

## Instalación

```bash
pip install discord-rut-transformer
```

## Uso

```python
import discord
from discord import app_commands
from rut_validator import Rut

from discord_rut_transformer import RutOption


class RutCommands(app_commands.Group):
    @app_commands.command()
    async def consultar(self, interaction: discord.Interaction, rut: RutOption) -> None:
        assert isinstance(rut, Rut)
        await interaction.response.send_message(rut.formatted)
```

Una entrada inválida genera `RutTransformError`, que se puede manejar en el
manejador de errores del árbol de comandos.

## Desarrollo

```bash
poetry install
poetry run pytest
poetry run ruff check .
poetry run mypy
```
