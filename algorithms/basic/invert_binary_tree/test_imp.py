import pytest

from algorithms.utils import BinaryTree

try:
    from algorithms.basic.invert_binary_tree.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/basic/invert_binary_tree/imp.py"
    )

test_data = [
    (
        (
            BinaryTree(
                value=1,
                left=BinaryTree(
                    value=2,
                    left=BinaryTree(value=7),
                    right=BinaryTree(value=6),
                ),
                right=BinaryTree(
                    value=3,
                    left=BinaryTree(value=5),
                    right=BinaryTree(value=4),
                ),
            ),
        ),
        BinaryTree(
            value=1,
            left=BinaryTree(
                value=3,
                left=BinaryTree(value=4),
                right=BinaryTree(value=5),
            ),
            right=BinaryTree(
                value=2,
                left=BinaryTree(value=6),
                right=BinaryTree(value=7),
            ),
        ),
    )
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_invert_binary_tree(test_input, expected):
    result = solution(*test_input)
    assert result == expected
