

from datetime import datetime
import time

odd = range(1, 60, 2)
print(list(odd))

right_this_minute = datetime.today().minute

for num in range(5):
    time.sleep(5)
    print(right_this_minute)
    if right_this_minute in odd:
        print('This minute seems a little odd.')
    else:
        print('Not an odd minute')
