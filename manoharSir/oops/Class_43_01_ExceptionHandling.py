

Class_43_01_ExceptionHandling.py

# One except block handling many exceptions

try:
    a = int(input())
    b = int(input())

    list1 = [1, 2, 3, 4]
    print(list1[2])

    c = a / b
    print(c)

except Exception as e:
    print(e)
    print(f"exception cought: {e}")

finally:
    print("finally called")

