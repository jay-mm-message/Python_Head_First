
def search_vowels(word):
    """ Return any vowels found in a supplied word. """
    vowels = set('aeiou')
    print('Vowels: ', vowels)

    found = vowels.intersection(set(word))

    return found

word = input('Provide a word to search for vowels: ')
print('Word is exist vowels: ', search_vowels(word))
