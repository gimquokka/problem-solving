import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = int(1e9)
distance = [INF]*(n+1)

start = 1
def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q: # 되도록이면 
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for adj in graph[now]:
            cost = 1 + dist
            if cost < distance[adj]:
                distance[adj] = cost
                heapq.heappush(q, (cost, adj))

dijkstra(1)
distance[0] = 0 # 중요!
max_d = max(distance)
count = 0
target = 0
for i in range(1, n+1):
    if distance[i] == max_d:
        if count == 0:
            target = i
        count += 1
print(target, max_d, count)
        



