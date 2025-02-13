import pytest

from basic import (
    decode_string,
    invert_binary_tree,
    minimum_depth_of_binary_tree,
    palindrome_check,
    top_k_most_frequent_element,
    three_sum,
    two_sum,
    valid_parentheses,
)
from tests.conftest import BinaryTree


@pytest.fixture(name="decode_string")
def decode_string_fixture():
    return decode_string.solution


decode_string_test_data = [
    (("22[a]3[bc]",), "aaaaaaaaaaaaaaaaaaaaaabcbcbc"),
    (("3[a2[c]]",), "acccccccccccccccccccccccccccccccc"),
    (("2[abc]3[cd]ef",), "abcabccdcdcdef"),
]


@pytest.fixture(name="invert_binary_tree")
def invert_binary_tree_fixture():
    return invert_binary_tree.solution


invert_binary_tree_test_data = [
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


@pytest.fixture(name="minimum_depth_of_binary_tree")
def minimum_depth_of_binary_tree_fixture():
    return minimum_depth_of_binary_tree.solution


minimum_depth_of_binary_tree_test_data = [
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


@pytest.fixture(name="palindrome_check")
def palindrome_check_fixture():
    return palindrome_check.solution


palindrome_check_test_data = [
    (("ana",), True),
    (("array",), False),
]


@pytest.fixture(name="top_k_most_frequent_element")
def top_k_most_frequent_element_fixture():
    return top_k_most_frequent_element.solution


top_k_most_frequent_element_test_data = [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1], 1), [1]),
    (([1, 1, 1, 2, 2, 3], 3), [1, 2, 3]),
]


@pytest.fixture(name="three_sum")
def three_sum_fixture():
    return three_sum.solution


three_sum_test_data = [
    (
        ([12, 3, 1, 2, -6, 5, -8, 6], 0),
        [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]],
    )
]


@pytest.fixture(name="two_sum")
def two_sum_fixture():
    return two_sum.solution


two_sum_test_data = [
    (([2, 7, 11, 15], 9), [2, 7]),
    (([3, 2, 4], 6), [2, 4]),
    (([3, 3], 6), [3, 3]),
]


@pytest.fixture(name="valid_parentheses")
def valid_parentheses_fixture():
    return valid_parentheses.solution


valid_parentheses_test_data = [
    (("([])",), True),
    (("([{}])",), True),
    (("([{})",), False),
    (("(}])",), False),
]
