from itertools import combinations

def solution(numbers):
    tmp = set(a+b for a, b in combinations(numbers, 2))
    answer = list(tmp)
    answer.sort()
    return answer
