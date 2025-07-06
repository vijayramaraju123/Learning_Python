
# Define a class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound.")

# Define a subclass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} barks.")

# Create objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Call methods
dog1.make_sound()  # Output: Buddy barks.
dog2.make_sound()  # Output: Max barks.

# Access attributes
print(dog1.name)  # Output: Buddy
print(dog1.species)  # Output: Dog
print(dog1.breed)  # Output: Golden Retriever


01_ClassObject.py
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return print(f"{self.name} is {self.age} years old and {self.species}")

    # Another instance method
    def speak(self, sound):
        return print(f"{self.name} says {sound}")


a = Dog("puppu", 24)
print(a.species)

a.description()
a.speak("meaow")

a.name = "monkey"
a.speak("jump")

a.age= 40
a.description()

01_Inheritance.py
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return print(f"{self.name} is {self.age} years old")

    def speak(self, sound):
        return print(f"{self.name} says {sound}")

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

buddy.speak("yap")
buddy.__str__()

02_Inheritance.py
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
