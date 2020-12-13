from sys import stdin

l = int(stdin.readline())

arr = [None] * l

for x in range(l):
    arr[l-x-1] = stdin.readline().strip()

for x in arr:
    print(x)
