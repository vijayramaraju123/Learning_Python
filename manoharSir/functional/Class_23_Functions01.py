## Normal function
def sayhello():
    print("say welcome to function")


sayhello()


def greet(name="World"):
    print(f"Hello, {name}!")


greet()


## parametrized function
def addition(a, b):
    c = a + b
    return c


value_frmFun = addition(2, 4)
print(f"the value of function is {value_frmFun}")


## conditional return
def max(a, b):
    if a > b:
        return a
    else:
        return b


value = max(2, 4)
print(f"the value is {value}")


## function returning multiple values
def arthimatic(a, b):
    add = a + b
    diff = a - b
    div = a / b
    return add, diff, div


result = arthimatic(2, 4)
print(type(result))
print(result)
addtion, subtraction, divition = result
print(addtion)
print(subtraction)
print(divition)
