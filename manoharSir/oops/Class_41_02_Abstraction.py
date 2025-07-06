
# we can not instantiate abstract class
# abstract class can have both abstract and concrete methods.

from abc import ABC, abstractmethod


class Test(ABC):

    @abstractmethod
    def m1(self):
        pass

    def f1(self):
        print("Hello")


class Test2(Test):
    def m1(self):
        print("Hi")


test = Test2()
test.m1()
test.f1()

