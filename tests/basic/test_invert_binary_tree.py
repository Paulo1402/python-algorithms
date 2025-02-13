import pytest

from tests.basic.conftest import invert_binary_tree_test_data


@pytest.mark.parametrize("test_input, expected", invert_binary_tree_test_data)
def test_invert_binary_tree(invert_binary_tree, test_input, expected):
    result = invert_binary_tree(*test_input)
    assert result == expected
