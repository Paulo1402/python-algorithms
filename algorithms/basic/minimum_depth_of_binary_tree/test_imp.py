import pytest

from algorithms.utils import BinaryTree

try:
    from algorithms.basic.minimum_depth_of_binary_tree.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/basic/minimum_depth_of_binary_tree/imp.py"
    )

test_data = [
    (
        (
            BinaryTree(
                value=3,
                left=BinaryTree(value=9),
                right=BinaryTree(
                    value=20, left=BinaryTree(value=15), right=BinaryTree(value=7)
                ),
            ),
        ),
        2,
    ),
    (
        (
            BinaryTree(
                value=2,
                right=BinaryTree(
                    value=3, right=BinaryTree(value=4, right=BinaryTree(value=5))
                ),
            ),
        ),
        4,
    ),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_minimum_depth_of_binary_tree(test_input, expected):
    result = solution(*test_input)
    assert result == expected
