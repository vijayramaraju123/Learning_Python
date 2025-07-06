


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

class C(A):
    def new_add(self):
        self.nadd = self.aa + (self.bb*5)
        print(f"the new sume is {self.nadd}")


b = B(2,4)
b.add()
b.getA()

c = C(4,8)
c.new_add()
c.getA()

