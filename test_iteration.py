import pytest


def test_iteration():
    total = 0
    for number in [1, 2, 3]:
        total += number
    assert total == 6

    total = 0
    for number in range(1, 4):
        total += number

    assert total == 6
    assert list(range(1, 3)) == [1, 2]

    # the 3rd argument adds 2 to each number, presumably it defaults to 1
    assert list(range(2, 11, 2)) == [2, 4, 6, 8, 10]

    numbers = list(range(0, 20))
    assert max(numbers) == 19
    assert min(numbers) == 0
    assert sum(numbers) == 190


def test_list_comprehension():
    squares = [value ** 2 for value in range(1, 11)]
    assert squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # slices just like go, and you can use them in for too
    assert squares[1:4] == [4, 9, 16]
    squares_copy = squares[:]
    squares_copy.pop()
    assert squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert squares_copy == [1, 4, 9, 16, 25, 36, 49, 64, 81]


def test_tuples():
    # tuples are immutable lists
    dimensions = (200, 50)
    assert dimensions[0] == 200

    with pytest.raises(Exception):
        dimensions[0] = 250

    dimensions = (100, 50)
    assert dimensions[0] == 100
