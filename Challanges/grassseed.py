from sys import stdin
cost = float(stdin.readline())
sum = 0
for lawn in range(int(stdin.readline())):
    w,h = [float(x) for x in stdin.readline().strip().split(' ')]
    sum+= w*h
sum = round(sum*cost,6)
print('{:0.6f}'.format(sum))
