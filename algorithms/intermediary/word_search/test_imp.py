import pytest

try:
    from algorithms.intermediary.word_search.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/intermediary/word_search/imp.py"
    )

test_data = [
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


@pytest.mark.parametrize("test_input, expected", test_data)
def test_word_search(test_input, expected):
    result = solution(*test_input)
    assert result == expected
