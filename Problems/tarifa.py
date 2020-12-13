# usage per month
perMonth = int(input())
# the number of months
months = int(input())
# determin next month based on usage
nextMonth = perMonth*(months+1) - sum([int(input()) for x in range(months)])
print(nextMonth)
