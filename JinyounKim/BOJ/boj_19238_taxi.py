"""
### Strategy ###
1. 각 파트별로 완성 후 동작여부를 확인함 => 디버깅 시간 확실히 감소
2. BFS의 특성(가까운 거리별 탐색)을 활용하여 가장 가까운 승객을 O(N*2)으로 찾아냄
3. edge case 확인
    (1) 택시 승객 같은 위치 (2) 승객위치 목적지 같은 위치(세상에 이런 승객이 어디있음 -,-)
4. BFS를 mode와 같은 변수를 이용하여 한번만 짤 수도 있겠지만 스스로 와 닿지 않아서 (1) 승객을 찾는것과, (2) 목적지까지 이동 나눠서 짬

### Time Complexity ###
find_client => Max: O(n^2), Tot: O(N^2)
move_to_dest => O(N^2)

=> O(N^2+M*N^2)
"""

import sys
import heapq
from collections import deque
input = sys.stdin.readline

# Get input
N, M, fuel = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(N)]

tmp = list(map(int, input().split()))
pos_taxi = tmp[0]-1, tmp[1]-1

client_info = dict()
for _ in range(M):
    sx, sy, dx, dy = map(int, input().split())
    # Rescaling considering B's index
    sx, sy, dx, dy = sx-1, sy-1, dx-1, dy-1
    # Marking client in Board
    B[sx][sy] = -1
    # Store client_info for 목적지를 쉽게 찾기 위하여
    client_info[(sx, sy)] = (dx, dy)

"""
[Clear]
# Check input part
print(B)
print(client_info)
"""

# Declare frequently used val
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_client(pos_taxi, fuel):
    global B
    x, y = pos_taxi
    # 1. 택시와 승객의 위치가 같을 경우
    if B[x][y] == -1:
        # 지도의 해당 위치의 승객 없에기, 이를 위하여 원칙상 global을 선언함(없어도 되긴할 듯?)
        B[x][y] = 0
        return (x, y, 0)
    q = deque()
    q.append(pos_taxi)
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    client_pq = []
    dist = 0
    while q:
        # 목적지랑 도착지가 같은 승객이 있을 수 있기 때문에 등호제거
        # 거리보다 연료가 적으면 더 이상 갈 수 없음으로
        dist += 1
        if dist > fuel:
            return -1
        # print('fuel, dist', fuel, dist)
        # 이런식으로 for문을 걸어주면 dist별로 client를 확인할 수 있음
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < N and 0 <= ny < N and (visited[nx][ny] == False) and B[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    if B[nx][ny] == -1:
                        heapq.heappush(client_pq, (nx, ny, dist))
        if client_pq:
            x, y, dist = heapq.heappop(client_pq)
            B[x][y] = 0
            return (x, y, dist)
    return -1


'''
[clear]
# Check find_client func
print(find_client(pos_taxi))
print(find_client(pos_taxi))
print(find_client(pos_taxi))
'''


def move_to_dest(pos_taxi, dest, fuel):
    x, y = pos_taxi
    if pos_taxi == dest:
        return 0
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    q = deque()
    q.append(pos_taxi)
    dist = 0
    while q:
        dist += 1
        if fuel < dist:
            return -1
        # print('fuel, dist', fuel, dist)
        for i in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and B[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    if (nx, ny) == dest:
                        return dist
    # 에초에 도달할 수 없는 경우
    return -1


"""
[Clear]
# Check move_to_dest function
Test
"""


def solve(pos_taxi, fuel):
    for i in range(M):
        next_client = find_client(pos_taxi, fuel)
        # print(next_client)
        if next_client == -1:
            return print(-1)
        else:
            *pos_taxi, dist_client = next_client
        fuel -= dist_client
        # print(fuel)
        dest = client_info[tuple(pos_taxi)]
        dist = move_to_dest(pos_taxi, dest, fuel)

        if dist == -1:
            return print(-1)
        else:
            pos_taxi = dest

        fuel += dist
        # print(fuel)
    return print(fuel)


solve(pos_taxi, fuel)
