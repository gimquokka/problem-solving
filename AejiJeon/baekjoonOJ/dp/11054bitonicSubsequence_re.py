# 시간 초과.. ㅠㅠㅠㅠㅠㅠ
import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

# sequence[:i+1] 에서 i를 마지막 원소로 하는 
# 증가하는 부분수열의 최대 길이 담는 array 
left_seq = [1]*n
# sequence[i:] 에서 i를 처음 원소로 하는 
# 감소하는 부분수열의 최대 길이 담는 array
right_seq = [1]*n

result = 0

# update left_seq 
for i in range(n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            left_seq[i] = max(left_seq[j]+1, left_seq[i])

# update right_seq
# 감소하는 부분수열 -> reversed sequence에서 
# 증가하는 부분 수열 찾는 방법으로 바꿔서 풀기 위해
# update right_seq with decreased order of index 
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if sequence[j] < sequence[i]:
            right_seq[i] = max(right_seq[j]+1, right_seq[i])

result = 0

for i in range(n):
    result = max(result, left_seq[i] + right_seq[i])

# result는 Sk 원소가 2번 더해진 상태
print(result - 1)
