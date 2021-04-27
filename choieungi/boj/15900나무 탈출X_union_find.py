#boj_15900

n = int(input())

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

parent = [0] * (n+1)
calculate = [0] *(n+1)

#부모 노드 초기화
for i in range(1,n+1):
    parent[i] = i

for _ in range(n-1):
    a,b = map(int, input().split())
    if a>b:
        a,b = b,a #반드시 a<b 로 받기
    union_parent(parent,a,b)
    calculate[b] = calculate[a] + 1

print(calculate)
'''
leaf_node = []

print(parent)
for i,j in enumerate(parent):
    if i != j:
        leaf_node.append(i)

cnt,ret =0,0

for i in leaf_node:
    if find_parent(parent,i) == 1:
        print(i)
        print(cnt)
        ret += cnt
        cnt = 0

#print(ret)
'''