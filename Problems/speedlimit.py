rows = int(input())
while rows != -1:
    prevH = 0
    miles = 0
    for x in range(rows):
        mph,h = [int(x) for x in input().split(' ')]
        miles+=(h-prevH)*mph
        prevH = h
    print(str(miles) + " miles")
    rows = int(input())
