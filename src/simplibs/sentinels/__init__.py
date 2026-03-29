from .base import SentinelType
from .UNSET import UnsetType, UNSET
from .MISSING import MissingType, MISSING
from .DEFAULT import DefaultType, DEFAULT
from .EMPTY import EmptyType, EMPTY

__all__ = [
    "SentinelType",
    "UnsetType", "UNSET",
    "MissingType", "MISSING",
    "DefaultType", "DEFAULT",
    "EmptyType", "EMPTY",
]


_DESIGN_NOTES = """
# simplibs/sentinels

## Contents
Sentinel values for the simplibs ecosystem — shared primitives for
distinguishing different states of absence and intent.
Each sentinel is a singleton and falsy — always compare using `is`.

| Name          | Type       | Semantics                                       |
|---------------|------------|-------------------------------------------------|
| `SentinelType`| base class | shared foundation — singleton + falsy           |
| `UnsetType`   | type       | parameter was not provided                      |
| `UNSET`       | instance   | shared instance of UnsetType                    |
| `MissingType` | type       | value was expected but is absent from input     |
| `MISSING`     | instance   | shared instance of MissingType                  |
| `DefaultType` | type       | explicit request for default behaviour          |
| `DEFAULT`     | instance   | shared instance of DefaultType                  |
| `EmptyType`   | type       | intentional emptiness, distinct from None       |
| `EMPTY`       | instance   | shared instance of EmptyType                    |

## Usage
```python
from simplibs.sentinels import UNSET, MISSING, DEFAULT, EMPTY
from simplibs.sentinels import UnsetType  # for type annotations
```
"""