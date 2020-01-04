string = "Don't panic!"
string_to_list = list(string)

print("string: ", string)
print("string to list: ", string_to_list)

list_to_string = ''.join(string_to_list)
print("list to string: ", list_to_string)

print("string: ", string)
print("string to list: ", string_to_list)

print("for i in range(4)")
for i in range(4):
    string_to_list.pop()
    print("string to list: ", string_to_list)

print("string_to_list.pop(0)")
string_to_list.pop(0)
print("string to list: ", string_to_list)

print("string_to_list.remove(')")
string_to_list.remove("'")
print("string to list: ", string_to_list)

print("string_to_list.extend([string_to_list.pop(), string_to_list.pop()])")
string_to_list.extend([string_to_list.pop(), string_to_list.pop()])
print("string to list: ", string_to_list)

print("string_to_list.insert(2, string_to_list.pop(3))")
string_to_list.insert(2, string_to_list.pop(3))
print("string to list: ", string_to_list)

print("list_to_string = ''.join(string_to_list)")
list_to_string = ''.join(string_to_list)
print("list to string: ", list_to_string)

