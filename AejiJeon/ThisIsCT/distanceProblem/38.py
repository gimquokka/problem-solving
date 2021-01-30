n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1): # a -> k -> b 존재시 a -> b edge 추가, 중간 경로로 k vertex 사용
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

count = 0
for i in range(1, n+1):
    know_rank = True
    for j in range(1, n+1):
        if i == j:
            continue
        if graph[i][j] + graph[j][i] != 1:
            know_rank = False
            break
    if know_rank:
        count += 1

print(count)
        
