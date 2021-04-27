n=int(input())

graph = [[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


depth = [0]*(n+1)
def dfs(graph,v,depth,visited):
    discovered= []
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v] :
            visited[v] = True
            for w in graph[v]:
                stack.append(w)
                depth[w] = depth[v] +1

dfs(graph,1,depth,visited)

ans=0
for i in range(2,n+1):
    if len(graph[i])==1:
        ans+=depth[i]
#print(ans)
if ans%2 ==0:
    print("No")
else:
    print("Yes")
