
import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)
n, p, k = map(int, input().split())

edges = []

for _ in range(p):
    edges.append(tuple(list(map(int, input().split()))))

# 비용이 0이 나오는 경우도 고려 즉, 최단 경로를 이루는 edges 수가 k 이하인 경우
edges.append((-1, -1, 0))

# edge weight에 대한 오름차순 정렬
edges.sort(key = lambda x: x[2])
length = len(edges)


def getGraph(mid):
    graph = [[] for _ in range(n+1)]
    for i in range(1, length):
        a, b, cost = edges[i]
        # 지불해야 하는 값 이하인 선
        if i <= mid:
            graph[a].append((b, 0))
            graph[b].append((a, 0))
        # 지불해야 하는 값 초과, 즉 공짜로 얻게되는 선
        else:
            graph[a].append((b, 1))
            graph[b].append((a, 1))
    return graph

def dijkstra(start, graph):
    q = []
    distances = [INF]*(n+1)
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        for adj, w in graph[now]:
            cost = dist + w
            if cost < distances[adj]:
                heapq.heappush(q, (cost, adj))
                distances[adj] = cost
    # 1부터 n까지 최단 경로
    # 실제 graph에서의 최단 경로에 포함된 
    # mid값보다 큰 weight를 가진 edges 수
    return distances[n]

# index
start = 0
end = length - 1

# n 번째 컴퓨터에 도달할 수 없는 경우로 초기화
result = -1

# binary search with parametric search
while start <= end:
    # 지불해야 하는 값
    mid = (start + end) // 2
    graph = getGraph(mid)
   
   
    numOfFreeLines = dijkstra(1, graph)
 
   
    # mid 적절한 값 
    if numOfFreeLines <= k:
        result = edges[mid][2]
        end = mid - 1
    else:
        start = mid + 1

print(result)

# 모든 선들을 공짜로 얻는 경우 존재할 수 있음

