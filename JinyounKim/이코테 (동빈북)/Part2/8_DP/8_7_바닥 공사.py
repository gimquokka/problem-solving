"""
서로 다른 1, 2, 2의 타일을 이용해서
N길이의 바닥을 채울수 있는 모든 경우의 수를 구하시오.

a_n+2 = a_n-1 + 2*a_n-2
"""

N = int(input())

dp = [0]*(N+1)
dp[0], dp[1] = 1, 1
for i in range(2, N+1):
    dp[i] = dp[i-1]+2*dp[i-2]

print(dp)
