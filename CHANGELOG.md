# Changelog

All notable changes to `simplibs-sentinels` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-03-29

### Added
- `SentinelType` — shared singleton base class for all sentinels.
- `UNSET` / `UnsetType` — signals that a parameter was not provided.
- `MISSING` / `MissingType` — signals that an expected value is absent from input data.
- `DEFAULT` / `DefaultType` — explicitly requests default behaviour.
- `EMPTY` / `EmptyType` — signals intentional emptiness, distinct from `None`.
- Full test coverage — singleton behaviour, repr, bool, isolation, and type checks.