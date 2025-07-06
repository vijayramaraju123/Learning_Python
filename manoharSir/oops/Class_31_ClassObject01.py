
class Item:
    def setItem(self):
        self.name = "vijay"
        self.age = 28
        self.loc = "Bhimavaram"

    def getItem(self):
        print(f"the name is {self.name}")
        print(f"the name is {self.age}")
        print(f"the name is {self.loc}")


item = Item()
item.setItem()
item.getItem()
