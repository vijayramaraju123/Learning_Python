

input_number = int(input())

sum_of_factors = 0
loop_value = 1
while (loop_value <= input_number):
    if (input_number % loop_value == 0):
        sum_of_factors = sum_of_factors + loop_value
        # print(loop_value)
    loop_value = loop_value + 1
print(f"sum of factors {sum_of_factors}")


i = 1
list = []

while i <= 10:
    i = i + 1
    if i == 5:
        continue
    print(i)
    list.append(i)
    print(list)

