
""" define function of searchVowels """
def searchVowels():
    vowels = set('aeiou')
    word = input('Provide a word to search for vowels: ')
    found = vowels.intersection(set(word))

    for letter in found:
        print('letter: ', letter)


#called search searchVowels function
searchVowels()
