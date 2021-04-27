#boj_4936
#speed DFS << BFS
w,h = map(int,input().split())

dx = [0, 0, -1, 1, -1, 1,  1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def DFS(x, y, graph):
    graph[x][y] =0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx <= h - 1 and ny >= 0 and ny <= w - 1:
            if graph[nx][ny]==1:
                DFS(nx,ny,graph)

land_num = []
while (w!=0 and h!=0):
    space = []
    for _ in range(h):
        space.append(list(map(int,input().split())))
    count = 0
    for i in range(h):
        for j in range(w):
            if space[i][j] == 1:
                DFS(i, j,space)
                count += 1

    land_num.append(count)
    w, h = map(int,input().split())

for i in land_num:
    print(i)