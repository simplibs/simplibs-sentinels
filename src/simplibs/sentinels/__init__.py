from .base import SentinelType
from .UNSET import UnsetType, UNSET
from .MISSING import MissingType, MISSING
from .DEFAULT import DefaultType, DEFAULT
from .EMPTY import EMPTY

__all__ = [
    "SentinelType",
    "UnsetType", "UNSET",
    "MissingType", "MISSING",
    "DefaultType", "DEFAULT",
    "EMPTY",
]


_DESIGN_NOTES = """
# simplibs/sentinels

## Contents

Sentinel values for the simplibs ecosystem — shared primitives for
distinguishing different states of absence and intent.

The package contains two kinds of sentinels:

1. sentinels owned and implemented by simplibs;
2. existing external sentinel objects adopted by simplibs.

All simplibs-owned sentinels are singletons and falsy. External sentinels
retain their original implementation and identity.

Always compare sentinel values using `is`.

| Name           | Type       | Semantics                                  |
|----------------|------------|--------------------------------------------|
| `SentinelType` | base class | foundation for simplibs-owned sentinels    |
| `UnsetType`    | type       | parameter or value was not provided        |
| `UNSET`        | instance   | singleton instance of `UnsetType`          |
| `MissingType`  | type       | expected value is absent                   |
| `MISSING`      | instance   | singleton instance of `MissingType`        |
| `DefaultType`  | type       | explicit request for default behaviour     |
| `DEFAULT`      | instance   | singleton instance of `DefaultType`        |
| `EMPTY`        | instance   | adopted empty sentinel from `inspect`      |

`EMPTY` intentionally has no corresponding `EmptyType` in this package.
It is an alias of Python's existing `inspect.Parameter.empty` sentinel.

## Usage

```python
from simplibs.sentinels import UNSET, MISSING, DEFAULT, EMPTY
from simplibs.sentinels import UnsetType
```

Type classes are available when they are useful for type annotations;
normally the sentinel instances themselves are what application code
uses.

## Sentinel ownership

The distinction between implementation and public API is intentional.

`simplibs` owns:

```text
DEFAULT
MISSING
UNSET
```

and therefore implements them using `SentinelType`.

`simplibs` adopts:

```text
EMPTY
```

from `inspect`, preserving the existing singleton rather than creating
a second object representing the same concept.

This allows:

```python
from simplibs.sentinels import EMPTY
import inspect

EMPTY is inspect.Parameter.empty
# True
```
"""
