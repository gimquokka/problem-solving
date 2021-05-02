# 0: 빈칸
# 1: 벽
# 2: 보물상자
# 3: 소마 위치
# 4: 열쇠위치
from collections import deque;
def bfs(graph, start, end):
    n = len(graph)
    m = len(graph[0])
    visited = [[False]*m for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 1 and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    if (nx, ny) == end:
                        return True
    return False

                

def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        """
        presure
        key
        swm
        """
        graph =[]
        for i in range(n):
            row = list(map(int, input().split()))
            graph.append(row)
            if 2 in row:
                presure = (i, row.index(2))
            if 3 in row:
                swm = (i, row.index(3))
            if 4 in row:
                key = (i, row.index(4))
        if bfs(graph, swm, key) and bfs(graph, key, presure):
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
