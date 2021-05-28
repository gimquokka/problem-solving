from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    q = deque()
    
    q.append([0,0,1])
    maps[0][0] = 0
    
    while q:
        x,y, dist = q.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if (nx,ny) == (n-1, m-1):
                    return dist+1
                q.append([nx,ny, dist+1])
                maps[nx][ny] = 0
    
    return -1


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))