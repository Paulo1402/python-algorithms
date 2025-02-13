import pytest

from tests.basic.conftest import minimum_depth_of_binary_tree_test_data


@pytest.mark.parametrize("test_input, expected", minimum_depth_of_binary_tree_test_data)
def test_minimum_depth_of_binary_tree(
    minimum_depth_of_binary_tree, test_input, expected
):
    result = minimum_depth_of_binary_tree(*test_input)
    assert result == expected
