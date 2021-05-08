import sys
input = sys.stdin.readline 

n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    upper_left, upper_right = 0, 0
    for j in range(i+1):
        if j != 0:
            upper_left = dp[i-1][j-1]
        if j != i:
            upper_right = dp[i-1][j]
        dp[i][j] += max(upper_left, upper_right)

result = max(dp[-1])
print(result)
