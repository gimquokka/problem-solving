import sys
input = sys.stdin.readline
import heapq

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)  

INF = 1e9
distance = [INF for _ in range(n+1)]

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0, start))

    while q:
        now = heapq.heappop(q)[1]

        for adj in graph[now]:

            if distance[adj] > distance[now] + 1:
                distance[adj] = distance[now] + 1
                heapq.heappush(q, (distance[adj], adj))

dijkstra(x)
count = 0
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        count += 1
if count == 0:
    print(-1)




