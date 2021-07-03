#仕事の数
from typing import Mapping


n = 5
#開始時刻
s = [1, 2, 4, 6, 8]
#終了時刻
t = [3, 5, 7, 9, 10]
#現在時間
ct = 0

jNum = 0
while s != []:

    tarIdx = t.index(min(t))
    if s[tarIdx] > ct:
        ct = t[tarIdx]
        jNum += 1
    
    s.pop(tarIdx)
    t.pop(tarIdx)

print(jNum)

     
