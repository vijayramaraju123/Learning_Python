






# create and open a file

try:
    file_var = open("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\abc1.txt", 'w')
    print(file_var)

    file_var.write("this is test \n")
    file_var.write("this is connected")

    file_var.close()
except Exception as e:
    print(e)
