from .SentinelType import SentinelType


_DESIGN_NOTES = """
# sentinels/base

## Contents
Shared foundation for all sentinel types in the simplibs ecosystem.

| Name            | Description                                        |
|-----------------|----------------------------------------------------|
| `SentinelType`  | Singleton base class — all sentinels inherit from it |

## Usage
```python
from simplibs.sentinels.base import SentinelType
```
Direct import is rarely needed — sentinels are typically imported
from `simplibs.sentinels` directly.
"""