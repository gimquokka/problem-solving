import sys
import heapq
input = sys.stdin.readline

n, m, c = map(int, input().split())

INF = sys.maxsize

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [INF]*(n+1)


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

time = 0
count = 0

for d in distance:
    if d not in [INF, 0]: # c~i로 도달할 수 있음, c는 제외
        count += 1
        time = max(time, d)

print(count, time)
