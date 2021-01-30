n = int(input())
p = [0]
t = [0]
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

dp = [0]*(n+2)
max_v = 0
for i in range(n,0,-1):
    time = i + t[i]
    if time <= n+1:
        dp[i] = max(p[i]+dp[time], max_v)
        if max_v != dp[i]:
            max_v = dp[i]
        
    else:
        dp[i] = max_v
    
print(max_v)