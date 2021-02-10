'''
Prob: 
FindLongest Bitonic sequence length

Ex)
10
1 5 2 1 4 3 4 5 2 1
=> 7
'''
n = int(input())

data = list(map(int, input().split()))

right_dp = [0]*n
left_dp = [0]*n

# Function find_Longest Common Sequence
def find_LIS(n, data, dp):
    for axis in range(n):
        for sub in range(axis):
            if data[sub] < data[axis] and dp[sub] > dp[axis]:
                dp[axis] = dp[sub]
        dp[axis] += 1

# Find Left_Hand LIS
find_LIS(n, data, left_dp)

# Find Right-Hand LIS
data.reverse()
find_LIS(n, data, right_dp)
right_dp.reverse()

# Find Max LIS for both of them
ans = 0
for i in range(n):
    ans = max(ans, right_dp[i]+left_dp[i]-1)

# Get answer
print(ans-1)