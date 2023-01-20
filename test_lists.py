import unittest


class ListsTestCase(unittest.TestCase):
    def test_lists(self):
        people = ['chris', 'ruth', 'pepper']
        self.assertEqual(people[0].title(), "Chris")
        self.assertEqual(people[-1], "pepper")

        people.append('tiago')
        self.assertEqual(people[-1], 'tiago')
        del people[-1]
        self.assertEqual(people[-1], 'pepper')

        people.insert(0, 'dave')
        self.assertEqual(people[0], 'dave')

        last_person = people.pop()
        self.assertEqual(last_person, 'pepper')
        self.assertEqual(people[-1], 'ruth')

        colours = ['red', 'yellow', 'blue']
        yellow = colours.pop(1)
        self.assertEqual(yellow, 'yellow')
        self.assertEqual(colours, ['red', 'blue'])


if __name__ == '__main__':
    unittest.main()
