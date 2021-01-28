import heapq
import sys
input = sys.stdin.readline  # 항상 적고 시작! 습관 들이기
t = int(input())

INF = int(1e9)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    distance = [[INF]*n for _ in range(n)]
    a, b = 0, 0
    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (distance[0][0], a, b)) 
    while q:
        dist, x, y = heapq.heappop(q)

        if dist > distance[x][y]: # 등호 들어가면 start에서 continue 되어 종료됨(개선된 다익스트라에서도 등호 안 들어감)
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                cost = distance[x][y] + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])


