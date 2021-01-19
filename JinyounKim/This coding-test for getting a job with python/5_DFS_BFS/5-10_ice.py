def dfs(graph, v, visited):
	visited[v] = True

	for i in graph[v]:
		if not visited[i]:
			visited[i] = True
			dfs(graph, i, visited)
	
	return visited
	

import sys
n, m = map(int, input().split())

arr = [[0]*m for _ in range(n)]

for i in range(n):
	l = sys.stdin.readline().rstrip()
	arr[i] = [int(j) for j in l] 

graph = [[] for _ in range(n*m)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(n):
	for j in range(m):
		for k in range(4):
			x, y = i+dx[k], j+dy[k]
			if (0<=x<n) and (0<=y<m) and (arr[x][y]== 0) and (arr[i][j]== 0):
				graph[i*m+j].append(x*m+y)

visited = [0]*(m*n)
for i in range(n):
	for j in range(m):
		if arr[i][j]: 
			visited[i*m+j] = True

cont = 0
for i in range(n):
	for j in range(m):
		if visited[i*m+j] == 0:
			cont += 1
			dfs(graph, i*m+j, visited)


print(cont)


