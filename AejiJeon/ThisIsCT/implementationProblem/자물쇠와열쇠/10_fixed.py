# rotate array 90 degree

def cw_rotate(array):
    n = len(array)
    m = len(array[0])
    n_arr = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            n_arr[j][n-i-1] = array[i][j] 
    return n_arr

# if all the numbers in lock are 1
def Is_fit(big_lock,m,n):  # 왜 m,n 넣어줘야 하지..? -> static binding?
    
    for i in range(m, m+n-1):
        for j in range(m, m+n-1):
            if big_lock[i][j] != 1:
                return False
    
    return True


  


def solution(key,lock):
    m = len(key)
    n = len(lock)
    big_lock = [[0]*(2*m+n-2) for _ in range(2*m+n-2)]
    a = 0
    for i in range(m-1, m+n-1):
        b = 0
        for j in range(m-1, m+n-1):
            big_lock[i][j] = lock[a][b]
            b += 1
        a += 1
    
    for _ in range(4):
        key = cw_rotate(key)
        for i in range(0, m+n-1):
            for j in range(0, m+n-1):
                
                for a in range(m):
                    for b in range(m):
                        big_lock[i+a][j+b] += key[a][b]
                # print(big_lock)
                
                if Is_fit(big_lock,m,n):
                    return True
                # big_lock 원상복귀
                for a in range(m):
                    for b in range(m):
                        big_lock[i+a][j+b] -= key[a][b]
                # print(big_lock)

    return False

key = [[0,0,0], [1,0,0], [0,1,1]]
lock = [[1,1,1], [1,1,0], [1,0,1]]
print(solution(key, lock))
