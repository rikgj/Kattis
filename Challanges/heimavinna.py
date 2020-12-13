probs = input().split(';')
sum = 0
for p in probs:
    num = 1
    prob = [int(x) for x in p.split('-')]
    if len(prob) > 1:
        num = prob[1]-prob[0]+1

    sum+=num
print(sum)
