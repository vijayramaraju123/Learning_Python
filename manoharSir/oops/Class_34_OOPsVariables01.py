
# loval variable :Defined inside a function and accessible only within that function
# Global variable : Defined outside any function and accessible throughout the program, including inside functions (if not overridden).

# a is global variable
a = 10

print(f"Global variable {a}")

def func1():
    a = 30 # local variable
    print(f"local in func1: {a}")

def func2():
    a = 35 # local variable
    print(f"local in func2: {a}")

func1()
func2()


# to access global variables in local method
a = 10
def func3():
    a = 25
    print(f"local in func3: {a}")
    print(f"global a: {globals()['a']}")

func3()
