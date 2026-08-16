"""Exceptions raised by discord-rut-transformer."""

from discord import app_commands


class RutTransformError(app_commands.AppCommandError):
    """Raised when a Discord command argument is not a valid Chilean RUT."""

    def __init__(self, value: object, message: str | None = None) -> None:
        self.value = value
        super().__init__(message or f"El RUT {value!r} no es válido")
