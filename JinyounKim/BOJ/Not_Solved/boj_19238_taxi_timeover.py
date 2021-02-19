"""
1. while fuel:
    ~~~
2. bfs로 현재 택시 위치에서 가장 가까운 승객위치 확인, 벽고려
3. bfs로 목적지까지 바래다 주기 => fuel + dist
4. 목적지 도착과 동시에 연료 충전
5. 거리 동일할 시 행 => 열 순으로

### val ###
fuel,
dx, dy

### def ###
1. 
find_passinger(passinger, pos)
=> 가장 가까운 승객중, 행과, 
열이 가장 작은 승객 정보를 (1, 1, 2 ,4) 반환 후 승객 목록에서 삭제,
그런 승객이 없다면 -1을 반환
Input: 택시현재위치(1x2), 승객 list
Output: 
1. 가장 가까t운 승객정보, 택시부터 승객까지 거리, 승객위치부터 목적지까지 거리
2. 만약 그런 승객이 없다면 -1을 반환

2. 
find_dist() <= visited
Input: 택시현재위치, 승객위치
ouput: 택시와 승객 사이의 거리 반환
"""
import sys
from collections import deque
import copy
input = sys.stdin.readline
INF = int(1e5)

N, M, fuel = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(N)]

tmp = list(map(int, input().split()))
pos_taxi = list(i-1 for i in tmp)

tmp = [list(map(int, input().split())) for _ in range(M)]
pas = []
for i in tmp:
    pas.append(list(j-1 for j in i))
pas.sort()


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_dist(loc, p):
    g = copy.deepcopy(B)
    g[p[0]][p[1]] = -1
    q = deque()
    q.append([*loc, 0])
    g[loc[0]][loc[1]] = 1
    if loc == p:
        return 0
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and g[nx][ny] != 1:
                if g[nx][ny] == -1:
                    return dist+1
                if g[nx][ny] == 0:
                    q.append((nx, ny, dist+1))
                    g[nx][ny] = 1
    return -1


def find_pas(loc, pas):
    taxi_to_pas = INF
    for i in pas:
        ### 모든 승객의 거리를 그때마다 계산해서 O(M*N^2) => O(N^4)이 되어 timeover ###
        ### BFS의 특성을 고려하지 못함 ###
        dist = find_dist(loc, i[:2])
        if dist == -1:
            return -1
        if taxi_to_pas > dist:
            taxi_to_pas = dist
            pas_info = copy.deepcopy(i)
    pas_to_dest = find_dist(pas_info[:2], pas_info[2:])
    pas.remove(pas_info)
    return pas_info, taxi_to_pas, pas_to_dest


def solve(fuel, pos_taxi, pas):
    while fuel and len(pas):
        p_info = find_pas(pos_taxi, pas)
        if p_info == -1:
            return print(-1)
        p, taxi_to_pas, pas_to_dest = p_info
        fuel -= (taxi_to_pas+pas_to_dest)
        if fuel >= 0:
            fuel += 2*pas_to_dest
            pos_taxi = p[2:4]
            if len(pas) == 0:
                return print(fuel)
        else:
            return print(-1)


solve(fuel, pos_taxi,  pas)
