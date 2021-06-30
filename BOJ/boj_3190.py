from collections import deque

n = int(input())
k = int(input())

graph = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    
l = int(input())
info = []
for _ in range(l):
    time, dirction = input().split()
    info.append((int(time), dirction))

def turn(LD, direction):
    if LD == "D":
        dirction = (direction+1)%4
    else:
        dirction = (direction-1)%4
    return dirction
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append((0, 0))
times = 0
dirction = 0
index = 0
while True:
    times += 1
    x, y = q[0]
    nx, ny = x + dx[dirction], y + dy[dirction]
    
    if not (0 <= nx < n and 0 <= ny < n and (nx, ny) not in q):
        break
    
    q.appendleft((nx, ny))
    if graph[nx][ny] != 1:
        q.pop()
    else:
        graph[nx][ny] = 0
   
    if index < l and times == info[index][0]:
        dirction = turn(info[index][1], dirction)
        index += 1

print(times) 