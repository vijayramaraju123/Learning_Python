










# APpend mode

try:
    f = open("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\abc1.txt", 'a')
    print(f)

    f.write("this is test \n")
    f.write("this is connected\n")
    print("write successifule1 \n")

    l2 = ["this is file \n", "the data given \n"]
    f.writelines(l2)
    print("write successifule2 \n")

    print("Hello how are you", file=f)
    print("write successifule3 \n")

    f.close()
except Exception as e:
    print(e)

