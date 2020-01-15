vowels = ['a', 'e', 'i', 'o', 'u']
print('vowels: ', vowels)

word = input('Please put the word: ')
print('word: ', word)

found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1

for letter in found:
    print('key: ', letter, ', value: ', found[letter])
