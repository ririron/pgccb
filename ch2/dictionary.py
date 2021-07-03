N = 6
S = list("ACDBCB")
rS = list(reversed(S))

res = ""
for i in range(N):

    if S[0] < rS[0]:
        res += S.pop(0)
    else :
        res += rS.pop(0)

print(res)