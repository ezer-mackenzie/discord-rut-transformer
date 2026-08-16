"""Discord application-command transformer for Chilean RUT values."""

from importlib.metadata import version

from .errors import RutTransformError
from .transformer import RutTransformer
from .types import RutOption

__all__ = ["RutOption", "RutTransformError", "RutTransformer"]
__version__ = version("discord-rut-transformer")
