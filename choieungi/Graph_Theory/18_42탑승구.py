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

gate_num = int(input())
p = int(input())
parent = [0] * (gate_num + 1)

for i in range(1, gate_num + 1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    #루트 노드와 연결
    union_parent(parent, data, data - 1)
    result += 1

print(result)