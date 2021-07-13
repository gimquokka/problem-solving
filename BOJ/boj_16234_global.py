'''
1. bfs로 조건에 맞는 셀 추가
2. vistied로 방문한셀 카운트
3. 평균값으로 업데이트
'''
from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, visited, x, y):
    global movement, l, r
    n = len(graph)
    
    q = deque([])
    
    q.append((x, y))
    store = [(x, y)]
    _sum = graph[x][y]
    visited[x][y] = True
    
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    store.append((nx, ny))
                    _sum += graph[nx][ny]
                    movement = True
    
    avg = int(_sum/len(store))
    if movement:
        for x, y in store:
            graph[x][y] = avg
    else:
        return 0;


n, l, r = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

ans = 0
while True:
    movement = False
    
    visited = [[False]*n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
           if not visited[x][y]:
               bfs(graph, visited, x, y)
    
    if not movement:
        break
    ans += 1
    
print(ans)
 
        
    
    
    
