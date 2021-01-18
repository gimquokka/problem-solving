from collections import deque

queue = deque()
n, m = map(int, input().split())
graph = []

dx = [0,1,0,-1] #방향 순서 상관 없음 
dy = [1,0,-1,0]

for _ in range(n):
    graph.append(list(map(int, input())))

def BFS(x, y):
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft() # visit Level1 
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 1: #no monster no visited
                    graph[nx][ny] =graph[x][y] + 1
                    queue.append((nx, ny))
    return
       
BFS(0,0)
print(graph[n-1][m-1])