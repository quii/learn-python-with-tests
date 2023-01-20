import unittest


class MyTestCase(unittest.TestCase):
    def test_iteration(self):
        total = 0
        for number in [1, 2, 3]:
            total += number
        self.assertEqual(6, total)

        total = 0
        for number in range(1, 4):
            total += number
        self.assertEqual(6, total)

        self.assertEqual([1, 2], list(range(1, 3)))

        # the 3rd argument adds 2 to each number, presumably it defaults to 1
        self.assertEqual([2, 4, 6, 8, 10], list(range(2, 11, 2)))

        numbers = list(range(0, 20))
        self.assertEqual(19, max(numbers))
        self.assertEqual(0, min(numbers))
        self.assertEqual(190, sum(numbers))

    def test_list_comprehension(self):
        squares = [value**2 for value in range(1, 11)]
        self.assertEqual([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], squares)

        # slices just like go, and you can use them in for too
        self .assertEqual([4, 9, 16], squares[1:4])
        squares_copy = squares[:]
        squares_copy.pop()
        self.assertEqual([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], squares)
        self.assertEqual([1, 4, 9, 16, 25, 36, 49, 64, 81], squares_copy)

    def test_tuples(self):
        # tuples are immutable lists
        dimensions = (200, 50)
        self.assertEqual(200, dimensions[0])
        # dimensions[0] = 250 <- cant do this

        # but you can override the variable
        dimensions = (100, 50)
        self.assertEqual(100, dimensions[0])



if __name__ == '__main__':
    unittest.main()
