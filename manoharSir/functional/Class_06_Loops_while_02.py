i = 1
result = []
total_sum = 0
while i <= 10:
    if i % 2 == 0:
        result.append(i)
        total_sum = total_sum + i
    i = i + 1

print(f"even numbers is {result}")
print(f"total sum is {total_sum}")

print(type(result))
print(type(total_sum))
