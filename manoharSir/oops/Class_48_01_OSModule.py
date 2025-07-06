

import os

# rename file or directory

# os.rename("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\division.log",
#          "C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\division123.log")


# join paths
# path = os.path.join("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del",
#                    "C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents",'division123.log')
# print(path)

# getting file or directory name
print(os.path.basename("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\division.log"))
print(os.path.dirname("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\division.log"))

print(os.path.split("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\division.log"))

print(os.path.isfile("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\division.log"))
print(os.path.isdir("C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\division.log"))

print(os.path.abspath("division.log"))

# print(os.name("division.log"))


print("current process ID", os.getpid())
print("current process ID", os.getppid())

for file in os.listdir("."):
    if file.endswith(".py"):
        print("python file :", file)

for file in os.listdir("."):
    print("python file :", file)
