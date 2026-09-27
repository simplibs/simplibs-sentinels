from inspect import Parameter as _Parameter
from typing import Final


EMPTY: Final = _Parameter.empty
"""
Sentinel representing the absence of a value.

`EMPTY` is the canonical empty sentinel adopted from Python's `inspect`
module.

It is used when an inspectable object has no associated value, such as a
parameter without a default value or without an annotation.

For example:

```python
import inspect

parameter = inspect.signature(func).parameters["value"]

if parameter.default is EMPTY:
    ...
```

`EMPTY` should be compared by identity using `is`.

The object is shared with `inspect`:

```python
EMPTY is inspect.Parameter.empty
EMPTY is inspect.Signature.empty
```

This means `simplibs.sentinels.EMPTY` does not create a second empty
sentinel. It exposes the existing Python sentinel under the common
`simplibs.sentinels` vocabulary.
"""


_DESIGN_NOTES = """
# EMPTY

## Purpose

`EMPTY` represents the absence of a value.

Unlike the other core sentinels, `EMPTY` is not implemented by
`simplibs.sentinels`. It is the existing sentinel object provided by
Python's `inspect` module:

```python
inspect.Parameter.empty
```

`simplibs` adopts that existing object directly.

## Why EMPTY is adopted rather than recreated

Creating an `EmptyType` here would produce two different objects with the
same apparent meaning:

```python
simplibs.sentinels.EMPTY is inspect.Parameter.empty
# False
```

That would unnecessarily split the concept of "empty".

Instead:

```python
EMPTY = inspect.Parameter.empty
```

creates one shared identity:

```python
from simplibs.sentinels import EMPTY
import inspect

EMPTY is inspect.Parameter.empty
# True

EMPTY is inspect.Signature.empty
# True
```

`inspect.Parameter.empty` and `inspect.Signature.empty` are therefore not
represented by separate simplibs sentinels.

## Why EMPTY belongs in simplibs.sentinels

The purpose of this package is not only to define new sentinel objects.
It also provides a common vocabulary for sentinel values that are useful
throughout the simplibs ecosystem.

`EMPTY` is a particularly good candidate because it already represents a
general absence-of-value concept and already has an established singleton
identity in the standard library.

`simplibs.sentinels.EMPTY` therefore acts as an import-level alias, not as
a new sentinel.

## Relationship with the other core sentinels

The four core concepts are deliberately different:

| Sentinel | Meaning |
|----------|---------|
| `DEFAULT` | Default behaviour was explicitly requested |
| `EMPTY` | There is no associated value |
| `MISSING` | An expected value is absent |
| `UNSET` | A value was not supplied/set |

The boundaries are semantic rather than purely technical. An API should
choose the sentinel whose meaning matches the state it needs to represent.

## Notes

- `EMPTY` is an external sentinel adopted by simplibs.
- It does not inherit from `SentinelType`.
- Its identity must not be recreated or replaced.
- Always compare it using `is`.
"""