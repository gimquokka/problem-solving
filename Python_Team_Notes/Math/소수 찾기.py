"""
# 전략
- 2 ~ root(x)까지만 확인하면 소수인지 수학적으로 판별 가능
    - 왜냐면 약수는 제곱근을 중심으로 대층성을 띄고 있음 16 =>1, 2, 4(=mid), 8, 16

# Time Complexity
- O(x^(1/2))
"""

import math


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# 테스트
print(is_prime_number(11))
