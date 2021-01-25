
import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())

graph = []
lst_0s = []
lst_2s = []

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] == 0:  # 벽 세울 수 있는 곳
            lst_0s.append((i,j))
        
        elif data[j] == 2:  # 바이러스 시작점들
            lst_2s.append((i,j))

set_walls = list(combinations(lst_0s, 3)) # 벽3개 설치 조합

dx = [1,-1,0,0] #bfs에서 사용할 변화량 아래 위 오 왼
dy = [0,0,1,-1]
def virus_bfs(x, y, graph): # 바이러스 전파시킴
    queue = [] # deque() 사용하지 않고 큐 구현
    queue.append((x,y))
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= m-1 and graph[nx][ny] == 0:#범위내, 0인지체크
                queue.append((nx,ny))
                graph[nx][ny] = 2

    

def nums_0s(graph):  # 안전구역 수
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count

result = 0

for walls in set_walls:
    n_graph = []   # 2차원배열 deepcopy
    for i in range(n):
        n_graph.append(graph[i][:])
    for x,y in walls: # 벽설치
        
        n_graph[x][y] = 1
    
    for x, y in lst_2s:
        virus_bfs(x,y,n_graph)
    
    
    result = max(result, nums_0s(n_graph))
    
print(result)

    



    
