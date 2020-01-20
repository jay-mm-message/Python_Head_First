
def search_vowels(word):
    """ Return a boolean based on any vowels founds. """
    vowels = set('aeiou')
    print('vowels: ', vowels)
    found = vowels.intersection(set(word))

    return bool(found)

word = input('Provide a word to search for vowels: ')
print('Word exist vowels: ', search_vowels(word))
