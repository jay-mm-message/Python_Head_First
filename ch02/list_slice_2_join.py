boot = 'The Hitchhiker\'s Guide to the Galaxy'
print('boot : ', boot)

list_boot = list(boot)
print('list_boot', list_boot)

print('list_boot[3:13:1]: ', list_boot[3:13:1])
print('list_boot[13:15:1]: ', list_boot[13:15:1])

print('list_boot[13:3:-1]: ', list_boot[13:3:-1])
print('list_boot[13:2:-1]: ', list_boot[13:2:-1])

print('list_boot[3]: ', list_boot[3])
print('list_boot[2]: ', list_boot[2])

word = ''.join(list_boot[13:3:-1])
print('\'\'.join(list_boot[13:3:-1]:', word)

