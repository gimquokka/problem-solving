t = int(input())
dx = [0, -1, 1]
dy = [1, 1, 1]

for i in range(t):
    
    n, m = map(int, input().split())
    array = []
    data = list(map(int, input().split()))
    for i in range(0,n*m,m):
        array.append(data[i:i+m])
    
    max_result = [[0]*m for _ in range(n)]
    for y in range(m-1):
        for x in range(n):
            for i in range(3):
                if i == 0:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                        max_result[nx][ny] = max(max_result[nx][ny],array[x][y]+ array[nx][ny])
                else:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                        max_result[nx][ny] = max(max_result[nx][ny],array[x][y]+ array[x][y+1] + array[nx][ny])
        for x in range(n):
            array[x][y+1] = max_result[x][y+1]
    result = -1e9
    for x in range(n):
        result = max(result, array[x][m-1])
    print(result)

