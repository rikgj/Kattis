_ = input()
# ignore cases that are not -1
cases = [int(x) for x in input().split(' ') if x[0]!='-']
mysum = sum(cases)/len(cases)
print(mysum)
