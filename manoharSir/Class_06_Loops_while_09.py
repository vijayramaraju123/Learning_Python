
input_number = int(input())

temp=input_number
sum_value = 0

while (input_number > 0):
    r = input_number%10
    sum_value = sum_value * 10 + r
    input_number = input_number//10

print(f"the reverse of given {temp} is {sum_value}")


#palindrome value
if(temp ==  sum_value):
    print(f"{temp} is palendrome")
else:
    print(f"{temp} is not a palindrome")

