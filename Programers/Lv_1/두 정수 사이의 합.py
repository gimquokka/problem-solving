# 이렇게 Swap하는 것도 괜춘
# if a > b: a, b = b, a
def solution(a, b):
    return sum(i for i in range(min(a, b), max(a, b)+1))
