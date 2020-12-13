from sys import stdin

n = int(stdin.readline())

for x in range(n):
    r,e,c = [int(x) for x in stdin.readline().split(' ')]
    e-=c

    if r > e:
        print('do not advertise')
    elif r < e:
        print('advertise')
    else:
        print('does not matter')
