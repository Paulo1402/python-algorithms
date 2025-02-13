import pytest

from tests.basic.conftest import valid_parentheses_test_data


@pytest.mark.parametrize("test_input, expected", valid_parentheses_test_data)
def test_valid_parentheses(valid_parentheses, test_input, expected):
    result = valid_parentheses(*test_input)
    assert result == expected
