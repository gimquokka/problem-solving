import sys
input = sys.stdin.readline

# returns the root node of x
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union of the set containing a and the set containing b
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]
    
n, m = map(int, input().split())
edges = []

parent = [0]*n
for i in range(n):
    parent[i] = i




# sum of cost of all street lamps 
allPay = 0 

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    allPay += cost

# uses kruscal algorithm for finding MST weight
totalPay = 0 

edges.sort()

for edge in edges:
    cost, a, b = edge
    # takes unoin of two sets and 
    # adds edge to the subgraph of MST
    if find_parent(parent, a) != find_parent(parent, b):
        totalPay += cost
        union_parent(parent, a, b)

# saving sum of money
print(allPay - totalPay)


