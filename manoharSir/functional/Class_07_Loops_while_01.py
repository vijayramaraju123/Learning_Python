input_number = int(input())

count = 0
loop_variable = 1

while (loop_variable <= input_number):
    if (input_number % loop_variable == 0):
        count = count + 1
    loop_variable += 1

print(f"count of factors of {input_number} is {count}")
