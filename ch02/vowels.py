
vowels = [ 'a', 'e', 'i', 'o', 'u' ]

word = 'Milliways'
print(word)

count = 0
for letter in word:
    if letter in vowels:
        print('word[', count, ']:', letter)
    count += 1
