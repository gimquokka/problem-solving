def solution(n):
    str_n = str(n)
    list_n = sorted(str_n, reverse=True)
    return int(''.join(list_n))

# print(solution(112415))