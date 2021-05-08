"""
문제
N개의 원소 중, data의 인접한 원소를 고르지 않고 얻을 수 있는 최댓값은?

dp[i] = max(dp[i-1], dp[i-2]+data[i])
이전 것과 2개 전과 현재의 값을 더한 수 중 큰 수를 선택

Ex) [1, 3, 1, 5]
=> 3 + 5 = 8
"""
N = int(input())
data = list(map(int, input().split()))

dp = [0]*N
dp[0] = data[0]
dp[1] = max(data[:2])
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+data[i])

print(dp)
