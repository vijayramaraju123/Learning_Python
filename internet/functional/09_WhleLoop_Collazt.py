







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