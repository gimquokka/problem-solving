import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
'''
# Value asignment part
data = [[0]*n for _ in range(n)]
for i in range(n):
    data[i] = list(map(int, input().split()))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            home.append((i,j))
        elif data[i][j] == 2:
            chicken.append((i,j))
'''
# simplify asignment
home, chicken = [], []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            home.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

# Assgin combinations at list
m_chicken = [i for i in list(combinations(chicken, m))]
"""
def find_shorest(homes, m_chicken):
    result = int(1e8)
    for chickens in m_chicken:
        new_result = 0 # 모든 조합의 경우의 수 마다 new_result를 초기화 시켜줘야함
        for home in homes:
            min_dist = int(1e8) # 집별로 치킨집들과의 최소거리 임으로 집마다 최소화를 시켜줘야함
            for chicken in chickens:
                dist = abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])
                min_dist = min(min_dist, dist)
            new_result += min_dist # 경우의 수 마다의 집들과 치킨집과의 최솟값
        result = min(result, new_result)
    return result
"""
# Make find_shorest more intuitivly


def find_shorest(homes, m_chicken):
    result = int(1e8)
    for chickens in m_chicken:
        new_result = 0  # 모든 조합의 경우의 수 마다 new_result를 초기화 시켜줘야함
        for hx, hy in homes:
            min_dist = int(1e8)  # 집별로 치킨집들과의 최소거리 임으로 집마다 최소화를 시켜줘야함
            for cx, cy in chickens:
                print(cx, cy)
                dist = abs(hx-cx) + abs(hy-cy)
                min_dist = min(min_dist, dist)
            new_result += min_dist  # 경우의 수 마다의 집들과 치킨집과의 최솟값
        result = min(result, new_result)
    return result

# print('home', home)
# print('chicken', chicken)
print(find_shorest(home, m_chicken))
