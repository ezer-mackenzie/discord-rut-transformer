# Usage

## Available representations

`RutOption` resolves to a validated `rut_validator.Rut`. You can select the
representation required by your application:

```python
rut.formatted  # "12.345.678-5"
rut.hyphenated  # "12345678-5"
rut.normalized  # "123456785"
rut.body  # 12345678
rut.check_digit  # "5"
```

Returning the value object instead of a string preserves the validation
guarantee throughout your command handler.

## Explicit transformer annotation

`RutOption` is a convenience alias for the longer discord.py annotation:

```python
from discord import app_commands
from rut_validator import Rut

from discord_rut_transformer import RutTransformer


rut: app_commands.Transform[Rut, RutTransformer]
```

Prefer `RutOption` in application code unless you need the expanded type for
documentation or introspection.
