
n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x,y,index):
    united = [(x, y)]
    union[x][y] = index # 연합 번호 
    
    q = [(x,y)]
    sum = graph[x][y]
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n  and 0 <= ny < n and union[nx][ny] == -1:
                
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx,ny))
                    united.append((nx,ny))
                    union[nx][ny] = index
                    sum += graph[nx][ny]
                   
    count = len(united)
    for x,y in united:
        graph[x][y] = sum // count


total_count = 0

while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i,j,index)
                index += 1
    if index == n*n:
        break
    total_count += 1

print(total_count) 
    