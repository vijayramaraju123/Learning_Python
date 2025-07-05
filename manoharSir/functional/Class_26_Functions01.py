

# map with multiple lists

l1 = [1,2,3,4]
l2 = [4,5,6,7]

result = list(map(lambda x,y: x+y,l1,l2))
print(result)

nums = [-4,0,1,2,3,4,5,6,7,8]
res = list(filter(lambda x: x != 0, nums))
print(res)


#type 02
def add(x):
    return x != 0

fltr_result = list(filter(add,nums))
print(fltr_result)


positive = list(filter(lambda x: x>0, nums))
negative = list(filter(lambda x: x<0, nums))
print(positive)
print(negative)

import functools

res_rduce =(functools.reduce(lambda x,y:x+y,nums))
print(res_rduce)


lstlst = [2,4,5,6,8]
rslts = functools.reduce(lambda x,y: x+y,lstlst,10)
print(rslts)

# zip function
fruts = ["apple","mango","oragne"]
rates = [23,54,34]
for f,p in zip(fruts,rates):
    print(f,p)

# example2
frns_lst = list(zip(fruts,rates))
print(frns_lst)

# example3
frns_lst_dict = dict(zip(fruts,rates))
print(frns_lst_dict)

#xample4
frut_list = {}
for f,p in zip(fruts,rates):
    frut_list[f]=p
print(frut_list)


#unzip
unizp = [('apple', 23), ('mango', 54), ('oragne', 34)]
nms,vlues = zip(*unizp)
print(list(nms),list(vlues))

#Recursive FUnction
def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact*i
    return fact

print(factorial(4))


#non recursion function
def factorial1(n):
    if (n==1):
        return 1
    fact1 = n*factorial(n-1)
    return fact1

print(factorial1(4))
