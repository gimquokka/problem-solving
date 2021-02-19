"""
(가격, 무게) sort: (+, -)
(1, 10) (3, 5) (3, 4) (4, 6) (5, 7) (5, 8) (6, 1) (7, 4)
m = 10

문제 제대로 안읽어서 삽질함...ㅜㅜ
1. 가격이 작을 때 무료 => 무게X
2. 가격이 같을 경우 고려 => 가격이 같으면 일단 더해주기
"""
import sys
input = sys.stdin.readline
INF = int(1e11)

n, m = map(int, input().split())

meat = [0]*n
for i in range(n):
    w, c = map(int, input().split())
    meat[i] = (c, w)
meat.sort(key=lambda x: (x[0], -x[1]))

ans = INF
tot_weight = 0
tot_cost = 0
for i in range(n):
    tot_weight += meat[i][1]

    if meat[i-1][0] == meat[i][0]:
        tot_cost += meat[i][0]
    else:
        tot_cost = meat[i][0]

    # For securing minimum cost over 0 ~ n
    if tot_weight >= m:
        ans = min(ans, tot_cost)

print(-1 if ans == INF else ans)
