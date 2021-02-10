# 시간 초과.. ㅠㅠㅠㅠㅠㅠ
import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

# return length of LIS which doesn't 
# contain number more than max_i(Sk)
def LIS_length(sequence, max_i):
    m = len(sequence)

    if m == 0:
        return 0
    # 이전에 계산된 값들 저장하는 dp table
    # d[k]는 k 번째 원소를 마지막 원소로 하는 LIS length를 의미
    dp = [0] * m

    for i in range(m):
        # consider numbers smaller than max_i
        if sequence[i] < max_i:
            dp[i] = 1

    for i in range(m):
        if sequence[i] >= max_i:
            continue
        for j in range(i):
            if sequence[j] >= max_i:
                continue
            if sequence[j] < sequence[i]:
                # i를 포함하는 증가하는 부분 수열들의 
                # 길이의 최댓값을 구함
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)


result = 0
# i 번째 원소를 Sk로 놓고 
for i in range(n):
    
    # i의 왼쪽 부분은 i 번째 원소보다 작으면서 
    # 증가하는 부분 수열의 최대 길이,
     left_seq = sequence[:i]

     # i의 왼쪽 부분은 i 번째 원소보다 작으면서 
     # 감소하는 부분 수열의 최대 길이를 구하기 위해 사용됨
    right_seq = sequence[i + 1 :]

    right_seq.reverse()
    # 왼쪽 부분 수열의 max length + 1(i 번째 원소) + 오른쪽 부분 수열의 max length
    result = max(result, LIS_length(left_seq, i) + 1 + LIS_length(right_seq, i))

print(result)
