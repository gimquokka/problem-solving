from math import gcd

def solution(n, m):
    for i in range(max(n, m), n*m+1):
        if i%n == 0 and i%m == 0:
            lcm = i
            break

    return [gcd(n,m), lcm]


print(solution(3, 12))
print(solution(2, 5))