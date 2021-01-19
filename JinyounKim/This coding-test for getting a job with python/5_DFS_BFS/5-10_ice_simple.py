def dfs(x, y):
	if (x < 0) or (y < 0) or (x>=n) or (y>=m):
		return False
	if g[x][y] == 0:
		# 해당 노드 방문처리
		g[x][y] = 1
		# 그래프 상하좌우 재귀적으로 호출
		dfs(x+1, y)
		dfs(x, y+1)
		dfs(x-1, y)
		dfs(x, y-1)
		return True
	return False
	 

import sys
n, m = map(int, input().split())

g = [[0]*m for _ in range(n)]

for i in range(n):
	g[i] = list(map(int, sys.stdin.readline().rstrip()))

ans = 0

for i in range(n):
	for j in range(m):
		if dfs(i, j) == True:
			ans += 1

print(ans)