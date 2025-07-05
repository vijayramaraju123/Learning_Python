



import csv

with open('C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\audit_columns_info.csv','r') as csvfile:
    empData=csv.reader(csvfile)
    print(empData)

    for row in empData:
        print(row)



with open('C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\audit_columns_info.csv','w') as csvfile:
    write_obj=csv.writer(csvfile)
    write_obj.writerow(('lata',24,48))
    write_obj.writerow(('rave',24,48))
print("write successiful")

with open('C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\audit_columns_info.csv','w') as csvfile:
    write_obj=csv.writer(csvfile)
    persons = [('lata',24,48),('rave',24,48)]
    for data in persons:
        write_obj.writerow(data)

