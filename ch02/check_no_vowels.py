vowels = [ 'a', 'e', 'i', 'o', 'u' ]

word = 'Milliways'
print(word)

vowels_exist_in_word = []

for letter in word:
    if letter in vowels:
        if letter not in vowels_exist_in_word:
            vowels_exist_in_word.append(letter)


if len(vowels_exist_in_word) != 0:
    print(vowels_exist_in_word)

