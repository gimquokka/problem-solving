#boj_2606
n= int(input())
m= int(input())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a>b:
        parent[b] = a
    elif a>b:
        parent[a] = b

parent = [0] * 101

for i in range(1, 101):
    parent[i] = i

networks = [ ]
s = set()
for _ in range(m):
    a,b =map(int,input().split())
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        union_parent(parent,b,a)
        s.add(a)
        s.add(b)
    networks.append((a,b))

ret = 0
for i in s:
    if (find_parent(parent,1) == find_parent(parent,i) and i!=1):
        ret +=1

print(ret)




