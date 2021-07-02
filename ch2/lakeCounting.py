def hoge(y, x):
    lake[y][x] = '.'

    for ty in range(y-1, y+2):
        for tx in range(x-1, x+2):

            if -1 < ty < N and -1 < tx < M and lake[ty][tx] == 'W':
                hoge(ty,tx)

global N
global M
N = 10
M = 12

#lakeの初期化
global lake
lake = list([list('W........WW.'),
             list('.WWW.....WWW'),
             list('....WW...WW.'),
             list('.........WW.'),
             list('.........W..'),
             list('..W......W..'),
             list('.W.W.....WW.'),
             list('W.W.W.....W.'),
             list('.W.W......W.'),
             list('..W.......W.')])


ct = 0
for i in range(N):
    for j in range(M):
        if lake[i][j] == 'W':
            ct += 1
            hoge(i,j)

print(ct)