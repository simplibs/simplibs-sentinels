from typing import ClassVar


class SentinelType:
    """Shared singleton base class for all sentinels in the simplibs ecosystem."""

    _instance: ClassVar["SentinelType | None"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __bool__(self) -> bool:
        return False


_DESIGN_NOTES = """
# SentinelType

## Purpose
Abstract base class for all sentinels in the simplibs ecosystem.
Implements the singleton pattern and falsy behaviour — subclasses only
need to override `__repr__`.

## Logic

### Singleton
Each subclass maintains its own `_instance` because `ClassVar` is bound
to the concrete class, not to `SentinelType` itself:
```python
UnsetType()   is UnsetType()    # True  — same instance
MissingType() is MissingType()  # True  — same instance
UnsetType()   is MissingType()  # False — different classes, different instances
```

### __bool__
All sentinels are falsy — simplifies conditional checks:
```python
if not value:
    ...  # true for UNSET, MISSING, DEFAULT, EMPTY, None, False, "", 0
```
For an explicit check, always use `is`:
```python
value is UNSET   # correct
value == UNSET   # never do this
```

## Notes
- `_instance` is a `ClassVar` — each subclass has its own slot, no sharing occurs.
- Subclasses do not need to call `super().__init__()` — `__new__` is sufficient.
- `__repr__` is intentionally not defined here — each subclass must override it.
"""