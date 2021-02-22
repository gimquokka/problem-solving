N, M = map(int, input().split())

INF = int(1e5)
data = [INF]*N
for i in range(N):
    data[i] = int(input())

dp = [INF]*int(1e4)
dp[0] = 0
# dp[0] = 0으로 초기화 하고 2를 돌리면, 초기화 필요없다.
'''
for coin in data:
    dp[coin] = 1
'''
# 2
for i in range(1, M+1):
    for coin in data:
        if 0 <= i-coin and dp[i-coin] != INF:
            dp[i] = min(dp[i], dp[i-coin]+1)
# Optmal
for i in range(N):
    for j in range(data[i], M+1):
        if dp[j-data[i]] != INF:
            dp[j] = min(dp[j], dp[j-data[i]]+1)
