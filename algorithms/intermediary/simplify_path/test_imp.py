import pytest

try:
    from algorithms.intermediary.simplify_path.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/intermediary/simplify_path/imp.py"
    )

test_data = [
    (("/home/",), "/home"),
    (("/home/../",), "/"),
    (("/home/../home/./",), "/home"),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_simplify_path(test_input, expected):
    result = solution(*test_input)
    assert result == expected
