# moving route of ant who moves to right or down
#if can't move anymore or finds the food, stop

b = [list(map(int, input().split())) for _ in range(10)]

x, y = 1, 1

while(1):
    # finding food
    if b[x][y] == 2:
        b[x][y] = 9
        break
    # not at the end and no food
    if b[x][y+1] != 1: # can go to the right
        b[x][y] = 9
        y += 1
    elif b[x+1][y] != 1: # to the down
        b[x][y] = 9
        x += 1
    else: # can't move
        b[x][y] = 9
        break

for i in range(10):
    print(*b[i])
