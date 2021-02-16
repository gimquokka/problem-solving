import sys
input = sys.stdin.readline

N = int(input())

data = []
for i in range(N):
    data.append(tuple(map(int, input().split())))
data.sort()

for x, y in data:
    print(x, y)
