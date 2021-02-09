import heapq
import sys
input = sys.stdin.readline

n = int(input())

gs_info = []
for i in range(n):
    heapq.heappush(gs_info, list(map(int, input().split())))
goal, fuel = map(int, input().split())

plan = []
cnt = 0
while fuel < goal:
    while gs_info and gs_info[0][0] <= fuel:
        d, f = heapq.heappop(gs_info)
        heapq.heappush(plan, (-f, d))

    if not plan:
        cnt = -1
        break

    added_fuel = -heapq.heappop(plan)[0]
    fuel += added_fuel
    cnt += 1

print(cnt)
