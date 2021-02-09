# 시간 초과
# knapsack algorithm
import sys


input = sys.stdin.readline

N, W = map(int, input().split())

# 1~N items에 대한 무게, 가치 담는 arrays
weights = [0] * (N + 1)
values = [0] * (N + 1)

for i in range(1, N + 1):
    weights[i], values[i] = map(int, input().split())


dp = [[0] * (N + 1) for _ in range(W + 1)]

for i in range(1, N + 1):
    for w in range(1, W + 1):
        # dp[w][i]는 1~i items로 w만큼의 무게를 채우는 경우 가치의 최댓값
        # i 번째 item을 넣을 수 없는 경우
        if w < weights[i]:
            dp[w][i] = dp[w][i - 1]
        # i 번째 item을 넣을 수 있는 경우
        else:
            dp[w][i] = max(dp[w - weights[i]][i - 1] + values[i], dp[w][i - 1])

print(dp[W][N])
