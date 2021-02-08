n = int(input())

data = list(map(int, input().split()))

right_dp = [0]*n
left_dp = [0]*n


def find_LIS(n, data, dp):
    for axis in range(n):
        for sub in range(axis):
            if data[sub] < data[axis] and dp[sub] > dp[axis]:
                dp[axis] = dp[sub]
        dp[axis] += 1


find_LIS(n, data, left_dp)
data.reverse()
find_LIS(n, data, right_dp)
right_dp.reverse()

ans = 0

for i in range(n):
    ans = max(ans, right_dp[i]+left_dp[i]-1)

# print(right_dp)
# print(left_dp)
print(ans)
