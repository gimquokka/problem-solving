n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


dx = [-1, 0, 0, 1] # 차례대로 U, L, D, R 방향으로 한칸 이동 변화량 (방향 순서 상관 없음)
dy = [0, -1, 1, 0]

def DFS(x, y):
    graph[x][y] = 1 # visited

      
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= m-1: # no index error 
            if  graph[nx][ny] == 0: # not visited
                DFS(nx, ny)
            
    
        

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: # 
            DFS(i, j)
            count += 1
            print(i, j)

print(count)



