
# lambda functions

# variableName =  lambda parameter(s): expression
# function object

result = lambda x: x+10
print(result(5))

# sum of numbers
def add(x,y):
    return x+y
print(add(1,2))

#TestCase01
print(lambda x,y:x+y)

#TestCase02
print((lambda x,y:x+y)(1,2))

# sorting a list of tuples by the second element
data = [(1,2),(4,5),(6,4)]
sorted_data =  sorted(data,key = lambda x:x[1])
print(f"sorted data {sorted_data}")

sorted_data1 =  sorted(data,key = lambda x:x[0])
print(f"sorted data {sorted_data1}")



def arthmaticOps(x,y):
    return {
        "add": (lambda x,y:x+y)(x,y),
        "sub":  (lambda x,y:x-y)(x,y),
        "div":  (lambda x,y:x*y)(x,y)
    }

value = arthmaticOps(3,2)
print(value)

cities  = {"Delhi": 24000,"Mumbai":14525,"Hyderabad": 200000}
cities_sorted = sorted(cities.items(),key = lambda x:x[0])
print(cities_sorted) # list of tuples

## to convert to dictionary
cities_sorted_1 = dict(sorted(cities.items(),key = lambda x:x[0]))
print(cities_sorted_1)

