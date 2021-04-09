from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            # 모든 order에 대해 c 개의 음식 조합을 모두 담아줌
            temp += combinations(sorted(order), c)

        # 각 음식 조합에 대해 중복된 개수 찾음
        counter = Counter(temp)
        print(counter)
        # 각 음식 조합에 포함된 음식 개수가 2개 이상인 경우
        if len(counter) != 0 and max(counter.values()) != 1:
            # maximum 개수에 해당되는 음식 조합을 담아줌
            answer += [
                "".join(alphabets)
                for alphabets in counter
                if counter[alphabets] == max(counter.values())
            ]

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))