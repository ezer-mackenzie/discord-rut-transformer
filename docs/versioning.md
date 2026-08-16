# Versioning and stability

The project follows [Semantic Versioning](https://semver.org/):

- Patch releases (`1.0.1`) contain compatible fixes and documentation updates.
- Minor releases (`1.1.0`) add backward-compatible functionality.
- Major releases (`2.0.0`) may contain breaking API changes.

## Stable API guarantee

Starting with `1.0.0`, these package-root imports are public and stable within
the `1.x` series:

```python
from discord_rut_transformer import (
    RutOption,
    RutTransformer,
    RutTransformError,
)
```

Modules, names, or behavior not documented as public may change in a minor
release. Deprecations will be announced in the changelog before removal whenever
practical.

## Documentation versions

Read the Docs builds documentation from Git tags. Use `stable` for the latest
stable release and `latest` for the current development branch.
