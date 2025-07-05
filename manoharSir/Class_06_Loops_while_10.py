
input_number = int(input())

temp=input_number
length = 0

while (input_number > 0):
    length += 1
    input_number = input_number//10

print(f"the length of {temp} is {length}")

