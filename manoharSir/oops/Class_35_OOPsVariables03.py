

# static variables and methods.

database = "dbdatabase"  # Global Variable


def m1():
    print(database)


class Test:
    def set_var(self):  # Static/Class Variable
        self.a = 10

    def incr(self):
        self.a = self.a + 1
        print(self.a)

    def test(self, databaseName):
        print(databaseName + "Connect")


def main():
    m1()        # 
    global database
    database = "mysql server "

    test1 = Test()
    test1.set_var()
    test1.incr()
    test1.test(database)
    m1()




if __name__ == '__main__':
    main()

