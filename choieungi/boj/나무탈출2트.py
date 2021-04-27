n=int(input())

visited = [False]* (n+1)
graph = [[] for _ in range(n+1)]
elements = []

for i in range(n-1):
    a,b = map(int,input().split())
    if a>b:
        a,b = b,a
    graph[a].append(b)
    graph[b].append(a)

print(graph)

def dfs(visited,v,graph):
    visited[v] = True
    elements.append(v)
    if not graph[v]:
        print(elements)
        elements.remove(v)
        v = elements[-1]

    for i in graph[v]:
        if visited[i] == False:
            visited[i] =True
            dfs(visited,i,graph)


dfs(visited,1,graph)