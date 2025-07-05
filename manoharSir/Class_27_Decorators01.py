







def decor(func):
    def inner(name):
        if name == "mano":
            print("hello mano today its raining")
        else:
            func(name)
    return inner

@decor
def f1(name):
    print("hello",name,"Good morning")


f1("mano")
f1("kishore")


def f2(func):
    print(id(func))
    print("peter")

my_mbda = lambda name:print("hello",name)
print(id(my_mbda))
f2(my_mbda)
