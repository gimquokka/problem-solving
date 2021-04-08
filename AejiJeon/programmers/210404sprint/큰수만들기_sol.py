from collections import deque


def solution(number, k):
    left = list(number[:1])
    right = deque(list(number[1:]))
    while right and k > 0:
        # 6 5 5 4 1 7(increasing number 발견)
        if left and left[-1] < right[0]:
            # 1 제거
            left.pop()
            k = k - 1
        else:
            left.append(right.popleft())
    result = list(map(str, left + list(right)))
    
    # k 개 제거하기 전에 내림차순으로 만들어진 경우
    # -> 맨 뒤에서 k 개 숫자를 제거
    if k > 0:
        result = result[: len(result) - k]

    return "".join(result)


print(solution("4177252841", 4))
print(solution("7777", 3))