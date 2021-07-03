cNum = [3,2,1,3,0,2]
coins = [1, 5, 10, 50, 100, 500]

resNum = [0, 0, 0, 0, 0, 0]
A = 620
cNum = cNum[::-1]
for i, c in enumerate(coins[::-1]):

    t = min(int(A / c), cNum[i])

    A -= c * t
    resNum[i] = t

print(resNum)