# 두 좌표가 주어졌을 때, 드는 비용이 x.y.z간의 거리 중 최솟값  이 때 드는 비용의 최솟값

# 1( 4, 5) 2(3,7) 3(-4, -3) 4(10,-1) 5(9,10)
#x: 3 (1) 4 1 5 2
#y: 3 (2) 4 1 2 5


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
location = []
edges = []

for i in range(1,n+1):
    parent[i] = i

for i in range(n):
    x,y,z  = map(int,input().split())
    location.append((i+1,x,y,z)) #노드, 좌표

location1 = sorted(location, key=lambda x: x[1])
location2 = sorted(location, key=lambda x: x[2])
location3 = sorted(location, key=lambda x: x[3])

for i in range(n-1):
    edges.append((location1[i+1][1]-location1[i][1], location1[i][0],location1[i+1][0]))
    edges.append((location2[i+1][2]-location2[i][2], location2[i][0],location2[i+1][0]))
    edges.append((location3[i+1][3]-location3[i][3], location3[i][0],location3[i+1][0]))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+= cost

print(result)


