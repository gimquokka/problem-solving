from collections import deque

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# Get input
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 이렇게 1 값들을 한번에 que에 넣고 bfs돌려도 결과 똑같이 나옴...ㅜㅜ
# 굳이 이중 for문 안에서 bfs돌릴 필요 없음
q = deque([])
for x in range(n):
    for y in range(m):
        if data[x][y] == 1:
            q.append((x, y))

# BFS
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
            data[nx][ny] = data[x][y]+1
            q.append((nx, ny))

# -1 조건체크를 마지막에 해주면 더 효율적
ans = -1
for x in range(n):
    for y in range(m):
        if data[x][y] == 0:
            print(-1)
            quit()
        # print(data)
        ans = max(ans, data[x][y])

print(ans-1)
