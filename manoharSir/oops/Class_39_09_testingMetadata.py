

class A:
    def __init__(self):
        print("A")

class B(A):
    pass

b =B()
print(B.__dict__)
print(B.__base__)
print(B.__doc__)

