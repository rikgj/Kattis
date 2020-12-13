from sys import stdin

limit = int(stdin.readline())

for i in range(limit):
    line = [int(x) for x in stdin.readline().split(' ')]
    students = line.pop(0)

    avg = sum(line)/students
    fil = list(filter(lambda x: x>avg, line))
    perc = round((len(fil)/students)*100,3)

    print('{:2.3f}%'.format(perc))

# Runtime on site 0.6s

# input
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

# Expected output
# 40.000%
# 57.143%
# 33.333%
# 66.667%
# 55.556%
