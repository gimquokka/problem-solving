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


a = []
for _ in range(4):
    a.append(list(map(int, input())))

n = int(input())

turn_info = []
for turn_count in range(n):
    t, d = map(int, input().split())
    # Check left
    next_d = -d
    for i in range(t, 1, -1):
        if not check(a[i-2], a[i-1]):
            break
        else:
            turn_info.append((i-2, next_d))
            next_d = -next_d
    # Check right
    next_d = -d
    for i in range(t, 4):
        if not check(a[i-1], a[i]):
            break
        else:
            # print('check')
            turn_info.append((i, next_d))
            next_d = -next_d
    turn(a[t-1], d)
    for i, direction in turn_info:
        turn(a[i], direction)

answer = 0
for i in range(4):
    answer += (2**i)*a[i][0]

# print(turn_info)
# print(a)
print(answer)

# (a +b)/2
#   (a-b)/2 +b
(a-b)/2 + b < int
a +b int> 