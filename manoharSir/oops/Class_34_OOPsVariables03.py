

class Test:
    a = "India"

    def func(self):
        print(f"the global may be {a}")
        load = 24
        print(f"load is {load}")


def main():
    mthd = Test()
    mthd.func()
if __name__ == '__main__':

    globals()['a'] = 65
    main()
