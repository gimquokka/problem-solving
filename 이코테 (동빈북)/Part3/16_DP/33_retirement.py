import sys 
input = sys.stdin.readline 

n = int(input())

t = [0]*n
p = [0]*n
for i in range(n):
    a, b = map(int, input().split())
    t[i] = a
    p[i] = b

dp = [0]*(n+1)
max_val = 0
for i in range(n-1, -1, -1):
    times = t[i]+i
    if times <= n:
        dp[i] = max(max_val, p[i]+dp[times])
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max_val)