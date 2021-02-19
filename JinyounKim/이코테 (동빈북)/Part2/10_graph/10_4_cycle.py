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

cycle = False

for i in range(m):
	v1, v2 = map(int, input().split())
	if find_parent(parent, v1) == find_parent(parent, v2):
		cycle = True
		break
	else: 
		union_parent(parent, v1, v2)

print('사이클 감지' if cycle else '사이클 미감지')
	