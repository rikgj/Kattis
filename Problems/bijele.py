fullSet = [1,1,2,2,2,8]
found = [int(x) for x in input().split(' ')]
# find the difference between the given set and a complete one
for i,x in enumerate(found):
    fullSet[i]-= found[i]

print(' '.join(map(str, fullSet)))
