import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

swith = []
lamp = [0]*(M+1)
for _ in range(N):
    _, *tmp = map(int, input().split())

    swith.append(tuple(tmp))
    for i in tmp:
        lamp[i] += 1


def solve():
    # print(swith)
    for i in range(N):
        swith_to_lamp = swith[i]
        # if not swith_to_lamp: continue
        # => 이건 외 안되징? 아! 0개면 이걸 빼야만 하는 경우가 있겠네

        # copy_lamp = copy.deepcopy(lamp)
        copy_lamp = lamp[:]
        cnt = 0
        for j in swith_to_lamp:
            copy_lamp[j] -= 1
            if copy_lamp[j] <= 0:
                break
            cnt += 1
        if cnt == len(swith_to_lamp):
            return print(1)

    return print(0)


solve()
# print('swith', swith)
# print('lamp', lamp)
