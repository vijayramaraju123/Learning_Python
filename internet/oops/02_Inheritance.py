

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello {self.name} my age is {self.age}")


class animal(person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def say_hello1(self):
        super().say_hello()
        print(f"i am the {self.gender} ang {self.gender}")


person = person("vijay", 24)
# person.say_hello()

anml = animal("raju", 28, "male")
anml.say_hello1()


03_getterAndSetter.py
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
