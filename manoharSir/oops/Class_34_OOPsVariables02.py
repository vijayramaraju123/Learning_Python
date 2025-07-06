
# Static or class variables

# Class variables
#   Belong to the class itself, not to any specific instance.
#   Shared across all instances of the class.
#   Defined inside the class, but outside any instance methods.

class Test:
    a = 10

    def func(self, data):
        print(f"the value of data is {data}")
        data = 24
        info = "data member"
        print(f"the value of data is {data}")


if __name__ == '__main__':
    tst = Test()
    print(Test.a)

    globals()['data1'] = 40
    tst.func(data1)
