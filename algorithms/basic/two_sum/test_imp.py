import pytest

try:
    from algorithms.basic.two_sum.imp import solution
except ImportError:
    raise ImportError("Could not find the solution in algorithms/basic/two_sum/imp.py")

test_data = [
    (([2, 7, 11, 15], 9), [2, 7]),
    (([3, 2, 4], 6), [2, 4]),
    (([3, 3], 6), [3, 3]),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_two_sum(test_input, expected):
    result = solution(*test_input)
    assert result == expected
