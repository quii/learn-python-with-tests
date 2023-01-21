from booleans import is_even


def test_is_even():
    assert is_even(2)
    assert is_even(3) is False
    assert is_even(2) and is_even(4)
