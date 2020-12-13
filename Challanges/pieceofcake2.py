from sys import stdin

n,h,v = [int(x) for x in stdin.readline().split(' ')]
nv = n-v
nh = n-h
sqrs = [h*v, h*nv,v*nh,nv*nh]
print(4*max(sqrs))
