from sys import stdin

limit = int(stdin.readline())

for x in range(limit):
    alim = int(stdin.readline())
    places = [stdin.readline() for x in range(alim)]
    print(len(set(places)))
