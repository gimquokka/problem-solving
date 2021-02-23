"""
# 전략
- 모두 소수로 초기화 후
- 2 ~ int(math.sqrt(x))+1까지 돌면서 x까지의 모든 배수를 False로 바꿔주면 됨

# Time Complexity
O(NloglogN)

# 주의 사항
- x 값이 클 경우 메모리를 많이 차지 함으로 주의!
""" 
import math

n = 1000 # 2 부터 1000까지의 모든 수에 대하여 소수 판별
d = [True for i in range(n+1)] # 모든 수 소수로 초기화
d[0], d[1] = False, False # 1은 소수가 아님으로

# 에라토스테네스의 체 알고리즘 
for i in range(2, int(math.sqrt(n))+1): # x의 제곱근까지만 판별하면 됨
    if d[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i*j <= n:
            d[i*j] = False
            j += 1
# 소수의 개수 반환
print(d.count(True))

"""
# 간결한 구현 (하지만 메모리 위에 것에 비하여 10배 정도 많이 차지함)
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,int(n**0.5)+1):
        if i in num:
            num-=set(range(i*i,n+1,i))
    # 소수의 개수 반환
    return len(num)
"""