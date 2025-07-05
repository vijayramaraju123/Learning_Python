
# Passing function as parameter
# Higher order functions.

def outer_functio():
    def inner_function(x):
        return x ** 2

    return inner_function

def apply_function(func,values):
    return [func(value) for value in values]

inner_func =  outer_functio()
numbers = [1,2,3,4]
result = apply_function(inner_func,numbers)
print(result)

