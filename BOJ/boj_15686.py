from itertools import combinations

n, m = map(int, input().split())

homes = []
stores = []
for r in range(n):
    row = list(map(int, input().split()))
    for c, _type in enumerate(row):
        if _type == 1:
            homes.append((r, c))
        elif _type == 2:
            stores.append((r,c))

ans = int(1e9)
for selected_store in combinations(stores, m):
    grobal_min = 0
    for hx, hy in homes:
        min_dist = 100
        for cx, cy in selected_store:
            new_dist = abs(hx-cx) + abs(hy-cy)
            min_dist = min(new_dist, min_dist)
        grobal_min += min_dist
    ans = min(grobal_min, ans)

print(ans)