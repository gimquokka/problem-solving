from collections import deque

def topology_sort(graph, indegree):
    q = deque()
    result = []

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    
    for i in range(n):
        if len(q) == 0:
            return "IMPOSSIBLE"
        if len(q) != 1:
            return "?"
        
        now = q.popleft()
        result.append(now)

        for node in graph[now]:
            indegree[node] -= 1
            
            if indegree[node] == 0:
                q.append(node)
    
    ans_str = ''
    for c in result:
        ans_str += str(c) + " "

    return ans_str
                
        
for tc in range(int(input())):
    n = int(input())
    rank = list(map(int, input().split()))
    
    graph = [[] for _ in range(n+1)]
    for j in range(n):
        for k in range(j+1, n):
            graph[rank[j]].append(rank[k])
    
    indegree = [0]*(n+1)
    for j in range(n):
        indegree[rank[j]] = j

    # 이 부분에서 햇갈림.
    # 항상 a => b 순서로 바뀌었다는게 아니라, 기존의 a <=> b의 관계가 바뀌었다는것
    # 따라서 a => b, b => a인 경우 각각 고려하여 처리해줘야함
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            graph[b].append(a)
            graph[a].remove(b)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a].append(b)
            graph[b].remove(a)
            indegree[a] -= 1
            indegree[b] += 1
        
    
    print(topology_sort(graph, indegree))