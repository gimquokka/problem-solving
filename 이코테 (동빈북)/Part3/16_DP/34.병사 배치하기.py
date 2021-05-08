n = int(input())

# 입력값 받기
data = list(map(int, input().split()))

# dp table 초기화
dp = [1]*n
# LIS => LDS로 변환
for i in range(1, n):
    for j in range(i):
        if data[j] > data[i]:
            dp[i] = max(dp[i], dp[j]+1, dp[i-1])

# print(dp)
print(n-dp[n-1])
