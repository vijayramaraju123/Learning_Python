

class Animal:
    def sound(self):
        print("animal sounds are different")

class Dog(Animal):
    def sound(self):
        print("Bow Bow")

class Cat(Animal):




    def sound(self):
        print("Meow")

def getSound(Animal):
    Animal.sound()

getSound(Animal())
getSound(Cat())
getSound(Dog())
# run time polymorphism occurs on object
