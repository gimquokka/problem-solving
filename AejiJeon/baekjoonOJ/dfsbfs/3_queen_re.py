import sys

input = sys.stdin.readline

n = int(input())
array = [[0]*n for _ in range(n)]

count = 0


# checking only left side  
def checkPossible(array, x, y): 
  
    # checking from left side horizontally
    for i in range(y): 
        if array[x][i] == 1: 
            return False
  
    # checking from left and upper side diagonally 
    for i, j in zip(range(x, -1, -1),  
                    range(y, -1, -1)): 
        if array[i][j] == 1: 
            return False
  
    # Check from left and lower side diagonally 
    for i, j in zip(range(x, n, 1),  
                    range(y, -1, -1)): 
        if array[i][j] == 1: 
            return False
  
    return True
  
def solve(array, y): 
    global count
    # all n queens can put
    if y >= n: 
        count += 1
        return
  
    # check all elems at y column
    for i in range(n): 
        
        if checkPossible(array, i, y): 
            # put
            array[i][y] = 1
  
            # recur about next column
            solve(array, y + 1)

            # remove
            array[i][y] = 0
  
    # impposible to put
    return

solve(array, 0)
print(count)