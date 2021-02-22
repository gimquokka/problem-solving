import heapq
import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())

edges = []
parent = [i for i in range(n+1)]
for i in range(m):
    a, b, cost = map(int, input().split())
    heapq.heappush(edges, (cost, a, b))

result = 0
biggest = 0
for i in range(m):
    cost, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        biggest = cost

print(result - biggest)
