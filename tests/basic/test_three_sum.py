import pytest

from tests.basic.conftest import three_sum_test_data


@pytest.mark.parametrize("test_input, expected", three_sum_test_data)
def test_three_sum(three_sum, test_input, expected):
    result = three_sum(*test_input)
    assert result == expected
