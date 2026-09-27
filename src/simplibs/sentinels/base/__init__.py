from .SentinelType import SentinelType


_DESIGN_NOTES = """
# sentinels/base

## Contents

Shared implementation foundation for sentinels owned by the simplibs
ecosystem.

| Name           | Description                                      |
|----------------|--------------------------------------------------|
| `SentinelType` | Singleton and falsy base for simplibs sentinels  |

Not every sentinel exposed by `simplibs.sentinels` inherits from this class.
Existing external sentinel objects may be adopted directly when preserving
their identity is semantically important.

## Usage

```python
from simplibs.sentinels.base import SentinelType
```

Direct import is rarely needed — sentinels are typically imported from
`simplibs.sentinels` directly.
"""