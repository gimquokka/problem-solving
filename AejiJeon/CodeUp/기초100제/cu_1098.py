# put sticks (specified with 1 ) on n*n grid board
# 2 0 1 1 means stick starts at (1, 1) and length is 2 with row direction

n, m = map(int, input().split())

a = int(input())

b = [[0]*m for _ in range(n)]
for _ in range(a):
    l, d, x, y = map(int, input().split())
    for i in range(l):
        if d == 0: b[x-1][y-1+i] = 1
        else: b[x-1+i][y-1] = 1

for i in range(n):
    print(*b[i])