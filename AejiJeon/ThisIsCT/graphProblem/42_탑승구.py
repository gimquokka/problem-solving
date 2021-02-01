import sys
sys.stdin.readline

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

g = int(input())
p = int(input())

# root gate of ith gate is the highest number of empty gate 
# among from gate1 to gate i 
parent = [0]*(g+1)
for i in range(g+1):
    parent[i] = i

count = 0

for _ in range(p):
    gi = int(input())
    
    # empty gate doesn't exist 
    if find_parent(parent, gi) == 0:
        break
    # emty gate exists
    count += 1
    # union of the set containing gate gi and 
    # the set containing gate which is 
    # 1 smaller than root gate of gate gi
    union_parent(parent, gi, parent[gi]-1)

print(count)