

vowels = set('aeiou')
print('vowels: ', vowels)

word = 'hello'
print('word: ', word)

u = vowels.difference(set(word))
print('u ( difference(vowels, word)): ', u)
