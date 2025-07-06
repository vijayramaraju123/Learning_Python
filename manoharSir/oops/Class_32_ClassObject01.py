
class Item:
    def setItem(self):
        self.name = "vijay"
        self.price = 28
        self.quantity = 40

    def getItem(self):
        print(f"the name is {self.name}")
        print(f"the price is {self.price}")
        print(f"the quantity is {self.quantity}")
        print(f"the total quantity is {self.totalPrice}")

    def getTotalPrice(self):
        self.totalPrice = self.price * self.quantity


item = Item()
item.setItem()
item.getTotalPrice()
item.getItem()

