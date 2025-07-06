# Even or Odd

try:
    value_one = input("enter the value_one")
    value_two = input("enter the value_two")
    try:
        value_one = int(value_one)
        value_two = int(value_two)
        if value_one % 2 == 0:
            print(f"value {value_one} is even")
        else:
            print(f"value {value_one} is odd")
    except Exception as e:
        print(f"value 1 is {e}")
except Exception as e:
    print(f"value 2 is {e}")

