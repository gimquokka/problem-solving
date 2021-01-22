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



n, m = map(int, input().split())

parent= [i for i in range(n+1)]
result = []

for i in range(m):
	t, a, b = map(int, input().split())
	if t == 0:
		union_parent(parent, a, b)
	else:
		if find_parent(parent, a) == find_parent(parent, b):
			result.append('YES')
		else:
			result.append('NO')

for i in result:
	print(i)
	