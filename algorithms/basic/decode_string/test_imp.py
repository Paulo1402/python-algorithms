import pytest

try:
    from algorithms.basic.decode_string.imp import solution
except ImportError:
    raise ImportError(
        "Could not find the solution in algorithms/basic/decode_string/imp.py"
    )

test_data = [
    (("22[a]3[bc]",), "aaaaaaaaaaaaaaaaaaaaaabcbcbc"),
    (("3[a2[c]]",), "acccccccccccccccccccccccccccccccc"),
    (("2[abc]3[cd]ef",), "abcabccdcdcdef"),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_decode_string(test_input, expected):
    result = solution(*test_input)
    assert result == expected
