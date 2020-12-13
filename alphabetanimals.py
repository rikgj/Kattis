from sys import stdin

lastletter = stdin.readline().strip()[-1]
numOfAnimals = int(stdin.readline())

animals = [None] * numOfAnimals
animals = [x.strip() for x in stdin.readlines()]
lettercomb = []
# st = 'abcdefghijklmnopqrstuvwxyz'
# animals_fl =  {x: 0 for x in st}
animals_fl = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

for a in animals:
    animals_fl[a[0]]+=1

def chooseCan():
    candidate = '?'
    for animal in animals:
        # a candidate with new potential
        if animal[0] == lastletter and animal[-1] not in lettercomb:
            # add last letter to checked
            last = animal[-1]
            lettercomb.append(last)

            # check if best candidate
            if animals_fl[last] == animal[0].count(last):
                return (animal + '!')
            elif candidate == '?':
                candidate = animal
    return candidate

print(chooseCan())
