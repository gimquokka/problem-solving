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

import sys

input = sys.stdin.readline

n = int(input())

x, y, z = [], [], []
for i in range(n):
    tx, ty, tz = map(int, input().split())
    x.append((tx, i))
    y.append((ty, i))
    z.append((tz, i))

x.sort()
y.sort()
z.sort()
graph = []
for i in range(n-1):
    graph.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    graph.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    graph.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

graph.sort()

ans = 0
parent = [i for i in range(n)]
# while graph// graph.pop(0)으로 하면 시간초과
for node in graph:
    cost, a, b = node
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += cost

print(ans)