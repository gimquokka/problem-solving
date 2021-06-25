import heapq

def solution(n, edge):
    INF = int(1e9)
    
    graph = [[] for _ in range(n+1)]
    distance = [INF]*(n+1)
    
    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    dijkstra(graph, distance, 1)

    distance.sort(reverse=True)
    '''
    # list method count로 대체 가능
    max_dist = distance[1]
    for dist in distance:
        if max_dist == dist:
            ans += 1
    '''
    print(distance)

    # return distance.count(distance[1])
    return distance.count(max(distance[1:]))


def dijkstra(graph, distance, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for v, d in graph[now]:
            cost = dist + d

            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

    return


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))