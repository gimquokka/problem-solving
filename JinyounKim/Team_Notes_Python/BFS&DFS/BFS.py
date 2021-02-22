from collections import deque


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    # 1. 기본코드
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    # 2. 거리별로 확인하기
    dist = 0
    while q:
        dist += 1
        # 이런식으로 while문 안에 for문을 걸어주면 dist별로 client를 확인할 수 있음
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < N and 0 <= ny < N and (visited[nx][ny] == False) and B[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    if B[nx][ny] == -1:
                        heapq.heappush(client_pq, (nx, ny, dist))
