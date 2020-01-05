from datetime import datetime

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]


# 當 Today 函式被呼叫, 會回傳一個時間物件, 這時間物件包含很多屬性, 在python可以透過 '.' 點號 ( dot-notation ) 取得
# 特定需要的屬性 ( attribute )
right_this_minue = datetime.today().minute

print(right_this_minue)

