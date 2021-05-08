import sys
import copy
input = sys.stdin.readline

w, h = map(int, input().split())

d = [[0]*w for _ in range(h)]

for i in range(h):
    d[i] = list(map(int, input().split()))

# F***...Wrong aproch... T.T


def mature(w, h, d):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    count = 0

    while True:
        d_copy = copy.deepcopy(d)
        c1 = 0
        for y in range(h):
            for x in range(w):
                c2 = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < w and 0 <= ny < h:
                        if d[ny][nx] == 0 and d[y][x] == 1:
                            d_copy[ny][nx] = 1
                            c1 += 1
                        if d[y][x] != 0 or d[ny][nx] == 0 or d[ny][nx] == 1:
                            c2 += 1
                            # print('nx, ny', nx, ny)
                if c2 == 0:
                    return -1

        if c1 == 0:
            return count
        count += 1
        d = copy.deepcopy(d_copy)


print(mature(w, h, d))
