from itertools import combinations
from collections import deque
import copy

# 사이즈 입력 받기
n, m = map(int, input().split())

# 그래프 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 0인 칸의 좌표 담기
blank = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i, j))

# 벽(=1)을 3개를 놓을 수 있는 iterable 객체 생성
candidate = combinations(blank, 3)

# 2가 놓여져 있는 위치 탐색 (start points)
start_pos = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_pos.append((i, j))

# bfs에 쓸 변수 초기화
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
# 벽 3개를 각기 다른 위치에 놓으며 bfs 수행
for candidate_pos in candidate:
    # deepcopy 이용하여 임시 graph 생성
    tmp_graph = copy.deepcopy(graph)
    # 벽 3곳에 놓기
    for x, y in candidate_pos:
        tmp_graph[x][y] = 1
    # bfs 수행 => 바이러스(=2) 전파
    q = deque()
    for x, y in start_pos:
        q.append((x, y))
        while q:
            pop_x, pop_y = q.popleft()
            for i in range(4):
                nx = pop_x + dx[i]
                ny = pop_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if tmp_graph[nx][ny] == 0:
                        tmp_graph[nx][ny] = 2
                        q.append((nx, ny))
    # 바이러스 전파 이후에도 0인 곳의 개수 확인
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 0:
                cnt += 1
    # 최댓값 갱신
    ans = max(ans, cnt)

# 정답 출력
print(ans)
