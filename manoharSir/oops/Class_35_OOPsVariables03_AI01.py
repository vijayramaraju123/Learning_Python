

# Instance Variable
# Defined inside a class method using self.
# Unique to each object (instance) of the class.
# Use case: When each object needs its own data.

class MyClass:
    def __init__(self, value):
        self.instance_var = value  # Instance variable

# Class Variable (Static Variable)
# Defined inside the class but outside any method.
# Shared across all instances of the class.
# Use case: When you want to share data among all instances (e.g., counting objects).

class MyClass:
    class_var = 0  # Class variable

    def __init__(self):
        MyClass.class_var += 1


#  Global Variable
# Defined outside all functions and classes.
# Accessible throughout the module unless shadowed.
# Use case: When a value needs to be accessed across multiple functions or classes

global_var = "I am global"

def func():
    print(global_var)

# Local Variable
# Defined inside a function or method.
# Accessible only within that function or method.
# Use case: Temporary values used only within a function.

def func():
    local_var = "I am local"
    print(local_var)

