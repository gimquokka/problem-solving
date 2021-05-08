import sys
input = sys.stdin.readline
INF = int(1e15)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]
members = [0]*(n+1)
for i in range(n):
    members[i+1] = list(map(int, input().split()))

for i in range(m):
    x, y, c = map(int, input().split())
    if c < graph[x][y]:
        graph[x][y], graph[y][x] = c, c
# for i in graph:
#     print(*i)


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


index_graph = [[0]*(n+1) for _ in range(n+1)]
for a in range(1, n+1):
    index_graph[a][0] = (INF, 0)
    for b in range(1, n+1):
        index_graph[a][b] = (graph[a][b], b)
    index_graph[a].sort()  # 아까 부분 파싱했을 때는 왜 정렬안됐을까?

for i in index_graph:
    print(*i)

ans = 0
for i in range(1, n+1):
    # 1, 2, 3 순으로 가까운 것으로 찾아야함
    for j in range(0, n):
        b = index_graph[i][j][1]
        if index_graph[i][j][0] != INF and b != i and b != 0:
            while members[b][0] < members[b][1] and members[i][0] > members[i][1]:
                # print(b)
                # print(index_graph[i][j][0])
                members[b][0] += 1
                members[i][0] -= 1
                ans = max(ans, index_graph[i][j][0])
                # print(i, b)
                # print(ans)

for i in range(1, n+1):
    now, maximum = members[i]
    # print(now, maximum)
    if now > maximum:
        ans = -1

print(ans)
