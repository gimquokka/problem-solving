'''
- 문제
    리스트(n)의 구간 합을 구하는 쿼리(m) (1, 4), (3, 4)....에 대하여 매번 
    sum(list[a, b+1])를 수행하기 되면 O(N*M)의 시간 복잡도를 가진다. 
    이를 해결하기 위하여 0 ~ n까지의 합을 각각 구해 놓은 Prefix Sum을 계산하여 배열 P에 저장해 놓으면
    O(n + m)의 시간 복잡도로 문제를 해결할 수 있다.

- 전략
    1. N개의 수에 대하여 접두사 합(Prefix Sum)을 계산하여 배열 P에 저장한다.
    2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간 합은 P[R] - P[L-1]이다.
'''

n = 5
data = [1, 2, 3, 2, 1]

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

L = 1
R = 5
print(prefix_sum[R]-prefix_sum[L-1])
