import pytest

from mystatistics import average

@pytest.mark.parametrize('ns, expected', [
    ([0.1, 0.1, 0.1], 0.1),
    ([1, 2, 3], 2),
    ([10, 20, 30, 40], 25),
])
def test_average(ns, expected):
    assert average(ns) == pytest.approx(expected)