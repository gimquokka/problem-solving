n = int(input())
arr = list(input().split())

direction = {"L": (0, -1), "R": (0, 1), "U": (-1, 0),"D": (1, 0)}

loc = (1, 1)

for dir in arr:
    x, y = loc
    dx, dy = direction[dir]
    if 1 <= x+dx <= n and 1 <= y+dy <= n:
        loc = (x+dx, y+dy)

print(*loc)
