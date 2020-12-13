cases,dominant = [x for x in input().split(' ')]
cases = int(cases)*4

lookup = {
'A':[11,11],
'K':[4,4],
'Q':[3,3],
'J':[20,2],
'T':[10,10],
'9':[14,0],
'8':[0,0],
'7':[0,0]
}
sum = 0
for c in range(cases):
    i=1
    card = input()
    if card[1] == dominant:
        i=0
    sum+= lookup[card[0]][i]
print(sum)
