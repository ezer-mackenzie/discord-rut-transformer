"""Public type aliases for Discord command parameters."""

from discord import app_commands
from rut_validator import Rut

from .transformer import RutTransformer

type RutOption = app_commands.Transform[Rut, RutTransformer]
