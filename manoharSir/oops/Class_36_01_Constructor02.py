
# it is a special funtion wich is used to decalre and initialize instace variable of a class
# constructor is autmatically called whewver the object is created.


class Book:
    def __init__(self,book,price):
        self.book1 = book
        self.price1 = price

    def getbook(self):
        print(f"the book name is {self.book1}")
        print(f"the book price is {self.price1}")


book1 = Book("Hindu",24)
book1.getbook()

book2 = Book("Mahabharatham",85)
book2.getbook()

