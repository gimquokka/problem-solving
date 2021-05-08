import heapq

INF = int(1e9)

def dijkstra(graph):
    length = len(graph)
    distance = [[INF]*length for _ in range(length)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    while q:
        dist, x, y = heapq.heappop(q)
        
        if  distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= length-1 and 0 <= ny <= length-1:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    return distance[length-1][length-1]

answer = []
for t in range(int(input())):
    n = int(input())
    
    a = [[INF]*n for _ in range(n)]
    
    for i in range(n):
        a[i] = list(map(int, input().split()))
    
    answer.append(dijkstra(a))

for i in answer:
    print(i)
    
    