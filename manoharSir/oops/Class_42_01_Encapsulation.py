

# it will restrict the access using private and protect methods

# by using setters we can modify the private members

class Person:
    def __init__(self, name, age, salary):
        self.name = name  # public
        self._age = age  # protected
        self.__salary = salary  # private

    # Public method
    def display_inf(self):
        print(f"name is {self.name}, age is {self._age} and salary is {self.__salary}")

    # Getter for the private salary attributes
    def get_salary(self):
        return self.__salary

    # setter for the private salary attribute
    def set_salary(self,salary):
        if salary> 0:
            self.__salary = salary
        else:
            print("salary should be the positive number")



person = Person("peter", 40, 200000)
person.display_inf()
person.set_salary(50000)
print(f" salary is {person.get_salary()}")

