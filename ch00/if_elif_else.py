

from datetime import datetime

odd = range(1, 60, 1)
print(list(odd))

odd_a = []
odd_b = []
odd_c = []
odd_d = []
odd_e = []
odd_f = []
odd_g = []

print()

for num in odd:
    if num >= 1 and num < 5:
        odd_a.append(num)
        #print("num >= 1 and num < 5: " + "(" + str(num) + ")")
    elif num >= 5 and num < 10:
        odd_b.append(num)
        #print("num >= 5 and num < 10: " + "(" + str(num) + ")")
    elif num >= 10 and num < 20:
        odd_c.append(num)
        #print("num >= 10 and num < 20: " + "(" + str(num) + ")")
    elif num >= 20 and num < 30:
        odd_d.append(num)
    elif num >= 30 and num < 40:
        odd_e.append(num)
        #print("num >= 30  and num < 40: " + "(" + str(num) + ")")
    elif num >= 40 and num < 50:
        odd_f.append(num)
        #print("num >= 40  and num < 50: " + "(" + str(num) + ")")
    else:
        odd_g.append(num)
        #print("num >= 50: " + "(" + str(num) + ")")

for num in odd_a:
    print("num >= 1 and num < 5: " + "(" + str(num) + ")")
print()

for num in odd_b:
    print("num >= 5 and num < 10: " + "(" + str(num) + ")")
print()

for num in odd_c:
    print("num >= 10 and num < 20: " + "(" + str(num) + ")")
print()

for num in odd_d:
    print("num >= 20 and num < 30: " + "(" + str(num) + ")")
print()

for num in odd_e:
    print("num >= 30 and num < 40: " + "(" + str(num) + ")")
print()

for num in odd_f:
    print("num >= 40 and num < 50: " + "(" + str(num) + ")")
print()

for num in odd_g:
    print("num >= 50: " + "(" + str(num) + ")")
print()

