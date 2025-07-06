

A = 12

data = lambda x:x*x
print(data(A))



inf="Welcome"

l= list(filter(lambda x:x != 'e',inf))
print(l)



inf = "Welcome"

remove_m = lambda s: s.replace('m', '')
print(remove_m(inf))




02_lambdaFilter.py
# filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
data = list(filter(lambda x: x % 2 == 0, numbers))
print(data)

words = ["apple", "banana", "cherry", "date"]
results = list(filter(lambda x: len(x) > 4, words))
print(results)

points = [(1, 2), (3, 1), (5, -1)]
tupresult = list(filter(lambda x: x[1] > 0, points))
print(tupresult)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evnResult = list(filter(lambda x: x % 2 == 0 and x > 5, numbers))
print(evnResult)



from functools import reduce

reduceNum = reduce(lambda x, y: x + y, numbers)
print(reduceNum)



import re

# Sample dataFiles list
dataFiles = ["control.txt", "dataCNTL.csv", "report.txt", "CNTL_summary.docx"]

# Compile the regular expression pattern
cntrlPattern = re.compile(".*CNTL.*", re.IGNORECASE)

# Filter the list based on the pattern
cntrlfile = list(filter(cntrlPattern.match, dataFiles))

print(cntrlfile)


03_lambdaMap.py
#map(function, iterable)


mapNumbers = list(map(lambda x: x * x, numbers))
print(mapNumbers)

04_lambdaSorted.py


# sorted(iterable, key=None, reverse=False)
# sorted(iterable, key=lambda x: some_expression)


numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)

strings = ["banana", "apple", "cherry"]
sorted_strings = sorted(strings)

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted_students = sorted(students, key=lambda student: student[2])
print(sorted_students)


words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)


05_lambdaReduce.py
#reduce(function, iterable)


from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)


06_CombineListToTuple.py



list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = list(zip(list1, list2))
print(combined)

07_regularExpression.py
import re

# Example list of filenames
dataFiles = ["control.txt", "CNTL123.txt", "cntl456.txt", "CnTl789.txt", "otherfile.txt"]

# Compile the pattern
cntrlPattern = re.compile(".*CNTL.*", re.IGNORECASE)


# Filter the filenames
cntrlfile = list(filter(cntrlPattern.match, dataFiles))

print(cntrlfile)  # Output: ['CNTL123.txt', 'cntl456.txt', 'CnTl789.txt']


from datetime import datetime
import time

date=datetime.now()
# timestampPath = f"{datetime.now.year:04d}{datetime.now.month:02d}{datetime.now.day:02d}_{datetime.now.hour:02d}{datetime.now.minute:02d}{datetime.now.second:02d}"
print(date)

08_jsonLoads_jsonDumps.py
#Json Loads : Converts a JSON string into a Python object.


import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_dict = json.loads(json_string)

print(python_dict)
# Output: {'name': 'John', 'age': 30, 'city': 'New York'}


#Json Dump : Converts a Python object into a JSON string


import json

python_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(python_dict, indent=4)

print(json_string)

09_WhleLoop_Collazt.py

n = input("enter the value")
n = int(n)

