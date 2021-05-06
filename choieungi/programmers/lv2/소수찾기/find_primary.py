from itertools import permutations

def check_primary(n):
    if n == 0 or n == 1: return 0
    temp = 2
    while temp < n / 2 + 1:
        if (n % temp == 0): return 0
        temp += 1
    return 1


def solution(numbers):
    answer = 0
    nums = []
    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        for j in list(permutations(numbers, i)):
            nums.append(int("".join(j)))

    nums = set(nums)
    for i in nums:
        answer += check_primary(i)
    return answer