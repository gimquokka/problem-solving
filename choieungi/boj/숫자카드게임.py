# 숫자 카드 게임
import sys

n,m=map(int,input().split())

nums = []

for i in range(n):
    a =  list(map(int,input().split()))
    nums.append(a)
    nums[i].sort()

max = nums[0][0]
for i in range(n-1):
    if nums[i][0]<nums[i+1][0]:
        max = nums[i+1][0]

print(max)



