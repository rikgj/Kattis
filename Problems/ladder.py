# the side we want x = height/sin(degrees)
from math import sin, ceil, radians
h,v = [int(x) for x in input().split(' ')]
print(ceil(h/sin(radians(v))))
