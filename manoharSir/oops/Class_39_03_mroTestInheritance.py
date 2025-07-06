
# MRO
# (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# check Bclass -> Aclass -> instance method
class A:
    def __init__(self):
        print("A's COnstructor")


class B(A):
    def __init__(self):
        super().__init__()
        print("Bs constructor")


b = B()

print(B.__mro__)
