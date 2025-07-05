
temp = start_value = int(input())
comp_value = int(input())

result = 0
while (start_value < comp_value):
    result = result + start_value
    start_value = start_value + 1
    print(f"the sume of numbers from {temp} to {comp_value} : {result}")

print(start_value)
