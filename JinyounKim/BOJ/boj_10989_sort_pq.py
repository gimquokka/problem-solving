import heapq

import sys
input = sys.stdin.readline

n = int(input())

q = []
for i in range(n):
    heapq.heappush(q, int(input()))

while q:
    print(heapq.heappop(q))

