_ = input()
paperlist = [int(x) for x in input().split(' ')]
# n is the number of the paper, An
# height = 2**((2*n-1)/4)
tape = 2**-(3/4)
req = 2
n = 6
for paper in paperlist:
    req-= paper
    if req <= 0:
        # we are done
        print(tape)
        exit()
    # add more tape and update vals
    tape+=2**-((n-1)/4)*req
    req*=2
    n+=2

print('impossible')
