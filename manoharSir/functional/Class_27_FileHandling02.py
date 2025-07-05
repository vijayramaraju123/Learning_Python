
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
        print(data)

    file_var.close()
except Exception as e:
    print(e)

