import pytest

from tests.intermediary.conftest import path_sum_2_test_data


@pytest.mark.parametrize("test_input, expected", path_sum_2_test_data)
def test_path_sum_2(path_sum_2, test_input, expected):
    result = path_sum_2(*test_input)
    assert result == expected
