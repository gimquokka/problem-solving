def solution(citations):
    citations.sort(reverse=True)
    ans = 0

    for idx, cite in enumerate(citations):
        if (idx+1) <= cite:
            ans = idx+1
    return ans


print(solution([3, 0, 6, 1, 5]))
print(solution([7, 3, 3, 3, 3]))
print(solution([7, 3]))
