
topic = 'Test if the word contains vowels, please enter the word : '

vowels = [ 'a', 'e', 'i', 'o', 'u' ]

word = input(topic)

flag = False
for letter in word:
    if letter in vowels:
        flag = True
        break;

if flag == True:
    print('Yes')
else:
    print('No')

print()
