i = 1

result1 = 0
result2 = 0
result = 0
while (i <= 4):
    result = result + i
    i = i + 1
    print(result)
    if (result != 0):
        result1 = result1 + result
        result2 = result2 + (result * result)
        print(result2)
print(f"the total sum is {result}")
print(f"the total sum is {result1}")
print(f"the total sum is {result2}")
