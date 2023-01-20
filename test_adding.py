from unittest import TestCase

from adding import add


class Test(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(1_000, 2_000), 3_000)
