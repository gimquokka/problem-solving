# 283.91ms, 117MB
import math


def solution(n):
    num = set(range(2, n+1))

    for i in range(2, int(n**0.5)+1):
        if i in num:
            num -= set(range(i*i, n+1, i))
    # 소수의 개수 반환
    return len(num)


# 280.90ms, 17.4MB


def solution1(n):
    d = [True for i in range(n+1)]  # 모든 수 소수로 초기화
    d[0], d[1] = False, False  # 0과 1은 소수가 아님으로

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n))+1):  # x의 제곱근까지만 판별하면 됨
        if d[i] == True:  # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i*j <= n:
                d[i*j] = False
                j += 1
    # 소수의 개수 반환
    return d.count(True)
