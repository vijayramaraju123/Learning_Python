

# Instance Method (Default Method)
# Takes self as the first parameter.
# Can access and modify instance variables.

class MyClass:
    def instance_method(self):
        print("This is an instance method")

# Class Method
# Takes cls as the first parameter.
# Can access and modify class variables.
# Defined using the @classmethod decorator.

class MyClass:
    class_var = 0

    @classmethod
    def class_method(cls):
        cls.class_var += 1
        print(f"Class variable: {cls.class_var}")


# Static Method
# Does not take self or cls.
# Cannot access or modify class or instance variables.
# Defined using the @staticmethod decorator.
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

# Local Method
# A method defined inside another method.
# Only accessible within the enclosing method.
def outer_function():
    def local_method():
        print("This is a local method")
    local_method()


# Global Method
# A function defined outside any class or function.
# Accessible from anywhere in the module (unless shadowed).
def global_function():
    print("This is a global function")

