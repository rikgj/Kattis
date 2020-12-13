from sys import stdin
greet = 'h'
for e in range(len(stdin.readline().strip()[1:-1])*2):
    greet+='e'
print(greet+'y')
