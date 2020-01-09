
list_a = [ 1, 2, 3, 4, 5 ]
list_b = list_a.copy()

print('list_a: ', list_a, ', type(list_a): ', type(list_a))
print('list_b: ', list_b, ', type(list_b): ', type(list_b))

list_b.append(6)
print('list_b.append(6): ', list_b)

list_b.extend([7, 8, 9])
print('list_b.extend([7, 8, 9]): ', list_b)

print('list_a: ', list_a)

