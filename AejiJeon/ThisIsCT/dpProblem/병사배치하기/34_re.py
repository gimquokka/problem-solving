import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.reverse()
dp = [1]*n 

for i in range(1, n):
    
    for j in range(0, i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], 1 + dp[j])

max_length = max(dp)

print(n - max_length)
