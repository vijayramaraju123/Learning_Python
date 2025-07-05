



# create and open a file

try:
    file_var = open("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\abc1.txt", 'r')
    data = file_var.read()
    print(data)
    print(type(data))

    # Splitting the data
    data1 = data.split("\n")
    print(data1)
    print(data1[0])

    for data in data1:
        print(data.rstrip())

    #to read first 10 characters of line
    file_var.seek(0)
    data3 = file_var.read(10)
    print(data3)

    #read one complete line
    file_var.seek(0)
    data4 = file_var.readline()
    print(data4)

    #to read lines as list of lines
    file_var.seek(0)
    data5 = file_var.readlines()
    print(data5)


    file_var.close()
except Exception as e:
    print(e)

