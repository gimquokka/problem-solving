from collections import deque

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))


def impossible(data):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for x in range(n):
        for y in range(m):
            if data[x][y] == 0:
                check = False
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != -1:
                        check = True
                if not check:
                    return -1


def bfs(data, start):
    q = deque([])
    q.append(start)
    visited = set()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        visited.add((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and ((nx, ny) not in visited):
                if data[nx][ny] == 0:
                    data[nx][ny] = data[x][y]+1
                    q.append((nx, ny))
                elif data[nx][ny] > 1:
                    data[nx][ny] = min(data[nx][ny], data[x][y]+1)
                    q.append((nx, ny))


if impossible(data) == -1:
    print(-1)
else:
    for x in range(n):
        for y in range(m):
            if data[x][y] == 1:
                bfs(data, (x, y))
    result = 0
    for low in data:
        result = max(result, max(low))
    print(result-1)