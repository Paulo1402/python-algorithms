import pytest

try:
    from algorithms.basic.palindrome_check.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/basic/palindrome_check/imp.py"
    )

test_data = [
    (("ana",), True),
    (("array",), False),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_palindrome_check(test_input, expected):
    result = solution(*test_input)
    assert result == expected
