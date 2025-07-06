
# it is the process of exposing the essential things hiding background details.
# Abstract protects method implementation details

class Test:
    def m1(self):  # concrete method
        print("Hello")

    # a emthod without body is called abstract method
    def m2(self):
        pass

    # to see proper abstract
    @abstractmethod
    def m3(self):
        pass


# to defined abstract method in a class the class should be abstract

