import sys
from collections import deque

def bfs(g, x, y):
	queue = deque([])
	queue.append((x, y))
	dx = [1,-1, 0, 0]
	dy = [0, 0, 1, -1]
	while queue:
		v = queue.popleft()
		print(v)
		x, y = v
		for i in range(4):
			nx, ny = (x+dx[i]), (y+dy[i])
			if (0<=nx<n) and (0<=ny<m) and (g[nx][ny] == 1):
				g[nx][ny] = g[x][y]+1
				queue.append((nx, ny))



n, m = map(int, input().split())

g  = [[0]*m for _ in range(n)]

for i in range(n):
	g[i] = list(map(int, sys.stdin.readline().rstrip()))

bfs(g, 0, 0)

print(g[n-1][m-1])

