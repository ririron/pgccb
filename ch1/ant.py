
L = 214
n = 7
x = [11, 12, 7, 13, 176, 23, 191]
"""
L = 10
n = 3
x = [2, 6, 7]
"""
def calcMin(x, L):
    minVal = x[0]
    for i in x:
        minVal = max(minVal, min(i, L-i))
    return minVal

def calcMax(x, L):
    maxVal = x[0]
    for i in x:
        maxVal = max(maxVal, max(i, L-i))
    return maxVal
    


print("min = {}".format(calcMin(x, L)))
print("max = {}".format(calcMax(x, L)))
