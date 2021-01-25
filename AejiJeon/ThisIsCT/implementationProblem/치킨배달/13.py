from itertools import combinations
n, m = map(int, input().split())

chicken = []  
home = []
for i in range(n):
    lst = list(map(int,input().split()))
    for j in range(n):
        if lst[j] == 1:
            home.append((i,j))
        elif lst[j] == 2:
            chicken.append((i,j))



print(comb_lst)
def min_sum(chickens):
    sum = 0
    for hx,hy in home:
        min_d = 1e9
        for cx,cy in chickens:
            min_d = min(min_d, abs(cx-hx)+abs(cy-hy))
        sum += min_d
    return sum
result = 1e9
for chickens in comb_lst:
    result = min(result, min_sum(chickens))

print(result)

