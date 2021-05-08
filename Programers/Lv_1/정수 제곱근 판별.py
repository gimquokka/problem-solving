def solution(n):
    # print(n**.5)
    return -1 if (n**.5)%1 != 0 else int((n**.5+1)**2)


print(solution(121))