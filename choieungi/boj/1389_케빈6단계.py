#boj_1389

INF = int(1e9)
n,m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] =0


for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1 #친구 관계이면 베이컨 단계 1
    graph[b][a] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

member =[]
for a in range(1, n+1):
    temp =0
    for b in range(1, n+1):
        if graph[a][b] != int(1e9):
            temp += graph[a][b]
        else:
            continue
    member.append(temp)

member_level = min(member)
print(member.index(member_level)+1)