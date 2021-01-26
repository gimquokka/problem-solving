n, k = map(int, input().split())

graph = []
data = []  # (virus number, time, x, y)
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append(graph[i][j], 0, i, j)

_s, _x, _y = map(int, input().split())

da = [1,-1,0, 0]
db = [0,0,1,-1]

q = data[:] # 큐


for i in range(1, s+1):
    
while q:
    virus, time, x, y = q.pop(0)
    if time == s:
        break
    for i in range(4):
        na = a + da[i]
        nb = b + db[i]

        if na >= 0 and na <= n-1 and nb >= 0 and nb <= n-1 and graph[na][nb] == 0:
            q.append((virus, time+1, na, nb))
            graph[na][nb] = virus  

print(graph[x-1][y-1])


            
