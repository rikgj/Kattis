
winner = -1
points = -1
for x in range(5):
    val = sum([int(i) for i in input().split(' ')])
    if val > points:
        points = val
        winner = x+1

print(winner,points)
