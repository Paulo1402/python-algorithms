import pytest

from tests.intermediary.conftest import compare_binary_search_test_data


@pytest.mark.parametrize("test_input, expected", compare_binary_search_test_data)
def test_compare_binary_search(compare_binary_search, test_input, expected):
    result = compare_binary_search(*test_input)
    assert result == expected
