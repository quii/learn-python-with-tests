def test_lists():
    people = ['chris', 'ruth', 'pepper']
    assert people[0].title() == "Chris"
    assert people[-1] == "pepper"

    # todo: this is begging to be a test fixture, learn how to do tha
    people.append('tiago')
    assert people[-1] == 'tiago'
    del people[-1]
    assert people[-1] == 'pepper'

    people.insert(0, 'dave')
    assert people[0]=='dave'

    last_person = people.pop()
    assert last_person == 'pepper'
    assert people[-1] == 'ruth'

    colours = ['red', 'yellow', 'blue']
    yellow = colours.pop(1)
    assert yellow == 'yellow'
    assert colours == ['red', 'blue']
    colours.remove('red')
    assert colours == ['blue']

    # remove only removes one thing
    numbers = [1, 1, 1]
    numbers.remove(1)
    assert numbers == [1, 1]

    numbers = [2, 1, 3]
    numbers.sort()
    assert numbers == [1, 2, 3]

    numbers.sort(reverse=True)
    assert numbers == [3, 2, 1]
    other_numbers = sorted(numbers)
    assert numbers == [3, 2, 1]
    assert other_numbers == [1, 2, 3]
    assert len(numbers) == 3
