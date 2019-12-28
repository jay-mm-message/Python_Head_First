

in_val = (int)(input("請輸入數字: "))

content_list = range(1, 10, 2)

print(list(content_list))
print(type(in_val))

if in_val in content_list:
    print(in_val , " in content list.")
else:
    print(in_val ," not in content list.")
