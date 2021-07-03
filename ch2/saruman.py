N = 6
R = 10
X = [1, 7, 15, 20, 30, 50]

#注目する点
ct = 0
#
i  = 0

tmpX = X
while 1:

    tmpX = [x for x in tmpX if x > X[ct] + R]
    if len(tmpX) == 0:
        break
    ct = X.index(tmpX[0])
    i += 1

print(i)