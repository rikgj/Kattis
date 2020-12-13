from sys import stdin
x,y = [int(''.join(list(reversed(x)))) for x in stdin.readline().strip().split(' ')]
if x > y:
    print(x)
else:
    print(y)
