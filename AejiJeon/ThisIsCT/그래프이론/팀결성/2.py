import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = []
for i in range(0, n+1):
    parent.append(i)

def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    
    return parent[x]

def union_team(parent, a, b):
    a = find_root(parent, a)
    b = find_root(parent, b)

    if a > b:
        parent[a] = b

    else:
        parent[b] = a
result = []   
for _ in range(m):
    op , a, b = map(int, input().split())
    if op == 0:
        union_team(parent, a, b)
    else:
        if find_root(parent, a) == find_root(parent, b):
            result.append("YES")
        else:
            result.append("NO")

for i in result:
    print(i)