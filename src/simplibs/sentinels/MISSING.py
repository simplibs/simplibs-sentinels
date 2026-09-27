from typing import Final

from .base import SentinelType


class MissingType(SentinelType):
    """Singleton sentinel representing an expected value that is absent."""

    def __repr__(self) -> str:
        return "MISSING"


MISSING: Final = MissingType()
"""
Sentinel representing a value that was expected but is absent.

`MISSING` is useful when the absence of a value needs to be distinguished
from a value that is explicitly present as `None`.

For example:

```python
value = data.get("name", MISSING)

if value is MISSING:
    ...
elif value is None:
    ...
```

The first case means that the expected key is absent.
The second means that the key exists and its value is explicitly `None`.

`MISSING` should always be compared by identity using `is`.
"""


_DESIGN_NOTES = """
# MissingType / MISSING

## Purpose

`MISSING` represents an expected value that is absent.

It is useful when an API needs to distinguish:

- a value that is absent;
- a value that is explicitly `None`;
- a value that was not supplied to an API.

For example:

```python
value = data.get("name", MISSING)

if value is MISSING:
    ...
elif value is None:
    ...
```

Here `MISSING` means that the expected key does not exist, while `None`
means that the key exists and explicitly contains `None`.

## Relationship with UNSET

`MISSING` and `UNSET` are close concepts, but describe different states.

| Sentinel | Meaning |
|----------|---------|
| `UNSET` | A value was not supplied or has not been set |
| `MISSING` | An expected value is absent from some data structure or source |

A useful mental distinction is:

```text
UNSET   → state of a value/parameter
MISSING → absence of an expected value
```

The distinction is semantic rather than enforced by the implementation.

## Relationship with EMPTY

`EMPTY` describes the absence of an associated value.

`MISSING` describes the absence of an expected value.

For example, an API may legitimately contain an empty value while a
required field is still considered present. `MISSING` is specifically
useful when the existence of the expected value itself matters.

## Implementation

`MISSING` is implemented by `MissingType`, which inherits from
`SentinelType`.

It is a simplibs-owned sentinel and therefore has its own singleton
instance.

## Notes

- `MISSING` is a singleton.
- `bool(MISSING)` is `False`.
- Always compare it using `is`.
- `Final` documents that the public constant itself is not intended to be
  reassigned.
"""