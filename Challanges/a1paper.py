'''
consider the required tape as a m-ary tree where the parents are tape joints
n is the number of the paper, An
height of paper = 2**((2*n-1)/4)
'''

_ = input() #ignore first line
paperlist = [int(x) for x in input().split(' ')]

tape = 2**-(3/4)
req = 2
n = 6
for paper in paperlist:
    req-= paper
    if req <= 0:
        # we are done
        print(tape)
        exit()
    # add more tape and update values
    tape+=2**-((n-1)/4)*req
    req*=2
    n+=2

print('impossible')
