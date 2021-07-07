import copy
from collections import deque
from itertools import combinations

def bfs(graph, pos):
    n = len(graph)
    m = len(graph[0])
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, -0]
    
    q = deque()
    q.append(pos)
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))
    
    return graph

def check_num_of_safty(graph):
    n = len(graph)
    m = len(graph[0])
    
    cnt = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                cnt += 1
    return cnt


n, m = map(int, input().split())

graph = []
virus_pos = []
blank_pos = []
for r in range(n):
    row = list(map(int, input().split()))
    for c, _type in enumerate(row):
        if _type == 2:
            virus_pos.append((r, c))
        elif _type == 0:
            blank_pos.append((r, c))
    graph.append(row)

ans = 0
for choosed_pos in combinations(blank_pos, 3):
    temp_graph = copy.deepcopy(graph)
    for bx, by in choosed_pos:
        temp_graph[bx][by] = 1
        
    for v_pos in virus_pos:
        temp_graph = bfs(temp_graph, v_pos)
        
    ans = max(ans, check_num_of_safty(temp_graph))
    
print(ans)     