import pytest

from adding import add

@pytest.mark.parametrize("x,y,expected", [
    (2, 2, 4),
    (1_000, 2_000, 3_000),
])
def test_add(x, y, expected):
    assert add(x, y) == expected
