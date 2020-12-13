from sys import stdin

x,y,n = [int(x) for x in stdin.readline().split(' ')]

for case in range(1,n+1):
    # improve by using the known proerties such as x%y or y%x
    xcase = case%x == 0
    ycase = case%y == 0
    if xcase and ycase:
        print('FizzBuzz')
    elif xcase:
        print('Fizz')
    elif ycase:
        print('Buzz')
    else:
        print(case)
