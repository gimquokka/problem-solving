from itertools import combinations

n = int(input())

arr = [[None]*n for _ in range(n)]
x_pos = []
t_pos = []
for i in range(n):
    arr[i] = list(input().split())
    for idx, x in enumerate(arr[i]):
        if x == 'X':
            x_pos.append((i, idx))
        elif x == 'T':
            t_pos.append((i, idx))
"""
# Test Input이 잘 받아지는지
print("arr", arr)
print("x_pos", x_pos)
"""


def dfs(arr, x, y, type):
    global found
    if not (0 <= x < n and 0 <= y < n):
        return
    elif arr[x][y] == "O":
        return
    elif arr[x][y] == "S":
        found = True
        return

    if type == 'u':
        dfs(arr, x-1, y, "u")
    elif type == 'd':
        dfs(arr, x+1, y, 'd')
    elif type == 'l':
        dfs(arr, x, y-1, 'l')
    elif type == 'r':
        dfs(arr, x, y+1, 'r')


for three_o in combinations(x_pos, 3):
    found = False
    # 장애물 설치
    for x, y in three_o:
        arr[x][y] = "O"
    # 각 선생님의 위치 상하좌우 방향 탐색
    for x, y in t_pos:
        dfs(arr, x, y, "r")
        dfs(arr, x, y, "l")
        dfs(arr, x, y, "u")
        dfs(arr, x, y, "d")
    # 원상복구
    for x, y in three_o:
        arr[x][y] = "X"
    # 찾지 못했으면 => 가능하면
    if not found:
        print("YES")
        quit()

# 결국 찾았으면 => 불가능
print("NO")
