from sys import stdin

a,b = [int(x) for x in stdin.readline().split(' ')]
diff = abs(a-b) +1
a = min(a,b) +1

print(a)
for x in range(1,diff):
    print(a+x)
