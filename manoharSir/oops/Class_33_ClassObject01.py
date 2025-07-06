
class Item:
    def setItem(self, name1, price1, quantity1):
        self.name = name1
        self.price = price1
        self.quantity = quantity1

    def getItem(self):
        print(f"the name is {self.name}")
        print(f"the price is {self.price}")
        print(f"the quantity is {self.quantity}")
        print(f"the total quantity is {self.totalPrice}")

    def getTotalPrice(self):
        self.totalPrice = self.price * self.quantity


item = Item()
item.setItem("vijay", 24, 40)
item.getTotalPrice()
item.getItem()

item = Item()
item.setItem("Raju", 8, 10)
item.getTotalPrice()
item.getItem()
