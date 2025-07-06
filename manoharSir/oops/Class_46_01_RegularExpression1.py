

try:
    a = int(input())
    b = int(input())

    list1 = [1, 2, 3, 4]
    print(list1[8])

    c = a / b
    print(c)

## order of different exceptions is really important 1:01:13 seconds
except ZeroDivisionError as e:
    print(e)

except IndexError as e:
    print(e)

except Exception as e:
    print(e)

finally:
    print("finally called")
