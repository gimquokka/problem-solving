from collections import deque

queue = deque()
n, m = map(int, input().split())
graph = []

dx = [0,1,0,-1] #방향 순서 상관 없음 
dy = [1,0,-1,0]

for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(x,y, c1, c2):
    global count
    
    graph[x][y] = 1 # visited
    if x == n-1 and y == m-1:
        count += 1
        print(count)
        return
     
    if c1 == 0:      # all elems in the breath level are popped.
        count += 1
        c1 = c2      
        c2 = 0       # initialization of the number of elems in next level


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx <= n-1 and ny <= m-1 : # inside
            if graph[nx][ny] == 1: # no monster and not visited
                queue.append((nx, ny))
                c2 += 1     # the number of ways to be able to go

    
    if c2 == 0:
        return
    e = queue.popleft()
    bfs(e[0], e[1], c1-1, c2)

        
count = 0

bfs(0,0,0,graph[0][1] + graph[1][0])
