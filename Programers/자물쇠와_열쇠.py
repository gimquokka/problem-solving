def rotate(key):
    n = len(key)
    new_key = [[0]*n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            new_key[y][n-x-1] = key[x][y]
            
    return new_key
            
def check(length, new_lock):
    for i in range(length, 2*length):
        for j in range(length, 2*length):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    for _ in range(4):
        key = rotate(key)
        length = len(lock)
        key_length = len(key)
        new_lock = [[0]*3*length for _ in range(3*length)]

        for i in range(length, 2*length):
            for j in range(length, 2*length):
                new_lock[i][j] = lock[i-length][j-length]
                
        
        for x in range(3*length-key_length+1):
            for y in range(3*length - key_length+1):
                
                for dx in range(key_length): 
                    for dy in range(key_length):
                        new_lock[x+dx][y+dy] += key[dx][dy]
                
                if check(length, new_lock):
                    return True
                
                for dx in range(key_length): 
                    for dy in range(key_length):
                        new_lock[x+dx][y+dy] -= key[dx][dy]
    return False
            
    
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
