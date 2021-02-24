from itertools import combinations

# 입력 받기
n, m = map(int, input().split())
data = list(input().split())

vowels = ['a', 'e', 'i', 'o', 'u']
# input에서 모음들만
v = [i for i in vowels if i in data]
# "" 자음들만
c = [i for i in data if i not in vowels]

ans = []
"""
# v, c 각각의 개수 경우의 수
    1. 1 < v < min(len(v), m - 2)
    2. 2 < c < n - v
"""
# 모음 개수의 범위
for i in range(1, min(len(v), n-2)+1):
    # list로 받아야 아래 in으로 걸었을 때 제대로 돌아감 (왜지?)
    v_list = list(combinations(v, i))
    c_list = list(combinations(c, n-i))  # n - 모음 = 자음
    # v_list = combinations(v, i) # 동작 X
    # c_list = combinations(c, n-i)
    for b in v_list:
        for a in c_list:
            alpha = ''.join(sorted(a+b))
            ans.append(alpha)

ans.sort()
for i in ans:
    print(i)
