import pytest

from algorithms.intermediary import (
    compare_binary_search,
    simplify_path,
    path_sum_2,
    word_search,
)

from tests.conftest import BinaryTree


@pytest.fixture(name="compare_binary_search")
def compare_binary_search_fixture():
    return compare_binary_search.solution


compare_binary_search_test_data = [
    (
        (
            BinaryTree(value=2, left=BinaryTree(value=1), right=BinaryTree(value=3)),
            BinaryTree(value=2, left=BinaryTree(value=1), right=BinaryTree(value=3)),
        ),
        True,
    )
]


@pytest.fixture(name="path_sum_2")
def path_sum_2_fixture():
    return path_sum_2.solution


path_sum_2_test_data = [
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


@pytest.fixture(name="simplify_path")
def simplify_path_fixture():
    return simplify_path.solution


simplify_path_test_data = [
    (("/home/",), "/home"),
    (("/home/../",), "/"),
    (("/home/../home/./",), "/home"),
]


@pytest.fixture(name="word_search")
def word_search_fixture():
    return word_search.solution


word_search_test_data = [
    (
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCCED",
        ),
        True,
    ),
    (
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "SEE",
        ),
        True,
    ),
    (
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCB",
        ),
        False,
    ),
]
