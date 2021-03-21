def solution(num):
    if num == 1:
        return 0
    for i in range(1, 501):
        if num % 2 == 0:
            num //= 2
            if num == 1:
                return i
        else:
            num = 3*num + 1
    return -1


print(solution(1))
print(solution(16))
print(solution(626331))
