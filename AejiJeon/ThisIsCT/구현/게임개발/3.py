n, m = map(int, input().split())
x, y, direction = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1
count = 1


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
turn = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if visited[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        visited[nx][ny] = 1
        count += 1
        turn = 0
        continue

    else:
        turn += 1

    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 1:
            break
        x = nx
        y = ny
        turn = 0

print(count)













