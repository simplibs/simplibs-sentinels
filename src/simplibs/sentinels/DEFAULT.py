from typing import Final

from .base import SentinelType


class DefaultType(SentinelType):
    """Singleton sentinel representing an explicit request for default behaviour."""

    def __repr__(self) -> str:
        return "DEFAULT"


DEFAULT: Final = DefaultType()
"""
Sentinel representing an explicit request for default behaviour.

`DEFAULT` is used when a caller wants to distinguish an explicit request
for the normal/default behaviour from simply not providing a value.

For example:

```python
def render(color: str | DefaultType = DEFAULT):
    if color is DEFAULT:
        color = theme.primary_color
```

The distinction is particularly useful when the default value is resolved
dynamically at runtime rather than being a fixed function default.

Use `UNSET` when the caller did not provide a value.
Use `DEFAULT` when the caller explicitly requests the default behaviour.

Always test the sentinel by identity:

```python
value is DEFAULT
```
"""


_DESIGN_NOTES = """
# DefaultType / DEFAULT

## Purpose

`DEFAULT` represents an explicit request for default behaviour.

It is intentionally different from `UNSET`:

- `UNSET` → no value was provided;
- `DEFAULT` → the caller explicitly requested default behaviour.

This distinction is useful when an API needs to distinguish omission from
an explicit request to fall back to its normal behaviour.

## Example

```python
def render(color: str | DefaultType = DEFAULT):
    if color is DEFAULT:
        color = theme.primary_color
```

The default may also be calculated dynamically:

```python
if color is DEFAULT:
    color = resolve_default_color()
```

Therefore `DEFAULT` does not necessarily represent a particular value.
It represents an instruction about how the value should be resolved.

## Relationship with UNSET

These two sentinels deliberately represent different states:

| Sentinel | Meaning |
|----------|---------|
| `UNSET` | No value was supplied |
| `DEFAULT` | Default behaviour was explicitly requested |

This distinction is one of the main reasons both sentinels exist.

## Implementation

`DEFAULT` is implemented by `DefaultType`, which inherits from
`SentinelType`.

Unlike `EMPTY`, it is not adopted from an external library. It is a
simplibs-owned semantic concept, so simplibs creates and owns its singleton
instance.

## Notes

- `DEFAULT` is a singleton.
- `bool(DEFAULT)` is `False`.
- Always compare it using `is`.
- `Final` documents that the public constant itself is not intended to be
  reassigned.
"""