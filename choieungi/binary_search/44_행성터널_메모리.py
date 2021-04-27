def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent, a)
    b= find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [0] *(n+1)
location = [0] * (n+1)
edges = [ ]

for i in range(1,n+1):
    parent[i] = i

for i in range(n):
    x,y,z  = map(int,input().split())
    location[i] = (i+1,x,y,z) #노드, 좌표

for i in range(n-1):
    for j in range(i+1,n-1):
        p, x,y,z = location[i]
        q, a,b,c = location[j]
        cost = min(abs(x-a),abs(y-b),abs(z-c))
        edges.append((cost,p,q))

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+= cost

print(result)
