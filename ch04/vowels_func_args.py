
def search_vowels(word):
    """ Display any vowels found in a supplied word. """
    vowels = set('aeiou')
    found = vowels.intersection(set(word))

    for letter in found:
        print('letter: ', letter)


word = input('Provide a word to search for vowels: ')

# TypeError: search_vowels() takes 1 positional argument but 2 were given
# search_vowels(word, 'apple')

# TypeError: search_vowels() missing 1 required positional argument: 'word'
# search_vowels()

search_vowels(word)
