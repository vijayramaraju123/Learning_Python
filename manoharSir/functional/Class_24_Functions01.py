


# default parameter function
def get_persions(name,age,gender="Male"):
    print(f"the name is {name} and age is {age} and the gender is {gender}")

get_persions("Vijay",28)

def get_persions_01(name,age,gender="Male"):
    print(f"the name is {name} and age is {age} and the gender is {gender}")

get_persions("radha",28,"Female")

# Its not mandatory to pass the third parameter, as it take the default value assigned in defining the function.
# limitation is we need to follow the order of passing the cosntructor arguments.

# Variable length parameter functions
# we have two different types of variable lenth paramter functions, *args, **kwargs
def var_lngthFunction(*args):  # Its a tuple by default.
    print(type(args))
    print(args)

#TestCase01
var_lngthFunction()
var_lngthFunction(1)
var_lngthFunction(1,2,3)


def var_secondFunction(**kwargs): # dictionary
    print(type(kwargs))
    print(kwargs)

#TestCase02
var_secondFunction()
var_secondFunction(a=1)
var_secondFunction(a=1,b=4)
