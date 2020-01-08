list_a = [ 1, 2, 3 ]
print('list_a: ', list_a)
list_b = [ 4, 5, 6 ]
print('list_b: ', list_b)

print('list_a.extand(list_b)')
list_a.extend(list_b)
print('list_a:', list_a)
print('list_b:', list_b)

list_b.extend([7, 8, 9])
print('list_a:', list_a)
print('list_b:', list_b)
