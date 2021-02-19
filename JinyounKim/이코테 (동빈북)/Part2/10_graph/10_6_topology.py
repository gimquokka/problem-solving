from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for i in range(m):
	a, b = map(int, input().split())
	edges[a].append(b)
	indegree[b] += 1

def topology_sort(edges, indegree):
	q = deque()
	result = []

	for i in range(1, n+1):
		if indegree[i] == 0:
			q.append(i)
	
	while q:	
		now = q.popleft()
		result.append(now)

		for node in edges[now]:
			indegree[node] -= 1
			if indegree[node] == 0:
				q.append(node)
	
	print(*result)

topology_sort(edges, indegree)
				
			
