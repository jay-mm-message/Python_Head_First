vowels = set('aeiou')
print('vowels: ', vowels)

word = 'hello'
print('word: ', word)

u = vowels.union(set(word))
print('union(vowel + word): ', u)
