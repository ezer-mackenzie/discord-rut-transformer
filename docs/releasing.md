# Releasing

Releases are automated from tags matching `vX.Y.Z`.

1. Choose the next version according to the [versioning policy](versioning.md).
2. Update `version` in `pyproject.toml`.
3. Move the changelog entries from `Unreleased` to the dated release heading.
4. Run all checks documented in the contribution guide.
5. Merge the release commit into `main`.
6. Create and push an annotated tag, for example `v1.0.0`.

The release workflow verifies that the tag matches the package version, builds
the wheel and source distribution, and publishes both to PyPI using Trusted
Publishing. Read the Docs builds the same tag as versioned documentation.

Before the first release, a maintainer must configure the `pypi` GitHub
environment and register `.github/workflows/release.yml` as a trusted publisher
for the `ezer-mackenzie/discord-rut-transformer` project on PyPI.
