n, k = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    data = list(map(int, input().split()))
    for j in range(1, n+1):
        graph[i][j] = data[j-1]
s, x, y = map(int, input().split())

da = [1,-1,0, 0]
db = [0,0,1,-1]

q = [] # 큐
for w in range(1,k+1):

    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == w:
                q.append((i,j)) 
next_q = []

for i in range(1, s+1):
    
    while q:
        a, b = q.pop(0)
        
        for i in range(3):
            na = a + da[i]
            nb = b + db[i]

            if na >= 1 and na <= n and nb >= 1 and nb <= n and graph[na][nb] == 0:
                next_q.append((na,nb))
                graph[na][nb] = graph[a][b]  
    q = next_q[:]
    next_q = []
print(graph[x][y])


            
