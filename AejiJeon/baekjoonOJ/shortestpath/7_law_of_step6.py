

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)

# 모든 vertex 쌍의 v1 -> v2 최단경로 담는 array 
distance = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0

# append edges
for _ in range(m):
    a, b = map(int,input().split())
    distance[a][b] = 1
    distance[b][a] = 1

# apply floyd warshall algorithm
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])


min_val = INF
result = 0
for i in range(1, n+1):
    bacon = 0
    # 모든 vertices에 대해서
    # i -> vertex 최단거리 합 구하기 
    for j in range(1, n+1):
        bacon += distance[i][j]
    # bacon 최솟값 구하기
    if min_val > bacon:
        result = i
        min_val = bacon

print(result)