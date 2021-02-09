import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

ans = 0
for i in range(2, n+1):
    if find_parent(parent, i) == 1:
        ans += 1
print(ans)
