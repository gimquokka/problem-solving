import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

# graph -> adjacent list structure
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# bfs에서 사용할 queue
queue = deque()

VISITED = [False] * (n + 1)


def bfs(start):
    # 시작 노드 setting
    queue.append(start)
    VISITED[start] = True

    count = 0
    while queue:
        now = queue.popleft()

        # 모든 adjacent vertices에 대해
        for adj in graph[now]:
            # 방문되지 않았을 경우에만 카운트
            if not VISITED[adj]:
                queue.append(adj)
                VISITED[adj] = True

                count += 1

    return count


print(bfs(1))
