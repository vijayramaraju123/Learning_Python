

listt= ['2025/reports/', '2025/reports/report1.csv', '2025/reports/report2.csv', '2025/reports/summary.txt']


inPath = '2025/reports/'

dataFiles = list(filter(lambda x: x != (inPath ), listt))
print(dataFiles)

add = lambda x:x+10
print(add(10))

sub = lambda x: x-2
print(sub(8))

mul = lambda x,y:x*y
print(mul(2,4))



points = [(1, 2), (3, 1), (5, -1)]
positive = list(filter(lambda x:x[1]>0,points))
print(positive)


