

# it will restrict the access using private and protect methods

# private __
# protected _

class Person:
    def __init__(self, name, age, salary):
        self.name = name  # public
        self._age = age  # protected
        self.__salary = salary  # private


person = Person("peter", 40, 200000)
print(person.name)  # Accessing name
print(person._age)  # accessing age, not recommended
print(person.__salary)  # Accessing salary
