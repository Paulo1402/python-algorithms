import pytest

from tests.basic.conftest import decode_string_test_data


@pytest.mark.parametrize("test_input, expected", decode_string_test_data)
def test_decode_string(decode_string, test_input, expected):
    result = decode_string(*test_input)
    assert result == expected
