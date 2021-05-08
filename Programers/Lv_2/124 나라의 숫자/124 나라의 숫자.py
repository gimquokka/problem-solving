def solution(n):
    recursion(int(n))


def recursion(n):
    if (n == 0):
        return ""

    if (n % 3 == 0):
        return recursion(int(n/3) - 1) + "4"
    elif (n % 3 == 1):
        return recursion(int(n/3)) + "1"
    else:
        return recursion(int(n/3)) + "2"


print(solution(4))

# 더욱 간결한 코드


def change124(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return change124(q) + '124'[r]
