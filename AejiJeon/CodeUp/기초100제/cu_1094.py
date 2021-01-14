# print numbers in decreasing order

n = int(input())

nums = input().split()

for i in range(1, n+1):
    print(nums[-i], end = ' ')

# with reverse()
"""
a = input()
nums = map(int, input().split())
nums.reverse()

print(nums)
"""