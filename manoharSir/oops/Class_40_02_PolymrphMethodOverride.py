


class Animal:
    def sound(self):
        print("animal sounds are different")

class Dog(Animal):
    def sound(self):
        print("Bow Bow")

class Cat(Animal):
    def sound(self):
        print("Meow")

a=Animal()
d=Dog()
c=Cat()

a.sound()
d.sound()
c.sound()
