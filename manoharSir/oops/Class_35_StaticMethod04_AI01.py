


# A static method in Python is a method that belongs to a class rather than an instance of the class,
# but it doesn't access or modify class or instance state

# It does not take self or cls as the first argument.
# It behaves like a regular function but lives in the class's namespace.

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

# Call using class name
print(MathUtils.add(5, 3))  # Output: 8

# Call using an instance
obj = MathUtils()
print(obj.add(10, 4))       # Output: 14


# Use a static method when:
# The method does not need access to instance (self) or class (cls) data.
# You want to group utility functions logically within a class.
