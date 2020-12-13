cases = int(input())

for case in range(cases):
    k,p = [int(x) for x in input().split(' ')]
    print(k,int(p+(p*(p+1))/2))
