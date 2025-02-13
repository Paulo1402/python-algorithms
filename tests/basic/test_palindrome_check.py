import pytest

from tests.basic.conftest import palindrome_check_test_data


@pytest.mark.parametrize("test_input, expected", palindrome_check_test_data)
def test_palindrome_check(palindrome_check, test_input, expected):
    result = palindrome_check(*test_input)
    assert result == expected
