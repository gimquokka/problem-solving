"""
### 문제 ###
입력 값 양의 정수 N에 대하여 -1, //5, //3, //2의 연산을 할 수 있을 때,
가장 적은 연산을 활용하여 1을 만들 수 있는 횟수를 구하시오.

dp[i] = max(dp[i//2], dp[i//3], dp[i//5], dp[i-1])+1

Ex) 26 => 26 -1 => 25//5 => 5//5 => 1
ans: 3
"""
N = int(input())


def solve(N):
    dp = [0]*(N+1)
    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i//5]+1)
    print(dp)
    return dp[N]


solve(N)
