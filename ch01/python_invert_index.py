
saying="Don't panic"
letters=list(saying)

for i in range(len(saying)):
    print(letters[i])

print('invert')

invert_letters=list(saying)
len_num = -1
for i in range(len(saying)):
    len_num = (-1 * i) + -1
    print(invert_letters[len_num])


