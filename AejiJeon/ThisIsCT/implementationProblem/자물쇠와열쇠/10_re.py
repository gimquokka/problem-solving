def solution(key, lock):
    n = len(lock[0])
    m = len(key[0])


    def cw_rotation(key):        
        n_arr = [[0]*m for _ in range(m)]
        column = m-1
        for row in key: # row = [0,0,0]
            for i in range(m):
                n_arr[i][column] = row[i]
            column -= 1
        return n_arr
    
    def big_reset(lock):

        n_lock = [[0]*(2*m+n-2) for _ in range(2*m+n-2)]
        a = 0
        for i in range(m-1, m+n-1):
            b = 0
            for j in range(m-1, m+n-1):
                n_lock[i][j] = lock[a][b]
                b += 1
            a += 1
        return n_lock
    
    def Isfit(key,big_lock, x, y):
        a=0
        for i in range(x, x+m):
            b=0
            for j in range(y, y+m):
                
                if i >= m-1 and i <= m+n-2 and j >= m-1 and j <= m+ n-2:
                    if key[a][b] == big_lock[i][j]:
                        return False
                    elif big_lock[i][j] == 0: #다르고 lock이 홈
                        big_lock[i][j] = 1    
                b += 1
            a += 1
        for i in range(m-1,m+n-1):
            for j in range(m-1, m+n-1):
                if big_lock[i][j] == 0:
                    return False

        return True  # 다 막힘
    
    for _ in range(4):
        
        for i in range(0, m+n-1):
            for j in range(0, m+n-1):
                big_lock = big_reset(lock)
                if Isfit(key,big_lock, i, j):
                    return True

        key = cw_rotation(key)
    
    return False
    
key = [[0,0,0], [1,0,0], [0,1,1]]
lock = [[1,1,1], [1,1,0], [1,0,1]]
print(solution(key, lock))

















        
    