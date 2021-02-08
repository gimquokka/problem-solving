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


n = int(input())

parent = [i for i in range(n)]
x, y, z = [], [], []
for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

graph = []
for i in range(n-1):
    graph.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    graph.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    graph.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))

graph.sort()
result = 0
for cost, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


'''
# 이렇게 짜도 돌아는 가지만 n이 1e5임으로 최대 (1e5)*2의 경우의 수를 고려해야함으로 메모리 초과 판정을 받을 수 있다.
for i in range(n):
    x, y, z = map(int, input().split())
    cord.append((i, x, y, z))

graph = []

for i in range(n):
    for j in range(i+1, n):
        if i != j:
            dist = min(abs(cord[i][1]-cord[j][1]), abs(cord[i]
                                                       [2]-cord[j][2]), abs(cord[i][3]-cord[j][3]))
            graph.append((dist, i, j))

graph.sort()
'''
