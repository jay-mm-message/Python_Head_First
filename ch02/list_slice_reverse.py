
word = '12345'
print('word : ', word)

list_word = list(word)
print('list_word : ', list_word)

reverse_list_word = list_word[::-1]
print('reverse_list_word : ', reverse_list_word)

reverse_list_word_2 = list_word[-1:-len(list_word)-1:-1]
print('reverse_list_word_2 : ', reverse_list_word_2)

reverse_word = ''.join(reverse_list_word)
print('reverse_word : ', reverse_word)
