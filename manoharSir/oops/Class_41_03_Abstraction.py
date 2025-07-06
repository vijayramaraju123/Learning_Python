

from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("im sleeping")

class Dog(Animal):
    def sound(self):
        print("woof woof,.....")

class Cat(Animal):
    def sound(self):
        print("meow meow,......")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()
