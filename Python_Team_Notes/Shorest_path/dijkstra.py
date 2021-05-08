"""
Time complexity: O(ElogE) = O(ElogV) 
(간선 개수 E <= V^2 임으로)
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 노드 연결관계 담을 리스트 선언
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블 무한대로 초기화
distance = [INF]*(n+1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    # a => b 노드 이동 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstart(start):
    q = []
    # 시작 노드 최단 경로 0으로 설정, 큐 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면,  최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if dist > distance[now]:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for v, d in graph[now]:
            cost = dist + d
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))


# 다익스트라 알고리즘 수행
dijkstart(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
print(distance)
