from typing import Final
from .base import SentinelType


class DefaultType(SentinelType):
    """Singleton sentinel representing an explicit request for default behaviour."""

    def __repr__(self) -> str:
        return "DEFAULT"


DEFAULT: Final = DefaultType()


_DESIGN_NOTES = """
# DefaultType / DEFAULT

## Purpose
Sentinel for explicitly expressing "I want the default behaviour" — distinct
from a parameter that was simply not provided (`UNSET`) or is absent (`MISSING`).

## When to use
```python
from simplibs.sentinels import DEFAULT, DefaultType

def render(color: str | DefaultType = DEFAULT):
    if color is DEFAULT:
        color = theme.primary_color  # default explicitly requested
```

## Difference from UNSET
`UNSET` means "the user provided nothing".
`DEFAULT` means "the user explicitly wants the default value" — even when
that default is not static but resolved dynamically at runtime.

## Notes
- Always compare using `is`, never `==`.
- `bool(DEFAULT)` returns `False` — DEFAULT is falsy.
"""