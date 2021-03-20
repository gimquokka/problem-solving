from collections import deque

n, l, r = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n*n):
    q = deque()
    