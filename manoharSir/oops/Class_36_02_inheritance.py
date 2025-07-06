

class A:
    def __init__(self,a,b):
        self.aa = a
        self.bb=b

    def getA(self):
        print(self.aa)
        print(self.bb)

class B(A):
    def add(self):
        self.result = self.aa+self.bb
        print(f"the sum is {self.result}")

b = B(5,4)
b.add()
