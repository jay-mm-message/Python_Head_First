
topic = 'Provide a word to search for vowels: '

vowels = [ 'a', 'e', 'i', 'o', 'u' ]

word = input(topic)

found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print('vowels len: ', len(found), ', vowels content is: ', found)

print()
