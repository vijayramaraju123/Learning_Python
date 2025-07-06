

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):        # use magic method for override
        return (self.x+other.x,self.y+other.y)

p1= Point(2,3)
print(p1)
p2= Point(4,5)
print(p2)
a3 = p2+p1
print(a3)

