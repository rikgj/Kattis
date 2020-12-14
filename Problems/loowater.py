'''
 “To slay the dragon, we must chop off all its heads.
 Each knight can chop off one of the dragon’s heads.
 The heads of the dragon are of different sizes.
 In order to chop off a head, a knight must be at least as tall as the diameter of the head.
 The knights’ union demands that for chopping off a head,
 a knight must be paid a wage equal to
 one gold coin for each centimetre of the knight’s height.
'''

while True:
    heads,knights = [int(x) for x in input().split(' ')]
    if heads+knights == 0: # check if we are done
        break
    elif knights >= heads:
        # get sorted lists for heads and heights
        headDiam = [int(input()) for _ in range(heads)]
        headDiam.sort()
        knightHeight = [int(input()) for _ in range(knights)]
        knightHeight.sort()
        gold = 0
        i = 0

        for height in knightHeight:
            knights-=1 # remove a knight from the fight
            if height >= headDiam[i]:
                # chop off the head
                i+=1
                # pay the knight for his height
                gold+=height
                heads-=1
            # check if we are done fighting
            if heads > knights:
                print('Loowater is doomed!')
                break
            elif heads == 0:
                print(gold)
                break
    else:
        # skip the data
        for x in range(heads+knights):
            input()
        print('Loowater is doomed!')
