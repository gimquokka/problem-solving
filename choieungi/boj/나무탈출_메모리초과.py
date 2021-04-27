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


stacks=[]
def dfs(visited,v,graph):
    global stacks
    visited[v] = True
    elements.append(v)

    for i in graph[v]:
        if visited[i] == False:
            visited[i] =True
            dfs(visited,i,graph)

    stacks.append(elements[:])
    elements.pop()

dfs(visited,1,graph)

#print(graph)
ans=0
for i,j in enumerate(graph):
    for k in stacks:
        if len(j) ==1 and k[-1]==i and i!=1:
            print(k)
            ans += (len(k)-1)

#print(graph)
#print(stacks)
#print(ans)
if ans%2 ==0:
    print("NO")
else:
    print("Yes")
