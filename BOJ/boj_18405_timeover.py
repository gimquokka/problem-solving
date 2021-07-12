import sys
import copy
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
v_pos = [[] for i in range(k+1)]
for vx in range(n):
    row = list(map(int, input().split()))
    
    for vy, virus in enumerate(row):
        if virus != 0:
            v_pos[virus].append((vx, vy))
            
    graph.append(row)
    
s, ax, ay = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
for step in range(s):
    for pos in v_pos:
        nv_pos = copy.deepcopy(v_pos)
        for x, y in pos:
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
            
                
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    nv_pos[graph[x][y]].append((nx, ny))
    v_pos = nv_pos               
        

# print(graph)
print(graph[ax-1][ay-1])
