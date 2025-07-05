
# Control statements control the execution flow of your program.
# Decision-making statements:
# If statement, if-else statement

# to reformat the code :  shft+cntrl+Alt+l




def compare_numbers():
    value_one = input("enter value one")
    value_two = input("enter value two")
    try:
        if value_one.isdigit and value_two.isdigit:
            value_one = int(value_one)
            value_two = int(value_two)
            if value_one > value_two:
                print(f"{value_one} is bigger than {value_two}")
            elif value_two > value_one:
                print(f"{value_one} is smaller than {value_two}")
            else:
                print("both {} and {} are same".format(value_one, value_two))
        else:
            print("please enter the valued number")
    except ValueError:
        print("Please enter valid numeric values (integers or decimals).")

compare_numbers()
