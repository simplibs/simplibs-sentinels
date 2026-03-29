from typing import Final
from .base import SentinelType


class EmptyType(SentinelType):
    """Singleton sentinel representing intentional emptiness, distinct from None."""

    def __repr__(self) -> str:
        return "EMPTY"


EMPTY: Final = EmptyType()


_DESIGN_NOTES = """
# EmptyType / EMPTY

## Purpose
Sentinel for intentional emptiness — signals that a value should be explicitly
cleared, without needing to pass an empty collection of a specific type.

## When to use
```python
from simplibs.sentinels import UNSET, EMPTY, EmptyType

def set_tags(tags: list | EmptyType | UnsetType = UNSET):
    if tags is UNSET:
        pass              # not provided → change nothing
    elif tags is EMPTY:
        self.tags = []    # intentionally clear all tags
    else:
        self.tags = tags  # apply the provided tags
```

## Difference from an empty list
`[]` is a value. `EMPTY` is a signal of intent — "I explicitly want an empty
state" without coupling the caller to a specific collection type.

## Notes
- Always compare using `is`, never `==`.
- `bool(EMPTY)` returns `False` — EMPTY is falsy.
"""