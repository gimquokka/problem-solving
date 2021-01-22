import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
	x, y, z = map(int, input().split())
	graph[x].append((y, z))
	

def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q:
		dist, now = heapq.heappop(q)
		if dist > distance[now]:
			continue
		for v, e in graph[now]:
			cost = dist + e
			if cost < distance[v]:
				distance[v] = cost
				heapq.heappush(q, (cost, v))

dijkstra(start)

count_city = 0
max_time = 0

for d in distance:
	if d != INF:
		count_city += 1
		# 이렇게 간결하게 짤 수 있음!
		max_time = max(max_time, d) 

'''
for i in range(n+1):
	if (distance[i] < INF):
		num_city += 1
	if (max_time < distance[i] < INF):
		max_time = distance[i]
'''
print(count_city-1, max_time)
	
	



