
word = input()
out = ''
prev = ''
# remove same letters which are the same as the previous
for x in word:
    if x != prev:
        out+=x
    prev = x
print(out)
