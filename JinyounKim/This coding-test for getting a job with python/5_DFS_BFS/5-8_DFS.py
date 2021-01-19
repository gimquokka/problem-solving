# DFS function
def dfs(graph, v, visited):
	visited[v] = True

	print(v, end = ' ')

	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

graph = [
	[], 		# v: 0
	[2, 3, 8],  # v: 1
	[1, 7], 	# v: 2
	[1, 4, 5],  # v: 3
	[3, 5], 	# v: 4
	[3, 4],		# v: 5
	[7], 		# v: 6
	[6, 8], 	# v: 7
	[1, 7], 	# v: 8
]

visited = [False]*len(graph)

dfs(graph, 1, visited)
	

