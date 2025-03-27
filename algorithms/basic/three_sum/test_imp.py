import pytest

try:
    from algorithms.basic.three_sum.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/basic/three_sum/imp.py"
    )

test_data = [
    (
        ([12, 3, 1, 2, -6, 5, -8, 6], 0),
        [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]],
    )
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_three_sum(test_input, expected):
    result = solution(*test_input)
    assert result == expected
