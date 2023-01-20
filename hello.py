class Greeter:
    def __init__(self, prefix):
        self.prefix = prefix

    def greet(self, name):
        return self.prefix + ", " + name