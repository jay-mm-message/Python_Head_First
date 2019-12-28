
from datetime import datetime

odds = range(1, 60, 2)
print("odds content: \n", list(odds))
print("odds.len: \n", len(odds))

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute seems a little odd.")
    print("假設你等待了必要的分鐘數.")
else:
    print("Not an add minute.")
