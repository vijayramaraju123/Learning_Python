

class Person:
    def __init__(self, name):
        self._name = name  # Conventionally private (single underscore)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

# Usage
p = Person("Alice")
print(p.get_name())  # Alice
p.set_name("Bob")
print(p.get_name())  # Bob
