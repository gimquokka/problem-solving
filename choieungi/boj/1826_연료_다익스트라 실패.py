#boj_1826
#1km 에 1L 나감
import heapq

n= int(input())
gas_station = []

graph = [[] for i in range(n + 3)]
start = 1
distance = [INF] *(n+3)

#거리 km, 그 주유소에서 채우는 연료 L ,
for i in range(n):
    a,b = map(int,input().split())
    gas_station.append((i+2,a,b))

l, p = map(int,input().split())

for i in range(1,n+3):
    for j in gas_station:
        if p >= j[1]:
            graph[i].append(())





l, p = map(int,input().split())




