def solution(n, times):
    
    left, right = 1, max(times)*n

    while left < right:
        total = 0
        mid = (left+right)//2

        for t in times:
            total += mid // t

        if total >= n:
            right = mid
        else:
            left = mid+1
    # print(left, right)
    
    return left


print(solution(2130, [7, 10]))

# ref: https://bit.ly/3pvyFad