# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-08-16

### Changed

- Read the Docs now installs locked documentation dependencies through Poetry.
- The publishing workflow supports verified manual runs for existing tags.
- Release and contributor documentation now describe the current publishing flow.

### Fixed

- Replaced the obsolete `release.yml` workflow with the configured `publish.yml`
  Trusted Publisher identity.
- Removed unrelated historical-package logic inherited from another project.

## [1.0.0] - 2026-08-16

### Added

- A typed `RutTransformer` for discord.py application commands.
- The `RutOption` convenience annotation.
- `RutTransformError` with format and check-digit error messages.
- Support for Python 3.12, 3.13, and 3.14.
- Type information through the `py.typed` marker.
- MkDocs documentation and versioned Read the Docs builds.
- CI checks, a Python compatibility matrix, and Codecov reporting.

[Unreleased]: https://github.com/ezer-mackenzie/discord-rut-transformer/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/ezer-mackenzie/discord-rut-transformer/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/ezer-mackenzie/discord-rut-transformer/releases/tag/v1.0.0
