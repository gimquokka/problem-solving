#boj_7576
from collections import deque

m,n = map(int,input().split())
box = [[0]*m for _ in range(n)]

for i in range(n):
    box[i] = list(map(int,input().split()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if nx >=0 and nx<n and ny>=0 and ny<m :
            if box[nx][ny] == 0:
