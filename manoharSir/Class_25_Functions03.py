
# Higher order functions

list1 = [1, 2, 3, 4]


def add(value):
    result = value + 108
    return result


result_data1 = list(map(add, list1))
print(result_data1)

result_data = map(add, list1)
print(result_data)

for value in result_data:
    print(value)



list2 = [1, 2, 3, 4]
result_updated = list(map(lambda x: x + 100, list2))
print(result_updated)
