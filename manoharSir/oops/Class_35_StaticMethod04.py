


class Test:
    a = 10

    @staticmethod
    def incr():
        Test.a = Test.a + 1
        print(Test.a)

Test.incr()
Test.incr()
Test.incr()
