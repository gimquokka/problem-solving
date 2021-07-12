import sys

input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
s, ax, ay = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

q = []

for x in range(n):
    for y in range(n):
        if graph[x][y] != 0:
            q.append((graph[x][y], x, y, 0))

q.sort()
while q:
    val, x, y, dist = q.pop(0)
    
    if dist+1 > s:
        break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                q.append((graph[nx][ny], nx, ny, dist+1))
            
print(graph[ax-1][ay-1])

