import pytest

from intermediary import compare_binary_search, path_sum_2, simplify_path, word_search


@pytest.fixture
def compare_binary_search_fixture():
    return compare_binary_search.Solution()
