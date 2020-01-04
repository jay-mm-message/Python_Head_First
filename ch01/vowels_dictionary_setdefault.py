
topic = 'Provide a word to search for vowels: '

vowels = [ 'a', 'e', 'i', 'o', 'u' ]

word = input(topic)

found = {}
#found['a'] = 0
#found['e'] = 0
#found['i'] = 0
#found['o'] = 0
#found['u'] = 0

print('\n', 'Before search for vowels: ')
for key, value in sorted(found.items()):
    print('\t', key, 'was found', value, 'time(s).')

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

print('\n', 'After search for vowels: ')
for key, value in sorted(found.items()):
    print('\t', key, 'was found', value, 'time(s).')

print()
