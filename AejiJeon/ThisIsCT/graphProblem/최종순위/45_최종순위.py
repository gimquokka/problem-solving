from collections import deque
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    
    # rank of teams
    data = list(map(int, input().split()))

    indegrees = [0]*(n+1)

    # add edges from team of rank i 
    # to teams of rank i+1, i+2, ..., n-1 
    # (rank is from 0 to n-1)  
    for i in range(n-1):
        for j in range(i+1, n):
            a = data[i]
            b = data[j]
            graph[a].append(b)
            
            # counts the number of indegree edges of team b 
            indegrees[b] += 1
    
    m = int(input())
    checking = True
    for _ in range(m):
        a, b = map(int, input().split())

        # rank is not changed
        if a not in graph[b]:
            checking = False
            continue
        # change the direction of edge from team b to team a
        graph[b].remove(a)
        indegrees[a] -= 1
        graph[a].append(b)
        indegrees[b] += 1
    if not checking:
        print("IMPOSSIBLE")
        continue
    result = []
    queue = deque()

    for i in range(1, n+1):
        if indegrees[i] == 0:
            queue.append(i)
    finishedWell = "yes"
    while queue:
        # there are at least 2 teams
        # without indegree edge
        # can't decide rank
        if len(queue) != 1:
            finishedWell = "no"
            break
        now = queue.popleft()
        result.append(now)
        for adj in graph[now]:
            indegrees[adj] -= 1
            if indegrees[adj] == 0:
                queue.append(adj)

    
    if finishedWell == "no":
        print("?")
    elif len(result) == n:
        print(*result)
    # while loop finished without break 
    # but no topological order
    else:
        print("IMPOSSIBLE")




    
