

from datetime import datetime

import time
import random

odds = range(1, 60, 2)
print(str(list(odds)))

right_this_minute = datetime.today().minute
print("datetime.today().minute: " + str( right_this_minute ))

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")

wait_time = random.randint(1, 3)
print("wait ( " + str(wait_time) + " ). ")
time.sleep( wait_time )
