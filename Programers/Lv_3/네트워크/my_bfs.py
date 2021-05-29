from collections import deque


def solution(n, computers):
    ans = 0
    
    visited = [0]*n
    
    for idx, checked in enumerate(visited):
        if not checked:
            ans += 1
            bfs(computers, visited, idx)
        
    return ans

def bfs(computers, visited, start):
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        now = q.popleft()
        for idx, connected in enumerate(computers[now]):
            if idx == now:
                continue
            if connected and not visited[idx]:
                q.append(idx)
                visited[idx] = 1


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # ans = 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # ans = 1