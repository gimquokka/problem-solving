from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def bfs(tree, start, visited, depth):
    q = deque([])
    q.append(start)
    visited[start] = True
    while q:
        parent = q.popleft()
        for node in tree[parent]:
            if visited[node] == False:
                q.append(node)
                depth[node] = depth[parent]+1
                visited[node] = True


visited = [False]*(n+1)
depth = [0]*(n+1)

bfs(tree, 1, visited, depth)

# print(depth)

tot_depth = 0
for i in range(2, n+1):
    if len(tree[i]) == 1:
        tot_depth += depth[i]

if tot_depth % 2 == 0:
    print('No')
else:
    print('Yes')
