



class A:
    def __init__(self):  #self holds the address of current class object
        print(self)
        self.x = 4
        self.y = 8

a1=A()
print(a1)
a2=A()
print(a2)

