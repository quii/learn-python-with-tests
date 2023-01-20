from unittest import TestCase

from hello import Greeter


class Test(TestCase):
    def test_greet(self):
        subject = Greeter("Hello")
        self.assertEqual(subject.greet("world"), "Hello, world")
