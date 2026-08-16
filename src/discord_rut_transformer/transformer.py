"""RUT transformer for Discord application commands."""

import discord
from discord import app_commands
from rut_validator import (
    Rut,
    RutInvalidFormatError,
    RutInvalidValueError,
    RutModuleElevenValidationError,
    validate_rut,
)

from .errors import RutTransformError


class RutTransformer(app_commands.Transformer):
    """Convert a string command option into a validated :class:`Rut` object."""

    @property
    def type(self) -> discord.AppCommandOptionType:
        return discord.AppCommandOptionType.string

    async def transform(self, interaction: discord.Interaction, value: str) -> Rut:
        """Validate *value* and return its immutable RUT representation."""
        del interaction
        try:
            return validate_rut(value)

        except (RutInvalidFormatError, RutInvalidValueError) as exc:
            raise RutTransformError(
                value, "El RUT debe tener un formato chileno válido."
            ) from exc

        except RutModuleElevenValidationError as exc:
            raise RutTransformError(
                value, "El dígito verificador del RUT no es válido."
            ) from exc
