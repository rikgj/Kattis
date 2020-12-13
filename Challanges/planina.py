from sys import stdin

n = int(stdin.readline())

print('%d'%((2**(n+1)-2**n + 1)**2))
