import sys

input = sys.stdin.readline

n, m = map(int, input().split())

INF = sys.maxsize

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for w in range(1, n+1):  # k 회사를 거쳐서 가는 최단경로는 여기서 안셈 -> 마지막에 1~k로 가는 최단거리 + k~x로가 는 최단거리 더함 
    for a in range(1, n+1):   
        for b in range(1, n+1):
            if w == k or w == x: 
                continue
            graph[a][b] = min(graph[a][b], graph[a][w]+graph[w][b])

oneTOk = graph[1][k]   # 1~x~k로 가는 것도 세지면..?
kTOx = graph[k][x]

if oneTOk != INF and kTOx != INF:
    print(oneTOk + kTOx)
else:
    print(-1)