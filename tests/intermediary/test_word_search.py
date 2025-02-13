import pytest

from tests.intermediary.conftest import word_search_test_data


@pytest.mark.parametrize("test_input, expected", word_search_test_data)
def test_word_search(word_search, test_input, expected):
    result = word_search(*test_input)
    assert result == expected
