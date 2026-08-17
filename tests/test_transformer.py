import asyncio
from unittest.mock import Mock

import discord
import pytest
from rut_validator import Rut

from discord_rut_transformer import RutTransformer, RutTransformError, __version__


def test_transform_returns_validated_rut() -> None:
    interaction = Mock(spec=discord.Interaction)

    result = asyncio.run(RutTransformer().transform(interaction, "12.345.678-5"))

    assert isinstance(result, Rut)
    assert result.normalized == "123456785"
    assert result.formatted == "12.345.678-5"


def test_transform_rejects_invalid_rut() -> None:
    interaction = Mock(spec=discord.Interaction)

    with pytest.raises(RutTransformError, match="no es válido") as error:
        asyncio.run(RutTransformer().transform(interaction, "12.345.678-9"))

    assert error.value.value == "12.345.678-9"


@pytest.mark.parametrize("value", ["", "not-a-rut"])
def test_transform_rejects_invalid_input(value: str) -> None:
    interaction = Mock(spec=discord.Interaction)

    with pytest.raises(RutTransformError, match="formato chileno válido") as error:
        asyncio.run(RutTransformer().transform(interaction, value))

    assert error.value.value == value


def test_transformer_declares_string_option() -> None:
    assert RutTransformer().type is discord.AppCommandOptionType.string


def test_transform_error_has_default_message() -> None:
    error = RutTransformError("invalid")

    assert error.value == "invalid"
    assert str(error) == "El RUT 'invalid' no es válido"


def test_package_version_matches_stable_release() -> None:
    assert __version__ == "1.0.1"
