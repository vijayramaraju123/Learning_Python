

# inner functions
# FUnction within a function is called inner function

def outer(x,y):
    def inner(x,y):
        return x+y
    return(inner(x,y))

print(outer(2,4))


def arthmaticOps(x,y):
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def div(x,y):
        return x*y
    return {
        "add": add(x,y),
        "sub": sub(x,y),
        "div": div(x,y)
    }

value = arthmaticOps(2,4)
print(value)


