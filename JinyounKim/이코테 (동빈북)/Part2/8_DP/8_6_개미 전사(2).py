N = int(input())
data = list(map(int, input().split()))

dp = [0]*N
dp[0] = data[0]
dp[1] = max(data[:2])
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+data[i])

print(dp)
