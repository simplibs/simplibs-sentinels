# Changelog

All notable changes to `simplibs-sentinels` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.2.0] - 2026-09-27

### Changed
- `EMPTY` now directly aliases `inspect.Parameter.empty`, preserving the canonical standard-library sentinel identity.
- `SentinelType` is now explicitly the implementation base for simplibs-owned sentinels rather than a required base for every public sentinel.
- Sentinel documentation and tests now distinguish simplibs-owned sentinels from externally adopted sentinel values.

### Added
- `EMPTY` is available as the shared simplibs import for Python's canonical empty sentinel.
- Dedicated type and identity tests for all public sentinel values.
- Documentation describing the semantic differences between `UNSET`, `MISSING`, `DEFAULT`, and `EMPTY`.

### Removed
- `EmptyType` — `EMPTY` no longer has a simplibs-owned implementation type.
- The previous custom `EmptyType` singleton implementation.

---

## [0.1.0] - 2026-03-29

### Added
- `SentinelType` — shared singleton base class for all sentinels.
- `UNSET` / `UnsetType` — signals that a parameter was not provided.
- `MISSING` / `MissingType` — signals that an expected value is absent from input data.
- `DEFAULT` / `DefaultType` — explicitly requests default behaviour.
- `EMPTY` / `EmptyType` — signals intentional emptiness, distinct from `None`.
- Full test coverage — singleton behaviour, repr, bool, isolation, and type checks.

---

## Legend

* 🔄 **Changed** — modifications to existing functionality
* ✨ **Added** — new features and components
* 🐛 **Fixed** — bug fixes
* 📋 **Improved** — enhancements to existing features
* ⚠️ **Deprecated** — deprecated functionality (not used yet in this project)
* 🗑️ **Removed** — removed functionality (not used yet in this project)