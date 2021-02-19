import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result_val = INF
for i in range(1, n+1):
    if sum(graph[i][1:]) < result_val:
        result = i
        result_val = sum(graph[i][1:])

print(result)
