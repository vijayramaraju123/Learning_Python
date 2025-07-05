
















import csv

with open("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\audit_columns_info.csv", 'w',newline='') as csvfile1:
    header = ['name', 'age', "location"]
    dict_writer = csv.DictWriter(csvfile1, fieldnames=header,delimiter = ',')
    dict_writer.writeheader()
    dict_writer.writerow({"name": "Jonhn", "age": 40, "location": 400})
    print("write successiful")

