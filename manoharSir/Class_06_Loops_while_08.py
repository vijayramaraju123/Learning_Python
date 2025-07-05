
input_number = int(input())

temp=input_number
sum_of_digit = 0

while (input_number > 0):
    r = input_number%10
    sum_of_digit = sum_of_digit + r
    input_number = input_number//10

print(f"the sum of digits of given {temp} is {sum_of_digit}")

