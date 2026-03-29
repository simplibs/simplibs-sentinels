from typing import Final
from .base import SentinelType


class MissingType(SentinelType):
    """Singleton sentinel representing a value that was expected but is absent."""

    def __repr__(self) -> str:
        return "MISSING"


MISSING: Final = MissingType()


_DESIGN_NOTES = """
# MissingType / MISSING

## Purpose
Sentinel for situations where a value was expected but is entirely absent
from the input data — semantically distinct from `UNSET` (not provided)
and `None` (explicitly empty).

## When to use
```python
from simplibs.sentinels import MISSING, MissingType

def validate(data: dict, key: str):
    value = data.get(key, MISSING)
    if value is MISSING:
        raise ValueError(f"Required key '{key}' is missing from input data.")
    elif value is None:
        ...  # key exists but value is None — different logic applies
```

## Difference from UNSET
| Sentinel  | Semantics                                      |
|-----------|------------------------------------------------|
| `UNSET`   | function parameter was not provided            |
| `MISSING` | key or field is absent from input data         |

## Notes
- Always compare using `is`, never `==`.
- `bool(MISSING)` returns `False` — MISSING is falsy.
- Also used by Python's standard library in the `inspect` module.
"""