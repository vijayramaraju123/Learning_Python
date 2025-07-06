

# In Python, you can modify static (class) variables in several ways. Here's how:

# Using the Class Name (Recommended)
class MyClass:
    static_var = 0

# Modify using class name
MyClass.static_var = 10
print(MyClass.static_var)  # Output: 10


# Inside a Class Method

class MyClass:
    static_var = 0

    @classmethod
    def update_static(cls, value):
        cls.static_var = value

MyClass.update_static(20)
print(MyClass.static_var)  # Output: 20



# Using an Instance (Not Recommended for Modification)
class MyClass:
    static_var = 0

obj = MyClass()
obj.static_var = 5  # Creates a new instance variable, doesn't change the class variable

print(MyClass.static_var)  # Output: 0
print(obj.static_var)      # Output: 5

