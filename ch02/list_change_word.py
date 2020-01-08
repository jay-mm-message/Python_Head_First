phrase= 'Don\'t panic!'
plist = list(phrase)
print(phrase)
print(plist)

for ch in range(4):
    plist.pop()

plist.remove('D')
plist.remove('\'')
plist.remove(' ')
plist.extend([plist.pop(), plist.pop()])

#plist.remove('D')
#plist.remove('\'')
#plist.remove(' ')
#plist.remove('i')
#plist.remove('c')
#plist.pop()
#plist.pop()
#plist.pop()
#plist.append('a')
#plist.append('p')"

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
