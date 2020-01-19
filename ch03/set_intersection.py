vowels = set('aeiou')
print('vowels: ', vowels)

word = 'hello'
print('word: ', word)

u = vowels.intersection(set(word))
print('u ( intersection( vowels, word ): ', u)
