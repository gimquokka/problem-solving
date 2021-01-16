#
import sys
def ToL(lst):
    for _ in range(3):
        for i in range(4):
            for j in range(3):


                if (lst[i][j] == lst[i][j + 1] and lst[i][j] != 0):

                    lst[i][j] = lst[i][j] * 2
                    lst[i][j + 1] = 0
        lst = compress(lst)

    return lst


def transp(lst):
    b_arr = []
    for i in range(4):
        b_arr.append([])
        for j in range(4):
            b_arr[i].append(lst[j][i])
    return b_arr

def flip(lst):
    b_arr=[]
    for i in range(4):
        b_arr.append([])
        for j in range(4):
            b_arr[i].append(lst[i][3-j])
    return b_arr

def compress(lst):
    b_arr=[[0]*4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if lst[i][j] != 0:
                b_arr[i][pos] = lst[i][j]
                pos += 1
    return b_arr


w = input()

arr = []

for i in range(4):
    arr.append(list(map(int, input().split())))


if w == 'L':
    arr = compress(arr)
    arr = ToL(arr)

elif w == 'R':
    arr = flip(arr)
    arr = compress(arr)
    arr = ToL(arr)
    arr = flip(arr)

if w == 'U':
    arr = transp(arr)
    arr = compress(arr)
    arr = ToL(arr)
    arr = transp(arr)

elif w == 'D':
    arr = transp(arr)
    arr = flip(arr)
    arr = compress(arr)
    arr = ToL(arr)
    arr = flip(arr)
    arr = transp(arr)

for i in range(4):
    print(*arr[i])


