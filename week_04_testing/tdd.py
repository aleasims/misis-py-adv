import pytest
from typing import List


def sort(numbers: List[int]) -> List[int]:
    """Sort integers.

    Args:
        numbers: List to sort.

    Returns:
        list: Sorted list of numbers in increasing order.

    Raises:
        TypeError: If the is a non-integer element in list.
    """
    if set(type(i) for i in numbers) != set([int]):
        raise TypeError
    return sorted(numbers)


def test_sort():
    assert sort([1, 3, 2]) == [1, 2, 3]
    assert sort([2, 1, 1]) == [1, 1, 2]
    assert sort([0, 4, -2, 1, 0, -1]) == [-2, -1, 0, 0, 1, 4]


def test_sort_raises():
    with pytest.raises(TypeError):
        sort(['a', 'b', 'c'])
    with pytest.raises(TypeError):
        sort(['a', 1, None])
