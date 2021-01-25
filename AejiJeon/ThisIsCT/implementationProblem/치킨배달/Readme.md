# 몰랐던 python 기능
from itertools import permutations/combinations

permutations(n_list, r)

combinations(n_list, r) : iteration가능한 객체 담고있는 contationer return
list로 사용하고 싶을 시 반드시 list(combinations(n_list,r))
r = 1인 경우는 주의(permutations, combinations 둘 다)
'''
from itertools import combinations
a = [1,2,3]
print(list(combinations(a,1))) #[(1,),(2,),(3,)] printed
'''

