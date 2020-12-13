for case in range(int(input())):
    _ = input() # we do not need case length
    arr = [int(x) for x in input().split(' ')]
    dist = (max(arr)-min(arr))*2
    print(dist)
