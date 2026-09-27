from typing import ClassVar


class SentinelType:
    """Shared singleton base class for sentinels owned by simplibs."""

    _instance: ClassVar["SentinelType | None"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __bool__(self) -> bool:
        return False


_DESIGN_NOTES = """
# SentinelType

## Purpose

`SentinelType` is the implementation base for sentinels that are defined
and owned by the simplibs ecosystem.

It provides two common properties:

- singleton behaviour;
- falsy boolean behaviour.

It is intentionally not a requirement for every sentinel exposed by
`simplibs.sentinels`. Some sentinels originate in Python or another external
library and already have an established singleton object. Those sentinels
are adopted directly rather than recreated.

## Singleton

Each concrete subclass receives its own singleton instance.

The `_instance` attribute is inherited, but assignment happens through the
concrete class, so the resulting value is stored on that subclass:

```python
UnsetType()   is UnsetType()    # True
MissingType() is MissingType()  # True
UnsetType()   is MissingType()  # False
```

This means every sentinel type has exactly one instance while different
sentinel types remain distinct.

## Boolean behaviour

Sentinels owned by simplibs are falsy:

```python
if not value:
    ...
```

This can be convenient when a sentinel naturally represents the absence
of a usable value.

However, truthiness does not identify a sentinel. Other values such as
`None`, `False`, `0`, and `""` are also falsy.

When the identity of a particular sentinel matters, always use `is`:

```python
value is UNSET
```

Never use equality as the sentinel check:

```python
value == UNSET
```

## External sentinels

Not every public sentinel needs to inherit from `SentinelType`.

For example, `EMPTY` is the existing `inspect.Parameter.empty` object.
Recreating it as an `EmptyType` would introduce a second object representing
the same general concept of emptiness.

The sentinel package therefore has two kinds of entries:

1. sentinels implemented by simplibs using `SentinelType`;
2. existing external sentinel objects adopted directly by simplibs.

This keeps `simplibs.sentinels` a unified public vocabulary without
duplicating established sentinel objects.

## Notes

- `_instance` is a `ClassVar`; concrete subclasses maintain their own
  singleton instance.
- No `__init__` is required because the singleton is established in
  `__new__`.
- `__repr__` is deliberately not implemented here. Each concrete sentinel
  defines its own public representation.
"""