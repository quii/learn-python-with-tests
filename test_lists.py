import pytest


@pytest.fixture
def people():
    return ['chris', 'ruth', 'pepper']


def test_list_index_ops(people):
    assert people[0].title() == "Chris"
    assert people[-1] == "pepper", "last person should be pepper"


def test_list_append(people):
    people.append('tiago')
    assert people[-1] == 'tiago'


def test_list_delete(people):
    del people[-1]
    assert people[-1] == 'ruth'


def test_insert_at_index(people):
    people.insert(0, 'dave')
    assert people[0] == 'dave'


def test_pop(people):
    person = people.pop()
    assert person == 'pepper'
    assert people == ['chris', 'ruth']


def test_pop_at_index(people):
    person = people.pop(1)
    assert person == 'ruth'
    assert people == ['chris', 'pepper']


def test_remove(people):
    people.remove('chris')
    assert people == ['ruth', 'pepper']


def test_sort(people):
    people.sort()
    assert people == ['chris', 'pepper', 'ruth']
    people.sort(reverse=True)
    assert people == ['ruth', 'pepper', 'chris']


def test_sorted(people):
    sorted_people = sorted(people)
    assert people == ['chris', 'ruth', 'pepper']
    assert sorted_people == ['chris', 'pepper', 'ruth']


def test_len(people):
    assert len(people) == 3


def test_map(people):
    assert list(map(lambda x: x.title(), people)) == ['Chris', 'Ruth', 'Pepper']
    assert [x.title() for x in people] == ['Chris', 'Ruth', 'Pepper']


def test_remove_multiple():
    numbers = [1, 1, 1]
    numbers.remove(1)
    assert numbers == [1, 1]
