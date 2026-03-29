from typing import Final
from .base import SentinelType


class UnsetType(SentinelType):
    """Singleton sentinel representing a value that was not provided."""

    def __repr__(self) -> str:
        return "UNSET"


UNSET: Final = UnsetType()


_DESIGN_NOTES = """
# UnsetType / UNSET

## Purpose
Sentinel for distinguishing a parameter that was not provided from an
intentionally passed `None` — because `None` is a valid Python value
with its own meaning.

## When to use
```python
from simplibs.sentinels import UNSET, UnsetType

def connect(host: str, timeout: int | UnsetType = UNSET):
    if timeout is UNSET:
        timeout = get_default_timeout()  # not provided → apply default
    elif timeout is None:
        timeout = 0                      # None passed intentionally → no timeout
```

## Notes
- Always compare using `is`, never `==`.
- `bool(UNSET)` returns `False` — UNSET is falsy.
- The `Final` annotation ensures that `UNSET` cannot be reassigned.
"""