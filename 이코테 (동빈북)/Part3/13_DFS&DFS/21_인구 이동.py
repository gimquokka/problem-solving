from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
all_tot = deque()
all_connected = deque()


def bfs(arr, visited, x, y):
    global cnt, movement

    # 연결된 국가들의 정보 저장
    tot_population = arr[x][y]
    connected = []
    # BFS를 수행하기 위한 정보 저장
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        now_x, now_y = q.popleft()
        connected.append((now_x, now_y))
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n):
                if not visited[nx][ny]:
                    if l <= abs(arr[now_x][now_y] - arr[nx][ny]) <= r:
                        tot_population += arr[nx][ny]
                        q.append((nx, ny))
                        visited[nx][ny] = True

    if len(connected) > 1:
        avg = int(tot_population/len(connected))
        all_tot.append(avg)
        all_connected.append(connected)

        if not movement:
            movement = True


cnt = 0
for _ in range(n*n):
    prev_cnt = cnt
    visited = [[False]*n for _ in range(n)]
    movement = False
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                bfs(arr, visited, x, y)

    for idx, avg in enumerate(all_tot):
        for x, y in all_connected[idx]:
            arr[x][y] = avg

    if movement:
        cnt += 1
    else:
        print(cnt)
        break
