# 라이브러리 스펠링 외워두어야함(마지막에 다 's' 붙음)
from itertools import combinations, permutations

data = [1, 2, 3, 4]

# 순열 (Permutations)
for i in permutations(data, 2):
    print(i)

# 조합 (Combinations)
for i in combinations(data, 2):
    print(i)

ans = sum(sum(combinations(data, 2)))
