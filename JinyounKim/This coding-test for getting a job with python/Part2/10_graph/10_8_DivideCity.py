import sys
input = sys.stdin.readline

def find_parent(parent, a):
	if parent[a] != a:
		parent[a] = find_parent(parent, parent[a])
	return parent[a]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a > b:
		parent[a] = b
	else:
		parent[b] = a

n , m = map(int, input().split())

edges = []
parent = [i for i in range(n+1)]

for i in range(m):
	a, b, cost = map(int, input().split())
	# union_parent(parent, a, b)
	edges.append((cost, a, b))

edges.sort()

print(edges)

result = 0
# cont = 0
last = 0
for cost, a, b in edges:
	if find_parent(parent, a) != find_parent(parent, b):
		# if cont <= n-2
		# cont += 1
		union_parent(parent, a, b)
		result += cost
		last = cost # Get last cost val
		# print('cont, cost: ', cont, cost)

print(result - last)

	
