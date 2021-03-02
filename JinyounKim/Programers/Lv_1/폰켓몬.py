def solution(nums):
    return len(set(nums)) if len(set(nums)) < len(nums)//2 else len(nums)//2

# Optimal Solution
def solution_opt(nums):
    return min(len(set(nums)), len(nums)//2)
