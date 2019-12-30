
from datetime import datetime

odd = range(1, 60, 2)
print(list(odd))

right_this_minute = datetime.today().minute

print(right_this_minute)
if right_this_minute in odd:
    print('This minute seems a little odd.')
else:
    print('Not an odd minute')
