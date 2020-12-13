from sys import stdin

limit = int(stdin.readline())

for i in range(limit):
    line = [int(x) for x in stdin.readline().split(' ')]
    students = line.pop(0)

    avg = sum(line)/students
    fil = list(filter(lambda x: x>avg, line))
    perc = round((len(fil)/students)*100,3)

    print('{:2.3f}%'.format(perc))
