import pytest

from tests.basic.conftest import two_sum_test_data


@pytest.mark.parametrize("test_input, expected", two_sum_test_data)
def test_two_sum(two_sum, test_input, expected):
    result = two_sum(*test_input)
    assert result == expected
