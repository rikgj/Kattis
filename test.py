#
# 0 0 10000
# 0 10000 0
# 10000 0 0
# 3000 4000 3000
#
# def gcd(x, y):
#     while(y):
#         x, y = y, x % y
#     return x
#
# g1 = gcd(0,gcd(0,10000))
# g2 = gcd(0,gcd(10000,0))
# g3 = gcd(10000,gcd(0,0))
# p = gcd(g1,gcd(g2,g3))
# print(p)
# s = gcd(p,3000)
# f = p/s
# print(f)

A = [12, 24, 27, 30, 36]

A = [
5215, 785, 4000,
0, 10000, 0,
3000, 4000, 3000,
2000, 6000, 2000
]

def Greatest_Common_Divisor(A):
    for c in A:
        while int(c) > 0:
            if int(c) > 12:
                c = int(c) % 12
            else:
                return 12 % int(c)
print(Greatest_Common_Divisor(A))
