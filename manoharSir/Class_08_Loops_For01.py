



for value in range(1,10,1):
    print(value)

for value in range(10,0,-1):
    print(value)


i = 1
while(i<=3):
    j=1
    while(j<=8):
        print("*", end='')
        j = j+1
    print()
    i=i+1

for i in range(1,5):
    for j in range(i):
        print("*",end = '')
    print()
