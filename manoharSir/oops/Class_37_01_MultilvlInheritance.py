


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

class C(B):
    def new_add(self):
        self.nadd = self.aa + (self.bb*5)
        print(f"the new sume is {self.nadd}")

c = C(2,42)
c.new_add()
c.add()
c.getA()

