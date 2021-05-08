"""
문제
화폐의 개수: n, 금액: m, 화폐: n개가 주어졌을 때
가장 적은 화폐를 활용하여 금액 m을 만들 수 있는 경우의 수, 만들수 없으면 -1

# dp[i]가 INF일 경우는 계산x
점화식: dp[i] = min(dp[i-coin], dp[i])

Ex) 
1, 5
5

Ans: 1
"""
N, M = map(int, input().split())

INF = int(1e5)
data = [INF]*N
for i in range(N):
    data[i] = int(input())

dp = [INF]*int(1e4)
dp[0] = 0
# dp[0] = 0으로 초기화 하고 2를 돌리면, 초기화 필요없다.
# Optmal
for i in range(N):
    for j in range(data[i], M+1):
        if dp[j-data[i]] != INF:
            dp[j] = min(dp[j], dp[j-data[i]]+1)
