def solution(numbers, target):
    global ans, arr, num
    
    # arr = numbers
    # num =  target 
    ans = 0
    
    dfs(numbers, target, 0, 0)
    return ans


def dfs(numbers, target, _sum, idx):
    global ans, arr, num
    
    if idx == len(numbers):
        if _sum == target:
            ans += 1
        return
    
    # print(idx)
    
    dfs(numbers, target, _sum + numbers[idx], idx+1)
    dfs(numbers, target, _sum - numbers[idx], idx+1)

print(solution([1, 1, 1, 1, 1], 3))
