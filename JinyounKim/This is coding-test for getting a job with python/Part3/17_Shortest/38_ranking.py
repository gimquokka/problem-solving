import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

cost = [[INF]*(n+1) for _ in range(n+1)]

for _  in range(m):
    a, b = map(int, input().split())
    cost[a][b] = 1

for i in range(1, n+1):
    cost[i][i] = 0

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            cost[x][y] = min(cost[x][y], cost[x][k]+cost[k][y])

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if cost[i][j] != INF or cost[j][i] != INF:
            count += 1
        else:
            break
    if count == n: 
        result += 1
            

print(result)
