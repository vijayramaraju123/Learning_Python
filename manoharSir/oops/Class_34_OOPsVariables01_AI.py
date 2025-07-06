
class Test:
    a = 10  # Class variable

    def func(self, data):
        print(f"Received data: {data}")
        data = 24  # This only changes the local copy
        print(f"Modified local data inside method: {data}")


if __name__ == '__main__':
    tst = Test()
    print(f"Class variable Test.a: {Test.a}")

    # Set a global variable
    globals()['data'] = 40
    print(f"Global variable 'data' before calling func: {data}")

    # Pass the global variable to the method
    tst.func(data)

    print(f"Global variable 'data' after calling func: {data}")
