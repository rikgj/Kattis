from sys import stdin

safe,evs = [int(x) for x in stdin.readline().split(' ')]

onT = 0
reject = 0
for e in range(evs):
    line = stdin.readline().split(' ')

    pers = int(line[1])
    if line[0] == 'enter':
        nonT = onT + pers
        if nonT <= safe:
            onT = nonT
        else:
            reject+=1
    else:#leave
        onT-= pers

print(reject)
