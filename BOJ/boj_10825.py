import sys
input = sys.stdin.readline

n = int(input())

info = [[] for _ in range(n)]
for i in range(n):
    info[i] = input().split()

info.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for row in info:
    print(row[0])
