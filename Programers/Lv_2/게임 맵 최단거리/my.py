from collections import deque


def solution(maps):
    # size of n, m
    n = len(maps)
    m = len(maps[0])

    # dx, dy for bfs
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # initialize deque
    q = deque()

    # append start point (0, 0)
    q.append([0, 0, 1])
    maps[0][0] = 0  # visited start point

    # bfs code
    while q:
        x, y, dist = q.popleft()

        # search graph 4-way
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 1) (nx, ny) in maps? 2) (nx, ny) is not visited
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # if arrive end point return answer
                if (nx, ny) == (n-1, m-1):
                    return dist+1
                # else append visited print to deque
                q.append([nx, ny, dist+1])
                maps[nx][ny] = 0
    # can not reach the end point? then return -1
    return -1


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))
maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps))
