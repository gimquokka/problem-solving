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

parent = [i for i in range(n+1)]

for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(n):
        if graph[j] == 1:
            union_parent(parent, i, j)

palce = list(map(int, input().split()))

for i in range(m-1):
    if find_parent(parent, palce[i]) != find_parent(parent, palce[i+1]):
        print('NO')
        quit()
print('YES')