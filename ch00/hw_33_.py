
from datetime import datetime

import random
import time

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

# for 迴圈迭代 5 次, 每一次 sleep 隨機的時間
for num in range(5):

    right_this_minute = datetime.today().minute
    print("right_this_minute: ", right_this_minute)

    if right_this_minute in odds:
        print('This minute seems a little odd.')
    else:
        print('Not an odd minute')

    wait_time = random.randint(1, 5)

    print("wait_time: ", wait_time)
    time.sleep(wait_time)
