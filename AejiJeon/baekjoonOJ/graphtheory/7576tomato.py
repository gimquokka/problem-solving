import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

array = [[0] * m for _ in range(n)]

queue = deque()

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        # 익은 토마토 위치 담기
        if data[j] == 1:
            array[i][j] = data[j]
            queue.append((i, j))
        elif data[j] == -1:
            array[i][j] = data[j]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 토바토 창고 탐색
def bfs():
    while True:
        if not queue:
            return
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 안 익은 토마토 위치
                if array[nx][ny] == 0:
                    # 시간 +1
                    array[nx][ny] = array[x][y] + 1
                    queue.append((nx, ny))


# 결과값 계산 해주는 함수
def getResult():
    max_value = 0
    for i in range(n):
        for j in range(m):
            # 안 익은 토마토 존재
            if array[i][j] == 0:
                return -1
            max_value = max(max_value, array[i][j])

    return max_value - 1


bfs()
print(getResult())
