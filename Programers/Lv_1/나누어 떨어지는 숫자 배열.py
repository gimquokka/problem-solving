def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    if not answer:
        answer = [-1]
    return answer


def solution_opt(arr, divisor):
    # 앞의 것이 참이면 앞을, 거짓이면 후자를 반환
    return sorted([n for n in arr if n % divisor == 0]) or [-1]
