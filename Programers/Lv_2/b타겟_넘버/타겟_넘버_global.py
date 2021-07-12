def solution(numbers, target):
    global ans, arr, num
    
    arr = numbers
    num =  target
    ans = 0
    
    dfs(0, 0)
    return ans


def dfs(_sum, idx):
    global ans, arr, num
    
    if idx == len(arr):
        if _sum == num:
            ans += 1
        return
    
    dfs(_sum + arr[idx], idx+1)
    dfs(_sum - arr[idx], idx+1)

print(solution([1, 1, 1, 1, 1], 3))
