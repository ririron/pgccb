import math

def func(tar, a):
    for i, l in enumerate(a):
        expe = int(math.sqrt(tar**2 - l**2))
        b = a[i+1:]
        if expe in b:
            return tar + l + b[b.index(expe)]
    
    return 0

n = 4
a = [4, 5, 10, 20]

#昇順にソート
a.sort(reverse=True)
#上から見ていく
for i,tar in enumerate(a):
    res = func(tar, a[i+1:])
    if  res != 0:
        break

print(res)