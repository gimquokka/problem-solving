from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, start):
    q = deque([start])
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, 1, -1, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx <= h-1) and (0 <= ny <= w-1):
                if graph[nx][ny] != 0:
                    graph[nx][ny] = 0
                    q.append((nx, ny))


answer = []
while True:
    w, h = map(int, input().split())
    if w == 0 or h == 0:
        break

    graph = [[0]*w for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int, input().split()))

    count = 0
    for a in range(h):
        for b in range(w):
            if graph[a][b] == 1:
                bfs(graph, (a, b))
                count += 1
    answer.append(count)

for i in answer:
    print(i)
