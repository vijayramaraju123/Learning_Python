










import csv

with open('C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\audit_columns_info.csv', 'r') as csvfile:
    empData = csv.DictReader(csvfile)
    print(empData)
    print(list(empData))

    for row in empData:
        print(row)
    