
class A:
    def __init__(self):
        super().__init__()
        self.aa = 4
        self.bb = 16

    def getA(self):
        print(f"the value of a is {self.aa}")
        print(f"the value of b is {self.bb}")


class B:

    def __init__(self):
        self.x = 100
        self.y = 200

    def getB(self):
        print(f"the value of x is {self.x}")
        print(f"the value of y is {self.y}")


class C(A, B):
    def __init__(self):
        super().__init__()
        self.u = 23
        self.v = 75

    def add(self):
        self.result = self.aa + (self.bb) + self.x + self.y + self.u + self.v
        print(f"the new sum is {self.result}")


def main():
    c = C()
    c.getA()
    c.getB()
    c.add()


if __name__ == '__main__':
    main()

