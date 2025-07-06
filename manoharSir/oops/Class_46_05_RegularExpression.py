

# to find the maximum number of occurences

import re

s = "greeks for geeks geer geet the boot boor geem booat aap bool aab aaat boot1 boomb"

regex1 = r'gee'
regex2 = r'boo'
regex3 = r'aa'

matche1 = re.findall(regex1,s)
matche2 = re.findall(regex2,s)
matche3 = re.findall(regex3,s)

print(matche1)
print(matche2)
print(matche3)

l1 = len(matche1)
l2 = len(matche2)
l3 = len(matche3)

if(l1>l2 and l1>l2):
    print("gee is having hight",l1)
elif(l2>l3):
    print("boo is having hight",l2)
else:
    print("as is having highest prefix")



result = re.match(r'Hello','Hello world')
print(result.group() if result else 'No Match')


result1 = re.search(r'workd','Hello world Hello')
print(result1.group() if result1 else 'No Match')

result2 = re.findall(r'\d+','there are 12 apples and 24 bananas')
print(result2)


for match in  re.finditer(r'\d+','12 there are 12 apples and 24 bananas'):
    print(match.group())

result4 = re.sub(r'apples','bananas','there are 12 apples and 24 bananas')
print(result4)

result5= re.split(r'\s+','Hello World! This is python.')
print(result5)

txxxt = "my email is example@test.com and phone is 123-234-32456."
email = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',txxxt)
print(email.group())

phone = re.search(r'\d{3}-\d{3}-\d{5}',txxxt)
print(phone.group())
