

import os


#to see the current pat
cwd = os.getcwd()
print(f"the current working directory is {cwd}")

#to change the path
os.chdir("C:\\Users\\AL02673\\PycharmProjects\\pythonProject3\\prabhakarSir\\Functional")
print(f"the current working directory is {os.getcwd()}")

#to create new directory
#os.mkdir("Func_dir1")

#to create nested directories
#os.makedirs("Functional\\funct\\dst")

#to remove directory
#os.rmdir("new_directory")

#to remove nested directories
#os.removedirs(("Functional\\funct\\dst"))



#to list files and directories
items=os.listdir(".")
print(items)

path1=os.listdir("C:\\Users\\AL02673\\PycharmProjects\\pythonProject3\\prabhakarSir")
print(path1)


path = "C:\\Users\\AL02673\\PycharmProjects\\pythonProject3\\prabhakarSir"

for i in path:
    if(i.startswith('Pandas') and os.path.exists(path+i)):
        #os.remove(path)
        print(os.getcwd())


file1 = 'abc123.txt'
if(os.path.exists(path+file1)):
    os.remove(path+file1)
else:
    print("file doesnot exists")
