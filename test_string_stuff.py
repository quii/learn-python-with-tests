from unittest import TestCase


class MyTestCase(TestCase):
    def test_something(self):
        self.assertEqual("poo".upper(), "POO")
        self.assertEqual("BUM".lower(), "bum")

        age = 38
        self.assertEqual("you are " + str(age) + " years old", "you are 38 years old")
