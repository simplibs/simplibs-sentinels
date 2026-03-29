"""
Testy pro všechny sentinely — singleton, repr, bool, identita a izolace.
"""
import pytest
from simplibs.sentinels import (
    SentinelType,
    UnsetType, UNSET,
    MissingType, MISSING,
    DefaultType, DEFAULT,
    EmptyType, EMPTY,
)

ALL_SENTINELS = [
    (UnsetType, UNSET, "UNSET"),
    (MissingType, MISSING, "MISSING"),
    (DefaultType, DEFAULT, "DEFAULT"),
    (EmptyType, EMPTY, "EMPTY"),
]


# -----------------------------------------------------------------------------
# Singleton
# -----------------------------------------------------------------------------

@pytest.mark.parametrize("cls, instance, _", ALL_SENTINELS)
def test_singleton_repeated_calls(cls, instance, _):
    """Opakované volání konstruktoru musí vrátit stejnou instanci."""
    assert cls() is cls()


@pytest.mark.parametrize("cls, instance, _", ALL_SENTINELS)
def test_singleton_is_shared_instance(cls, instance, _):
    """Globální instance musí být totožná s výsledkem konstruktoru."""
    assert cls() is instance


# -----------------------------------------------------------------------------
# __repr__
# -----------------------------------------------------------------------------

@pytest.mark.parametrize("_, instance, expected_repr", ALL_SENTINELS)
def test_repr(_, instance, expected_repr):
    """repr() musí vrátit přesný název sentinelu."""
    assert repr(instance) == expected_repr


# -----------------------------------------------------------------------------
# __bool__
# -----------------------------------------------------------------------------

@pytest.mark.parametrize("_, instance, __", ALL_SENTINELS)
def test_bool_is_false(_, instance, __):
    """Každý sentinel musí být falsy."""
    assert bool(instance) is False


# -----------------------------------------------------------------------------
# Izolace — sentinely se nesmí zaměňovat
# -----------------------------------------------------------------------------

def test_sentinels_are_distinct():
    """Žádné dva sentinely nesmí být identické."""
    instances = [UNSET, MISSING, DEFAULT, EMPTY]
    for i, a in enumerate(instances):
        for b in instances[i + 1:]:
            assert a is not b


def test_sentinels_are_not_none():
    """Žádný sentinel nesmí být None."""
    for _, instance, _ in ALL_SENTINELS:
        assert instance is not None


def test_sentinels_are_not_common_types():
    """Sentinely nesmí být instancemi běžných typů."""
    for _, instance, _ in ALL_SENTINELS:
        assert not isinstance(instance, (str, int, float, list, dict))


# -----------------------------------------------------------------------------
# SentinelType — základ
# -----------------------------------------------------------------------------

def test_all_sentinels_inherit_from_sentinel_type():
    """Všechny sentinely musí dědit ze SentinelType."""
    for _, instance, _ in ALL_SENTINELS:
        assert isinstance(instance, SentinelType)


def test_identity_check_with_is():
    """Identita se ověřuje pomocí is, ne ==."""
    value = UNSET
    assert value is UNSET