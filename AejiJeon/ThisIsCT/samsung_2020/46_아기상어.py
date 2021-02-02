import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())

graph = []

x, y = 0, 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        # start position
        if data[j] == 9:
            x, y = i, j

# return list containing positions of fishes 
# whose sizes are less than the baby shark
def getEatable(size):
    n = len(graph)
    positions = []
    for i in range(n):
        for j in range(n):
            if 1 <= graph[i][j] < size:
                positions.append((i, j))

    return positions

# return array containing distances from (x,y) 
def bfs(x, y, size):
    n = len(graph)
    array = [[0]*n for _ in range(n)]
    VISITED = [[False]*n for _ in range(n)]
    
    queue = deque()
    queue.append((x, y))
    VISITED[x][y] = True

    while queue:
        pos = queue.popleft()
        
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            
            # is in index range and can go by 
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and graph[nx][ny] <= size:
                
                if VISITED[nx][ny]:
                    continue
                
                array[nx][ny] = 1 + array[pos[0]][pos[1]]
                VISITED[nx][ny] = True
                queue.append((nx, ny))
    
    return array
    
# returns position of shortest distance 
#from (x,y) to eatable positions 

def getNearest(lst, x, y, size):
    min_pos = (0, 0)
    min_val = int(1e9)
    distance_lst = bfs(x, y, size)

    

    for target in lst:
        i, j = target   
        temp = distance_lst[i][j]
        if temp == 0:
            continue
        if min_val > temp:
            min_val = temp
            min_pos = (i, j)
        elif min_val == temp:
            # same distane -> higher, same height -> further left
            if min_pos[0] > i or (min_pos[0] == i and min_pos[1] > j):
                min_pos = (i, j)
    
    return min_pos, min_val



time = 0
size = 2
eaten = 0
while True:
    eatable = getEatable(size)
    
    
    if not eatable:
        break
    
    

    goEat, distance = getNearest(eatable, x, y, size)
    # can't go to eatable positions
    if distance == int(1e9):
        break
    time += distance
    eaten += 1
    print("냠:", goEat)
    graph[x][y] = 0
    x, y = goEat
    graph[x][y] = 9
    
    if size == eaten:
        size += 1
        eaten = 0

print(time)






