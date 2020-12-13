from sys import stdin
from math import pow
lines = int(stdin.readline())
sum = 0
for x in range(lines):
    num = stdin.readline().strip()
    num, p = int(num[:-1]), int(num[-1])
    sum+= pow(num,p)

print('{:.0f}'.format(sum))
