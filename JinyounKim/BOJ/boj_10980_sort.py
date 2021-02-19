import sys
input = sys.stdin.readline

n = int(input())

ans = [0]*(10001)

for i in range(n):
    ans[int(input())] += 1

for i in range(10001):
    for j in range(ans[i]):
        print(i)
