import sys 
input = sys.stdin.readline

INF =int(1e10)

n = int(input())
m = int(input())

cost = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    cost[i][i] = 0

for _ in range(m):
    x, y, c = map(int, input().split())
    cost[x][y] = min(cost[x][y], c) 

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cost[a][b] = min(cost[a][b], cost[a][k]+cost[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == INF:
            print(0, end = ' ')
        else:
            print(cost[i][j], end = ' ')
    print()

