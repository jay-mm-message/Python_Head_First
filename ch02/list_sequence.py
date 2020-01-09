

word = 'Don\'t panic!'
list_word = list(word)
print('word: ', word)

seq_list = []
for i in range(len(list_word)):
    seq_list.append(list_word[i])
print('       sequence print: ', seq_list)

revert_seq_list = []
for i in range(-1, -len(list_word)-1, -1):
    revert_seq_list.append(list_word[i])
print('revert sequence print: ', revert_seq_list)

