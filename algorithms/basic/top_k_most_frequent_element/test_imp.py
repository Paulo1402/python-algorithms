import pytest

try:
    from algorithms.basic.top_k_most_frequent_element.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/basic/top_k_most_frequent_element/imp.py"
    )

test_data = [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1], 1), [1]),
    (([1, 1, 1, 2, 2, 3], 3), [1, 2, 3]),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_top_k_most_frequent_element(test_input, expected):
    result = solution(*test_input)
    assert result == expected
