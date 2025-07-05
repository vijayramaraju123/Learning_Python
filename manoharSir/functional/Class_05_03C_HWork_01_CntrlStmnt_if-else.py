
# Electricity bill


def bill_consumption():
    Units_Consumed = input("enter the units consumed")
    result = 0
    try:
        units = float(Units_Consumed)
        if units <= 100:
            result = units * 1
            print(result)
        elif units > 100 and units <= 150:
            result1 = (100 * 1) + ((units - 100) * 1.5)
            print(result1)
        elif units > 150:
            result = 100 * 1 + 50 * 1.5 + (units - 150) * 2
            print(result)
    except Exception as e:
        print(e)


bill_consumption()


Class_06_Loops_while_01.py
i = 1

while i <= 10:
    print(i)
    i = i+1


Class_06_Loops_while_02.py

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

Class_06_Loops_while_03.py
i = 1

result1=0
result2=0
result = 0
while (i <= 4):
    result = result + i
    i = i+1
    print(result)
    if(result != 0 ):
        result1=result1+result
        result2 = result2 + (result*result)
        print(result2)
print(f"the total sum is {result}")
print(f"the total sum is {result1}")
print(f"the total sum is {result2}")
