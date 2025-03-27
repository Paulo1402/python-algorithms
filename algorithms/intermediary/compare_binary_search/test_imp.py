import pytest

from algorithms.utils import BinaryTree

try:
    from algorithms.intermediary.compare_binary_search.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/intermediary/compare_binary_search/imp.py"
    )

test_data = [
    (
        (
            BinaryTree(value=2, left=BinaryTree(value=1), right=BinaryTree(value=3)),
            BinaryTree(value=2, left=BinaryTree(value=1), right=BinaryTree(value=3)),
        ),
        True,
    )
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_compare_binary_search(test_input, expected):
    result = solution(*test_input)
    assert result == expected
