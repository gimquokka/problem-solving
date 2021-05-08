from itertools import combinations


def prime(n):
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    cnt = 0
    for choosed in combinations(nums, 3):
        if prime(sum(choosed)):
            cnt +