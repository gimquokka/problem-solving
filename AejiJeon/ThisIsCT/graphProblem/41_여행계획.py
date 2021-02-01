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
# initialization
parent = [0]*(n+1)

# assigns the parent node of each vertex to its vertex number 
for i in range(1, n+1):
    parent[i] = i

# union of incident vertices of each edge
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)


answer = "YES"
places = list(map(int, input().split()))
# the root node of start vertex for traveling
startParent = find_parent(parent, places[0])


for place in places:
    # belongs to each other sets
    if startParent != find_parent(parent, place):
        answer = "NO"
        break

print(answer)


