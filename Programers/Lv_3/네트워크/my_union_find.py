def solution(n, computers):
    parent = [i for i in range(n)]
    
    for i, connections in enumerate(computers):
        for j, connected in enumerate(connections):
            if i == j: continue
            
            if connected:
                union_parent(parent, i, j)
    
    for i in range(n):
        parent[i] = find_parent(parent, i) 

    return len(set(parent))

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


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # ans = 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # ans = 1