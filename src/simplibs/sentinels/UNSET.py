from typing import Final

from .base import SentinelType


class UnsetType(SentinelType):
    """Singleton sentinel representing a value that was not provided."""

    def __repr__(self) -> str:
        return "UNSET"


UNSET: Final = UnsetType()

"""
Sentinel representing a value that was not provided or has not been set.

`UNSET` is useful when `None` is itself a meaningful value and therefore
cannot also represent the absence of an argument.

For example:

```python
def connect(timeout: int | None | UnsetType = UNSET):
    if timeout is UNSET:
        timeout = get_default_timeout()
    elif timeout is None:
        timeout = 0
```

Here omission and an explicit `None` remain distinguishable.

`UNSET` should always be compared by identity using `is`.
"""


_DESIGN_NOTES = """
# UnsetType / UNSET

## Purpose

`UNSET` represents a value that was not supplied or has not been set.

Its main purpose is to preserve the distinction between:

```text
not supplied
```

and:

```text
explicitly supplied as None
```

This is especially useful for function parameters where `None` is itself
a valid value.

## Example

```python
def connect(timeout: int | None | UnsetType = UNSET):
    if timeout is UNSET:
        timeout = get_default_timeout()
    elif timeout is None:
        timeout = 0
```

The three states can therefore remain distinct:

```text
UNSET → caller supplied nothing
None  → caller explicitly supplied None
value → caller supplied an actual value
```

## Relationship with DEFAULT

`UNSET` and `DEFAULT` are intentionally different:

```text
UNSET   → nothing was supplied
DEFAULT → default behaviour was explicitly requested
```

An API may choose to make these states equivalent internally, but the
sentinels themselves preserve the distinction.

## Relationship with MISSING

`UNSET` normally describes the state of an argument, property, or value
that has not been supplied/set.

`MISSING` describes an expected value that cannot be found in some input
data or source.

```text
UNSET   → "this was not set"
MISSING → "the thing we expected is absent"
```

## Implementation

`UNSET` is a simplibs-owned sentinel implemented by `UnsetType`, which
inherits from `SentinelType`.

It is one of the original core sentinels of the package.

## Notes

- `UNSET` is a singleton.
- `bool(UNSET)` is `False`.
- Always compare it using `is`.
- `Final` documents that the public constant itself is not intended to be
  reassigned.
"""