while n != 1:
    print(n, end = " -> ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1



10_WhleLoop_MaxPasswordsAttempt.py


attempts  = 0
set_password = "1234"
while attempts <= 3:
    Password = input("Enter the password")
    if Password == set_password:
        print("entered the correct password")
        break
    else:
        print("entered the wrong password")
        print(f"max retries left {3 - attempts}")
    attempts = attempts + 1
print("you have reached the max attempts")

11_WhileLoop_GuessRandomNumber.py

secretNumber = 1
guessNumber = 0

while guessNumber != secretNumber:
    secretNumber = int(input("enter secrete number"))
    guessNumber = int(input("PLease enter the guessing number"))
    if guessNumber < secretNumber:
        print("guess number is less than the secret number")
        print(f"Hint: please add {secretNumber - guessNumber} to the guessing number you have entered")
    elif guessNumber > secretNumber:
        print("guess number is greater than the secrete number")
        print(f"Hint: please subtract {guessNumber - secretNumber} from the guessing number you have entered")
print("Congrats both the guess and secrete numbers are the same")


11_WhleLoop_MaxPasswordsReset.py



def password_reset():
    max_attmpts = 3
    attempts = 0
    print("please enter your password")
    reset_password = input()
    print("Congrats the password has been set")
    while attempts <= max_attmpts:
        Password = input("Enter the password")
        if Password == reset_password:
            print("entered the correct password")
            break
        else:
            print("entered the wrong password")
            if max_attmpts - attempts != 0:
                print(f"max retries left {max_attmpts - attempts}")
        if (max_attmpts - attempts ) != 0:
            attempts = attempts + 1
            continue
        print("you have reached the max attempts")
        print("reset your password")
        reset_password = input("enter the new password")
        print(f"Congrats the new password is {reset_password}")
        attempts = attempts -max_attmpts

def main():
    password_reset()

if __name__== '__main__':
    main()


12_ATMFunction.py
amount = 100
balance = 100
prcd = "yes"
print("Welcome to SBI")
print("Are you want to proceed.. yes or not")
proceed = input()
while proceed == "yes":
    amount = balance
    print("select the below options :Balance, Statement, Withdrawl or press no")
    transaction_typ = input()
    if transaction_typ == "no":
        print("Thank you for visiting SBI")
        break
    if transaction_typ == "Balance":
        print(f"balance in your account is {amount}")
        print("do you want to proceed further!!!...yes or not")
        furtherproceed = input()
        if furtherproceed == "no":
            print("Have a great day ahead")
            break
    elif transaction_typ == "Statement":
        print(f"please collect your mini statement")
        print("do you still want further transaction!!!...yes or not")
        furtherproceed = input()
        if furtherproceed != "yes":
            print("Have a great day ahead")
            break
    elif transaction_typ == "Withdrawl":
        print("enter the amount to be withdrawn")
        wthdrwn = int(input())
        if wthdrwn < amount:
            print(f"your remaining amount after the withdrawl is {amount - wthdrwn}")
            print("please press ok to continue")
            continue1 = input()
            if continue1 == "ok":
                print("please collect your amount")
                balance = amount - wthdrwn
                print(f"the balance in your account is {balance}")
                print("do you wanto to proceed further, type yes else press no")
                furtherproceed = input()
                if furtherproceed == "no":
                    break
# elif transaction_typ == "no":
#    proceed = "no"
# break


13_lambda_listOfMap.py

from functools import reduce

rds = reduce(lambda x,y:x+y,fltr)
print(rds)



from functools import reduce

products = [
 {"name": "Laptop", "price": 1000},
{"name": "Monitor", "price": 300},
 {"name": "Keyboard", "price": 50}
]

finddata=reduce(lambda x,y:x+y['price'],products,0)
print(finddata)



products = [
 {"name": "Mouse", "price": 500},
 {"name": "Keyboard", "price": 500},
 {"name": "Monitor", "price": 1500}
]


srted=sorted(products,key=lambda x:(x['price'],x["name"]))
sorted_products = sorted(products, key=lambda x: (x["price"], x["name"]))
print(sorted_products)


14_lambd_listOfTuple.py


pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs) # Output: [(4, 1), (2, 2), (1, 3)]

sort = sorted(pairs,key =lambda x:x[0])
print(sort)

max_val =lambda x,y: x if x>y else y
print(max_val(2,4))

tsttest.py



print("please enter your password")
attempts  = 0
reset_password= input()
print("Congrats the password has been set")
max_attmpts = 3
while attempts <= max_attmpts:
    Password = input("Enter the password")
    if Password == reset_password:
        print("entered the correct password")
        break
    else:
        print("entered the wrong password")
        if max_attmpts - attempts != 0:
            print(f"max retries left {max_attmpts - attempts}")
    if (max_attmpts - attempts ) != 0:
        attempts = attempts + 1
        continue
    print("you have reached the max attempts")
    print("reset your password")
    reset_password = input("enter the new password")
    print(f"Congrats the new password is {reset_password}")
    attempts = attempts -max_attmpts


test.py


import json

# Example metadata dictionary
metadict = {
    'etl_stp_parms':
        '{"cfxinpath": "/data/claims/2025/"}'
}

data = json.loads(metadict.get('etl_stp_parms')).get('cfxinpath')
print(data)
# Extracting the claims file path
cfxInpath = json.loads(metadict.get('etl_stp_parms')).get('cfxinpath', 'na')

print(cfxInpath)


ARGS = { 'metadata_dict': '{"file1": "/data/files/file1.txt", "file2": "/data/files/file2.txt"}'
}
data1 = json.loads(ARGS.get('metadata_dict')).get('file1')
print(data1)


metadict = json.loads(ARGS['metadata_dict'])
print(metadict)

detail  = {
    'data': '{"name":"raju","age":34}'
}

output=json.loads(detail.get('data')).get('name')
print(output)