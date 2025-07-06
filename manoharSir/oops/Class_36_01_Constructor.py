
# it is a special funtion wich is used to decalre and initialize instace variable of a class
# constructor is autmatically called whewver the object is created.


class Book:
    def __init__(self):
        self.book = "Sentiment"
        self.price = 50

    def getbook(self):
        print(f"the book name is {self.book}")
        print(f"the book price is {self.price}")


book = Book()
book.getbook()
