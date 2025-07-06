


class A:
    def __init__(self):
        self.a = 10
        self.b=14

    def getA(self):
        print(self.a)
        print(self.b)

class B(A):
    def add(self):
        self.result = self.a+self.b
        print(f"the sum is {self.result}")

b = B()
b.add()
