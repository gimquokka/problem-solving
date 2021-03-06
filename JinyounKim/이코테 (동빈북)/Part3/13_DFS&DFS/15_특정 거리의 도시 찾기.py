from collections import deque

# 첫 줄 입력 받기
n, m, k, start = map(int, input().split())

# m개의 단방향 간선 입력 받기
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 방문 그래프 초기화
visted = [False]*(n+1)
# BFS를 위한 Queue 선언
q = deque()

# BFS에 쓰일 변수 값 선언
ans = []
q.append((start, 0))
visted[start] = True
# BFS 수행
while q:
    now, cost = q.popleft()
    for node in graph[now]:
        if not visted[node]:
            q.append((node, cost+1))
            visted[node] = True
            # 거리가 k인 node를 찾았다면 ans에 담기
            if cost + 1 == k:
                ans.append(node)
            # 거리가 k인 부분을 지나쳤다면 While문 종료
            # 왜냐면 BFS의 경우 거리가 가까운 곳부터 먼 곳 까지 순차로 탐색하기 때문에 k를 지나쳤다면,
            # 더 이상 거리가 k인 곳은 없다는 뜻 임으로
            elif cost+1 > k:
                break
# ans를 순차로 정렬. BFS는 순서를 보장하지 않음으로
ans.sort()
# 거리가 k인 노드가 없는 경우
if len(ans) == 0:
    print(-1)
# 거리가 k인 노드가 있는 경우
else:
    for i in ans:
        print(i)
