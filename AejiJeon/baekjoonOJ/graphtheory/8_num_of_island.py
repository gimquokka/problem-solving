#  dx, dy 반시계방향 시계방향 순서..
import sys
from collections import deque
input = sys.stdin.readline

# to visit 8 adjacent vertices
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

# traverse all connected lands
def bfs(graph, x, y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    
    while q:
        x, y = q.popleft()

        # 인접한 vertices checking
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경계 밖 x, adjacent, case of land
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1:
                    # 
                    q.append((nx, ny))
                    graph[nx][ny] = 0
    return




while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break

    graph = []

    for _ in range(h):
        graph.append(list(map(int, input().split())))
    count = 0
    for i in range(h):
        for j in range(w):
            # 모든 lands에 대해서 완전 탐색
            if graph[i][j] == 1:
                bfs(graph, i, j)
                count += 1
    print(count)


