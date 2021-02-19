import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append((b, 1))
	graph[b].append((a, 1))
x, k = map(int, input().split())

distance = [INF]*(n+1)

def dijkstra(start):
	q = []
	# global distance
	distance[start] = 0
	heapq.heappush(q, (0, start))

	while q:
		dist, now = heapq.heappop(q)
		
		if distance[now] < dist:
			continue

		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(1)
start_k = distance[k]
# print(distance)

distance = [INF]*(n+1)
dijkstra(k)
# print(distance)
k_x = distance[x]

start_x = start_k + k_x

if INF <= start_x:
	print(-1)
else: print(start_x)
