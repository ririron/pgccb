def dfTree(cSum, i, a, k):

    if i == len(a): return cSum == k

    if dfTree(cSum + a[i], i+1, a, k): return True

    if dfTree(cSum, i+1, a, k): return True

    return False


n = 4
#与えらえた数
a = [1, 2, 4, 7]
#対象の和の値
k = 15

print(dfTree(0, 0, a, k))

