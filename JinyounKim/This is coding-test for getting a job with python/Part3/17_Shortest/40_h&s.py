import sys 
import heapq

from bisect import bisect_left, bisect_right


input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph):
    length = len(graph)
    q = []
    distance = [INF]*(length)
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for node, line_cost in graph[now]:
            cost = dist + line_cost
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
    
    return distance


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = dijkstra(graph)

max_distance = 0
"""
for i in distance:
    if i != INF:
        max_distance = max(max_distance, i)
"""

max_distance = max(distance[1:])
node_num = bisect_left(distance, max_distance)
num_of_same = bisect_right(distance, max_distance) - bisect_left(distance, max_distance)

print(node_num, max_distance, num_of_same)
# print(distance)
