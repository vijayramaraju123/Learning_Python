

#In Python, a class method is a method that is bound to the class and not the instance of the class.
#@classmethod allows access to the class (cls) rather than an instance (self).
#Class variables are shared across all instances and the class itself.
#You can access and modify class variables using either cls or the class name (Test).


class Test:
    a = 10   # Static Variable

    @classmethod
    def m1(cls):
        Test.a = Test.a + 1  #11
        cls.a = cls.a + 1    #12  # we can access static variable using class method
        print(Test.a)
        print(cls.a)

Test.m1()
