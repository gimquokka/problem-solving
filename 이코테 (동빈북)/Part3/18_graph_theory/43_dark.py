import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

graph = []
parent = [i for i in range(n)]
tot = 0
for i in range(m):
    a, b, cost = map(int, input().split())
    # union_parent(parent, a, b)
    graph.append((cost, a, b))
    tot += cost

graph.sort()

min_tot = 0
for cost, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_tot += cost

print(tot - min_tot)
# print(tot)
# print(min_tot)
