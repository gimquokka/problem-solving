import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append((x, 0))
visited[x] = True

ans = []
while q:
    now, dist = q.popleft()
    
    if dist == k:
        ans.append(now)
    # elif dist > k:
    #     break
    
    for next in graph[now]:
        if visited[next] is False:
            q.append((next, dist+1))
            visited[next] = True


if not len(ans):
    print(-1)
else:
    for a in ans:
        print(a)