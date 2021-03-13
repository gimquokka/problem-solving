'''
상세
1. 자기보다 큰 물고기 못 지나감
2. 같은 물고기는 지나는 가지만, 먹을 수는 없음
3. 처음 아기상어 크기 2
4. 크기 만큼의 수의 물고기를 먹어야 크기 1 증가

구현
bfs => (size, dist) => size < 상어 => 
bfs => 다음 먹을 것 찾고, 이동
eat_cnt => 먹은 개수
다음 먹을 것이 없으면 => q가 비면
'''
from collections import deque
import heapq

# board size 입력 받기
n = int(input())

# board 입력 받기
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

    # 초기 상어의 위치 찾기
    # 이와 같이 입력 받을 때 같이 찾으면 다시 이중 for문을 돌려줄 필요 없음
    if 9 in row:
        init_pos = (i, row.index(9))
        # 원활한 bfs를 위하여 9 => 0으로 초기화
        graph[init_pos[0]][init_pos[1]] = 0


# 상어 사이즈 초기화
shack_size = 2


def bfs(init_pos):
    # 외부 변수를 바꿔주고 싶음으로 global 선언
    # => 없어도 돌아가네? 불필요! 이미 두 변수 모두 global임으로
    # global shack_size, graph

    # bfs를 위한 변수 초기화
    q = deque()
    q.append((*init_pos, 0))
    visited = [[False]*n for _ in range(n)]
    visited[init_pos[0]][init_pos[1]] = True
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    # bfs 수행
    while q:
        eaten = []
        # 이렇게 for문을 한번 걸어주면 같은 거리별로 나누어 탐색 가능
        for _ in range(len(q)):
            x, y, dist = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # board 안에 있다면,
                if 0 <= nx < n and 0 <= ny < n:
                    # 아직 방문하지 않았고, 이동할 위치의 물고기가 상어보다 작거나 같다면
                    if not visited[nx][ny] and graph[nx][ny] <= shack_size:
                        q.append((nx, ny, dist+1))
                        visited[nx][ny] = True
                        # 이동할 위치의 물고기가 상어보다 작다면
                        if 0 < graph[nx][ny] < shack_size:
                            # heap로 넣어주면 속도도 빠르고, 따로 정렬 안해줘도 됨
                            heapq.heappush(eaten, ((nx, ny), dist+1))
        # 방금 전 순회한 거리에 먹을 수 있는 물고기가 있다면
        if eaten:
            next_pos, dist = heapq.heappop(eaten)
            # 물고기 먹었으면으로 board 상에서 해당 노드 0으로 초기화
            graph[next_pos[0]][next_pos[1]] = 0
            return next_pos, dist
    # 먹을 수 없는 물고기가 없다면 그냥 초기 위치 반환
    # 이렇게 하는게 null, False보다 처리하기가 쉬운 듯 => Optional?
    return init_pos, 0


# Simulation 수행을 위하여 변수 초기화
tot_dist = 0
eaten_cnt = 0
# simulation 수행
while True:
    # 탐색 수행
    next_pos, dist = bfs(init_pos)

    # 먹을 수 있는 물고기가 없을 경우
    if next_pos == init_pos:
        break

    # 있다면 먹은 물고기 수 count
    eaten_cnt += 1

    # 먹은 물고기가 상어의 사이즈와 같다면
    if eaten_cnt == shack_size:
        # 상어 사이즈 up 및 먹은 물고기 개수 초기화
        shack_size += 1
        eaten_cnt = 0

    # 총거리에 움직인 거리 및 이동 좌표 반영
    tot_dist += dist
    init_pos = next_pos

# 총거리 출력
print(tot_dist)
