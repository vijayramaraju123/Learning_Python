
# leap year


def leap_year():
    year_number = input("enter the year number")
    try:
        year_number = int(year_number)
        if (year_number % 4 == 0 and year_number % 400 != 0) or (year_number % 400 == 0):
            print(f"it is leap year")
        elif ((year_number % 100 == 0) and (year_number % 400 != 0)) or (year_number % 4 != 0):
            print(f"it is not a leap year")
    except Exception as e:
        print(e)


leap_year()

