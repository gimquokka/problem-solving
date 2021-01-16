import sys

def merge(lst):


    for _ in range(3):
        for i in range(4):
            for j in range(3):

                # if current cell has same value as
                # next cell in the row and they
                # are non empty then
                if (lst[i][j] == lst[i][j + 1] and lst[i][j] != 0):
                    # double current cell value and
                    # empty the next cell
                    lst[i][j] = lst[i][j] * 2
                    lst[i][j + 1] = 0
        lst = compress(lst)

    return lst

def compress(mat):
    # bool variable to determine
    # any change happened or not
    changed = False

    # empty grid
    new_mat = []

    # with all cells empty
    for i in range(4):
        new_mat.append([0] * 4)

        # here we will shift entries
    # of each cell to it's extreme
    # left row by row
    # loop to traverse rows
    for i in range(4):
        pos = 0

        # loop to traverse each column
        # in respective row
        for j in range(4):
            if (mat[i][j] != 0):

                # if cell is non empty then
                # we will shift it's number to
                # previous empty cell in that row
                # denoted by pos variable
                new_mat[i][pos] = mat[i][j]

                if (j != pos):
                    changed = True
                pos += 1

    # returning new compressed matrix
    # and the flag variable.
    return new_mat
mm = [[0, 0, 2, 2],[2,2,4,0],[4,2,0,2],[0,2,4,0]]
print(mm)
mm = compress(mm)
print(mm)
mm = merge(mm)
print(mm)
mm = compress(mm)
print(mm)
'''
kk = [[4, 0, 0, 0], [4, 0, 4, 0], [4, 4, 0, 0], [2, 4, 0, 0]]
print(kk)
print(compress(kk))'''