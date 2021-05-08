from collections import deque
# import copy
import sys
input = sys.stdin.readline

n = int(input())

d = [0]*(n+1)
edges = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for v in range(1, n+1):
	cost, *a = list(map(int, input().split()))
	d[v] = cost
	# edges[i].append(a[:-1]) # This case hard to organize topolgical sort
	indegree[v] += len(a[:-1])
	for incoming_v in a[:-1]:
		edges[incoming_v].append(v)

def topolgy_sort(edges, d):
	q = deque()

	# address reference
	# nd = d

	# Using_Deepcopy
	# nd = copy.deepcopy(d)
	
	# List comprehension
	nd = [i for i in d]

	for i in range(1, n+1):
		if indegree[i] == 0:
			q.append(i)
	while q:
		now = q.popleft()
		for v in edges[now]:
			indegree[v] -= 1
			nd[v] = max(nd[now]+d[v], nd[v])
			if indegree[v] == 0:
				q.append(v)
	
	for i in range(1, n+1):
		print(nd[i])
			  
topolgy_sort(edges, d)

		

