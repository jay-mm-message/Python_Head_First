vowels = ['a', 'e', 'i', 'o', 'u']
print('type(vowels): ', vowels)

vowels2 = ('a', 'e', 'i', 'o', 'u')
print('type(vowels2): ', vowels2)

vowels.extend(['ggg'])
print('vowels: ', vowels)

vowels2[2] = 'g'
print('vowels2: ', vowels2)
