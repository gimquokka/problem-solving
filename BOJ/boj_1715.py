import sys
import heapq
input = sys.stdin.readline

n = int(input())

hq = []
for i in range(n):
    heapq.heappush(hq, int(input()))
    

ans = 0
for i in range(1, n):
    temp = heapq.heappop(hq) + heapq.heappop(hq)
    ans += temp
    heapq.heappush(hq, temp)
    
print(ans)
