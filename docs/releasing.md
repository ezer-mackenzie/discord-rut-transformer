# Releasing

Releases are automated when a GitHub Release is published from a tag matching
`vX.Y.Z`.

1. Choose the next version according to the [versioning policy](versioning.md).
2. Update `version` in `pyproject.toml`.
3. Move the changelog entries from `Unreleased` to the dated release heading.
4. Run all checks documented in the contribution guide.
5. Merge the release commit into `main`.
6. Create and push an annotated tag, for example `v1.0.1`.
7. Create and publish the corresponding GitHub Release.

The publish workflow verifies that the tag matches the package version, builds
the wheel and source distribution, and publishes both to PyPI using Trusted
Publishing. Read the Docs builds the same tag as versioned documentation.

If a GitHub Release was published before the workflow was available, run
**Publish to PyPI** manually from the Actions tab and enter the existing tag.
Rerunning a historical workflow does not switch it to the new workflow file.

Before the first release, a maintainer must configure the `pypi` GitHub
environment and register `.github/workflows/publish.yml` as a trusted publisher
for the `ezer-mackenzie/discord-rut-transformer` project on PyPI.
