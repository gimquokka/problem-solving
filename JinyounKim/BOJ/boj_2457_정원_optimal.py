"""
Ref: https://bit.ly/3ap3iZe
"""
import sys
import heapq
input = sys.stdin.readline

N = int(input())

data = [0]*N
for i in range(N):
    m, d, m1, d1 = map(int, input().split())
    a, b = m*100+d, m1*100+d1
    data[i] = (a, b)
data.sort()


def solve():
    tmp = 0
    date = 301
    index = -1
    ans = 0

    while date <= 1130:
        index += 1
        flag = False

        for i in range(index, N):
            if data[i][0] > date:
                break
            if data[i][1] > tmp:
                tmp = data[i][1]
                index = i
                flag = True

        if flag:
            ans += 1
            date = tmp
        else:
            return print('0')

    return print(ans)


solve()
