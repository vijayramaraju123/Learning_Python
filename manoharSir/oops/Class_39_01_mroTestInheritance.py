
#MRO
# (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# check Bclass -> Aclass -> instance method
class A:
    def __init__(self):
        print("A's COnstructor")

class B(A):
    pass

b = B()

print(B.__mro__)
