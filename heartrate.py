from sys import stdin

for x in range(int(stdin.readline())):
    b,p = [float(x) for x in stdin.readline().split(' ')]
    bpm = b*60/p
    diff = 60/p
    print('{:0.4f} {:0.4f} {:0.4f}'.format(round(bpm-diff,4),round(bpm,4),round(bpm+diff,4)))
