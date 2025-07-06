
# using objects of one class from other class without any relation is called has a relation
# to use properties of in one class with in another class with out having inheritance.
class A:
    def __init__(self):
        self.x = 5
        self.y = 8

class B:
    def add(self,a):
        self.c=a.x+a.y
        print(self.c)

a= A()
b =  B()
b.add(a)
