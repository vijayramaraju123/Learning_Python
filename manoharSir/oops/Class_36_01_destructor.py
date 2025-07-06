

class Test:
    def __del__(self):
        print("object destroyed")
        
obj1=Test()
obj2=Test()
obj3=Test()

print(f"the program ends here")

