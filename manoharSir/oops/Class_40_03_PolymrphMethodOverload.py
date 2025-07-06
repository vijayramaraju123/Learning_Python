


# Method overloading

def add(a,b):
    return a+b

print(add(2,4))
print(add(6,8))
print(add("a","b"))


def add1(*args):
    return sum(args)

print(add1(2,4))
print(add1(6,8))
print(add1(1,2,3,4))

