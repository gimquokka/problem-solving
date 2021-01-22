from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

pre_courses = [[] for _ in range(n+1)]

times = [0]*(n+1)
indegrees = [0]*(n+1)

for i in range(1, n+1):
    l = list(map(int, input().split()))
    times[i] = l[0]
    for x in l[1:-1]:
        indegrees[i] += 1       # i의 indegree 값 증가
        pre_courses[x].append(i)  # 선수 강의들로부터의 edge 더해줌 순서 중요!


result = times[:]

def topological_cal():
    queue = deque()
    for i in range(1, n+1):
        if indegrees[i] == 0:
            queue.append(i)
    
    while queue:
        now = queue.popleft()

        for i in pre_courses[now]:
            
            result[i] = max(result[i], result[now] + times[i])
           
            indegrees[i] -= 1
            if indegrees[i] == 0:
                queue.append(i)

topological_cal()

for i in range(1, n+1):
    print(result[i])


