alphabet ={
'A':'@',
'B':'8',
'C':'(',
'D':'|)',
'E':'3',
'F':'#',
'G':'6',
'H':'[-]',
'I':'|',
'J':'_|',
'K':'|<',
'L':'1',
'M':'[]\/[]',
'N':'[]\[]',
'O':'0',
'P':'|D',
'Q':'(,)',
'R':'|Z',
'S':'$',
'T':"']['",
'U':'|_|',
'V':'\/',
'W':'\/\/',
'X':'}{',
'Y':'`/',
'Z':'2'
}
# translate input string with custom alphabet
out = ''
for l in input():
    l = l.upper()
    if l in alphabet:
        out+=alphabet[l]
    else:
        out+=l
print(out)
