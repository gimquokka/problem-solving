#
import sys
def ToR(lst):
    #case1: ****
    if lst[0] == lst[1] == lst[2] == lst[3]:
        l = [0, 0, 0, 4 * lst[3]]

    # case2: ***_ or _***
    elif lst[0] == lst[1] == lst[2] != lst[3]:
        l = [0, 0, lst[0], 4 * lst[0]] if lst[3] == 2 * lst[0] else [0, lst[0], 2 * lst[0], lst[3]]
    elif lst[0] != lst[1] == lst[2] == lst[3]:
        l = [0, lst[0], lst[1], 2 * lst[3]]

    #case3: **##
    elif lst[0] == lst[1] != lst[2] == lst[3]:
        l = [0, 0, 2 * lst[0], 2 * lst[3]]

    #case4 :##*@ or *##* or *##@ or *@##
    elif lst[0] == lst[1] != lst[2] != lst[3]:
        if lst[2] != 2*lst[1]:
            l = [0, 2 * lst[1], lst[2], lst[3]]
        else:
            l = [0, 0, 4 * lst[1], lst[3]] if lst[3] != 4 * lst[1] else [0, 0, 0, 8 * lst[1]]

    elif lst[0] != lst[1] == lst[2] != lst[3]:
        if lst[0] != 2*lst[1] != lst[3]:
            l = [0, lst[0], 2 * lst[1], lst[3]]
        elif lst[0] != 2*lst[1] == lst[3]:
            l = [0, 0, lst[0], 4 * lst[1]] if lst[0] != 4 * lst[1] else [0, 0, 0, 8 * lst[1]]
        elif lst[0] == 2 * lst[1] != lst[3]:
            l = [0, 0, 4 * lst[1], lst[3]] if lst[3] != 4 * lst[1] else [0, 0, 0, 8 * lst[1]]
        else:
            l = [0, 0, 2 * lst[1], 4 * lst[1]]
    # @*## ...
    elif lst[0] != lst[1] != lst[2] == lst[3]:
        if lst[1] != 2*lst[2]:
            l = [0, lst[0], lst[1], 2*lst[2]]
        else: l = [0, 0, lst[0], 4*lst[2]] if lst[0] != 4*lst[2] else [0, 0, 0, 8*lst[2]]

    #case5 : not changed
    else: l = lst[:]
    return l

def transp(lst):
    b_arr = [[0] * 4 for i in range(4)]
    for i in range(4):
        s = []
        for j in range(4):
            s.append(lst[j][i])
        b_arr[i] = s
    return b_arr

def flip(lst):
    #s = []
    b_arr = [[0] * 4 for i in range(4)]
    for i in range(4):
        s = lst[i][:]
        s.reverse()
        b_arr[i] = s
    return b_arr

w = input()

arr = [[0]*4 for i in range(4)]

for i in range(4):
    arr[i] = list(map(int, input().split()))

if w == 'R':
    for i in range(4):
        arr[i] = ToR(arr[i])

if w == 'D':
    arr = transp(arr)
    for i in range(4):
        arr[i] = ToR(arr[i])
    arr = transp(arr)

elif w == 'L':
    arr = flip(arr)
    for i in range(4):
        arr[i] = ToR(arr[i])
    arr = flip(arr)


elif w == 'U':
    arr = transp(arr)
    arr = flip(arr)
    for i in range(4):
        arr[i] = ToR(arr[i])
    arr = flip(arr)
    arr = transp(arr)

for i in range(4):
    print(*arr[i])


