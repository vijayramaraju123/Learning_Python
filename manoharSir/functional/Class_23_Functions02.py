


#positional parameters, default, keyed, variable length args

# Positional parmeters
def get_person(name,age):
    print(f"name is {name}")
    print(f"age is {age}")

get_person("vijay",28)

get_person(28,"vijay")
# limitation is we must have to follow the order

#named parameters
get_person(age=28,name="vijay") ## order of values in important
# we no need to follow the order of parameters.

# the positions should be match
# if positions are changed while calling the function, then we need to mention the name of the argemnts
# the number of constructor parameters should be same in defining and calling the fucntion.

