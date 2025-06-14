import pytest
from student import Duration

@pytest.mark.parametrize("amount, expected_seconds", [
    (1, 1),
    (2, 2),
    (60, 60),
    (3600, 3600),
])
def test_from_seconds(amount, expected_seconds):
    duration = Duration.from_seconds(amount)
    assert duration.seconds() == expected_seconds

@pytest.mark.parametrize("amount, expected_seconds", [
    (1, 60),
    (2, 120),
    (5, 300),
])
def test_from_minutes(amount, expected_seconds):
    duration = Duration.from_minutes(amount)
    assert duration.seconds() == expected_seconds

@pytest.mark.parametrize("amount, expected_seconds", [
    (1, 3600),
    (2, 7200),
    (5, 18000),
])
def test_from_hours(amount, expected_seconds):
    duration = Duration.from_hours(amount)
    assert duration.seconds() == expected_seconds

@pytest.mark.parametrize("amount, expected_minutes", [
    (60, 1),
    (120, 2),
    (300, 5),
])
def test_minutes(amount, expected_minutes):
    duration = Duration.from_seconds(amount)
    assert duration.minutes() == expected_minutes

@pytest.mark.parametrize("amount, expected_hours", [
    (3600, 1),
    (7200, 2),
    (18000, 5),
])
def test_hours(amount, expected_hours):
    duration = Duration.from_seconds(amount)
    assert duration.hours() == expected_hours

