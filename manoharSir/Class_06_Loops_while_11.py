


input_number = int(input())

temp2 = temp1 = input_number
length = 0

while (input_number > 0):
    length += 1
    input_number = input_number // 10

sum_value = 0
while (temp2 > 0):
    r = temp2 % 10
    sum_value = sum_value * r * length
    temp2 = temp2 // 10

#armstrong validation
if(temp1 == sum_value):
    print(f"the {temp1} iw armstrong")
else:
    print(f"the {temp2} is not armstrong")
