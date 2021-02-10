import sys
import copy

input = sys.stdin.readline


n, m, x, y, k = map(int, input().split())

# map
array = [[0] * m for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        array[i][j] = data[j]

moves = list(map(int, input().split()))

# 주사위 전개도 4x3 array로 표현
dice = [[0] * 3 for _ in range(4)]

# 주어진 방향으로 주사위를 굴린 후의 전개도의 모습 return
def rollDice(dice, d):

    new_dice = copy.deepcopy(dice)
    # (0,1) ~ (3,1) 4개의 숫자들이
    # 위로 한 칸씩 이동함(맨 위 숫자는 맨 아래로)
    if d == 3:

        for i in range(4):
            if i == 3:
                new_dice[i][1] = dice[0][1]
            else:
                new_dice[i][1] = dice[i + 1][1]
    # (0,1) ~ (3,1) 4개의 숫자들이
    # 아래로 한 칸씩 이동함(맨 아래 숫자는 맨 위로)
    elif d == 4:

        for i in range(4):
            if i == 3:
                new_dice[0][1] = dice[i][1]
            else:
                new_dice[i + 1][1] = dice[i][1]

    # (1,0), (1,1), (1,2), (3,1) 숫자들이
    # 오른쪽으로 한 칸씩 이동(맨 오른쪽 숫자는 맨 왼쪽으로)
    elif d == 1:
        new_dice[1][0] = dice[3][1]
        new_dice[1][1] = dice[1][0]
        new_dice[1][2] = dice[1][1]
        new_dice[3][1] = dice[1][2]

    # (1,0), (1,1), (1,2), (3,1) 숫자들이
    # 왼쪽으로 한 칸씩 이동(맨 왼쪽 숫자는 맨 오른쪽으로)
    elif d == 2:
        new_dice[1][0] = dice[1][1]
        new_dice[1][1] = dice[1][2]
        new_dice[1][2] = dice[3][1]
        new_dice[3][1] = dice[1][0]

    return new_dice


# 시작 주사위
dice[0][0] = array[x][y]

# 동, 서, 북, 남 으로 이동할 경우의 좌표 변화량
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


for i in moves:
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]

    # 지도 밖으로 나가버리는 경우
    if not (0 <= nx < n and 0 <= ny < m):
        continue

    dice = rollDice(dice, i)

    if array[nx][ny] == 0:
        # 주사위 바닥에 있는 숫자를 지도에 적음
        array[nx][ny] = dice[3][1]

    else:
        # 지도에 적힌 숫자를 주사위 바닥에 적은 후
        # 지도에 0을 적어줌
        dice[3][1] = array[nx][ny]
        array[nx][ny] = 0

    x, y = nx, ny

    # 주사위 바닥에 있는 숫자 print
    print(dice[1][1])
