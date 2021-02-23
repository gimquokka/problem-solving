def solution(a, b):
    answer = 0
    # 이렇게 Swap하는 것도 괜춘
    # if a > b: a, b = b, a
    for i in range(min(a, b), max(a, b)+1):
        answer += i
    return answer
