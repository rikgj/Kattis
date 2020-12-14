# a somewhat messy solution to a simple problem
from collections import Counter

x = []
y = []
for _ in range(3):
    coor = [int(x) for x in input().split(' ')]
    x.append(coor[0])
    y.append(coor[1])

cx = Counter(x)
cy = Counter(y)
x = str([x for x in cx if cx[x] ==1]).strip('[]')
y = str([y for y in cy if cy[y] ==1]).strip('[]')
print(x,y)
