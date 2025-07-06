

try:
    a = int(input())
    b = int(input())

    list1 = [1,2,3,4]
    print(list1[8])

    c = a / b
    print(c)

except Exception as e:
    print(e)
finally:
    print("finally called")
