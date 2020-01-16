vowels = ['a', 'e', 'i', 'o', 'u']
print('vowels:', vowels)

word = input('Provide a word to search for vowels: ')
print('word:', word)

#found = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

# 建立一個空的 dictionary
found = {}
# 裝入五個建值 'a', 'e', 'i', 'o', 'u'
# found['a'] = 0
# found['e'] = 0
# found['i'] = 0
# found['o'] = 0
# found['u'] = 0

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for key, value in found.items():
    print('The key: ', key, 'was found', value, 'time(s).')
