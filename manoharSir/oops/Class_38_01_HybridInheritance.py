


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

class D(C,B):
    def div(self):
        self.div_result=self.result+self.aa+self.nadd
        print(self.div_result)


d = D(2,4)
d.getA()
d.add()
d.new_add()
d.div()


