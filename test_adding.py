from adding import add


def test_add():
    assert add(2, 2) == 4
    assert add(1_000, 2_000) == 3_000
