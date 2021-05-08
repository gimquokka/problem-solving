"""
- 위상 정렬(Topology Sort)
: 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것

- 전략
1. 진입차수가 0인 노드를 큐에 넣는다
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    (1) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거하낟.
    (2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

- Time Complexity
O(V+E) # 모든 간선과 노드를 확인함으로
"""
from collections import deque
import sys
input = sys.stdin.readline

# 노드와 간선의 개수를 입력받기
n, m = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(n+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(n+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # B의 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입. 0이 들어가면 안됨
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌  때까지 반복 => 큐가 중간에 빈다면 Cycle, 즉, 위상정렬 불가능
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 결과 값 반환
    return result

print(*topology_sort())
 

