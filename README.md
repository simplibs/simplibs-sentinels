# ⚖️ `simplibs-sentinels`

[![PyPI](https://img.shields.io/pypi/v/simplibs-sentinels)](https://pypi.org/project/simplibs-sentinels/)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![Licence](https://img.shields.io/badge/licence-MIT-green)](https://github.com/simplibs/simplibs-sentinels/blob/main/LICENSE)

**Shared sentinel values for the simplibs ecosystem — precise tools for distinguishing different states of absence and intent.**

`simplibs-sentinels` provides a small, dependency-free vocabulary for representing states that ordinary Python values cannot always distinguish clearly — such as "nothing was provided", "an expected value is missing", "use the default behaviour", or "there is no associated value".

The library deliberately stays small. It defines only the sentinel concepts that are useful as general-purpose building blocks across the simplibs ecosystem, while leaving domain-specific sentinels and existing standard-library sentinels where they naturally belong.

```python
from simplibs.sentinels import UNSET, MISSING, DEFAULT, EMPTY


def configure(timeout: int | None | UnsetType = UNSET):
    if timeout is UNSET:
        timeout = get_default_timeout()
    elif timeout is None:
        timeout = 0
```

---

## 🧭 The Core Philosophy

A sentinel is useful when several states that look similar at the value level need to remain semantically distinct.

For example, `None` alone cannot distinguish between:

```text
the caller provided nothing
the caller explicitly provided None
```

A sentinel gives the API a separate identity for the first state:

```python
def connect(timeout: int | None | UnsetType = UNSET):
    if timeout is UNSET:
        timeout = get_default_timeout()
    elif timeout is None:
        timeout = 0
```

The important distinction is not the sentinel's truthiness but its **identity**.

Always test sentinels using `is`:

```python
if timeout is UNSET:
    ...
```

rather than:

```python
if timeout == UNSET:
    ...
```

`simplibs`-owned sentinels are singletons and falsy. `EMPTY` is an existing
sentinel adopted from Python's `inspect` module and retains its original
implementation and identity.

---

## 📦 Installation

```bash
pip install simplibs-sentinels
```

The library has **no runtime dependencies**.

It is intentionally positioned at the bottom of the simplibs dependency
hierarchy so that other simplibs libraries can depend on it without
introducing a dependency chain of their own.

---

## 🚀 The Four Core Sentinels

`simplibs-sentinels` currently exposes four general-purpose sentinel values:

| Sentinel  | Semantics                                    | Typical use                                  |
|-----------|----------------------------------------------|----------------------------------------------|
| `UNSET`   | A value was not supplied or has not been set | optional parameters, object state            |
| `MISSING` | An expected value is absent                  | dictionaries, input data, parsing            |
| `DEFAULT` | Default behaviour was explicitly requested   | dynamic defaults, configuration              |
| `EMPTY`   | There is no associated value                 | absence of a value, especially introspection |

These concepts overlap at the edges, but they deliberately describe different
states.

### `UNSET`

`UNSET` represents a value that was **not provided or has not been set**.

Its most common use is distinguishing an omitted function argument from an
explicitly supplied `None`:

```python
from simplibs.sentinels import UNSET, UnsetType


def connect(
    host: str,
    timeout: int | None | UnsetType = UNSET,
):
    if timeout is UNSET:
        timeout = get_default_timeout()
    elif timeout is None:
        timeout = 0

    ...
```

The resulting states are distinct:

```text
UNSET → the caller supplied nothing
None  → the caller explicitly supplied None
value → the caller supplied an actual value
```

`UNSET` is implemented by `UnsetType`, a `SentinelType` subclass.

---

### `MISSING`

`MISSING` represents an **expected value that is absent** from some input
data or source.

It is particularly useful when the absence of a key or field must be
distinguished from an existing key whose value happens to be `None`:

```python
from simplibs.sentinels import MISSING, MissingType


def validate(data: dict, key: str):
    value = data.get(key, MISSING)

    if value is MISSING:
        raise ValueError(f"Required key '{key}' is missing.")
    elif value is None:
        ...
```

Here:

```text
MISSING → the expected key is absent
None    → the key exists and explicitly contains None
```

`MISSING` is implemented by `MissingType`, a `SentinelType` subclass.

---

### `DEFAULT`

`DEFAULT` represents an **explicit request for default behaviour**.

This is different from simply omitting a value:

```python
from simplibs.sentinels import DEFAULT, DefaultType


def render(color: str | DefaultType = DEFAULT):
    if color is DEFAULT:
        color = theme.primary_color

    ...
```

The distinction is:

```text
UNSET   → nothing was supplied
DEFAULT → default behaviour was explicitly requested
```

This is particularly useful when the default is resolved dynamically at
runtime rather than being a fixed value.

For example:

```python
if color is DEFAULT:
    color = resolve_default_color()
```

`DEFAULT` is implemented by `DefaultType`, a `SentinelType` subclass.

---

### `EMPTY`

`EMPTY` represents the **absence of an associated value**.

Unlike `UNSET`, `MISSING`, and `DEFAULT`, `EMPTY` is not implemented by
`simplibs`.

It is the existing sentinel provided by Python's `inspect` module:

```python
from inspect import Parameter

EMPTY is Parameter.empty
```

`simplibs.sentinels.EMPTY` therefore refers to the same object:

```python
from simplibs.sentinels import EMPTY
import inspect

EMPTY is inspect.Parameter.empty
# True

EMPTY is inspect.Signature.empty
# True
```

This identity is intentional.

Rather than creating another `EmptyType` and introducing a second object
representing the same general concept, `simplibs` adopts the existing
standard-library sentinel.

This also means that `EMPTY` has **no corresponding `EmptyType`** in the
`simplibs.sentinels` API.

The type of the existing object can always be obtained with:

```python
type(EMPTY)
```

but that implementation type is not part of the `simplibs.sentinels`
public vocabulary.

---

## 🔍 How the Sentinels Differ

The four sentinels can be viewed as four different questions:

| Sentinel  | Question it answers                                  |
|-----------|------------------------------------------------------|
| `UNSET`   | Was anything supplied or set?                        |
| `MISSING` | Is the expected value present in the input?          |
| `DEFAULT` | Did the caller explicitly request default behaviour? |
| `EMPTY`   | Is there an associated value at all?                 |

For example:

```text
UNSET
    "This was not set."

MISSING
    "The thing I expected is not there."

DEFAULT
    "I explicitly want the normal/default behaviour."

EMPTY
    "There is no associated value."
```

The distinctions are semantic rather than mechanically enforced. An API
should use the sentinel whose meaning matches the state it needs to
represent.

---

## 🧱 Sentinel Types

The three simplibs-owned sentinels expose their implementation types:

```python
from simplibs.sentinels import (
    DefaultType,
    MissingType,
    UnsetType,
)
```

This allows them to be used in type annotations:

```python
from simplibs.sentinels import UNSET, UnsetType


def process(
    value: str | UnsetType = UNSET,
) -> None:
    ...
```

The sentinel instances themselves are the values normally used by application
code.

`SentinelType` is the shared implementation base:

```python
from simplibs.sentinels import SentinelType
```

It provides singleton behaviour and falsy boolean behaviour for
simplibs-owned sentinels.

`EMPTY` is deliberately excluded from this hierarchy because it is an
existing external sentinel whose identity is preserved.

---

## 🧩 Singleton Behaviour

Each simplibs-owned sentinel is a singleton:

```python
from simplibs.sentinels import UNSET, UnsetType

UNSET is UnsetType()
# True
```

Different sentinel types remain distinct:

```python
from simplibs.sentinels import MISSING, UNSET

MISSING is UNSET
# False
```

The same principle applies to `EMPTY`, although its singleton identity is
provided by `inspect` rather than by `SentinelType`:

```python
from simplibs.sentinels import EMPTY
import inspect

EMPTY is inspect.Parameter.empty
# True
```

Sentinel identity should therefore always be checked using `is`.

---

## 🪶 Minimal by Design

The package deliberately does **not** attempt to collect every sentinel-like
object from Python's standard library.

Many standard-library sentinels are tightly coupled to a particular module
or protocol. For example, a sentinel meaningful specifically to `argparse`,
`subprocess`, `signal`, or `unittest.mock` does not automatically become
more useful merely because it is re-exported from `simplibs.sentinels`.

Likewise, a sentinel whose import path is already direct and unambiguous
does not benefit from being duplicated here.

The package therefore focuses on a much smaller question:

> Is this sentinel a general-purpose concept that benefits from being part
> of the shared simplibs vocabulary?

At present, the answer is the four values exposed by this library.

---

## 🔭 About the library, from the author's point of view

`simplibs-sentinels` was originally created for a very simple reason:
multiple simplibs libraries needed an `UNSET` sentinel, and defining that
sentinel independently in every library would create multiple sources of
truth.

The original goal was therefore to have one small, dependency-free library
that could provide a shared `UNSET` object to the rest of the ecosystem.

The intention was always to return to the library later and expand it with
other generally useful sentinel values.

When that time finally came, the question turned out to be less about
finding things to add and more about determining which things genuinely
belonged here.

The standard library contains many sentinel-like objects, but most of them
are specific to the API that owns them. Re-exporting those objects through
`simplibs.sentinels` would add another import path without providing a
meaningful abstraction.

Other concepts are useful in particular domains — for example configuration
states such as `AUTO` or `DISABLED` — but they are not sufficiently general
to justify making them part of this core library without a concrete need.

The one notable exception is `EMPTY`.

Python's `inspect` module already provides a canonical empty sentinel through
`inspect.Parameter.empty`, and that same object is also used by
`inspect.Signature.empty`. Creating another `EMPTY` object in `simplibs`
would unnecessarily split one established concept into two identities.

Starting with version `0.2.0`, `simplibs.sentinels.EMPTY` therefore adopts
the existing `inspect.Parameter.empty` object directly.

The result is intentionally small:

- `UNSET`, `MISSING`, and `DEFAULT` are concepts owned by `simplibs`;
- `EMPTY` is an existing canonical sentinel adopted by `simplibs`;
- domain-specific standard-library sentinels remain in their own APIs;
- no additional sentinel is added merely for completeness.

In that sense, the library's small size is not an unfinished feature list.
It is the result of deliberately keeping the lowest-level vocabulary small
and unambiguous.

---

## ☯️ About simplibs

All libraries in the **simplibs** (Simple Libraries) ecosystem share a common
engineering philosophy:

* **Dyslexia-friendly:**
We actively minimize cognitive load. Code is atomized into small, self-contained units,
files are named directly after the logical task they perform, and explanations describe
*why* something is designed, not just *what* it is.
* **Programmer's Zen:**
Nothing should be missing, and nothing should be superfluous. We value clean execution
paths and robust, understandable code architectures over rushed, messy feature sets.
* **Defensive Style:**
We actively anticipate edge cases and failure modes so that only safe operational paths
remain. Our code is built to degrade gracefully rather than crash unexpectedly.
* **Minimalism:**
Find the most direct path to the goal in as few operational steps as possible without
taking shortcuts on safety, readability, or completeness.
* **Code as Craft:**
Code should be pleasant to look at, readable at a glance, and evoke structural harmony.
We treat software engineering as a precision trade.

---

### 🤝 Contributing & Community

This is an **open-source project** built with love and care. We strongly believe in
community collaboration and welcome any feedback, bug reports, or feature ideas!

* **Want to contribute?** Feel free to open an Issue or submit a Pull Request.
* **Want to get in touch?** If you'd like to discuss the project further, collaborate,
  or just say hello, feel free to open a GitHub Issue or start a Discussion.

---

### 📝 License

This library is released under the **MIT License**. Build great things!

---

[▲ Back to Top](#-simplibs-sentinels)