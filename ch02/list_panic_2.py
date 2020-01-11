# topic: on tap

phrase = "Don\'t panic!"
plist = list(phrase)
print('phrase: ', phrase)
print('plist: ', plist)

# list ( slice ) 因為可以個別一筆一筆讀取所以不會破壞 plise 的結構
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

# list ( pop, remove, extend, insert.) 操作在 plist.extend([plist.pop(), plist.pop()]) 會破壞 plist 的結構
# for i in range(4):
#    plist.pop()

# plist.pop(0)
# plist.remove("'")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))
# new_phrase = ''.join(plist)

print('plist: ', plist)
print('new_phrase: ', new_phrase)

