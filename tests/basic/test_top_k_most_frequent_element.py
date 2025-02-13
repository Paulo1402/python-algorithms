import pytest

from tests.basic.conftest import top_k_most_frequent_element_test_data


@pytest.mark.parametrize("test_input, expected", top_k_most_frequent_element_test_data)
def test_top_k_most_frequent_element(top_k_most_frequent_element, test_input, expected):
    result = top_k_most_frequent_element(*test_input)
    assert result == expected
