














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