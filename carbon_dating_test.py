import pytest

from carbon_dating import get_age_carbon_14_dating

def test_get_age_carbon_14_dating():
    assert get_age_carbon_14_dating(0.35) == 8680.34743633106

def test_get_age_carbon_14_dating_zero():
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(0)

def test_get_age_carbon_14_dating_negative():
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(-10)

def test_get_age_carbon_14_dating_greater_than_one():
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(10)