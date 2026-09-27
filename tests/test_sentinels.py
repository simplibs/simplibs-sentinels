"""Tests for the public sentinel values."""

import inspect

import pytest

from simplibs.sentinels import (
    DEFAULT,
    EMPTY,
    MISSING,
    UNSET,
    DefaultType,
    MissingType,
    SentinelType,
    UnsetType,
)


OWNED_SENTINELS = (
    (UnsetType, UNSET, "UNSET"),
    (MissingType, MISSING, "MISSING"),
    (DefaultType, DEFAULT, "DEFAULT"),
)


ALL_SENTINELS = (
    UNSET,
    MISSING,
    DEFAULT,
    EMPTY,
)


# -----------------------------------------------------------------------------
# Simplibs-owned sentinels
# -----------------------------------------------------------------------------

@pytest.mark.parametrize("sentinel_type, sentinel, name", OWNED_SENTINELS)
def test_owned_sentinel_is_singleton(sentinel_type, sentinel, name):
    """Repeated construction must return the same instance."""
    assert sentinel_type() is sentinel_type()
    assert sentinel_type() is sentinel


@pytest.mark.parametrize("sentinel_type, sentinel, expected_repr", OWNED_SENTINELS)
def test_owned_sentinel_repr(sentinel_type, sentinel, expected_repr):
    """Each owned sentinel must have its public representation."""
    assert repr(sentinel) == expected_repr


@pytest.mark.parametrize("sentinel_type, sentinel, name", OWNED_SENTINELS)
def test_owned_sentinel_is_falsy(sentinel_type, sentinel, name):
    """Each simplibs-owned sentinel must be falsy."""
    assert bool(sentinel) is False


@pytest.mark.parametrize("sentinel_type, sentinel, name", OWNED_SENTINELS)
def test_owned_sentinel_inherits_from_sentinel_type(sentinel_type, sentinel, name):
    """Each simplibs-owned sentinel type must inherit from SentinelType."""
    assert issubclass(sentinel_type, SentinelType)
    assert isinstance(sentinel, SentinelType)


# -----------------------------------------------------------------------------
# EMPTY — external sentinel adopted from inspect
# -----------------------------------------------------------------------------

def test_empty_is_inspect_parameter_empty():
    """EMPTY must be identical to inspect.Parameter.empty."""
    assert EMPTY is inspect.Parameter.empty


def test_empty_is_inspect_signature_empty():
    """EMPTY must be identical to inspect.Signature.empty."""
    assert EMPTY is inspect.Signature.empty


def test_empty_is_not_sentinel_type_instance():
    """EMPTY must remain outside the simplibs-owned SentinelType hierarchy."""
    assert not isinstance(EMPTY, SentinelType)


# -----------------------------------------------------------------------------
# Identity
# -----------------------------------------------------------------------------

def test_sentinels_are_distinct():
    """Different public sentinels must have different identities."""
    for index, sentinel in enumerate(ALL_SENTINELS):
        for other in ALL_SENTINELS[index + 1:]:
            assert sentinel is not other


@pytest.mark.parametrize("sentinel", ALL_SENTINELS)
def test_sentinel_is_not_none(sentinel):
    """No public sentinel may be None."""
    assert sentinel is not None


# -----------------------------------------------------------------------------
# Public identity contract
# -----------------------------------------------------------------------------

@pytest.mark.parametrize("sentinel", ALL_SENTINELS)
def test_sentinel_identity_is_stable(sentinel):
    """A sentinel must remain identical to itself."""
    value = sentinel

    assert value is sentinel


def test_identity_comparison_with_is():
    """Sentinel values must be identifiable by object identity."""
    value = UNSET

    assert value is UNSET
    assert value is not MISSING
    assert value is not DEFAULT
    assert value is not EMPTY
