
# to find the greatest of three numbers with multiple if conditions

a = int(input("enter value one"))
b = int(input("enter value two"))
c = int(input("enter value three"))

# Multiple If condition
if a > b and a > c:
    print(f"{a} is greater")
if b > c:
    print(f"{b} is greater than {c}")
else:
    print(f"{c} is greater")
# to reformat the code :  shft+cntrl+Alt+l


# Nested If condition
if a > b:
    if a > c:
        print(f"{a} is greater")
if b > c:
    if b > a:
        print(f"{b} is greater than {c}")
else:
    print(f"{c} is greater")

