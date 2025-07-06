


class Test:
    a = 10  #Static/class variable

    def m1(self):  # Instance method
        self.x = 50
        print(f"the instance variable is {self.x}")

    def m2(self):  # Instance method
        print(Test.a)
        Test.f2()
        self.m1()
        print(self.x)
        #self.x = 50

    @staticmethod
    def f2():
        print("This is test2")

    @staticmethod
    def f1():
        print(Test.a)

        test=Test()
        test.m1()
        print(Test.a)
        print(test.x)
        Test.f2()

test=Test()
test.m1()
print("**************")
test.m2()
print("**************")
Test.f1()

