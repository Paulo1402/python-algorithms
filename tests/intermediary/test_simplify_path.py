import pytest

from tests.intermediary.conftest import simplify_path_test_data


@pytest.mark.parametrize("test_input, expected", simplify_path_test_data)
def test_simplify_path(simplify_path, test_input, expected):
    result = simplify_path(*test_input)
    assert result == expected
