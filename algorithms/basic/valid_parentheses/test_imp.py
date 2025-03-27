import pytest

try:
    from algorithms.basic.valid_parentheses.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/basic/valid_parentheses/imp.py"
    )

test_data = [
    (("([])",), True),
    (("([{}])",), True),
    (("([{})",), False),
    (("(}])",), False),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_valid_parentheses(test_input, expected):
    result = solution(*test_input)
    assert result == expected
