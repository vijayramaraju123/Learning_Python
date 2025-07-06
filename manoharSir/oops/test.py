


test.py
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return print(f"{self.name} is {self.age} years old")

    # Another instance method
    def speak(self, sound):
        return print(f"{self.name} says {sound}")

a = Dog("puppu",24)
a.description()

a.speak("meaow")