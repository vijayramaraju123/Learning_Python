
a = int(input("enter value one"))
b = int(input("enter value two"))
c = int(input("enter value three"))

if a > b and a > c:
    print(f"{a} is greater")
elif b > c:
    print(f"{b} is greater than {c}")
else:
    print(f"{c} is greater")
