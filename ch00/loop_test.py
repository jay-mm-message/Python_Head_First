
from datetime import datetime
import time

odd = range(1, 60, 2)
print("odd list content: " + str(list(odd)))

for _ in range(5):

    time.sleep(1)

    right_this_minute = datetime.today().second
    print("Datetime.today().mintue: " + str(right_this_minute))

    if right_this_minute in odd:
        print("This minute seems a little odd.")
    else:
        print("Not minute an odd.")
