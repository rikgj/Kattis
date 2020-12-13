word = input()
out = ''
prev = ''
for x in word:
    if x != prev:
        out+=x
    prev = x
print(out)
