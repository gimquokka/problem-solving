"""
전략
1. n x n 행렬을 만들어 자신보다 낮은 순위의 노드로 간선이 향하는 방향 그래프 생성
2. Topological Sort 수행시 len(q)가 0이 되는 경우가 있으면 사이클이 있는 것
=> "IMPOSSIBLE"
3. ''' len(q)가 2개 이상인 경우는 순위를 정할 수 없는 모호한 경우 
=> "?" 
"""
from collections import deque

for tc in range(int(input())):
    n = int(input())

    # 작년도 순위 list로 받기
    data = list(map(int, input().split()))

    # graph 초기화
    graph = [[False]*(n+1) for _ in range(n+1)]
    # indegree 초기화
    indegree = [0]*(n+1)
    # 작년도 순위를 기반으로 graph 만들기
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 순위가 바뀐 팀의 관계의 수
    m = int(input())

    # 바뀐 관계 만큼 반복하여 입력 받기
    for i in range(m):
        # 관계가 바뀐 간선 a, b
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        # => 작년에 따라 a,b의 상대 순위가 바뀜! a => b가 아님! 작년과 a,b의 관계가 달라졌다는 뜻 일 뿐!
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # queue 초기화
    q = deque()
    for i in range(1, n+1):
        # 시작점 q에 넣어주기
        if indegree[i] == 0:
            q.append(i)
    # 변수 초기화
    cycle = False
    ambiguous = False
    rank = []
    # 노드의 개수 만큼 반복
    for _ in range(n):
        # q가 비었다? => Cycle이 있다.
        if len(q) == 0:
            cycle = True
            break
        # q가 2개 이상이다? => ambiguity가 있다.
        if len(q) > 1:
            ambiguous = True
            break
        now = q.popleft()
        rank.append(now)
        # now => i를 순회하며 indegree가 0이 되는 값 q에 삽입
        for i in range(1, n+1):
            if graph[now][i]:
                # (1) now가 빠져 나감으로 상대 노드의 indegree 감소
                indegree[i] -= 1
                # (2) indegree가 0이된 노드 q에 삽입
                if indegree[i] == 0:
                    q.append(i)
    # 조건에 따라 출력
    if cycle:
        print('IMPOSSIBLE')
    elif ambiguous:
        print("?")
    else:
        print(*rank)
