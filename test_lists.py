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
        colours.remove('red')
        self.assertEqual(colours, ['blue'])

        # remove only removes one thing
        numbers = [1, 1, 1]
        numbers.remove(1)
        self.assertEqual(numbers, [1, 1])

        numbers = [2, 1, 3]
        numbers.sort()
        self.assertEqual(numbers, [1, 2, 3])
        numbers.sort(reverse=True)
        self.assertEqual(numbers, [3, 2, 1])
        other_numbers = sorted(numbers)
        self.assertEqual(numbers, [3, 2, 1])
        self.assertEqual(other_numbers, [1, 2, 3])
        self.assertEqual(len(numbers), 3)


if __name__ == '__main__':
    unittest.main()
