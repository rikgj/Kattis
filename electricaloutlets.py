from sys import stdin

cases = int(stdin.readline())

for case in range(cases):
    lits = 1
    outlets = [int(x) for x in stdin.readline().split(' ')]
    for outlet in outlets:
        lits+= outlet-1
    lits-=outlets[0]-1
    print(lits)
