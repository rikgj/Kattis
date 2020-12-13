# the starting position of the cups
cups = [1,0,0]

for swap in input():
    p1,p2,p3 = cups
    if swap == 'A':
        cups = [p2,p1,p3]
    elif swap == 'B':
        cups = [p1,p3,p2]
    else:#C
        cups = [p3,p2,p1]

# show location of 1
print(cups.index(1)+1)
