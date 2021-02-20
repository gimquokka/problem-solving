from itertools import combinations

def solution(numbers):
    # 조합을 이용하여 2개 추출하고 집합으로 중복 제거
    tmp = set(a+b for a, b in combinations(numbers, 2))
    # Set => List
    answer = list(tmp)
    answer.sort()
    return answer