







with open("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\abc2.txt", "w") as f:
    f.write("Hello world \n")

with open('file11111111111.txt', 'wt') as f:
    f.write("Hello world \n")

#with open('file111111111113.txt', 'xt') as f:
#    f.write("Hello world \n")


with open('file11111111111.txt', 'rt') as f:
        for line in f:
            print(line, end='')

#to rename a file
import os

os.rename("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\abc2.txt"
          ,"C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\abc11235.txt")
print("file rename successsifule")

os.remove("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\abc11235.txt")
print("file removed successiful")
