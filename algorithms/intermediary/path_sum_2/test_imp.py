import pytest

from algorithms.utils import BinaryTree

try:
    from algorithms.intermediary.path_sum_2.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/intermediary/path_sum_2/imp.py"
    )

test_data = [
    ((BinaryTree(value=5), 5), [[5]]),
    (
        (
            BinaryTree(
                value=5,
                left=BinaryTree(
                    value=4,
                    left=BinaryTree(value=11, left=BinaryTree(7), right=BinaryTree(2)),
                ),
                right=BinaryTree(
                    value=8,
                    left=BinaryTree(13),
                    right=BinaryTree(value=4, left=BinaryTree(5), right=BinaryTree(1)),
                ),
            ),
            22,
        ),
        [[5, 4, 11, 2], [5, 8, 4, 5]],
    ),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_path_sum_2(test_input, expected):
    result = solution(*test_input)
    assert result == expected
