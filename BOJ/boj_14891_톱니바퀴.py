def turn(a, d):
    if d == 1:
        a.insert(0, a.pop())
    else:
        a.append(a.pop(0))


def check(a1, a2):
    if a1[2] != a2[6]:
        return True
    else:
        return False


a = [0]*5
for i in range(1, 5):
    a[i] = list(map(int, input()))
n = int(input())

for turn_count in range(n):
    t, d = map(int, input().split())
    turn_info = []
    # Check left
    next_d = -d
    for i in range(t, 1, -1):
        if not check(a[i-1], a[i]):
            break
        else:
            turn_info.append((i-1, next_d))
            next_d = -next_d
    # Check right
    next_d = -d
    for i in range(t, 4):
        if not check(a[i], a[i+1]):
            break
        else:
            turn_info.append((i+1, next_d))
            next_d = -next_d
    # Turn input gear
    turn(a[t], d)

    for i, direction in turn_info:
        turn(a[i], direction)

answer = 0
for i in range(1, 5):
    answer += (2**(i-1))*a[i][0]

print(answer)
