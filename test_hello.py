import pytest

from hello import Greeter

@pytest.fixture
def greeter():
    return Greeter("Hello")

def test_greet(greeter):
    assert greeter.greet("world") == "Hello, world"
