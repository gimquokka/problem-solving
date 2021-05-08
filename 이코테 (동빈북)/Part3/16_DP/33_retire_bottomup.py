'''
import sys 
input = sys.stdin.readline

n = int(input())

t = [0]*(n+1)
p = [0]*(n+1)
dp = [0]*(n+1)
max_val = 0

for i in range(n+1):
    t[i], p[i] = map(int, input().split())
    times = i+t[i]
    
    if times <= n:
        dp[times] = max(max_val, dp[i]+p[i])
        max_val = dp[times]

    dp[i] = max(dp[i], dp[i+1])
'''
n = int(input())
d = [0]*(n+15)
for i in range(1,n+1):
    t,p = map(int,input().split())
    d[i] = max(d[i],d[i-1])
    d[i+t] = max(d[i+t],d[i]+p)
# print(max(d[:n+2]))
print(d)