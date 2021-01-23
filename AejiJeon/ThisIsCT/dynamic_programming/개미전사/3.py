import sys
n = int(input())

lst = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0]*n
d[0] = lst[0]
d[1] = max(lst[0], lst[1])

for i in range(2, n):
    d[i] = max(lst[i] + d[i-2], d[i-1])


print(d[n-1])
