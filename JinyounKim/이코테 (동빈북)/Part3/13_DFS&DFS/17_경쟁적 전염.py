# n, k 입력 받기
n, k = map(int, input().split())

# Graph 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 시간, 결과값 좌표 입력 받기
s, ax, ay = map(int, input().split())

# 거리가 0인 시작점들 입력 받기
q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append((graph[i][j], i, j, 0))

# bfs를 위한 변수 선언
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
# bfs 수행
while q:
    # s초가 되면 멈추기
    if q[0][3] == s:
        break
    # 우선순위가 높은 바이러스부터 전파시키기
    q.sort()
    for _ in range(len(q)):
        val, x, y, dist = q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 이미 우선 순위가 높은 바이러스는 전파를 끝냈을 것임으로.
                if graph[nx][ny] == 0:
                    graph[nx][ny] = val
                    # 다음 탐색할 노드 삽입
                    q.append((val, nx, ny, dist+1))

# 결과값 출력
print(graph[ax-1][ay-1])

# for i in range(n):
#     print(*graph[i])
