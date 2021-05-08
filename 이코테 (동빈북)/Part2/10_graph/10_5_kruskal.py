import sys
input = sys.stdin.readline

def find_parent(parent, v):
	if parent[v] != v:
		parent[v] = find_parent(parent, parent[v])
	return parent[v]

def union_parent(parent, v1, v2):
	v1 = find_parent(parent, v1)
	v2 = find_parent(parent, v2)

	if v1 > v2:
		parent[v1] = v2
	else: 
		parent[v2] = v1

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
edges = []
result = 0

for i in range(m):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

edges.sort()

for cost, a, b in edges:
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost

print(result)