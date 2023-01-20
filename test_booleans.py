from unittest import TestCase

from booleans import is_even


class Test(TestCase):
    def test_is_even(self):
        self.assertEqual(is_even(2), True)
        self.assertEqual(is_even(3), False)
        self.assertEqual(is_even(2) and is_even(4), True)
