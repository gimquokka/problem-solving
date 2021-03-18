import copy

arr = [[None]*4 for i in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = [data[j*2], data[j*2+1]-1]

'''
# Input Check
for i in range(4):
     print(arr[i])
'''
# Global Vars
result = 0
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 반시계 방향회전


def turn(direction):
    return (direction + 1) % 8

# 해당 번호의 물고기 위치 반환


def find_fish(arr, fish_num):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == fish_num:
                return (i, j)
    return None


'''
# Check "find_fish" work well
print(find_fish(arr, 4))
'''

# 모든 물고기 이동


def move_all_fish(arr, shack_x, shack_y):
    # new_arr = copy.deepcopy(arr)
    for fish_num in range(1, 17):
        fish_pos = find_fish(arr, fish_num)
        if fish_pos != None:
            x, y = fish_pos
            direction = arr[x][y][1]
            for i in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (shack_x == nx and shack_y == ny):
                        arr[x][y][1] = direction
                        arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                        break
                direction = turn(direction)


"""
# Check "move_all_fish" work well
move_all_fish(arr, 0, 0)
for i in range(4):
    print(arr[i])
"""

# 상어의 이동 가능한 모든 위치 반환


def find_next_shack_pos(arr, shack_x, shack_y):
    next_pos = []
    x, y = shack_x, shack_y
    direction = arr[shack_x][shack_y][1]
    for i in range(4):
        x += dx[direction]
        y += dy[direction]
        if 0 <= x < 4 and 0 <= y < 4:
            if arr[x][y][0] != -1:
                next_pos.append((x, y))
    return next_pos


'''
##TEST##
print(find_next_shack_pos(arr, 1, 2))
'''

# dfs로 모든 경우 구현


def dfs(arr, shack_x, shack_y, total):
    global result

    arr = copy.deepcopy(arr)

    total += arr[shack_x][shack_y][0]
    arr[shack_x][shack_y][0] = -1

    move_all_fish(arr, shack_x, shack_y)

    next_pos = find_next_shack_pos(arr, shack_x, shack_y)

    if len(next_pos) == 0:
        result = max(result, total)
        return

    for x, y in next_pos:
        # print(total)
        dfs(arr, x, y, total)


dfs(arr, 0, 0, 0)

print(result)
