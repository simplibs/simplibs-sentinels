# simplibs-sentinels

> Shared sentinel values for the simplibs ecosystem —
> precise tools for distinguishing different states of absence and intent.

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Licence](https://img.shields.io/badge/licence-MIT-green)
![PyPI](https://img.shields.io/pypi/v/simplibs-sentinels)

---

## Contents

- [Installation](#installation)
- [Why sentinels?](#why-sentinels)
- [Overview](#overview)
- [UNSET](#unset)
- [MISSING](#missing)
- [DEFAULT](#default)
- [EMPTY](#empty)
- [Type annotations](#type-annotations)
- [About the simplibs ecosystem](#about-the-simplibs-ecosystem)

---

## Installation
```bash
pip install simplibs-sentinels
```

---

## Why sentinels?

Python has no built-in way to distinguish between "parameter was not provided",
"value is intentionally absent", and "value is `None`" — yet these are three
different situations requiring different logic.
```python
# Problem — None can mean anything
def connect(host: str, timeout: int | None = None):
    if timeout is None:
        # was timeout omitted? or intentionally passed as None?
        ...

# Solution — each state has its own sentinel
def connect(host: str, timeout: int | UnsetType = UNSET):
    if timeout is UNSET:
        timeout = get_default_timeout()  # not provided → use default
    elif timeout is None:
        timeout = 0                      # None passed intentionally → no timeout
```

All sentinels are **singletons** and **falsy** — always compare using `is`.

---

## Overview

| Sentinel  | Semantics                                          | Typical context              |
|-----------|----------------------------------------------------|------------------------------|
| `UNSET`   | function parameter was not provided                | default parameter values     |
| `MISSING` | value was expected but is absent from input data   | input data validation        |
| `DEFAULT` | explicit request for default behaviour             | overriding dynamic defaults  |
| `EMPTY`   | intentional emptiness, distinct from `None`        | clearing or resetting values |

---

## UNSET

Distinguishes a parameter that was not provided from an intentionally passed `None`.
```python
from simplibs.sentinels import UNSET, UnsetType

def connect(host: str, timeout: int | UnsetType = UNSET):
    if timeout is UNSET:
        timeout = get_default_timeout()
    elif timeout is None:
        timeout = 0
```

---

## MISSING

Signals that a value was expected but is entirely absent from the input data.
Useful when validating dictionaries, forms, or API payloads.
```python
from simplibs.sentinels import MISSING, MissingType

def validate(data: dict, key: str):
    value = data.get(key, MISSING)
    if value is MISSING:
        raise ValueError(f"Required key '{key}' is missing.")
    elif value is None:
        ...  # key exists, value is None — different logic applies
```

---

## DEFAULT

Expresses the explicit intent "I want the default behaviour" — even when the
default value is not static but decided at runtime.
```python
from simplibs.sentinels import DEFAULT, DefaultType

def render(color: str | DefaultType = DEFAULT):
    if color is DEFAULT:
        color = theme.primary_color
```

Difference from `UNSET`: `UNSET` means "the user provided nothing",
`DEFAULT` means "the user explicitly wants the default value".

---

## EMPTY

Intentional emptiness — a signal that a value should be explicitly cleared,
without needing to pass an empty collection of a specific type.
```python
from simplibs.sentinels import UNSET, EMPTY, EmptyType

def set_tags(tags: list | EmptyType | UnsetType = UNSET):
    if tags is UNSET:
        pass              # not provided → change nothing
    elif tags is EMPTY:
        self.tags = []    # intentionally clear all tags
    else:
        self.tags = tags
```

---

## Type annotations

Use the sentinel types directly in type annotations:
```python
from simplibs.sentinels import UNSET, UnsetType

def process(value: str | UnsetType = UNSET) -> None:
    ...
```

---

## About the simplibs ecosystem

`simplibs-sentinels` is part of the **simplibs** ecosystem — a collection of
small, self-contained Python libraries. Each one solves exactly one thing —
but all of them share a common philosophy:

**Dyslexia-friendly** — minimise mental load. Atomise code into self-contained
units, name files after the logic they contain, write explanations that describe
*why* — not just *what*.

**Programmer's zen** — nothing should be missing and nothing should be
superfluous. The journey is the destination: code should be fully understood;
better to go slowly and correctly than quickly and with mistakes. The
crystallisation approach — not perfection on the first try, but gradual
refinement towards it.

**Defensive style** — anticipate all possible failure modes so that only safe
paths remain. Never raise unexpected errors; degrade gracefully.

**Minimalism** — find the path to the goal in as few steps as possible, but
leave nothing out. Each file has one responsibility.

**Code as craft** — code should be pleasant to look at and evoke a sense of
harmony. Treat code as a small work of art — like a carpenter carving a
sculpture. Optimise for the user: everything should make sense without having
to study the documentation at length.

These are aspirations — a sense of direction. And that is exactly what the
note about the journey becoming the destination is all about. 🙂

---

*The library is covered by tests across all modules. Tests are part of the
repository and serve as living documentation of the expected behaviour.*