from sys import stdin
p = int(stdin.readline())
sum = 0
for x in range(p):
    sr = [float(x) for x in stdin.readline().split(' ')]
    sum+=(sr[0]*sr[1])

print('{:2.3f}'.format(round(sum,3)))
