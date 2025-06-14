import pytest
import itertools
from mergesort import split_in_two, merge_sorted, merge_sort

# ----------------------------
# Test split_in_two
# ----------------------------
@pytest.mark.parametrize('ns', [
    list(range(n)) for n in range(101)  # Lists of length 0 to 100
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns
    assert abs(len(left) - len(right)) <= 1

# ----------------------------
# Test merge_sorted
# ----------------------------
@pytest.mark.parametrize('left', [
    [], [1], [1, 2, 3], [4, 10, 15], [2, 5, 5, 9]
])
@pytest.mark.parametrize('right', [
    [], [1], [3, 4, 5], [0, 6, 20], [1, 5, 5, 10]
])
def test_merge_sorted(left, right):
    merged = merge_sorted(left, right)
    assert merged == sorted(left + right)

# ----------------------------
# Test merge_sort
# ----------------------------
@pytest.mark.parametrize('expected', [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [2, 2, 3],
    [0, 1, 1, 2],
])
def test_merge_sort(expected):
    permutations = list(itertools.permutations(expected))
    for ns in permutations:
        assert merge_sort(list(ns)) == expected
